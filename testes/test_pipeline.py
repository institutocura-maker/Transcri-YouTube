# -*- coding: utf-8 -*-
"""Teste de fumaça do pipeline — sem dependência de pytest.

    python testes/test_pipeline.py

Cobre o que já quebrou de verdade neste projeto, para não quebrar de novo:

 1. todos os módulos importam;
 2. o validador de slug aceita o padrão e recusa acento, espaço, maiúscula e data inválida;
 3. a medição do bruto acha o corpo (a linha mais longa) e não chuta o cabeçalho;
 4. o montador DOCX preserva parágrafos, negrito e nota em itálico;
 5. o conversor Markdown não deixa asterisco à mostra em ênfase aninhada
    (**negrito com `código` dentro** e ***negrito-itálico*** já saíram errados);
 6. formas proibidas são varridas COM fronteira de palavra — "Demiurg" não pode
    acusar dentro de "Demiurgo", nem "enoteísmo" dentro de "henoteísmo";
 7. os portões rápidos do QA continuam verdes na transcrição de referência;
 8. o catálogo mede a transcrição de referência como ela é;
 9. o modelo de pasta continua íntegro (é dele que toda transcrição nova nasce).
"""
from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))

FIXTURE = RAIZ / "testes" / "fixtures" / "mini-transcricao.txt"
REFERENCIA = RAIZ / "transcricoes" / "2026-09-14-revelacoes-cosmicas-urgente"

_falhas: list[str] = []
_ok = 0


def verificar(nome: str, condicao: bool, detalhe: str = "") -> None:
    global _ok
    if condicao:
        _ok += 1
        print(f"  ok   {nome}")
    else:
        _falhas.append(f"{nome} — {detalhe}")
        print(f"  FALHA {nome} — {detalhe}")


# --------------------------------------------------------------------------------------
print("\n1. módulos importam")
modulos = {}
for nome in ["rc_kb", "rc_lexicon", "rc_variantes", "rc_diagnostico", "rc_docx",
             "md_para_docx", "rc_qa", "rc_indice", "rc_novo"]:
    try:
        modulos[nome] = __import__(nome)
        verificar(f"import {nome}", True)
    except Exception as exc:  # noqa: BLE001
        verificar(f"import {nome}", False, str(exc))

DX = modulos.get("rc_docx")
MD = modulos.get("md_para_docx")
QA = modulos.get("rc_qa")
IND = modulos.get("rc_indice")
NOVO = modulos.get("rc_novo")

# --------------------------------------------------------------------------------------
print("\n2. validador de slug")
if NOVO:
    bons = ["2026-10-02-lemuria-terry-fabris", "2027-01-15-jan-val-ellam", "2026-12-31-a"]
    for s in bons:
        verificar(f"aceita '{s}'", NOVO.validar_slug(s) is None, str(NOVO.validar_slug(s)))
    ruins = {
        "Revelações Cósmicas": "acento e maiúscula",
        "2026-10-02 titulo": "espaço",
        "2026-10-02-Titulo": "maiúscula",
        "lemuria-terry-fabris": "sem data",
        "2026-02-30-lemuria": "data inexistente",
        "2026-10-02-" + "x" * 70: "longo demais",
    }
    for s, por_que in ruins.items():
        verificar(f"recusa '{s[:34]}' ({por_que})", NOVO.validar_slug(s) is not None, "foi aceito")

# --------------------------------------------------------------------------------------
print("\n3. medição do bruto")
if NOVO:
    m = NOVO.medir_bruto(FIXTURE)
    verificar("sha256 tem 64 hex", re.fullmatch(r"[0-9a-f]{64}", m["sha256"]) is not None, m["sha256"])
    verificar("corpo detectado na linha 13", m["corpo_linha"] == 13, f"achou {m['corpo_linha']}")
    verificar("cabeçalho com 12 linhas", m["linhas_cabecalho"] == 12, f"achou {m['linhas_cabecalho']}")
    verificar("corpo tem palavras", m["corpo_palavras"] > 50, str(m["corpo_palavras"]))
    verificar("bytes batem com o arquivo", m["bytes"] == FIXTURE.stat().st_size)

# --------------------------------------------------------------------------------------
print("\n4. montador DOCX")
if DX:
    from docx import Document
    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "b.md"
        md.write_text("## Bloco 1 — teste\n\n**[JAN VAL ELLAM]** Texto com **negrito** "
                      "e uma nota [NOTA: no bruto, \"Xavé\"].\n", encoding="utf-8")
        itens = DX.analisar_blocos([md], [])
        saida = DX.montar(itens, Path(tmp) / "s.docx", "Título", "Subtítulo")
        verificar("arquivo gerado", saida.exists())
        d = Document(str(saida))
        textos = [p.text for p in d.paragraphs]
        verificar("heading presente", any(t.startswith("Bloco 1") for t in textos), str(textos[:4]))
        corpo = next(p for p in d.paragraphs if "negrito" in p.text)
        verificar("negrito aplicado", any(r.bold and r.text == "negrito" for r in corpo.runs))
        verificar("nota em itálico", any(r.italic and r.text.startswith("[NOTA") for r in corpo.runs))
        # o validador não pode punir a nota que cita o bruto
        verificar("nota não conta como sobrevivência",
                  DX.MARCADOR_RE.sub(" ", corpo.text).count("Xavé") == 0)

