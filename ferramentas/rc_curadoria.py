# -*- coding: utf-8 -*-
"""rc_curadoria — aplica a fila de curadoria da KB-RC, com evidência e trilha.

Fecha o ciclo do Guia v2 §10: o revisor **propõe** (em `transcricoes/<slug>/40-devolucao/` e na
fila `KB-RC/_fila-de-curadoria.csv`); o curador **aplica** na fonte de verdade. Esta ferramenta é
a mão do curador — mecânica onde dá para ser mecânica, e explícita sobre o que não é.

O que ela faz hoje (`--tipo nova-variante`, o único lote totalmente mecânico):

1. localiza a ficha pelo `codigo_afetado`;
2. **atesta** cada variante no bruto da transcrição de origem (contagem com fronteira de palavra,
   a mesma disciplina do portão G3) — variante não atestada NÃO é aplicada sem `--forcar`;
3. grava a variante em `## Etimologia e Grafias` → rótulo STT (criando a seção quando a ficha
   não a tem, na posição canônica);
4. registra a proveniência em `## Atualização` (quem, quando, quantas ocorrências, item da fila);
5. marca a linha da fila como `aplicada` e acrescenta a entrada no `KB-RC/CHANGELOG.md`.

O que ela NÃO faz, e por quê:

- **novo-termo**: exige código novo (RC-947+), entrada em `canonico.json` e — antes de tudo — o
  registro da fonte. Uma transcrição do YouTube ainda não tem código em `biblio.json`, e a de
  referência nem URL tem (`metadados.yaml: url: null`). Criar termo citando fonte inexistente
  envenena a base.
- **correcao-ficha**: é reescrita de prosa curatorial (status, definições, alertas de falso amigo).
  Julgamento humano, uma ficha por vez.
- **divergencia-factual**: já está tratada no produto como `[NOTA]`. Na KB vira alerta de
  Quarentena ou nada — decide o Comandante.

Uso:
    python ferramentas/rc_curadoria.py --simular                  # relatório, não toca em nada
    python ferramentas/rc_curadoria.py --aplicar                  # aplica nova-variante
    python ferramentas/rc_curadoria.py --aplicar --ids 0011,0014  # só estes itens
    python ferramentas/rc_curadoria.py --aplicar --sem-changelog   # CHANGELOG à mão depois
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_kb as KB  # noqa: E402
import rc_lexicon as L  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
FILA_PADRAO = RAIZ / "KB-RC" / "_fila-de-curadoria.csv"
CHANGELOG_PADRAO = RAIZ / "KB-RC" / "CHANGELOG.md"
ROTULO_STT_NOVO = "Variações STT capturadas"
ORDEM_SECOES = KB.SECOES  # posição canônica de "Etimologia e Grafias" entre as seções


# --------------------------------------------------------------------------- fila


def carregar_fila(caminho: Path) -> tuple[list[dict], list[str]]:
    with caminho.open(encoding="utf-8-sig", newline="") as fh:
        leitor = csv.DictReader(fh)
        campos = list(leitor.fieldnames or [])
        return list(leitor), campos


def gravar_fila(caminho: Path, linhas: list[dict], campos: list[str]) -> None:
    with caminho.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


def variantes_do_item(linha: dict) -> list[str]:
    """'arcontos / arces / arcos' -> ['arcontos', 'arces', 'arcos']."""
    bruto = (linha.get("termo") or "").strip()
    partes = [p.strip(" .,;") for p in re.split(r"\s*/\s*|\s*;\s*", bruto)]
    return [p for p in partes if p and p not in {"—", "-"}]


# ------------------------------------------------------------------------ atestação


def bruto_de(slug: str, raiz: Path = RAIZ) -> Path | None:
    cand = raiz / "transcricoes" / slug / "00-fonte" / "transcricao-bruta.txt"
    return cand if cand.exists() else None


def atestar(texto_norm: str, variante: str) -> int:
    """Ocorrências com fronteira de palavra — 'Demiurg' não casa dentro de 'Demiurgo'."""
    v = L.norm(variante)
    if not v:
        return 0
    return len(re.findall(r"\b" + re.escape(v) + r"\b", texto_norm))


# ------------------------------------------------------------------ cirurgia na ficha


def _span_secao(texto: str, titulo: str) -> tuple[int, int] | None:
    """(início, fim) do corpo de '## <titulo>', sem o cabeçalho."""
    m = re.search(r"^##\s+" + re.escape(titulo) + r"\s*$(.*?)(?=^##\s|\Z)", texto, re.S | re.M)
    return (m.start(1), m.end(1)) if m else None


def _ponto_de_insercao(texto: str, titulo_novo: str) -> int:
    """Onde inserir uma seção ausente: depois da seção canonicamente anterior."""
    ordem = [s for s in ORDEM_SECOES if re.search(r"^##\s+" + re.escape(s) + r"\s*$", texto, re.M)]
    if titulo_novo in ordem:
        ordem.remove(titulo_novo)
    anterior = None
    for s in ORDEM_SECOES:
        if s == titulo_novo:
            break
        if s in ordem:
            anterior = s
    if anterior:
        span = _span_secao(texto, anterior)
        if span:
            return span[1]
    # sem seção anterior: depois do título H1 (ou do frontmatter, se não houver H1)
    m = re.search(r"^#\s+.*$", texto, re.M)
    if m:
        return m.end()
    m = re.search(r"^\+\+\+\s*$", texto, re.M)  # fim do frontmatter
    if m:
        return m.end()
    return 0


def _linha_rotulo_stt(secao: str) -> re.Match | None:
    """A linha de rótulo STT efetiva (a mesma precedência de rc_kb._rotulo)."""
    for rotulo in KB.ROTULOS_STT:
        padrao = re.compile(
            r"(?P<pre>^[ \t]*(?:[-*][ \t]*)?\*\*[ \t]*" + re.escape(rotulo) + r"[ \t]*:?\*\*[ \t]*:?[ \t]*)"
            r"(?P<val>[^\n]*)$",
            re.M | re.I,
        )
        m = padrao.search(secao)
        if m:
            return m
        padrao2 = re.compile(
            r"(?P<pre>^[ \t]*[-*][ \t]*" + re.escape(rotulo) + r"[ \t]*:?[ \t]*)(?P<val>[^\n]*)$",
            re.M | re.I,
        )
        m = padrao2.search(secao)
        if m:
            return m
    return None


def _inserir(texto: str, pos: int, bloco: str) -> str:
    """Insere `bloco` em `pos` com exatamente uma linha em branco antes e depois.

    Sem isto a seção criada cola no cabeçalho seguinte (`- item\n## Ampliação`), que é
    markdown inválido, e o arquivo fica com três linhas em branco onde havia uma.
    """
    antes = texto[:pos].rstrip("\n")
    depois = texto[pos:].lstrip("\n")
    meio = bloco.strip("\n")
    if not depois:
        return antes + "\n\n" + meio + "\n"
    return antes + "\n\n" + meio + "\n\n" + depois


def aplicar_variantes(caminho: Path, ficha: KB.Ficha, novas: list[str], nota: str) -> dict:
    """Grava `novas` na ficha. Devolve o que fez — nunca silencia."""
    texto = caminho.read_text(encoding="utf-8")
    ja = {L.norm(v) for v in ficha.variacoes_stt + ficha.variacoes + ficha.grafia_preferida}
    canonico = L.norm(ficha.nome)
    adicionar, puladas = [], []
    for v in novas:
        n = L.norm(v)
        if not n:
            continue
        if n in ja:
            puladas.append((v, "já constava na ficha"))
        elif n == canonico:
            puladas.append((v, "é a própria grafia canônica"))
        elif n and re.search(r"\b" + re.escape(n) + r"\b", canonico):
            puladas.append((v, "está contida no canônico — só faria ruído"))
        else:
            adicionar.append(v)
            ja.add(n)

    if not adicionar:
        return {"adicionadas": [], "puladas": puladas, "secao_criada": False, "rotulo": None}

    span = _span_secao(texto, "Etimologia e Grafias")
    secao_criada = False
    if span is None:
        bloco = ("## Etimologia e Grafias\n"
                 f"- **Grafia preferida:** {ficha.nome}\n"
                 f"- **{ROTULO_STT_NOVO}:** " + "; ".join(adicionar))
        texto = _inserir(texto, _ponto_de_insercao(texto, "Etimologia e Grafias"), bloco)
        secao_criada = True
        rotulo_usado = ROTULO_STT_NOVO + " (seção criada)"
    else:
        secao = texto[span[0]:span[1]]
        m = _linha_rotulo_stt(secao)
        if m:
            valor = m.group("val").rstrip()
            valor = valor.rstrip(";•| ").rstrip()
            novo_valor = (valor + "; " if valor else "") + "; ".join(adicionar)
            nova_secao = secao[:m.start("val")] + novo_valor + secao[m.end("val"):]
            rotulo_usado = m.group("pre").strip().strip("-* ").strip(":* ")
        else:
            # sem rótulo STT: entra depois da grafia preferida, ou no fim da seção
            gp = re.search(r"^[ \t]*[-*][ \t]*\*\*[ \t]*Grafia[^\n]*$", secao, re.M | re.I)
            linha = f"\n- **{ROTULO_STT_NOVO}:** " + "; ".join(adicionar)
            pos = gp.end() if gp else len(secao.rstrip())
            nova_secao = secao[:pos] + linha + secao[pos:]
            rotulo_usado = ROTULO_STT_NOVO + " (rótulo novo na seção existente)"
        texto = texto[:span[0]] + nova_secao + texto[span[1]:]

    # proveniência: entra em "## Atualização" (criada se não existir)
    span_at = _span_secao(texto, "Atualização")
    if span_at is None:
        texto = _inserir(texto, _ponto_de_insercao(texto, "Atualização"),
                         "## Atualização\n" + nota.strip("\n"))
    else:
        corpo = texto[span_at[0]:span_at[1]].rstrip("\n")
        resto = texto[span_at[1]:]
        # o fim da seção é exatamente onde o próximo "## " começa: com uma quebra só,
        # o cabeçalho seguinte fica colado na última linha da nota (markdown inválido)
        separador = "\n\n" if resto.strip() else "\n"
        texto = texto[:span_at[0]] + corpo + "\n" + nota.strip("\n") + separador + resto

    # frontmatter: data de atualização
    texto = re.sub(r'^(atualizado\s*=\s*)"[^"]*"', r'\1"' + date.today().isoformat() + '"',
                   texto, count=1, flags=re.M)

    caminho.write_text(texto, encoding="utf-8")
    return {"adicionadas": adicionar, "puladas": puladas,
            "secao_criada": secao_criada, "rotulo": rotulo_usado}


# ------------------------------------------------------------------------- changelog


def entrada_changelog(itens: list[dict], data: str, curador: str, slug: str) -> str:
    linhas = [f"\n## {data} — lote 01: variantes STT devolvidas por `{slug}`\n"]
    linhas.append(f"Curadoria: {curador}. Ferramenta: `ferramentas/rc_curadoria.py` "
                  "(atestação no bruto antes de gravar).\n")
    for it in itens:
        cod = it["codigo"]
        vs = ", ".join(f'"{v}"' for v in it["adicionadas"]) or "—"
        n = it.get("ocorrencias") or 0
        ocorr = f" ({n} ocorrência{'s' if n != 1 else ''} no bruto)" if n else ""
        linhas.append(f"- {cod} acrescentadas {vs} — origem: {slug}, item {it['id']} da fila" + ocorr)
    return "\n".join(linhas) + "\n"


def acrescentar_changelog(caminho: Path, entrada: str) -> None:
    texto = caminho.read_text(encoding="utf-8")
    caminho.write_text(texto.rstrip() + "\n" + entrada, encoding="utf-8")


# ------------------------------------------------------------------------------ CLI


STATUS_APRAZAVEIS = {"", "pendente", "proposta"}


def selecionar(linhas: list[dict], tipo: str, ids: list[str], incluir_bloqueadas: bool = False) -> list[dict]:
    """Itens do tipo pedido que ainda podem ser aplicados.

    `aplicada` nunca volta (idempotência); `bloqueada` só entra com pedido explícito —
    o bloqueio é uma decisão curatorial registrada na coluna evidencia, não um acaso.
    """
    sel = [l for l in linhas if (l.get("tipo") or "").strip() == tipo]
    if ids:
        # pedido explícito por id: o operador assume o que está pedindo,
        # inclusive rever um item já aplicado (o guarda de duplicação na ficha protege)
        return [l for l in sel if (l.get("id") or "").strip() in ids]
    aceitos = set(STATUS_APRAZAVEIS) | ({"bloqueada"} if incluir_bloqueadas else set())
    # "aplicada" nunca volta sozinha: é isso que torna a ferramenta idempotente
    return [l for l in sel if (l.get("status") or "").strip().lower() in aceitos]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Aplica a fila de curadoria da KB-RC.")
    ap.add_argument("--fila", type=Path, default=FILA_PADRAO)
    ap.add_argument("--kb", type=Path, default=RAIZ / "KB-RC")
    ap.add_argument("--tipo", default="nova-variante",
                    help="tipo de item aplicável mecanicamente (default: nova-variante)")
    ap.add_argument("--ids", default="", help="restringe a estes ids, separados por vírgula")
    ap.add_argument("--curador", default="Agente 86")
    ap.add_argument("--data", default=date.today().isoformat())
    ap.add_argument("--simular", action="store_true", help="não grava nada (default)")
    ap.add_argument("--aplicar", action="store_true", help="grava fichas, fila e CHANGELOG")
    ap.add_argument("--forcar", action="store_true", help="aplica mesmo sem atestação no bruto")
    ap.add_argument("--sem-changelog", action="store_true")
    ap.add_argument("--incluir-bloqueadas", action="store_true",
                    help="tenta também os itens com status 'bloqueada'")
    args = ap.parse_args(argv)

    aplicar = args.aplicar and not args.simular
    ids = [i.strip() for i in args.ids.split(",") if i.strip()]
    linhas, campos = carregar_fila(args.fila)
    itens = selecionar(linhas, args.tipo, ids, args.incluir_bloqueadas)
    if not itens:
        print(f"[nada a fazer] nenhum item do tipo '{args.tipo}'"
              + (f" com ids {ids}" if ids else ""))
        return 0

    fichas = KB.carregar_fichas(str(args.kb))
    caches_bruto: dict[str, str] = {}
    aplicados, bloqueados = [], []

    for l in itens:
        codigo = (l.get("codigo_afetado") or "").strip()
        ficha = fichas.get(codigo)
        variantes = variantes_do_item(l)
        slug = (l.get("origem_slug") or "").strip()
        if ficha is None:
            bloqueados.append((l, f"ficha {codigo or '—'} não encontrada em {args.kb}/termos"))
            continue
        if not variantes:
            bloqueados.append((l, "nenhuma variante legível no campo termo"))
            continue
        if slug not in caches_bruto:
            arq = bruto_de(slug)
            caches_bruto[slug] = L.norm(arq.read_text(encoding="utf-8")) if arq else ""
        texto_bruto = caches_bruto[slug]
        contas = {v: (atestar(texto_bruto, v) if texto_bruto else 0) for v in variantes}
        # aplicação parcial: o que está atestado entra; o que não está fica sinalizado.
        # Bloquear o item inteiro por causa de uma variante puniria as outras, que têm evidência.
        nao_atestadas = [v for v, n in contas.items() if n == 0]
        atestadas = [v for v, n in contas.items() if n > 0] or (variantes if args.forcar else [])
        if not atestadas:
            bloqueados.append((l, "nenhuma variante ocorre no bruto: "
                               + ", ".join(f"'{v}'" for v in nao_atestadas)
                               + " (use --forcar se a evidência for externa ao bruto)"))
            continue

        total = sum(contas.values())
        nota = (f"\n### {args.data} — variante STT devolvida por `{slug}` (fila {l['id']})\n"
                + "".join(f'- **"{v}"** — {contas[v]} ocorrência(s) no bruto; adjudicada no '
                          f"livro-razão da transcrição. Curadoria: {args.curador}.\n"
                          for v in atestadas)
                + "".join(f'- **"{v}"** — NÃO atestada no bruto; ficou de fora (evidência externa '
                          "ou forma inexistente).\n" for v in nao_atestadas if not args.forcar)
                + (f"- Evidência do item: {l.get('evidencia','').strip()}\n" if l.get("evidencia") else ""))

        if aplicar:
            res = aplicar_variantes(args.kb / "termos" / ficha.arquivo, ficha, atestadas, nota)
        else:
            ja = {L.norm(v) for v in ficha.variacoes_stt + ficha.variacoes + ficha.grafia_preferida}
            res = {"adicionadas": [v for v in atestadas if L.norm(v) not in ja],
                   "puladas": [(v, "já constava") for v in atestadas if L.norm(v) in ja],
                   "secao_criada": not ficha.secoes.get("Etimologia e Grafias"),
                   "rotulo": "(simulação)"}
        res["nao_atestadas"] = nao_atestadas
        l["_res"] = res
        l["_contas"] = contas
        aplicados.append((l, res, total))
        if aplicar:
            l["status"] = "aplicada"
            l["data_aplicada"] = args.data
            l["curador"] = args.curador

    modo = "APLICADO" if aplicar else "SIMULAÇÃO"
    print(f"\n=== {modo}: {args.tipo} — {len(aplicados)} item(ns), {len(bloqueados)} bloqueado(s) ===")
    for l, res, total in aplicados:
        vs = ", ".join(f'"{v}"' for v in res["adicionadas"]) or "(nenhuma nova)"
        extra = " · seção Etimologia criada" if res["secao_criada"] else ""
        pul = "".join(f' · pulada "{v}" ({m})' for v, m in res["puladas"])
        na_list = res.get("nao_atestadas", [])
        na = (" · SEM EVIDÊNCIA: " + ", ".join(f"'{v}'" for v in na_list)) if na_list else ""
        print(f"  {l['id']} {l['codigo_afetado']:<8} {vs}{extra} · {total} ocorr.{pul}{na}")
    for l, motivo in bloqueados:
        print(f"  {l['id']} {l.get('codigo_afetado','—'):<8} BLOQUEADO — {motivo}")

    acrescentos = [(l, res, total) for l, res, total in aplicados if res["adicionadas"]]
    if aplicar and not acrescentos:
        # reexecução: as variantes já constam das fichas. Nada a gravar — e gravar
        # produziria uma entrada de CHANGELOG vazia ("acrescentadas —"), que é ruído.
        print("[ok] idempotente: nenhuma variante nova a acrescentar; fila e CHANGELOG intactos")
        return 0

    if aplicar:
        gravar_fila(args.fila, [{k: v for k, v in l.items() if not k.startswith("_")} for l in linhas],
                    campos)
        print(f"[ok] fila atualizada: {len(aplicados)} linha(s) como 'aplicada'")
        if acrescentos and not args.sem_changelog:
            entrada = entrada_changelog(
                [{"id": l["id"], "codigo": l["codigo_afetado"],
                  "adicionadas": res["adicionadas"], "ocorrencias": total}
                 for l, res, total in acrescentos],
                args.data, args.curador, (itens[0].get("origem_slug") or "").strip())
            acrescentar_changelog(CHANGELOG_PADRAO, entrada)
            print(f"[ok] {CHANGELOG_PADRAO.relative_to(RAIZ)} recebeu a entrada do lote")
        print("[próximo passo] rode rc_qa.py --tudo e testes/test_pipeline.py antes de commitar")
    return 0 if aplicados or not bloqueados else 1


if __name__ == "__main__":
    raise SystemExit(main())
