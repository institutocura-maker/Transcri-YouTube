# -*- coding: utf-8 -*-
"""rc_termo — cria termo novo na KB-RC (canonico.json + ficha) a partir de uma especificação.

Segunda mão do curador (a primeira é `rc_curadoria.py`, que aplica variantes a termos existentes).
Criar termo é o passo mais consequente da curadoria: entra na fonte de verdade, ganha código
definitivo e passa a alimentar todo diagnóstico futuro. Por isso a ferramenta não improvisa nada —
ela exige uma especificação escrita e confere o que escreve.

O que faz:

1. lê a especificação (`KB-RC/_lote-NN-termos.json`);
2. **valida antes de gravar**: código livre, nome único, categoria/subcategoria dentro da taxonomia
   já existente, relacionados que existem de fato, fonte registrada em `biblio.json`, nome de
   arquivo ASCII;
3. escreve a ficha `KB-RC/termos/RC-NNN-<slug>.md` no formato da casa (frontmatter `+++` e as
   seções canônicas);
4. acrescenta o termo em `canonico.json` e as arestas em `relacoes`;
5. faz **round-trip**: relê o que gravou com `rc_kb` e confere código, nome, variantes STT e
   relacionados — se o parser da casa não enxergar, a criação é recusada;
6. marca o item correspondente na fila e escreve a entrada no `CHANGELOG.md`.

Os JSON são reescritos com `indent=1, ensure_ascii=False`, que é a serialização exata dos arquivos
atuais (verificado por round-trip byte a byte): o diff mostra só o que foi acrescentado.

Uso:
    python ferramentas/rc_termo.py KB-RC/_lote-02-termos.json --simular
    python ferramentas/rc_termo.py KB-RC/_lote-02-termos.json --aplicar
    python ferramentas/rc_termo.py KB-RC/_lote-02-termos.json --aplicar --somente RC-947,RC-948
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_kb as KB  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CAMPOS_TERMO = ["codigo", "nome", "categoria", "subcategoria", "status",
                "fontes", "relacionados", "ficha", "via", "confianca_fonte"]
STATUS_VALIDOS = {"verificado", "provisório", "em análise", "candidato"}
VIAS_VALIDAS = {"P6-evidência", "P7-conhecimento"}
CONFIANCAS_VALIDAS = {"alta", "média", "baixa"}


# --------------------------------------------------------------------- especificação


def carregar_spec(caminho: Path) -> dict:
    spec = json.loads(caminho.read_text(encoding="utf-8"))
    if "termos" not in spec or "meta" not in spec:
        raise SystemExit(f"[recusado] especificação sem 'meta' ou sem 'termos': {caminho}")
    return spec


def slug_arquivo(codigo: str, nome: str) -> str:
    """'RC-948' + '/Kaggen' -> 'RC-948-kaggen.md'. ASCII, sem espaço, sem acento."""
    import unicodedata
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    s = re.sub(r"-{2,}", "-", s)
    return f"{codigo}-{s}.md"


def proximo_codigo(termos: list[dict]) -> str:
    nums = [int(m.group(1)) for t in termos if (m := re.match(r"RC-(\d{3,})$", t["codigo"]))]
    return f"RC-{max(nums) + 1:03d}" if nums else "RC-001"


# ------------------------------------------------------------------------ validação


def validar(spec: dict, canon: dict, obras: list[dict], existentes: dict) -> tuple[list[dict], list[str]]:
    """Devolve (termos prontos, problemas). Com problema, não se grava nada."""
    problemas: list[str] = []
    categorias = {t["categoria"] for t in canon["termos"]}
    subcats = {(t["categoria"], t["subcategoria"]) for t in canon["termos"]}
    codigos_fonte = {o["codigo"] for o in obras}
    nomes = {KB.L_norm(t["nome"]) for t in canon["termos"]}
    prontos: list[dict] = []
    codigos_lote = set()
    auto = None

    # pré-alocação: um termo pode se relacionar com outro do MESMO lote (RC-947 -> RC-955).
    # Sem este passo, o primeiro da fila é recusado por apontar para um irmão que ainda não foi lido.
    for t in spec["termos"]:
        c = (t.get("codigo") or "").strip()
        if not c:
            c = auto or proximo_codigo(canon["termos"])
            auto = f"RC-{int(c[3:]) + 1:03d}"
        t["codigo"] = c
        codigos_lote.add(c)

    for i, t in enumerate(spec["termos"]):
        rot = t.get("nome", f"termo #{i + 1}")
        codigo = t["codigo"]
        if codigo in existentes:
            problemas.append(f"{rot}: código {codigo} já existe na base")
            continue
        if sum(1 for x in spec["termos"] if x.get("codigo") == codigo) > 1:
            problemas.append(f"{rot}: código {codigo} repetido dentro do lote")
            continue
        if KB.L_norm(rot) in nomes:
            problemas.append(f"{rot}: nome já existe na base (duplicata)")
        if t.get("categoria") not in categorias:
            problemas.append(f"{rot}: categoria '{t.get('categoria')}' fora da taxonomia")
        if (t.get("categoria"), t.get("subcategoria")) not in subcats:
            problemas.append(f"{rot}: subcategoria '{t.get('subcategoria')}' não é usada nessa categoria")
        if t.get("status") not in STATUS_VALIDOS:
            problemas.append(f"{rot}: status '{t.get('status')}' inválido — {sorted(STATUS_VALIDOS)}")
        if t.get("via", "P6-evidência") not in VIAS_VALIDAS:
            problemas.append(f"{rot}: via inválida")
        if t.get("confianca_fonte") not in CONFIANCAS_VALIDAS:
            problemas.append(f"{rot}: confianca_fonte inválida")
        for f in t.get("fontes", []):
            if f not in codigos_fonte:
                problemas.append(f"{rot}: fonte '{f}' não está em biblio.json — registre antes (padrão Y)")
        for r in t.get("relacionados", []):
            alvo = r["codigo"] if isinstance(r, dict) else r
            if alvo not in existentes and alvo not in codigos_lote:
                problemas.append(f"{rot}: relacionado {alvo} não existe")
        if not t.get("definicao"):
            problemas.append(f"{rot}: sem definição sintética")
        arquivo = slug_arquivo(codigo, rot)
        if not re.fullmatch(r"[A-Za-z0-9._-]+", arquivo):
            problemas.append(f"{rot}: nome de arquivo não é ASCII-safe: {arquivo}")
        if (RAIZ / "KB-RC" / "termos" / arquivo).exists():
            problemas.append(f"{rot}: arquivo {arquivo} já existe")
        t["_arquivo"] = arquivo
        prontos.append(t)
    return prontos, problemas


# --------------------------------------------------------------------------- escrita


def montar_ficha(t: dict, meta: dict) -> str:
    codigo, nome = t["codigo"], t["nome"]
    relacionados = t.get("relacionados", [])
    fontes = t.get("fontes", [meta.get("fonte", "")])
    linhas = [
        "+++",
        f"# frontmatter curatorial (lote {meta.get('lote', '?')} — padrão {meta.get('padrao_fonte', 'Y')})"
        f" — fonte: {', '.join(fontes)}",
        f'codigo = "{codigo}"',
        f'nome = "{nome}"',
        f'categoria = "{t["categoria"]}"',
        f'subcategoria = "{t["subcategoria"]}"',
        f'status = "{t["status"]}"',
        "fontes = [" + ", ".join(f'"{f}"' for f in fontes) + "]",
        f'via = "{t.get("via", "P6-evidência")}"',
        f'confianca_fonte = "{t.get("confianca_fonte", "média")}"',
        f'atualizado = "{meta.get("data", date.today().isoformat())}"',
        "+++",
        f"# {nome} — {codigo}",
        "",
        "## Definição Sintética",
        t["definicao"].strip(),
        "",
        "## Contexto / Origem",
        t.get("contexto", "").strip() or "—",
        "",
        "## Etimologia e Grafias",
        f'- **Grafia preferida:** {t.get("grafia_preferida", nome)}',
    ]
    if t.get("variacoes"):
        linhas.append("- **Variações:** " + "; ".join(t["variacoes"]))
    if t.get("variacoes_stt"):
        linhas.append("- **Variações STT capturadas:** " + "; ".join(t["variacoes_stt"]))
    linhas.append(f'- **Idioma de origem / etimologia:** {t.get("idioma", "Português (neologismo do autor)")}')
    linhas += ["", "## Citações-chave", ""]
    for c in t.get("citacoes", []):
        onde = c.get("onde", f"bloco {c.get('bloco', '?')}")
        linhas.append(f"- «{c['texto'].strip()}» — *ver:* **{onde}** de "
                      f"`{meta.get('slug', '')}` ({', '.join(fontes)})")
    if not t.get("citacoes"):
        linhas.append("- (sem citação literal registrada)")
    linhas += ["", "## Termos Relacionados", "| Termo | Código | Tipo de relação |", "|---|---|---|"]
    for r in relacionados:
        if isinstance(r, dict):
            linhas.append(f"| {r.get('nome', '—')} | {r['codigo']} | {r.get('tipo', 'associado')} |")
    if not relacionados:
        linhas.append("| — | — | — |")
    linhas += ["", "## Fontes", ""]
    for f in fontes:
        linhas.append(f"- **{f}** — {meta.get('descricao_fonte', 'fonte audiovisual (padrão Y)')}")
    linhas += ["", "## Observações", "", t.get("observacoes", "").strip() or "—", ""]
    if meta.get("despacho"):
        linhas += [f"Criação autorizada por: {meta['despacho']}. Curadoria: "
                   f"{meta.get('curador', '—')} em {meta.get('data', '')}.", ""]
    return "\n".join(linhas)


def entrada_canonico(t: dict) -> dict:
    rel = sorted({(r["codigo"] if isinstance(r, dict) else r) for r in t.get("relacionados", [])})
    return {
        "codigo": t["codigo"],
        "nome": t["nome"],
        "categoria": t["categoria"],
        "subcategoria": t["subcategoria"],
        "status": t["status"],
        "fontes": t.get("fontes", []),
        "relacionados": rel,
        "ficha": True,
        "via": t.get("via", "P6-evidência"),
        "confianca_fonte": t.get("confianca_fonte", "média"),
    }


def arestas(t: dict, meta: dict) -> list[dict]:
    fonte = (t.get("fontes") or [meta.get("fonte", "")])[0]
    out = []
    for r in t.get("relacionados", []):
        if isinstance(r, dict):
            out.append({"a": t["codigo"], "tipo": r.get("tipo", "associado"),
                        "b": r["codigo"], "fonte": fonte})
    return out


def gravar_json(caminho: Path, dado: dict, sufixo: str) -> None:
    caminho.write_text(json.dumps(dado, ensure_ascii=False, indent=1) + sufixo, encoding="utf-8")


# ------------------------------------------------------------------------------ CLI


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Cria termos novos na KB-RC a partir de especificação.")
    ap.add_argument("spec", type=Path, help="KB-RC/_lote-NN-termos.json")
    ap.add_argument("--kb", type=Path, default=RAIZ / "KB-RC")
    ap.add_argument("--simular", action="store_true", help="valida e mostra, sem gravar (default)")
    ap.add_argument("--aplicar", action="store_true")
    ap.add_argument("--somente", default="", help="só estes códigos, separados por vírgula")
    ap.add_argument("--sem-fila", action="store_true")
    ap.add_argument("--sem-changelog", action="store_true")
    args = ap.parse_args(argv)
    aplicar = args.aplicar and not args.simular

    spec = carregar_spec(args.spec)
    meta = dict(spec["meta"])
    meta.setdefault("data", date.today().isoformat())
    canon_path = args.kb / "canonico.json"
    biblio_path = args.kb / "biblio.json"
    fila_path = args.kb / "_fila-de-curadoria.csv"
    changelog_path = args.kb / "CHANGELOG.md"

    orig_canon = canon_path.read_text(encoding="utf-8")
    canon = json.loads(orig_canon)
    obras = json.loads(biblio_path.read_text(encoding="utf-8")).get("obras", [])
    existentes = {t["codigo"]: t for t in canon["termos"]}
    fichas = KB.carregar_fichas(str(args.kb))

    termos = spec["termos"]
    if args.somente:
        want = {c.strip() for c in args.somente.split(",")}
        termos = [t for t in termos if (t.get("codigo") or "").strip() in want]
    spec = dict(spec, termos=termos)

    prontos, problemas = validar(spec, canon, obras, {**existentes, **{c: 1 for c in fichas}})
    if problemas:
        print(f"[recusado] {len(problemas)} problema(s) de validação — nada foi gravado:")
        for p in problemas:
            print("   -", p)
        return 1

    print(f"\n=== {'APLICAÇÃO' if aplicar else 'SIMULAÇÃO'}: lote {meta.get('lote','?')} — "
          f"{len(prontos)} termo(s) novo(s) ===")
    for t in prontos:
        print(f"  {t['codigo']} {t['nome'][:44]:<44} {t['categoria'][:22]:<22} "
              f"{t['subcategoria'][:30]:<30} {t['status']:<11} -> {t['_arquivo']}")
        if t.get("variacoes_stt"):
            print(f"      variantes STT: {', '.join(t['variacoes_stt'])}")
    if not aplicar:
        print("\n[simulação] validação ok; nada gravado. Use --aplicar para criar.")
        return 0

    novas_arestas = []
    for t in prontos:
        (args.kb / "termos" / t["_arquivo"]).write_text(montar_ficha(t, meta), encoding="utf-8")
        canon["termos"].append(entrada_canonico(t))
        novas_arestas += arestas(t, meta)
    canon["relacoes"] += novas_arestas
    gravar_json(canon_path, canon, "\n")

    # round-trip: o que a casa lê precisa ser o que eu quis escrever
    falhas = []
    fichas_novas = KB.carregar_fichas(str(args.kb), [t["codigo"] for t in prontos])
    for t in prontos:
        f = fichas_novas.get(t["codigo"])
        if f is None:
            falhas.append(f"{t['codigo']}: rc_kb não encontrou a ficha")
            continue
        if f.nome != t["nome"]:
            falhas.append(f"{t['codigo']}: nome lido '{f.nome}' != '{t['nome']}'")
        if set(f.variacoes_stt) != set(t.get("variacoes_stt", [])):
            falhas.append(f"{t['codigo']}: variantes STT {f.variacoes_stt} != {t.get('variacoes_stt')}")
        if f.fontes != t.get("fontes", []):
            falhas.append(f"{t['codigo']}: fontes {f.fontes} != {t.get('fontes')}")
        if f.status != t["status"]:
            falhas.append(f"{t['codigo']}: status lido '{f.status}'")
    novo_canon = json.loads(canon_path.read_text(encoding="utf-8"))
    for t in prontos:
        e = next((x for x in novo_canon["termos"] if x["codigo"] == t["codigo"]), None)
        if not e:
            falhas.append(f"{t['codigo']}: não entrou em canonico.json")
        elif list(e.keys()) != CAMPOS_TERMO:
            falhas.append(f"{t['codigo']}: campos fora da ordem da casa: {list(e.keys())}")
    if falhas:
        print("[FALHA no round-trip] revertendo canonico.json:")
        for f_ in falhas:
            print("   -", f_)
        canon_path.write_text(orig_canon, encoding="utf-8")
        for t in prontos:
            (args.kb / "termos" / t["_arquivo"]).unlink(missing_ok=True)
        return 1

    print(f"[ok] {len(prontos)} fichas criadas e relidas por rc_kb sem divergência")
    print(f"[ok] canonico.json: {len(existentes)} -> {len(novo_canon['termos'])} termos; "
          f"relacoes +{len(novas_arestas)}")

    # fila: o item que pediu o termo passa a aplicado
    marcados = 0
    if not args.sem_fila and fila_path.exists():
        por_codigo = {t["codigo"]: t for t in prontos}
        with fila_path.open(encoding="utf-8-sig", newline="") as fh:
            leitor = csv.DictReader(fh)
            campos = list(leitor.fieldnames or [])
            linhas = list(leitor)
        for l in linhas:
            fid = (l.get("id") or "").strip()
            alvo = next((t for t in prontos if str(t.get("fila_id", "")) == fid), None)
            if alvo is None:
                continue
            l["status"] = "aplicada"
            l["data_aplicada"] = meta["data"]
            l["curador"] = meta.get("curador", "—")
            l["codigo_afetado"] = alvo["codigo"]
            marcados += 1
        with fila_path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=campos, lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
        print(f"[ok] fila: {marcados} item(ns) marcado(s) como aplicada")

    if not args.sem_changelog and changelog_path.exists():
        texto = changelog_path.read_text(encoding="utf-8")
        entrada = [f"\n## {meta['data']} — lote {meta.get('lote','?')}: "
                   f"{len(prontos)} termos novos (padrão {meta.get('padrao_fonte','Y')})\n",
                   f"Curadoria: {meta.get('curador','—')}. Ferramenta: `ferramentas/rc_termo.py` "
                   f"a partir de `{args.spec.name}`. Autorização: {meta.get('despacho','—')}.\n",
                   f"Fonte registrada: **{meta.get('fonte','—')}** em `biblio.json`. "
                   f"`canonico.json` foi de {len(existentes)} para {len(novo_canon['termos'])} termos; "
                   f"`relacoes` ganhou {len(novas_arestas)} arestas.\n"]
        for t in prontos:
            entrada.append(f"- {t['codigo']} **{t['nome']}** ({t['categoria']} / {t['subcategoria']}; "
                           f"status {t['status']}) — origem: {meta.get('slug','—')}, "
                           f"item {t.get('fila_id','—')} da fila")
        changelog_path.write_text(texto.rstrip() + "\n" + "\n".join(entrada) + "\n", encoding="utf-8")
        print(f"[ok] CHANGELOG recebeu a entrada do lote {meta.get('lote','?')}")

    print("[próximo passo] rc_qa.py --tudo · rc_indice.py --checar · testes/test_pipeline.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
