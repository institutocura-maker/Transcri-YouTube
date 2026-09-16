# -*- coding: utf-8 -*-
"""rc_indice — catálogo das transcrições: gera, confere e mantém `_indice.csv`.

Por que um catálogo derivado e não preenchido à mão: catálogo escrito a dedo mente
em duas semanas. Aqui quase todo campo é **medido no disco** — número de blocos,
palavras, marcadores, estágio — e o que não dá para medir vem do `metadados.yaml`
que a captura gravou. A coluna `estatus` é calculada pelos artefatos presentes, não
declarada: status aspiracional é a forma mais comum de autoengano em acervo.

Uso:
    python ferramentas/rc_indice.py                 # regenera _indice.csv e _indice.md
    python ferramentas/rc_indice.py --checar        # não escreve: reclama se estiver velho
    python ferramentas/rc_indice.py --checar --json # idem, para o CI
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_qa as QA  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
TRANSCRICOES = RAIZ / "transcricoes"
MARCADOR_RE = QA.MARCADOR_RE
PALAVRA_RE = re.compile(r"[\wÀ-ÿ']+")

CAMPOS = ["slug", "data", "titulo", "canal", "url", "duracao_min", "falantes", "estatus",
          "palavras_brutas", "palavras_revisadas", "blocos", "paragrafos", "notas",
          "a_confirmar", "inaudivel", "devolucao", "curadoria_aplicada", "revisor",
          "responsavel"]

# Estágio -> o que é obrigatório existir para que ele seja declarado (Plano §6.2).
ARTEFATOS = {
    "00-nova": ["00-fonte/transcricao-bruta.txt", "00-fonte/metadados.yaml"],
    "10-em-diagnostico": ["10-diagnostico/variantes-propostas.csv"],
    "20-em-revisao": ["20-blocos/"],
    "30-revisada": ["30-produto/transcricao-revisada.docx"],
    "40-devolvida": ["40-devolucao/devolucao-a-kb.md"],
}


def _contar(texto: str) -> int:
    return len(PALAVRA_RE.findall(texto))


def _corpo(pasta: Path) -> str:
    """Corpo do bruto: a linha mais longa do arquivo.

    O STT do YouTube entrega cabeçalho curto e o texto inteiro numa linha só. Usar a
    linha mais longa evita chutar um número fixo de linhas de cabeçalho, que muda de
    vídeo para vídeo.
    """
    arq = pasta / "00-fonte" / "transcricao-bruta.txt"
    if not arq.exists():
        return ""
    linhas = arq.read_text(encoding="utf-8").splitlines()
    return max(linhas, key=len) if linhas else ""


def medir(pasta: Path) -> dict:
    meta = QA.ler_metadados(pasta)
    resultado = meta.get("resultado", {}) or {}
    revisao = meta.get("revisao", {}) or {}
    bruto_meta = meta.get("bruto", {}) or {}

    blocos = QA._blocos(pasta)
    texto_blocos = "\n".join(b.read_text(encoding="utf-8") for b in blocos) if blocos else ""
    limpo = MARCADOR_RE.sub(" ", texto_blocos)
    corpo = _corpo(pasta)

    falantes = ""
    dir_falantes = pasta / "00-fonte"
    if (dir_falantes / "metadados.yaml").exists():
        nomes = re.findall(r'rotulo:\s*"?\[([^\]"]+)\]"?',
                           (dir_falantes / "metadados.yaml").read_text(encoding="utf-8"))
        falantes = "; ".join(dict.fromkeys(nomes))

    dev = pasta / "40-devolucao" / "devolucao-a-kb.md"
    return {
        "slug": pasta.name,
        "data": meta.get("data_gravacao", "") or "",
        "titulo": meta.get("titulo", "") or "",
        "canal": meta.get("canal", "") or "",
        "url": meta.get("url", "") or "",
        "duracao_min": meta.get("duracao_min", "") or "",
        "falantes": falantes,
        "estatus": QA.estagio(pasta),
        "palavras_brutas": _inteiro(bruto_meta.get("corpo_palavras")) or _contar(corpo),
        "palavras_revisadas": _contar(limpo),
        "blocos": len(blocos),
        "paragrafos": sum(1 for l in texto_blocos.splitlines()
                          if l.strip() and not l.startswith("#")),
        "notas": len(re.findall(r"\[NOTA:", texto_blocos)),
        "a_confirmar": len(re.findall(r"\[A CONFIRMAR:", texto_blocos)),
        "inaudivel": len(re.findall(r"\[INAUDÍVEL:", texto_blocos)),
        "devolucao": resultado.get("concluido_em", "") or "",
        "curadoria_aplicada": revisao.get("curadoria_aplicada", "pendente") or "pendente",
        "revisor": resultado.get("revisor", "") or "",
        "responsavel": meta.get("responsavel", "") or "Comandante",
    }


def _inteiro(v, padrao=0) -> int:
    try:
        return int(str(v).replace(".", "").strip())
    except (TypeError, ValueError):
        return padrao


def pastas() -> list[Path]:
    if not TRANSCRICOES.exists():
        return []
    return sorted(p for p in TRANSCRICOES.iterdir() if p.is_dir() and not p.name.startswith("_"))


def artefatos_faltando(pasta: Path, estagio: str) -> list[str]:
    """Confere se o estágio declarado tem os artefatos que o justificam."""
    faltam = []
    ordem = list(ARTEFATOS)
    if estagio not in ordem:
        return [f"estatus desconhecido '{estagio}'"]
    for est in ordem[:ordem.index(estagio) + 1]:
        for item in ARTEFATOS[est]:
            if not (pasta / item).exists():
                faltam.append(f"{est} exige {item}")
    return faltam


def escrever(linhas: list[dict]) -> None:
    with (TRANSCRICOES / "_indice.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(linhas)

    md = ["# Catálogo de transcrições", "",
          f"**{len(linhas)} transcrição(ões)** · gerado por `ferramentas/rc_indice.py` — não editar à mão.",
          "",
          "| slug | data | título | canal | estágio | blocos | palavras | `[NOTA]` | devolução | revisor |",
          "|---|---|---|---|---|---:|---:|---:|---|---|"]
    for l in linhas:
        md.append(f"| `{l['slug']}` | {l['data'] or '—'} | {l['titulo'] or '—'} | {l['canal'] or '—'} "
                  f"| **{l['estatus']}** | {l['blocos']} | {l['palavras_revisadas'] or l['palavras_brutas']:,} "
                  f"| {l['notas']} | {l['devolucao'] or '—'} | {l['revisor'] or '—'} |")
    md += ["", "## Estágios", "",
           "| estágio | critério |", "|---|---|",
           "| `00-nova` | pasta criada, bruto capturado e hash registrado |",
           "| `10-em-diagnostico` | motor rodou, fila de decisão gerada |",
           "| `20-em-revisao` | pelo menos um bloco revisado |",
           "| `30-revisada` | todos os blocos prontos, produto montado, QA verde |",
           "| `40-devolvida` | extrato final escrito |",
           "| `50-publicada` | curadoria aplicada na KB-RC e produto distribuído |",
           "| `90-suspensa` | parada por decisão ou falta de insumo |", "",
           "Regra: **o estágio só avança com o artefato correspondente presente** — quem",
           "declara o estágio é o disco, conferido por `rc_indice.py --checar` e pelo portão G7.",
           ""]
    (TRANSCRICOES / "_indice.md").write_text("\n".join(md), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Catálogo das transcrições.")
    ap.add_argument("--checar", action="store_true", help="não escreve: reclama se o catálogo estiver velho")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    linhas = [medir(p) for p in pastas()]
    problemas = []
    for l, pasta in zip(linhas, pastas()):
        faltam = artefatos_faltando(pasta, l["estatus"])
        if faltam:
            problemas.append(f"{l['slug']}: " + "; ".join(faltam[:3]))
        if not (pasta / "00-fonte" / "metadados.yaml").exists():
            problemas.append(f"{l['slug']}: sem metadados.yaml")

    if args.checar:
        csv_path = TRANSCRICOES / "_indice.csv"
        antigo = []
        if csv_path.exists():
            with csv_path.open(encoding="utf-8-sig", newline="") as fh:
                antigo = list(csv.DictReader(fh))
        if antigo != linhas:
            problemas.append("o catálogo está desatualizado (rode `rc_indice.py` sem --checar)")
        if args.json:
            print(json.dumps(dict(ok=not problemas, problemas=problemas, indice=linhas),
                             ensure_ascii=False, indent=1))
        else:
            for p in problemas:
                print("[checar]", p)
            if not problemas:
                print(f"[ok] catálogo em dia: {len(linhas)} transcrição(ões)")
        return 1 if problemas else 0

    escrever(linhas)
    if args.json:
        print(json.dumps(linhas, ensure_ascii=False, indent=1))
    else:
        print(f"[ok] {TRANSCRICOES/'_indice.csv'} — {len(linhas)} transcrição(ões)")
        for l in linhas:
            print(f"     {l['slug']:<48} {l['estatus']:<18} blocos={l['blocos']} palavras={l['palavras_revisadas']}")
        for p in problemas:
            print("[aviso]", p)
    return 1 if problemas else 0


if __name__ == "__main__":
    raise SystemExit(main())