# --------------------------------------------------------------------------------------
print("\n5. conversor Markdown — ênfase aninhada")
if MD:
    from docx import Document
    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "d.md"
        md.write_text("# Título\n\n**Por que `bloco-01.md` e não `bloco-1.md`:** o glob "
                      "`bloco-*.md` ordena errado.\n\n- ***A Divina Colmeia*** e *Deep Utopia*.\n\n"
                      "```\n*.docx binary\n```\n", encoding="utf-8")
        MD.converter(md, Path(tmp) / "d.docx", "T", "S")
        d = Document(str(Path(tmp) / "d.docx"))
        for p in d.paragraphs:
            em_code = any(r.font.name == "Consolas" for r in p.runs)
            if em_code:
                continue
            verificar(f"sem markup à mostra em '{p.text[:38]}…'",
                      "*" not in p.text and "`" not in p.text, p.text[:80])
        negrito_codigo = next((p for p in d.paragraphs if "Por que" in p.text), None)
        verificar("negrito com código dentro",
                  bool(negrito_codigo) and any(r.bold and r.font.name == "Consolas" for r in negrito_codigo.runs))
        bi = next((p for p in d.paragraphs if "Divina Colmeia" in p.text), None)
        verificar("negrito-itálico (***…***)",
                  bool(bi) and any(r.bold and r.italic for r in bi.runs))

# --------------------------------------------------------------------------------------
print("\n6. fronteira de palavra nas formas proibidas")
if QA:
    # o texto contém só as formas corretas: as truncadas aparecem aqui apenas como
    # padrão de busca — se casarem, é porque a varredura está sem fronteira de palavra
    texto = "O Demiurgo e o henoteísmo aparecem aqui; as formas truncadas não devem casar."
    sem_marcador = QA.MARCADOR_RE.sub(" ", texto)
    for forma in ["Demiurg", "enoteísmo"]:
        n = len(re.findall(r"\b" + re.escape(forma) + r"\b", sem_marcador, re.I))
        verificar(f"'{forma}' não casa dentro da palavra correta", n == 0, f"{n} ocorrências")
    for forma in ["Demiurgo", "henoteísmo"]:
        n = len(re.findall(r"\b" + re.escape(forma) + r"\b", sem_marcador, re.I))
        verificar(f"'{forma}' casa", n == 1, f"{n} ocorrências")
    proibidas = QA.formas_proibidas(REFERENCIA, RAIZ / "KB-RC")
    verificar("formas proibidas derivadas da KB + ledger", len(proibidas) >= 10, f"{len(proibidas)}")
    verificar("Quarentena 'Sofia' capturada", "Sofia" in proibidas, str(sorted(proibidas)[:5]))

# --------------------------------------------------------------------------------------
print("\n7. portões rápidos na transcrição de referência")
if QA and REFERENCIA.exists():
    meta = QA.ler_metadados(REFERENCIA)
    verificar("metadados.yaml lido", meta.get("slug") == REFERENCIA.name, str(meta.get("slug")))
    for codigo, nome, funcao in QA.PORTOES:
        if codigo not in {"G1", "G2", "G4", "G7"}:
            continue
        status, detalhe = funcao(REFERENCIA, meta)
        verificar(f"{codigo} {nome}", status == QA.OK, f"{status}: {detalhe}")
    verificar("estágio medido no disco", QA.estagio(REFERENCIA) == "40-devolvida",
              QA.estagio(REFERENCIA))

# --------------------------------------------------------------------------------------
print("\n8. catálogo mede a referência")
if IND and REFERENCIA.exists():
    linha = IND.medir(REFERENCIA)
    verificar("8 blocos", linha["blocos"] == 8, str(linha["blocos"]))
    verificar("18.966 palavras revisadas", linha["palavras_revisadas"] == 18966, str(linha["palavras_revisadas"]))
    verificar("32 notas", linha["notas"] == 32, str(linha["notas"]))
    verificar("status 40-devolvida", linha["estatus"] == "40-devolvida", linha["estatus"])
    verificar("falantes listados", "JAN VAL ELLAM" in linha["falantes"], linha["falantes"])
    verificar("artefatos do estágio presentes",
              IND.artefatos_faltando(REFERENCIA, linha["estatus"]) == [])

# --------------------------------------------------------------------------------------
print("\n9. modelo de pasta íntegro")
MODELO = RAIZ / "transcricoes" / "_modelo"
esperados = ["README.md", "00-fonte/metadados.yaml", "00-fonte/midia/README.md",
             "10-diagnostico/README.md", "20-blocos/notas-de-revisao.md",
             "30-produto/README.md", "40-devolucao/README.md",
             "90-registro/diario-de-bordo.md", "90-registro/despachos/README.md"]
for rel in esperados:
    verificar(f"_modelo/{rel}", (MODELO / rel).exists())
if (MODELO / "00-fonte" / "metadados.yaml").exists():
    modelo_txt = (MODELO / "00-fonte" / "metadados.yaml").read_text(encoding="utf-8")
    verificar("modelo tem marcadores {{…}} para substituir", "{{slug}}" in modelo_txt)

# --------------------------------------------------------------------------------------
print(f"\n{'=' * 66}\n{_ok} verificações ok, {len(_falhas)} falhas")
for f in _falhas:
    print("  -", f)
sys.exit(1 if _falhas else 0)
