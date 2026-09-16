# -*- coding: utf-8 -*-
"""rc_ledger — mantém o livro-razão da adjudicação (`10-diagnostico/variantes-propostas.csv`).

Por que existe: o motor escreve 12 colunas; o revisor acrescenta três — `adjudicacao`,
`motivo_adjudicacao` e `ocorrencias_no_revisado`. Na primeira transcrição isso foi feito com um
script provisório que se perdeu. Este arquivo torna o passo reproduzível por qualquer pessoa (ou
qualquer outra sessão), e é o que alimenta o portão G4 do QA.

Vocabulário fechado de `adjudicacao` (Plano §6.2 e Guia §10):

    aceita           a variante foi substituída e não sobrevive no texto revisado
    aceita-parcial   aplicada onde cabe; as ocorrências restantes são legítimas
                     (topônimo, citação direta, expansão só na primeira menção)
    recusada         falso positivo do motor, flexão legítima ou alvo errado
    informativa      registro de artigo/flexão; não gera substituição
    protecao         variante e canônico coincidem: a semente existe para IMPEDIR outra troca
    superada         resolvida por despacho do Comandante ou por decisão posterior

Uso:
    python ferramentas/rc_ledger.py transcricoes/<slug> --resumo
    python ferramentas/rc_ledger.py transcricoes/<slug> --pendencias
    python ferramentas/rc_ledger.py transcricoes/<slug> --recalcular
    python ferramentas/rc_ledger.py transcricoes/<slug> --marcar "Brama=recusada" \\
        --motivo "flexão legítima; o canônico Brahma já está aplicado"
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_docx as DX  # noqa: E402
import rc_lexicon as L  # noqa: E402

DECISOES = {"aceita", "aceita-parcial", "recusada", "informativa", "protecao", "superada"}
COLUNAS_HUMANAS = ["adjudicacao", "motivo_adjudicacao", "ocorrencias_no_revisado"]


def caminho(pasta: Path) -> Path:
    return pasta / "10-diagnostico" / "variantes-propostas.csv"


def carregar(pasta: Path) -> tuple[list[dict], list[str]]:
    arq = caminho(pasta)
    if not arq.exists():
        raise SystemExit(f"[recusado] livro-razão ausente: {arq}")
    with arq.open(encoding="utf-8-sig", newline="") as fh:
        leitor = csv.DictReader(fh)
        campos = list(leitor.fieldnames or [])
        linhas = list(leitor)
    return linhas, campos


def gravar(pasta: Path, linhas: list[dict], campos: list[str]) -> None:
    for c in COLUNAS_HUMANAS:
        if c not in campos:
            campos.append(c)
    # lineterminator explícito: o padrão do csv.writer é CRLF, e o .gitattributes
    # normaliza para LF — sem isto o arquivo fica eternamente "modificado" no git status
    with caminho(pasta).open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


def texto_revisado(pasta: Path) -> str:
    """Corpo dos blocos, sem o conteúdo dos marcadores editoriais.

    `[NOTA: no bruto, "Xavé"]` cita a forma proibida DE PROPÓSITO: é evidência. Contá-la
    como sobrevivência puniria o revisor por documentar.
    """
    blocos = sorted((pasta / "20-blocos").glob("bloco-*.md")) if (pasta / "20-blocos").exists() else []
    if not blocos:
        return ""
    txt = "\n".join(b.read_text(encoding="utf-8") for b in blocos)
    return L.norm(DX.MARCADOR_RE.sub(" ", txt))


def recalcular(pasta: Path) -> int:
    linhas, campos = carregar(pasta)
    nb = texto_revisado(pasta)
    if not nb:
        raise SystemExit("[recusado] nenhum bloco em 20-blocos/ — nada a medir")
    for l in linhas:
        v = L.norm(l.get("variante", ""))
        l["ocorrencias_no_revisado"] = len(re.findall(r"\b" + re.escape(v) + r"\b", nb)) if v else 0
    gravar(pasta, linhas, campos)
    return len(linhas)


def pendencias(pasta: Path) -> list[dict]:
    linhas, _ = carregar(pasta)
    return [l for l in linhas
            if not (l.get("adjudicacao") or "").strip()
            or (l.get("adjudicacao") or "").strip().lower() not in DECISOES]


def marcar(pasta: Path, pares: list[str], motivo: str) -> int:
    linhas, campos = carregar(pasta)
    indice = {L.norm(l.get("variante", "")): l for l in linhas}
    feitos = 0
    for par in pares:
        if "=" not in par:
            raise SystemExit(f"[recusado] '{par}' não está no formato variante=decisao")
        variante, _, decisao = par.partition("=")
        decisao = decisao.strip().lower()
        if decisao not in DECISOES:
            raise SystemExit(f"[recusado] decisão '{decisao}' fora do vocabulário: {sorted(DECISOES)}")
        alvo = indice.get(L.norm(variante))
        if alvo is None:
            raise SystemExit(f"[recusado] variante '{variante}' não está no livro-razão")
        alvo["adjudicacao"] = decisao
        if motivo:
            alvo["motivo_adjudicacao"] = motivo
        feitos += 1
    if feitos:
        gravar(pasta, linhas, campos)
    return feitos


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Livro-razão da adjudicação.")
    ap.add_argument("pasta", type=Path, help="transcricoes/<slug>")
    ap.add_argument("--resumo", action="store_true")
    ap.add_argument("--pendencias", action="store_true")
    ap.add_argument("--recalcular", action="store_true",
                    help="remece ocorrencias_no_revisado a partir dos blocos")
    ap.add_argument("--marcar", action="append", default=[], metavar="VARIANTE=DECISAO")
    ap.add_argument("--motivo", default="", help="motivo gravado junto com --marcar")
    args = ap.parse_args(argv)

    pasta = args.pasta if args.pasta.is_absolute() else Path.cwd() / args.pasta
    if not pasta.exists():
        raise SystemExit(f"[recusado] pasta inexistente: {pasta}")

    if args.recalcular:
        n = recalcular(pasta)
        print(f"[ok] ocorrencias_no_revisado remeçadas em {n} linhas")
    if args.marcar:
        n = marcar(pasta, args.marcar, args.motivo)
        print(f"[ok] {n} linha(s) marcadas" + (f" — motivo: {args.motivo}" if args.motivo else ""))

    linhas, _ = carregar(pasta)
    if args.pendencias or not (args.resumo or args.recalcular or args.marcar):
        pend = [l for l in linhas
                if not (l.get("adjudicacao") or "").strip()
                or (l.get("adjudicacao") or "").strip().lower() not in DECISOES]
        if args.pendencias or pend:
            print(f"[pendências] {len(pend)} linha(s) sem decisão válida:")
            for l in pend[:20]:
                print(f"    {l.get('variante',''):<30} -> {l.get('canonico_proposto',''):<32} "
                      f"{l.get('codigo_base','')}")
            if len(pend) > 20:
                print(f"    … e mais {len(pend) - 20}")
        elif args.pendencias:
            print("[ok] nenhuma linha sem decisão")
    if args.resumo:
        conta = Counter((l.get("adjudicacao") or "(vazio)").strip().lower() for l in linhas)
        print(f"[resumo] {len(linhas)} linhas:")
        for k, v in conta.most_common():
            print(f"    {v:>4}  {k}")
        sem_motivo = sum(1 for l in linhas if (l.get("adjudicacao") or "").strip()
                         and not (l.get("motivo_adjudicacao") or "").strip())
        if sem_motivo:
            print(f"[aviso] {sem_motivo} linha(s) decididas sem motivo escrito")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
