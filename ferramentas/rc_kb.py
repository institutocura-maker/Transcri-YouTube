# -*- coding: utf-8 -*-
"""
rc_kb — camada 1 (fonte de verdade): leitura da KB-RC.

A KB-RC substitui a planilha como fonte de verdade do Passo 1:
    KB-RC/canonico.json   946 termos + 1.887 relações (verdade-mestra, formato canonico-1.1)
    KB-RC/biblio.json     obras (B###, ART-, PER-, EXT-)
    KB-RC/termos/RC-*.md  820 fichas completas (definição, contexto, ETIMOLOGIA E GRAFIAS,
                          citações-chave, ampliação por fonte, observações, quarentenas)

O que este módulo acrescenta: extrai de cada ficha a seção "Etimologia e Grafias"
— que a planilha não tinha (4.100 células placeholder) — e monta o **índice de
alias** (grafia preferida + variações + variações STT capturadas), que é o elo
variante -> canônico de que o fluxo de revisão precisa.

Atenção de governança: os rótulos dessa seção são heterogêneos na KB (ver
ROTULOS_GRAFIA / ROTULOS_VARIACOES). Este módulo normaliza a leitura, mas NÃO
altera as fichas: qualquer padronização de rótulo é decisão do curador.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

# Rótulos encontrados na KB-RC, do mais específico ao mais genérico.
ROTULOS_GRAFIA = (
    "Grafia preferida (canônica)",
    "Grafia (paridade verbatim absoluta)",
    "Grafia preferida",
    "Grafia canônica",
    "Grafia",
)
ROTULOS_STT = (
    "Variações STT capturadas",
    "Variações STT posteriores",
    "Grafia STT",
    "Variações STT",
)
ROTULOS_VARIACOES = (
    "Variações / grafias alternativas",
    "Variações capturadas",
    "Variações fundidas neste termo",
    "Variações",
    "Grafias alternativas",
    "Outras grafias",
)
SECOES = (
    "Definição Sintética", "Contexto / Origem", "Etimologia e Grafias",
    "Citações-chave", "Citação-chave", "Termos Relacionados", "Seres Associados",
    "Fontes", "Ampliação", "Atualização", "Observações", "Escopo e evidência",
    "Quarentena Terminológica", "Cautela editorial", "Glossário interno / absorções",
)


@dataclass
class Ficha:
    codigo: str
    arquivo: str
    nome: str = ""
    categoria: str = ""
    subcategoria: str = ""
    status: str = ""
    via: str = ""
    confianca_fonte: str = ""
    atualizado: str = ""
    fontes: List[str] = field(default_factory=list)
    secoes: Dict[str, str] = field(default_factory=dict)

    # camada de grafias
    grafia_preferida: List[str] = field(default_factory=list)
    variacoes: List[str] = field(default_factory=list)
    variacoes_stt: List[str] = field(default_factory=list)
    idioma: str = ""
    quarentena: str = ""
    cautela: str = ""


# --------------------------------------------------------------------------------------
# Verdade-mestra
# --------------------------------------------------------------------------------------

def carregar_kb(raiz: str | Path = "KB-RC"):
    """Lê canonico.json e biblio.json. Retorna (meta, termos, relacoes, obras)."""
    raiz = Path(raiz)
    canon = json.loads((raiz / "canonico.json").read_text(encoding="utf-8"))
    biblio_path = raiz / "biblio.json"
    biblio = json.loads(biblio_path.read_text(encoding="utf-8")) if biblio_path.exists() else {"obras": []}
    return canon.get("meta", {}), canon["termos"], canon["relacoes"], biblio.get("obras", [])


# --------------------------------------------------------------------------------------
# Fichas
# --------------------------------------------------------------------------------------

_FRONT = re.compile(r"^\+\+\+\s*\n(.*?)\n\+\+\+", re.S)


def _parse_frontmatter(bloco: str) -> dict:
    dados = {}
    for linha in bloco.splitlines():
        m = re.match(r"^([a-z_]+)\s*=\s*(.*)$", linha.strip())
        if not m:
            continue
        chave, valor = m.group(1), m.group(2).strip()
        if valor.startswith("["):
            try:
                dados[chave] = json.loads(valor.replace("'", '"'))
            except json.JSONDecodeError:
                dados[chave] = [v.strip().strip('"') for v in valor.strip("[]").split(",")]
        else:
            dados[chave] = valor.strip('"')
    return dados


def secao(texto: str, titulo: str) -> str:
    """Extrai o conteúdo de '## <titulo>' até o próximo cabeçalho de mesmo nível."""
    padrao = re.compile(r"^##\s+" + re.escape(titulo) + r"\s*$(.*?)(?=^##\s|\Z)", re.S | re.M)
    m = padrao.search(texto)
    return m.group(1).strip() if m else ""


def _itens_de_lista(valor: str) -> List[str]:
    """'Senhor Javé; Jeová; Yahweh (B031)' -> ['Senhor Javé', 'Jeová', 'Yahweh (B031)']"""
    valor = valor.strip().strip("-•").strip()
    partes = re.split(r"\s*[;•]\s*|\s*\|\s*", valor)
    out = []
    for p in partes:
        p = re.sub(r"^\s*[-*]\s*", "", p).strip(" .,")
        p = re.sub(r"^\*\*(.+?)\*\*:?\s*$", r"\1", p).strip()
        if p and p.lower() not in {"não", "nao", "—", "-", "n/a"}:
            out.append(p)
    return out


def _rotulo(secao_texto: str, rotulos: Sequence[str]) -> str:
    """Devolve o valor do primeiro rótulo (negrito) encontrado na seção."""
    for rotulo in rotulos:
        m = re.search(r"\*\*\s*" + re.escape(rotulo) + r"\s*:?\*\*\s*(.+)", secao_texto, re.I)
        if m:
            return m.group(1).strip()
        m = re.search(r"^\s*[-*]\s*" + re.escape(rotulo) + r"\s*:?\s*(.+)$", secao_texto, re.I | re.M)
        if m:
            return m.group(1).strip()
        m = re.search(re.escape(rotulo) + r"\s*:?\s*(.+)", secao_texto, re.I)
        if m:
            return m.group(1).strip()
    return ""


def carregar_ficha(caminho: Path) -> Ficha:
    texto = caminho.read_text(encoding="utf-8")
    f = Ficha(codigo="", arquivo=caminho.name)
    m = _FRONT.search(texto)
    if m:
        front = _parse_frontmatter(m.group(1))
        f.codigo = front.get("codigo", "")
        f.nome = front.get("nome", "")
        f.categoria = front.get("categoria", "")
        f.subcategoria = front.get("subcategoria", "")
        f.status = front.get("status", "")
        f.via = front.get("via", "")
        f.confianca_fonte = front.get("confianca_fonte", "")
        f.atualizado = front.get("atualizado", "")
        f.fontes = front.get("fontes", []) or []
    if not f.codigo:
        m2 = re.search(r"(RC-\d{3})", caminho.name)
        f.codigo = m2.group(1) if m2 else caminho.stem
    if not f.nome:
        m3 = re.search(r"^#\s+(.*?)(?:\s*[—-]\s*RC-\d{3})?\s*$", texto, re.M)
        f.nome = m3.group(1).strip() if m3 else ""

    for titulo in SECOES:
        corpo = secao(texto, titulo)
        if corpo:
            f.secoes[titulo] = corpo

    eti = f.secoes.get("Etimologia e Grafias", "")
    if eti:
        gp = _rotulo(eti, ROTULOS_GRAFIA)
        if gp:
            f.grafia_preferida = _itens_de_lista(gp)
        stt = _rotulo(eti, ROTULOS_STT)
        if stt:
            f.variacoes_stt = _itens_de_lista(stt)
        var = _rotulo(eti, ROTULOS_VARIACOES)
        if var:
            f.variacoes = _itens_de_lista(var)
        f.idioma = _rotulo(eti, ("Idioma de origem / etimologia", "Idioma de origem", "Idioma", "Etimologia"))
    f.quarentena = f.secoes.get("Quarentena Terminológica", "")
    f.cautela = f.secoes.get("Cautela editorial", "")
    return f


def carregar_fichas(raiz: str | Path = "KB-RC", codigos: Iterable[str] | None = None) -> Dict[str, Ficha]:
    dir_termos = Path(raiz) / "termos"
    fichas: Dict[str, Ficha] = {}
    for caminho in sorted(dir_termos.glob("RC-*.md")):
        if codigos is not None:
            m = re.search(r"(RC-\d{3})", caminho.name)
            if not m or m.group(1) not in set(codigos):
                continue
        f = carregar_ficha(caminho)
        fichas[f.codigo] = f
    return fichas


# --------------------------------------------------------------------------------------
# Índice de alias (variante -> canônico)
# --------------------------------------------------------------------------------------

def _formas_do_nome(nome: str) -> List[str]:
    """'Wyrd / Urd (Teia do Destino)' -> ['Wyrd / Urd', 'Teia do Destino'] e partes."""
    formas = [nome]
    m = re.search(r"\(([^)]*)\)", nome)
    if m:
        formas.append(nome[: m.start()].strip())
        formas += [p.strip() for p in re.split(r"[/;,]", m.group(1)) if len(p.strip()) > 2]
    for f in list(formas):
        formas += [p.strip() for p in f.split("/") if len(p.strip()) > 2]
    vistas, out = set(), []
    for f in formas:
        f = f.strip(" .")
        if f and f.lower() not in vistas and len(f) > 1:
            vistas.add(f.lower())
            out.append(f)
    return out


def indice_alias(fichas: Dict[str, Ficha], termos: Sequence[dict] | None = None,
                 incluir_nome: bool = True) -> Dict[str, List[tuple]]:
    """superfície normalizada -> [(código, papel)] com papel em
    {canonico, grafia_preferida, variacao, variacao_stt}.

    `termos` (canonico.json) entra como reforço: garante cobertura dos 946 códigos
    mesmo quando não há ficha Markdown (820 fichas para 946 termos).
    """
    import rc_lexicon as L

    indice: Dict[str, List[tuple]] = {}

    def add(superficie: str, codigo: str, papel: str) -> None:
        s = L.norm(superficie)
        if len(s) < 2:
            return
        indice.setdefault(s, [])
        if (codigo, papel) not in indice[s]:
            indice[s].append((codigo, papel))

    if termos:
        for t in termos:
            if incluir_nome:
                for f in _formas_do_nome(t["nome"]):
                    add(f, t["codigo"], "canonico")
    for codigo, f in fichas.items():
        if incluir_nome and f.nome:
            for forma in _formas_do_nome(f.nome):
                add(forma, codigo, "canonico")
        for g in f.grafia_preferida:
            add(g, codigo, "grafia_preferida")
        for v in f.variacoes:
            add(v, codigo, "variacao")
        for v in f.variacoes_stt:
            add(v, codigo, "variacao_stt")
    return indice


def estatisticas(fichas: Dict[str, Ficha], termos: Sequence[dict]) -> dict:
    com_eti = sum(1 for f in fichas.values() if "Etimologia e Grafias" in f.secoes)
    return dict(
        termos_canonico_json=len(termos),
        fichas_md=len(fichas),
        fichas_com_etimologia_grafias=com_eti,
        com_grafia_preferida=sum(1 for f in fichas.values() if f.grafia_preferida),
        com_variacoes=sum(1 for f in fichas.values() if f.variacoes),
        com_variacoes_stt=sum(1 for f in fichas.values() if f.variacoes_stt),
        com_quarentena=sum(1 for f in fichas.values() if f.quarentena),
        com_cautela=sum(1 for f in fichas.values() if f.cautela),
        total_grafias_preferidas=sum(len(f.grafia_preferida) for f in fichas.values()),
        total_variacoes=sum(len(f.variacoes) for f in fichas.values()),
        total_variacoes_stt=sum(len(f.variacoes_stt) for f in fichas.values()),
        termos_sem_ficha=len(termos) - len(fichas),
    )


# --------------------------------------------------------------------------------------
# Adaptador para o rc_diagnostico (mesma forma de dados do loader da planilha)
# --------------------------------------------------------------------------------------

def como_termos(termos_json: Sequence[dict], fichas: Dict[str, "Ficha"],
                regras_substituicao: Sequence[dict] = ()) -> Dict[str, dict]:
    """Converte canonico.json + fichas no formato que `rc_diagnostico.varrer` consome.

    Acrescenta o que a planilha não tinha: `grafia_preferida`, `variacoes`,
    `variacoes_stt` e as regras de substituição extraídas da prosa das fichas.
    """
    por_codigo: Dict[str, dict] = {}
    for t in termos_json:
        codigo = t["codigo"]
        f = fichas.get(codigo)
        nome = t.get("nome", "") or (f.nome if f else "")
        nucleo, glossas, anotacoes = nome, [], []
        if "(" in nome:
            nucleo = nome[: nome.index("(")].strip()
            glossas = [nome[nome.index("(") + 1: nome.rindex(")")]]
        for sep in ("—", " – "):
            if sep in nucleo:
                nucleo, resto = nucleo.split(sep, 1)
                anotacoes.append(resto.strip())
                break
        formas = [p.strip() for p in re.split(r"\s*/\s*", nucleo.strip()) if len(p.strip()) > 2]
        por_codigo[codigo] = dict(
            codigo=codigo, termo=nome, nucleo=nucleo.strip(" ."), glossas=glossas,
            anotacoes=anotacoes, formas=formas or [nucleo],
            categoria=t.get("categoria", ""), subcategoria=t.get("subcategoria", ""),
            status=t.get("status", ""), fontes=", ".join(t.get("fontes", []) or []),
            relacionados=t.get("relacionados", ""), atualizado=(f.atualizado if f else ""),
            via=(f.via if f else ""), confianca_fonte=(f.confianca_fonte if f else ""),
            tem_ficha=f is not None,
            grafia_preferida=(f.grafia_preferida if f else []),
            variacoes=(f.variacoes if f else []),
            variantes_stt=list(f.variacoes_stt) if f else [],
            quarentena=(f.quarentena[:300] if f and f.quarentena else ""),
        )
    # regras extraídas da prosa (rc_variantes) entram como variantes STT do canônico
    for r in regras_substituicao:
        cod = r.get("codigo_base") or r.get("codigo") or ""
        alvo = cod if cod in por_codigo else None
        if alvo is None:
            # localiza pelo nome canônico
            alvo = next((c for c, t in por_codigo.items()
                         if L_norm(t["nucleo"]) == L_norm(r.get("canonico", ""))), None)
        if alvo:
            v = r["variante"]
            if v not in por_codigo[alvo]["variantes_stt"]:
                por_codigo[alvo]["variantes_stt"].append(v)
    return por_codigo


def L_norm(s: str) -> str:  # evita import circular no topo do módulo
    import rc_lexicon
    return rc_lexicon.norm(s)
