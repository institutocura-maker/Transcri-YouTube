# -*- coding: utf-8 -*-
"""rc_leitura — onde começa o corpo de um arquivo de STT. Uma resposta só, para a esteira inteira.

Nasceu do experimento de motor de 16/09/2026 (`docs/pareceres/parecer-motor-stt.md`, §5 e §8 item 1).
A esteira respondia à mesma pergunta de **dois jeitos diferentes**:

* `rc_novo.py` e `rc_indice.py`: corpo = `max(linhas, key=len)` — a linha mais longa;
* `rc_diagnostico.carregar_transcricao`: corpo = o que vem depois do marcador
  "Transcrição Automática".

Sobre o STT do YouTube os dois critérios coincidem (o corpo é uma linha só, com 101.468 caracteres)
e por isso ninguém notou. Sobre um STT **paragraphado** — que é o que a camada de reescrita do
NotebookLM entrega: 287 turnos no corpo, 295 linhas não vazias no arquivo inteiro, diferença que é o
cabeçalho e que o `rc_perfil_stt.py` conta junto — a linha mais longa cobre 3,9% do arquivo: `rc_novo` gravaria em
`metadados.yaml` um `corpo_palavras` fracionário, sem exceção, sem aviso e com o QA verde, porque o
portão G1 confere sha256, não coerência da medição.

A cascata abaixo é determinística e **diz qual critério usou**. Quando nenhum critério é confiável,
ela devolve um aviso em vez de um número que parece bom:

    1. marcador de cabeçalho ("Transcrição Automática") — o que vem depois dele é o corpo;
    2. linha mais longa, se cobrir >= COBERTURA_MINIMA do arquivo;
    3. o arquivo inteiro, com aviso.

Uso:
    import rc_leitura as RL
    corpo = RL.localizar_corpo(texto)          # dict com criterio, corpo, aviso, medidas
    numeros = RL.medir_arquivo(caminho)        # + bytes, linhas, sha256 (o que o rc_novo grava)
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

MARCADOR_PADRAO = "Transcrição Automática"
COBERTURA_MINIMA = 0.80
PALAVRA_RE = re.compile(r"[\w'’]+", re.U)


def localizar_corpo(texto: str, marcador: str = MARCADOR_PADRAO,
                    cobertura_minima: float = COBERTURA_MINIMA) -> dict:
    """Localiza o corpo de um bruto de STT e devolve as medidas + o critério usado.

    Nunca chuta em silêncio: se a maior linha não cobre o arquivo e não há marcador, o corpo
    assumido é o arquivo inteiro e `aviso` explica por quê.
    """
    linhas = texto.splitlines()
    maior = max((len(l) for l in linhas), default=0)
    cobertura = maior / max(len(texto), 1)

    corpo, inicio, criterio, aviso = "", 0, "arquivo-inteiro", None
    idx = next((i for i, l in enumerate(linhas) if marcador in l), None)
    if idx is not None:
        corpo = "\n".join(linhas[idx + 1:]).strip("\n")
        inicio = idx + 1
        criterio = "marcador"
    elif linhas and cobertura >= cobertura_minima:
        corpo = max(linhas, key=len)
        inicio = linhas.index(corpo)
        criterio = "linha-mais-longa"
    else:
        corpo = texto
        aviso = (f"nenhum critério confiável: sem o marcador '{marcador}' e a maior linha cobre "
                 f"{cobertura:.1%} do arquivo (< {cobertura_minima:.0%}). Corpo assumido como o "
                 f"arquivo inteiro — confira `linhas_cabecalho` em metadados.yaml")

    linhas_corpo = [l for l in corpo.splitlines() if l.strip()]
    return {
        "criterio_corpo": criterio,
        "corpo": corpo,
        "corpo_inicio": inicio,
        "linhas_cabecalho": inicio,
        "corpo_linha": inicio + 1,
        "corpo_caracteres": len(corpo),
        "corpo_palavras": len(PALAVRA_RE.findall(corpo)),
        "corpo_segmentos": len(linhas_corpo),
        "maior_linha_chars": maior,
        "cobertura_maior_linha": round(cobertura, 4),
        "marcador_cabecalho": idx is not None,
        "aviso_corpo": aviso,
    }


def medir_arquivo(caminho: Path, marcador: str = MARCADOR_PADRAO,
                  cobertura_minima: float = COBERTURA_MINIMA) -> dict:
    """O que o `rc_novo.py` grava em metadados.yaml: identidade + medição do corpo.

    Inclui o sha256 do arquivo (o portão G1 fiscaliza) e as medidas do corpo pelo critério único.
    """
    caminho = Path(caminho)
    dados = caminho.read_bytes()
    texto = dados.decode("utf-8-sig", errors="replace")
    medida = localizar_corpo(texto, marcador, cobertura_minima)
    medida.pop("corpo", None)  # o corpo inteiro não vai para o YAML
    return {
        "bytes": len(dados),
        "linhas": len(texto.splitlines()),
        "sha256": hashlib.sha256(dados).hexdigest(),
        **medida,
    }


def ler_texto(caminho: Path) -> str:
    """Leitura tolerante: BOM, CRLF e bytes inválidos não derrubam a medição."""
    return Path(caminho).read_bytes().decode("utf-8-sig", errors="replace")
