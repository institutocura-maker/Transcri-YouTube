# -*- coding: utf-8 -*-
"""
rc_lexicon — camada única de acesso à base terminológica (base-terminologica.xlsx).

A planilha guarda apenas TERMOS CANÔNICOS. O conhecimento de "variante -> canônico"
está disperso (algumas linhas na aba Relações com tipo 'erro-stt-de' e as tabelas do
Guia em DOCX). Esta módulo concentra tudo isso em estruturas de dados:

  * carregar_base()      -> dicionário de termos, obras e relações
  * superficies()        -> índice invertido superfície_canônica -> [(código, papel, confiança)]
  * carregar_sementes()  -> pares variante/canônico curados (ferramentas/sementes-variantes-stt.csv)
  * norm() / chave()     -> normalização e dobra fonética pt-BR para detecção de variantes STT

Decisão de projeto importante: glossas entre parênteses (ex.: "Antares (Sistema)",
"Jan Val Ellam (Rogério de Almeida Freitas)") NÃO são tratadas como alias confiáveis
por padrão. Elas misturam alias reais com texto explicativo, e o aproveitamento
automático gera falsos positivos (ver analise/PARECER-DE-VIABILIDADE.md, item 4.4).
Use incluir_glossas=True apenas para varredura exploratória.
"""
from __future__ import annotations

import collections
import csv
import re
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

try:
    import openpyxl
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "openpyxl não instalado. Rode: pip install -r ferramentas/requirements.txt"
    ) from exc

# --------------------------------------------------------------------------------------
# Normalização
# --------------------------------------------------------------------------------------

def strip_accents(texto: str) -> str:
    """Remove diacríticos (preservando a letra base)."""
    return "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    )


def norm(texto: str) -> str:
    """Forma de comparação: minúsculas, sem acentos, sem pontuação, espaços colapsados."""
    texto = strip_accents(texto.lower())
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


_DIGRAMAS: Tuple[Tuple[str, str], ...] = (
    ("ph", "f"), ("ch", "s"), ("sh", "s"), ("lh", "l"), ("nh", "n"),
    ("ss", "s"), ("sc", "s"), ("xc", "s"), ("rr", "r"), ("qu", "k"),
)


def chave(texto: str) -> str:
    """Dobra fonética agressiva para GERAÇÃO DE CANDIDATOS (nunca para decisão final).

    Agrupa as oposições que o reconhecimento de fala mais confunde em pt-BR
    (p/b, t/d, k/g, f/v, s/z/x/j/ch, m/n final, vogais átonas finais), de modo que
    "Janva Elan" e "Jan Val Ellam" caiam na mesma vizinhança. Por ser agressiva,
    produz muitos falsos positivos: todo candidato deve ser re-avaliado com
    similaridade sobre `norm()` e, sobretudo, com julgamento contextual.
    """
    s = norm(texto).replace(" ", "")
    s = re.sub(r"^h", "", s)
    for a, b in _DIGRAMAS:
        s = s.replace(a, b)
    s = s.replace("c", "k").replace("q", "k")
    s = re.sub(r"g(?=[ei])", "j", s)
    s = s.replace("g", "k")
    s = s.replace("z", "s").replace("x", "s").replace("j", "s")
    s = s.replace("y", "i").replace("w", "v").replace("f", "v")
    s = s.replace("p", "b").replace("t", "d").replace("k", "g")
    s = s.replace("v", "b").replace("b", "p")
    s = re.sub(r"m$", "n", s).replace("m", "n")
    s = re.sub(r"e$", "i", s)
    s = re.sub(r"(.)\1+", r"\1", s)
    s = re.sub(r"[aeiou]+(?![aeiou])", lambda m: m.group(0)[0], s)
    return s


# --------------------------------------------------------------------------------------
# Base terminológica
# --------------------------------------------------------------------------------------

def _separar_nucleo(termo: str) -> Tuple[str, List[str], List[str]]:
    """Separa 'Núcleo (glossa) — anotação' em (núcleo, glossas, anotações)."""
    anotacoes: List[str] = []
    nucleo = termo
    for sep in ("—", " – ", " - "):
        if sep in nucleo:
            nucleo, resto = nucleo.split(sep, 1)
            anotacoes.append(resto.strip())
            break
    glossas: List[str] = []
    m = re.search(r"\(([^)]*)\)", nucleo)
    if m:
        nucleo = (nucleo[: m.start()] + " " + nucleo[m.end():]).strip()
        glossas.append(m.group(1).strip())
    return nucleo.strip(" ."), glossas, anotacoes


