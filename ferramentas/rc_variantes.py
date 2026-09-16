# -*- coding: utf-8 -*-
"""
rc_variantes — extrai a camada variante -> canônico que vive na PROSA das fichas KB-RC.

A KB-RC documenta erros de STT de três modos diferentes, nenhum deles estruturado:
  1. campo da seção "Etimologia e Grafias" (Variações / Variações STT capturadas / Grafia STT);
  2. anotações de prosa («STT "Alamaior"», "STT «quarques» = quarks", "grafia oral … por erro de STT");
  3. seções de governança ("Quarentena Terminológica": **Brahma** (RC-037) — NUNCA "Brama";
     "Forma deprecada: Impérial. Forma correta/remissão: Perpérion — RC-087").

Este script converte os três modos num único CSV machine-readable, que é a **camada 2**
do fluxo de revisão (variante -> canônico), sem inventar nenhuma grafia: cada linha
carrega o trecho-fonte e o arquivo de origem como evidência.

Uso:
    python ferramentas/rc_variantes.py --kb KB-RC --saida ferramentas/dados/variantes-kb-extraidas.csv
    python ferramentas/rc_variantes.py --kb KB-RC --transcricao "arquivo.txt"   # + cobertura
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_kb as K  # noqa: E402
import rc_lexicon as L  # noqa: E402

ASPAS = r"[«\"'“”‘’]"
FECHA = r"[»\"'“”‘’]"

# «STT "x"» / (STT 'x') / STT «x»
RE_STT_SIMPLES = re.compile(r"STT\s*" + ASPAS + r"([^»\"'“”‘’\n]{2,70})" + FECHA)
# STT «x» = y   |  STT «x» prov. "y"
RE_STT_MAPEADO = re.compile(
    r"STT\s*" + ASPAS + r"([^»\"'“”‘’\n]{2,60})" + FECHA +
    r"\s*(?:=|→|prov\.?|provavelmente|corrigid[oa] para|l[eê]-se|leia-se)\s*" +
    ASPAS + r"?([^»\"'“”‘’,;)\n]{2,60})")
# STT: a, b, c   |  Variações de STT: a, b, c   |  Variações STT capturadas: ...
RE_CAMPO_STT = re.compile(
    r"(?:Varia[çc][õo]es (?:de )?STT(?: capturadas| posteriores)?|Grafia STT|STT)\s*:?\s*(.+)",
    re.I)
# Forma deprecada: X. Forma correta/remissão: Y — RC-NNN
RE_DEPRECADA = re.compile(
    r"Forma deprecada:\s*(.+?)\.\s*Forma correta/remi[çs][ãa]o:\s*(.+?)(?:\s*[—-]\s*(RC-\d{3}))?", re.I)
# **Canon** (RC-NNN) — NUNCA "X"
RE_NUNCA_LINHA = re.compile(r"NUNCA", re.I)
RE_CANON_COD = re.compile(r"\*\*([^*]{2,60})\*\*\s*\(((?:RC-\d{3})(?:\s*/\s*RC-\d{3})*)\)")
RE_NUNCA_ITEM = re.compile(r"NUNCA\s+" + ASPAS + r"([^»\"'“”‘’\n]{2,60})" + FECHA, re.I)
# grafia oral ... registrada como "X" por erro de STT
RE_ORAL = re.compile(r"registrad[ao] como\s*" + ASPAS + r"([^»\"'“”‘’\n]{2,70})" + FECHA +
                     r"[^.]{0,60}?erro de STT", re.I)
# X (STT «y») -> o alvo é X, o termo imediatamente anterior à anotação
RE_STT_PARENTETICO = re.compile(
    r"([A-ZÀ-Ü][\wÀ-ÿ'´\-]*(?:\s+[A-ZÀ-Üa-zà-ÿ][\wÀ-ÿ'´\-]*){0,3})\s*\(\s*(?:[^()]{0,30}?\b)?"
    r"STT\s*" + ASPAS + r"([^»\"'“”‘’\n]{2,60})" + FECHA)
# corruptela
RE_CORRUPTELA = re.compile(r"corruptela[^.\n]{0,40}?" + ASPAS + r"([^»\"'“”‘’\n]{2,50})" + FECHA, re.I)


def _limpa_alvo(texto: str) -> str:
    """Alvos canônicos vêm da prosa: remove quebras de linha, cabeçalhos e markdown."""
    texto = texto.split("\n")[0]
    texto = re.sub(r"^#+\s*", "", texto).strip()
    texto = re.sub(r"[*_`]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip(" .;:,")
    return texto[:70]


def _canonico(f: K.Ficha) -> str:
    if f.grafia_preferida:
        gp = f.grafia_preferida[0]
        # grafia preferida às vezes vem com texto de governança junto; pega só a forma curta
        gp = re.split(r"\s*(?:fixada|antiga|Varia|STT|:)", gp)[0].strip(" .;")
        if 2 < len(gp) < 70:
            return gp
    return f.nome or ""


LIXO = re.compile(r"[*`_|#>\[\]{}]|\*{2,}|^\W+$")


def _divide_lista(texto: str) -> list[str]:
    itens = re.split(r"\s*/\s*|\s*;\s*|\s*,\s*", texto.strip(" .;"))
    out = []
    for i in itens:
        i = i.strip(" .;«»\"'“”‘’()")
        i = re.sub(r"^(todas corrigidas para|prov\.|no|na|em)\b.*$", "", i, flags=re.I).strip()
        if LIXO.search(i):          # máscaras de redação (`p****`) e artefatos de Markdown
            continue
        if 2 < len(i) < 70 and not i.isdigit():
            out.append(i)
    return out


def extrair_da_ficha(f: K.Ficha, texto: str) -> list[dict]:
    """Devolve as linhas variante->canônico encontradas numa ficha."""
    canon = _limpa_alvo(_canonico(f))
    linhas: list[dict] = []

    def add(variante: str, classe: str, alvo: str, evidencia: str, codigo: str = "",
            origem: str = "prosa", mapeamento: str = "baixa") -> None:
        for v in _divide_lista(variante):
            if L.norm(v) == L.norm(alvo or canon) or not v:
                continue
            alvo_limpo = _limpa_alvo(alvo) if alvo else canon
            risco = "sim" if L.norm(v) in GUARDA else "nao"
            # alvo longo (>4 palavras) não é grafia canônica: é título de conceito.
            # Esses pares documentam como o conceito foi referido oralmente, não
            # autorizam substituição de palavra comum por título.
            if len(alvo_limpo.split()) > 4 or len(alvo_limpo) > 45:
                mapeamento = "referencia_oral"
            linhas.append(dict(codigo=codigo or f.codigo, canonico=alvo_limpo,
                               variante=v, classe=classe, origem=origem,
                               confianca_mapeamento=mapeamento, risco_palavra_comum=risco,
                               evidencia=re.sub(r"\s+", " ", evidencia)[:180],
                               arquivo=f.arquivo, status=f.status,
                               confianca=f.confianca_fonte))

    # 1) campos estruturados da seção Etimologia e Grafias
    eti = f.secoes.get("Etimologia e Grafias", "")
    for v in f.variacoes:
        # ATENÇÃO: "Variações" na KB mistura equivalência conceitual (Javé ~ Criador)
        # com grafia alternativa. Não usar como regra de substituição.
        add(v, "variacao", canon, eti[:180], origem="etimologia", mapeamento="conceitual")
    for v in f.variacoes_stt:
        add(v, "stt", canon, eti[:180], origem="etimologia", mapeamento="alta")
    for m in RE_CAMPO_STT.finditer(eti):
        add(m.group(1), "stt", canon, m.group(0), origem="etimologia", mapeamento="alta")

    # 2) prosa: STT «x» = y  (mapeamento explícito, prioridade)
    for m in RE_STT_MAPEADO.finditer(texto):
        add(m.group(1), "stt_mapeado", m.group(2).strip(" .;"),
            texto[max(0, m.start() - 60):m.end() + 20], origem="prosa", mapeamento="alta")
    # 2b) X (STT «y»): o alvo é o termo imediatamente anterior à anotação
    for m in RE_STT_PARENTETICO.finditer(texto):
        add(m.group(2), "stt_contextual", m.group(1).strip(" .;"),
            texto[max(0, m.start() - 40):m.end() + 20], origem="parentetico", mapeamento="alta")
    # 3) prosa: STT «x» (canônico = o termo da ficha)
    for m in RE_STT_SIMPLES.finditer(texto):
        trecho = texto[max(0, m.start() - 70):m.end() + 40]
        if RE_STT_MAPEADO.search(texto[max(0, m.start() - 5):m.end() + 60]):
            continue  # já capturado como mapeamento explícito
        add(m.group(1), "stt", canon, trecho)
    # 4) forma deprecada com remissão
    for m in RE_DEPRECADA.finditer(texto):
        alvo = m.group(2).strip(" .;")
        add(m.group(1), "deprecada", alvo, m.group(0), origem="deprecada", mapeamento="alta")
    # 5) quarentena terminológica: NUNCA "X"
    if f.quarentena:
        for linha in f.quarentena.splitlines():
            if not RE_NUNCA_LINHA.search(linha):
                continue
            canons = RE_CANON_COD.findall(linha)
            proibidos = [x for m in RE_NUNCA_ITEM.finditer(linha) for x in _divide_lista(m.group(1))]
            if not canons:
                continue
            pares = list(zip(proibidos, [c for c, _ in canons] * len(proibidos))) if len(canons) == 1 \
                else list(zip(proibidos, [c for c, _ in canons]))
            for proibido, canon_linha in pares:
                cod = next((cd for c, cd in canons if c == canon_linha), "")
                add(proibido, "nunca", canon_linha, linha, codigo=cod.split("/")[0],
                    origem="quarentena", mapeamento="alta")
    # 6) grafia oral registrada por erro de STT / corruptelas
    for rx, classe in ((RE_ORAL, "oral"), (RE_CORRUPTELA, "corruptela")):
        for m in rx.finditer(texto):
            add(m.group(1), classe, canon, texto[max(0, m.start() - 80):m.end() + 30],
                origem="prosa", mapeamento="media")
    return linhas


GUARDA: set[str] = set()


def carregar_guarda(caminho: Path) -> None:
    global GUARDA
    if caminho.exists():
        GUARDA = {L.norm(l.strip()) for l in caminho.read_text(encoding="utf-8").splitlines()
                  if l.strip() and not l.lstrip().startswith("#")}


def extrair_tudo(raiz_kb: Path) -> list[dict]:
    dir_termos = raiz_kb / "termos"
    todas: list[dict] = []
    for caminho in sorted(dir_termos.glob("RC-*.md")):
        texto = caminho.read_text(encoding="utf-8")
        f = K.carregar_ficha(caminho)
        todas += extrair_da_ficha(f, texto)
    # deduplica preservando a primeira evidência
    vistas, out = set(), []
    for l in todas:
        k = (L.norm(l["variante"]), L.norm(l["canonico"]), l["classe"])
        if k in vistas:
            continue
        vistas.add(k)
        out.append(l)
    return out


def cobertura(linhas: list[dict], transcricao: Path) -> list[dict]:
    """Marca quais variantes extraídas ocorrem de fato na transcrição."""
    corpo = L.norm(transcricao.read_text(encoding="utf-8-sig"))
    for l in linhas:
        l["ocorrencias"] = len(re.findall(r"\b" + re.escape(L.norm(l["variante"])) + r"\b", corpo))
    return linhas


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Extrai a camada variante->canônico das fichas KB-RC.")
    ap.add_argument("--kb", type=Path, default=Path("KB-RC"))
    ap.add_argument("--saida", type=Path, default=Path("ferramentas/dados/variantes-kb-extraidas.csv"))
    ap.add_argument("--transcricao", type=Path, default=None,
                    help="se informado, conta ocorrências de cada variante no texto")
    args = ap.parse_args(argv)

    raiz = Path(__file__).resolve().parent.parent
    kb = args.kb if args.kb.is_absolute() else raiz / args.kb
    saida = args.saida if args.saida.is_absolute() else raiz / args.saida

    guarda_path = raiz / "ferramentas" / "vocabular-guarda-pt.txt"
    carregar_guarda(guarda_path)
    linhas = extrair_tudo(kb)
    if args.transcricao:
        txt = args.transcricao if args.transcricao.is_absolute() else raiz / args.transcricao
        linhas = cobertura(linhas, txt)
    else:
        for l in linhas:
            l["ocorrencias"] = ""

    por_classe = Counter(l["classe"] for l in linhas)
    codigos = {l["codigo"] for l in linhas}
    saida.parent.mkdir(parents=True, exist_ok=True)
    campos = ["variante", "canonico", "codigo", "classe", "origem", "confianca_mapeamento",
              "risco_palavra_comum", "ocorrencias", "status", "confianca", "arquivo", "evidencia"]
    with saida.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        for l in sorted(linhas, key=lambda x: (-(x["ocorrencias"] or 0), x["classe"], x["variante"].lower())):
            w.writerow(l)

    print(f"[ok] {len(linhas)} pares variante->canônico extraídos de {len(codigos)} fichas")
    print("     por classe:", dict(por_classe))
    if args.transcricao:
        com = [l for l in linhas if l["ocorrencias"]]
        print(f"[ok] {len(com)} dessas variantes ocorrem na transcrição "
              f"({sum(l['ocorrencias'] for l in com)} ocorrências no total)")
        subst = [l for l in com if l["confianca_mapeamento"] in ("alta", "media")
                 and l["risco_palavra_comum"] == "nao"]
        arriscadas = [l for l in com if l["confianca_mapeamento"] in ("alta", "media")
                      and l["risco_palavra_comum"] == "sim"]
        print(f"[!]  {len(arriscadas)} regras cuja variante é palavra comum do português "
              f"(exigem contexto; não aplicar às cegas): "
              f"{', '.join(sorted({l['variante'] for l in arriscadas})[:12])}")
        print(f"[ok] das quais {len(subst)} são regra de SUBSTITUIÇÃO "
              f"(mapeamento alta/media); as demais são equivalência conceitual")
        for l in sorted(subst, key=lambda x: -x["ocorrencias"])[:25]:
            print(f"     {l['ocorrencias']:3d}x  {l['variante'][:28]:28s} -> {l['canonico'][:28]:28s} "
                  f"[{l['codigo']} {l['classe']}/{l['confianca_mapeamento']}]")
    print(f"[ok] gravado em {saida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
