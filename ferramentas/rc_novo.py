# -*- coding: utf-8 -*-
"""rc_novo — cria o diretório de uma transcrição a partir de `transcricoes/_modelo/`.

Por que um script e não "copie a pasta à mão": sem ele, cada transcrição nova nasce
com uma estrutura ligeiramente diferente — falta um README, o slug vem com acento, o
hash não é registrado — e a diferença vira exceção permanente que o QA não consegue
cobrar. Aqui a estrutura é sempre a mesma e o bruto já entra com SHA-256 gravado.

Uso:
    python ferramentas/rc_novo.py \\
        --slug 2026-10-02-lemuria-terry-fabris \\
        --titulo "LEMÚRIA ESTÁ em busca URGENTE DE CONTATO" \\
        --canal "Paranormal Experience" \\
        --url https://youtu.be/9DvQf6DikA8 \\
        --data 2026-10-02 \\
        --bruto ~/Downloads/legenda.txt

O que faz: valida o slug, recusa duplicidade, copia o modelo, deriva do bruto os
números (bytes, linhas, hash, onde começa o corpo), substitui os marcadores `{{…}}`,
registra a linha no catálogo e devolve os próximos comandos.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_indice as IND  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
TRANSCRICOES = RAIZ / "transcricoes"
MODELO = TRANSCRICOES / "_modelo"

SLUG_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
DATA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PALAVRA_RE = re.compile(r"[\wÀ-ÿ']+")


def validar_slug(slug: str) -> str | None:
    """Devolve o motivo da recusa, ou None se o slug serve."""
    if len(slug) > 60:
        return f"tem {len(slug)} caracteres; o teto é 60"
    if not SLUG_RE.match(slug):
        return ("fora do padrão AAAA-MM-DD-titulo-em-kebab-case: só minúsculas, dígitos e "
                "hífen, sem acento, sem espaço, sem pontuação")
    if not DATA_RE.match(slug[:10]):
        return "não começa com uma data AAAA-MM-DD"
    try:
        dt.date.fromisoformat(slug[:10])
    except ValueError:
        return f"a data '{slug[:10]}' não existe"
    if (TRANSCRICOES / slug).exists():
        return "já existe uma transcrição com esse slug"
    return None


def medir_bruto(arq: Path) -> dict:
    """Números do bruto, incluindo onde o corpo começa.

    O STT do YouTube entrega um cabeçalho curto e o texto inteiro numa linha só. O corpo
    é detectado como a linha mais longa — o número de linhas de cabeçalho varia de vídeo
    para vídeo e chutá-lo produziria metadados mentirosos.
    """
    dados = arq.read_bytes()
    linhas = dados.decode("utf-8", errors="replace").splitlines()
    corpo = max(linhas, key=len) if linhas else ""
    indice = linhas.index(corpo) if corpo else 0
    return {
        "bytes": len(dados),
        "linhas": len(linhas),
        "sha256": hashlib.sha256(dados).hexdigest(),
        "linhas_cabecalho": indice,
        "corpo_linha": indice + 1,
        "corpo_caracteres": len(corpo),
        "corpo_palavras": len(PALAVRA_RE.findall(corpo)),
    }


def substituir(pasta: Path, mapa: dict[str, str]) -> int:
    """Troca os marcadores `{{chave}}` nos arquivos de texto copiados do modelo."""
    trocas = 0
    for arq in pasta.rglob("*"):
        if not arq.is_file() or arq.suffix.lower() not in {".md", ".yaml", ".yml", ".txt", ".csv"}:
            continue
        texto = arq.read_text(encoding="utf-8")
        novo = texto
        for chave, valor in mapa.items():
            novo = novo.replace("{{" + chave + "}}", str(valor))
        if novo != texto:
            arq.write_text(novo, encoding="utf-8")
            trocas += 1
    return trocas


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Cria a pasta de uma transcrição nova.")
    ap.add_argument("--slug", required=True, help="AAAA-MM-DD-titulo-em-kebab-case")
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--canal", default="")
    ap.add_argument("--url", default="null", help="endereço do vídeo; 'null' se não foi registrado")
    ap.add_argument("--data", default=None, help="data da gravação (AAAA-MM-DD); padrão: a do slug")
    ap.add_argument("--bruto", type=Path, required=True, help="arquivo .txt/.vtt capturado")
    ap.add_argument("--duracao", default="", help="duração em minutos")
    ap.add_argument("--revisor", default="")
    ap.add_argument("--responsavel", default="Comandante")
    args = ap.parse_args(argv)

    motivo = validar_slug(args.slug)
    if motivo:
        print(f"[recusado] slug '{args.slug}': {motivo}", file=sys.stderr)
        return 1
    if not MODELO.exists():
        print(f"[recusado] modelo ausente em {MODELO}", file=sys.stderr)
        return 1
    bruto = args.bruto.expanduser().resolve()
    if not bruto.exists():
        print(f"[recusado] bruto não encontrado: {bruto}", file=sys.stderr)
        return 1

    destino = TRANSCRICOES / args.slug
    shutil.copytree(MODELO, destino)
    (destino / "README.md").unlink(missing_ok=True)  # o README é do modelo, não da transcrição

    numeros = medir_bruto(bruto)
    shutil.copy2(bruto, destino / "00-fonte" / "transcricao-bruta.txt")

    mapa = {
        "slug": args.slug,
        "titulo": args.titulo,
        "canal": args.canal or "",
        "url": args.url if args.url.startswith("http") else "null",
        "data": args.data or args.slug[:10],
        "data_captura": dt.date.today().isoformat(),
        "responsavel": args.responsavel,
        **{k: str(v) for k, v in numeros.items()},
    }
    if args.url.startswith("http"):
        mapa["url"] = args.url
    if args.duracao:
        mapa["duracao"] = args.duracao
    trocas = substituir(destino, mapa)

    IND.main([])  # regenera o catálogo com a linha nova
    print(f"[ok] {destino.relative_to(RAIZ)} criada ({trocas} arquivos preenchidos)")
    print(f"     bruto: {numeros['bytes']} bytes, {numeros['linhas']} linhas, "
          f"corpo na linha {numeros['corpo_linha']} ({numeros['corpo_palavras']} palavras)")
    print(f"     sha256: {numeros['sha256']}")
    print()
    print("     próximos passos:")
    print(f"       1. conferir 00-fonte/metadados.yaml (url, duração, chamada) e preencher o que falta")
    print(f"       2. python ferramentas/rc_diagnostico.py transcricoes/{args.slug}/00-fonte/transcricao-bruta.txt --kb KB-RC")
    print(f"       3. revisar em transcricoes/{args.slug}/20-blocos/bloco-NN.md (zero à esquerda!)")
    print(f"       4. montar o produto e rodar os portões:")
    print(f"          python ferramentas/rc_docx.py transcricoes/{args.slug}/20-blocos/bloco-*.md \\")
    print(f"              --lexico transcricoes/{args.slug}/10-diagnostico/dossie-bloco.txt \\")
    print(f"              --saida transcricoes/{args.slug}/30-produto/transcricao-revisada.docx \\")
    print(f"              --titulo \"{args.titulo}\" \\")
    print(f"              --validar transcricoes/{args.slug}/10-diagnostico/variantes-propostas.csv")
    print(f"          python ferramentas/rc_qa.py transcricoes/{args.slug}")
    if not args.url.startswith("http"):
        print()
        print("     [aviso] a URL do vídeo não foi informada: sem proveniência o bruto é um .txt órfão.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