def _partes_glossa(glossa: str) -> Iterable[str]:
    """Quebra uma glossa em candidatos a alias ('Brahma/Javé/Demiurgo' -> 3 itens)."""
    bruto = re.split(r"[/;,=]|\bver\b", glossa)
    for item in bruto:
        item = re.sub(r"^RC-\d+\s*", "", item.strip()).strip(" .")
        item = re.sub(
            r"^(grafia d[oe]|nomes? d[oe]|conceito|sin[ôo]nimo|varia[çc][ãa]o|erro)\b",
            "", item, flags=re.I).strip()
        if len(item) > 2 and not item.isdigit():
            yield item


def carregar_base(caminho: str | Path = "base-terminologica.xlsx"):
    """Lê Índice Mestre, Fichas, Bibliografia e Relações.

    Retorna (termos, obras, relacoes) onde `termos` é {código: dict} com:
    codigo, termo, nucleo, glossas, anotacoes, formas, categoria, subcategoria,
    status, fontes, relacionados, variantes_stt (vindo da aba Relações).
    """
    caminho = Path(caminho)
    wb = openpyxl.load_workbook(caminho, data_only=True, read_only=True)

    termos: Dict[str, dict] = {}
    im = wb["Índice Mestre"]
    linhas = im.iter_rows(values_only=True)
    next(linhas, None)  # cabeçalho
    for linha in linhas:
        if not linha or not linha[0]:
            continue
        codigo, termo, categoria, subcategoria, status, fontes, relacionados, ficha, atualizado = linha[:9]
        nucleo, glossas, anotacoes = _separar_nucleo(str(termo))
        formas = [p.strip() for p in re.split(r"\s*/\s*", nucleo) if len(p.strip()) > 2]
        termos[codigo] = dict(
            codigo=codigo, termo=str(termo), nucleo=nucleo, glossas=glossas,
            anotacoes=anotacoes, formas=formas, categoria=categoria,
            subcategoria=subcategoria, status=status, fontes=fontes,
            relacionados=relacionados, ficha_completa=ficha, atualizado=str(atualizado),
            variantes_stt=[],
        )

    relacoes = collections.defaultdict(list)
    rel = wb["Relações"]
    linhas = rel.iter_rows(values_only=True)
    next(linhas, None)
    for linha in linhas:
        if not linha or not linha[0]:
            continue
        a_cod, a_nome, tipo, b_cod, b_nome, fonte = linha[:6]
        relacoes[tipo].append((a_cod, a_nome, b_cod, b_nome, fonte))
        # 'erro-stt-de': A é a forma corrompida; B é o canônico -> alimenta variantes_stt
        if tipo == "erro-stt-de" and b_cod in termos:
            nucleo_a, _, _ = _separar_nucleo(str(a_nome))
            termos[b_cod]["variantes_stt"].append(nucleo_a)

    obras: List[dict] = []
    bib = wb["Bibliografia"]
    linhas = bib.iter_rows(values_only=True)
    cabecalho = next(linhas, None)
    for linha in linhas:
        if not linha or not linha[0]:
            continue
        obras.append(dict(zip(cabecalho, linha)))

    fichas_ocupacao = None
    if "Fichas" in wb.sheetnames:
        fichas = wb["Fichas"]
        linhas = fichas.iter_rows(values_only=True)
        cab = next(linhas, None)
        cols_ricas = ["Definição sintética", "Contexto / Origem", "Etimologia / Grafias",
                      "Citações-chave", "Observações"]
        idx = [cab.index(c) for c in cols_ricas if c in (cab or [])]
        total = preenchidas = placeholder = 0
        for linha in linhas:
            if not linha or not linha[0]:
                continue
            total += 1
            for i in idx:
                v = linha[i]
                if isinstance(v, str) and "ver ficha completa" in v:
                    placeholder += 1
                elif v not in (None, "", "—"):
                    preenchidas += 1
        fichas_ocupacao = dict(total_registros=total, colunas_ricas=cols_ricas,
                               celulas_placeholder=placeholder, celulas_preenchidas=preenchidas)
    wb.close()
    return termos, obras, dict(relacoes), fichas_ocupacao


# Palavras que, mesmo aparecendo como termo da base, são vocabulário comum e
# NÃO devem disparar substituição/negrito automático.
_GENERICOS = {
    "deus", "deuses", "divindades", "criador", "criatura", "conceito", "conceitos",
    "sistema", "sistemas", "mente", "mentes", "humano", "humanos", "ser", "seres",
    "alma", "almas", "corpo", "corpos", "terra", "céu", "ceu", "mundo", "mundos",
    "vida", "morte", "tempo", "espaço", "espaco", "energia", "matéria", "materia",
    "consciência", "consciencia", "espírito", "espirito", "anjo", "anjos",
    "demônio", "demonio", "demônios", "demonios", "revelação", "revelacao",
    "transição", "transicao", "criação", "criacao", "queda", "ascensão", "ascensao",
    "luz", "trevas", "caos", "ordem", "amor", "medo", "verdade", "mentira",
}


GENERICOS = _GENERICOS  # alias público (usado pelo rc_diagnostico)


def superficies(termos: Dict[str, dict], incluir_glossas: bool = False,
                incluir_sementes: Sequence[dict] = ()) -> Dict[str, List[tuple]]:
    """Índice invertido: superfície normalizada -> [(código, papel, confiabilidade)].

    confiabilidade: 'alta' (núcleo do termo / variante STT registrada / semente curada),
                    'media' (parte de núcleo composto, ex.: 'Quarto Logos' em
                    'O Quarto Logos'), 'baixa' (glossa entre parênteses).
    """
    indice: Dict[str, List[tuple]] = collections.defaultdict(list)

    for codigo, t in termos.items():
        for forma in t["formas"]:
            conf = "alta" if len(t["formas"]) == 1 else "media"
            indice[norm(forma)].append((codigo, "canonico", conf))
        if norm(t["nucleo"]) not in {norm(f) for f in t["formas"]}:
            indice[norm(t["nucleo"])].append((codigo, "canonico", "alta"))
        for v in t.get("variantes_stt", []):
            indice[norm(v)].append((codigo, "variante_stt", "alta"))
        if incluir_glossas:
            for g in t["glossas"]:
                for parte in _partes_glossa(g):
                    indice[norm(parte)].append((codigo, "glossa", "baixa"))

    for s in incluir_sementes:
        indice[norm(s["variante"])].append((s.get("codigo_base") or "?", "semente", "alta"))
    return dict(indice)


def carregar_sementes(caminho: str | Path = "ferramentas/sementes-variantes-stt.csv") -> List[dict]:
    """Pares variante -> canônico curados manualmente (origem: Guia, seções 5.1/5.2/5.4)."""
    caminho = Path(caminho)
    if not caminho.exists():
        return []
    with caminho.open(encoding="utf-8-sig", newline="") as fh:
        corpo = [l for l in fh if not l.lstrip().startswith("#")]  # comentários permitidos
        linhas = [l for l in csv.DictReader(corpo)
                  if l.get("variante") and not l["variante"].startswith("#")]
    for l in linhas:
        l["aprovada"] = l.get("status_aprovacao", "aprovada").strip().lower() in {"aprovada", "sim", "1", "true"}
    return linhas


def dossie(termos: Dict[str, dict], codigos: Iterable[str] | None = None,
           campos: Sequence[str] = ("codigo", "nucleo", "status")) -> str:
    """Exporta um recorte enxuto da base (para caber no contexto de trabalho)."""
    itens = termos.values() if codigos is None else (termos[c] for c in codigos if c in termos)
    return "\n".join("|".join(str(t.get(c, "")) for c in campos) for t in itens)


def filtrar_relevantes(termos: Dict[str, dict], janelas_norm: Iterable[str],
                       incluir_glossas: bool = True, incluir_sementes: Sequence[dict] = ()) -> List[str]:
    """Pré-filtro: códigos da base cuja superfície (ou chave fonética) aparece no texto.

    É isto que torna o fluxo viável: em vez de injetar os 946 termos (~9,5 mil tokens)
    em cada bloco de revisão, injeta-se apenas o subconjunto plausível para aquela
    transcrição (normalmente 60-150 termos, ~1-2 mil tokens).

    `janelas_norm` deve conter as formas normalizadas das janelas 1..4 do texto
    (ver rc_diagnostico.janelas), já restritas a ocorrências interessantes.
    """
    janelas = set(janelas_norm)
    chaves_janela = {chave(j) for j in janelas}
    achados = set()
    for superficie, alvos in superficies(termos, incluir_glossas=incluir_glossas,
                                         incluir_sementes=incluir_sementes).items():
        if len(superficie) < 4:
            continue
        conf_uteis = [c for c, _, conf in alvos if conf != "baixa"]
        if not conf_uteis:
            continue
        if superficie in janelas or chave(superficie) in chaves_janela:
            achados.update(conf_uteis)
    return sorted(achados)
