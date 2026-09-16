# -*- coding: utf-8 -*-
"""
rc_diagnostico — varredura de uma transcrição STT contra a base terminológica.

Uso:
    python ferramentas/rc_diagnostico.py "Revelações Cósmicas Urgente – Jan Val Ellam.txt" \
        --base base-terminologica.xlsx --saida analise/<pasta>

Gera, na pasta de saída:
    diagnostico.json          métricas e achados completos (para máquinas)
    diagnostico.md            versão legível do diagnóstico
    variantes-propostas.csv   candidatas a entrar na camada de variantes STT (a aprovar)
    ausentes-da-base.csv      nomes próprios/entidades do texto sem registro na base
    dossie-bloco.txt          recorte ENXUTO da base relevante para esta transcrição

O que este script NÃO faz (por princípio): decidir substituições. Ele levanta
evidências e as ordena; a decisão é contextual e cabe ao revisor (humano ou agente),
conforme o item 4.4 do parecer de viabilidade.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_lexicon as L  # noqa: E402

try:
    from rapidfuzz import process
    from rapidfuzz.distance import Levenshtein
except ImportError as exc:  # pragma: no cover
    raise SystemExit("rapidfuzz não instalado. Rode: pip install -r ferramentas/requirements.txt") from exc

PALAVRAS_COMUNS = {
    "não", "mas", "eu", "e", "a", "o", "ah", "ei", "uhum", "você", "é", "aí", "sim",
    "ok", "então", "bom", "bem", "olá", "pq", "né", "tá", "tô", "ó", "oh", "eh",
    "Deus", "Não", "Mas", "Eu", "E", "A", "O", "Ah", "Ei", "Você", "É", "Aí", "Sim",
}


# --------------------------------------------------------------------------------------
# Entrada
# --------------------------------------------------------------------------------------

def carregar_transcricao(caminho: Path) -> tuple[str, str]:
    """Separa o cabeçalho (metadados/resumo) do corpo transcrito."""
    texto = caminho.read_text(encoding="utf-8-sig")
    marcador = "Transcrição Automática"
    if marcador in texto:
        cabecalho, _, corpo = texto.partition(marcador)
    else:
        cabecalho, corpo = "", texto
    return cabecalho.strip(), corpo.strip()


def metricas(corpo: str) -> dict:
    """Métricas estruturais: o retrato do trabalho de normalização pela frente."""
    palavras = corpo.split()
    n = len(palavras)
    tipos = len({L.norm(p) for p in palavras})
    sem_acento = 0
    for bruta in palavras:
        if unicodedata.normalize("NFD", bruta) == bruta and re.search(r"[aeiou]", bruta.lower()):
            pass  # contagem refinada abaixo por par mínimo
    pares = [("nao", "não"), ("voce", "você"), ("entao", "então"), ("ja", "já"), ("so", "só"),
             ("la", "lá"), ("ne", "né"), ("ta", "tá"), ("to", "tô"), ("ai", "aí"),
             ("ate", "até"), ("esta", "está"), ("tambem", "também"), ("consciencia", "consciência")]
    nb = L.norm(corpo)
    perda_diacriticos = {}
    for forma, correta in pares:
        total = len(re.findall(r"\b" + forma + r"\b", nb))
        acentuada = len(re.findall(r"\b" + re.escape(correta) + r"\b", corpo))
        if total:
            perda_diacriticos[forma] = dict(total=total, acentuadas=acentuada, sem_acento=total - acentuada)
    repetidas = sum(1 for i in range(n - 1)
                    if L.norm(palavras[i]) == L.norm(palavras[i + 1]) and len(L.norm(palavras[i])) > 1)
    return dict(
        palavras=n,
        caracteres=len(corpo),
        tipos_lexicais=tipos,
        paragrafos=len([l for l in corpo.splitlines() if l.strip()]),
        pontuacao=dict(virgulas=corpo.count(","), pontos=corpo.count("."),
                       dois_pontos=corpo.count(":"), aspas=corpo.count('"'),
                       reticencias=corpo.count("...")),
        duracao_estimada_min=round(n / 150),
        palavras_repetidas_consecutivas=repetidas,
        perda_diacriticos=perda_diacriticos,
        marcadores_orais={m: len(re.findall(r"\b" + m + r"\b", nb))
                          for m in ("ne", "eh", "uhum", "ai", "ta", "to", "entao", "tipo", "sabe", "cara")},
    )


def janelas(corpo: str, max_n: int = 4, freq_max: int = 5):
    """Tokens, posições suspeitas e janelas 1..N restritas a tokens suspeitos.

    'Suspeito' = token capitalizado no bruto (candidato a nome próprio) ou token
    de frequência <= freq_max com 4+ letras (candidato a termo raro/corrompido).
    Restringe o espaço de busca de ~50 mil janelas para ~34 mil nesta transcrição.
    """
    tokens = corpo.split()
    freq = collections.Counter(L.norm(t) for t in tokens)
    suspeitos = set()
    for i, t in enumerate(tokens):
        nt = L.norm(t)
        if t[:1].isupper() and t.strip(".,:;!?\"'()") not in PALAVRAS_COMUNS:
            suspeitos.add(i)
        elif len(nt) >= 4 and freq[nt] <= freq_max:
            suspeitos.add(i)
    grams: dict[str, dict] = {}
    for n in range(1, max_n + 1):
        for i in range(len(tokens) - n + 1):
            if not any(j in suspeitos for j in range(i, i + n)):
                continue
            texto = " ".join(tokens[i:i + n])
            k = L.norm(texto)
            if not k:
                continue
            if k not in grams:
                grams[k] = dict(texto=texto, n=n, cont=0, pos=i,
                                contexto=corpo[max(0, corpo.find(texto) - 60):corpo.find(texto) + len(texto) + 60])
            grams[k]["cont"] += 1
    return tokens, suspeitos, grams


# --------------------------------------------------------------------------------------
# Varredura
# --------------------------------------------------------------------------------------

ARTIGOS = r"(?:a|o|as|os|de|do|da|dos|das|em|no|na|nos|nas|um|uma|uns|umas|ao|à|e|ou|se|que|com|para|pra|tá|é|aí|já|só|mas|eu|ele|ela|esse|essa|isso|meu|minha|seu|sua|nos|você|vocês)"


def classificar(achado: str, base: str) -> str:
    """Classifica a relação entre a forma achada no texto e a superfície da base.

    exato            -> idênticas (após normalização)
    flexao           -> plural/conjugação natural ('choques de realidade' vs 'choque de realidade')
    artigo           -> a janela apenas acrescenta artigo/preposição ('o Demiurgo')
    truncamento      -> o texto cortou o fim do termo ('Demiurg' vs 'Demiurgo')
    variante         -> divergência real de grafia (candidato a correção)
    """
    a, b = L.norm(achado), L.norm(base)
    if a == b:
        return "exato"
    if a.rstrip("s") == b.rstrip("s") or a == b + "s" or b == a + "s" or a == b + "es" or b == a + "es":
        return "flexao"
    m = re.match(r"^" + ARTIGOS + r"\s+(.*)$", a)
    if m and (m.group(1) == b or m.group(1).rstrip("s") == b.rstrip("s")):
        return "artigo"
    m = re.match(r"^(.*)\s+" + ARTIGOS + r"$", a)
    if m and (m.group(1) == b or m.group(1).rstrip("s") == b.rstrip("s")):
        return "artigo"
    if b.startswith(a) and len(b) - len(a) <= 3:
        return "truncamento"
    if a.startswith(b) and len(a) - len(b) <= 3:
        return "truncamento"
    return "variante"


def carregar_guarda(caminho: Path) -> set[str]:
    """Vocabulário comum pt-BR: formas que nunca devem virar 'variante STT'."""
    if not caminho.exists():
        return set()
    return {L.norm(l.strip()) for l in caminho.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.lstrip().startswith("#")}


def proteger_externos(externos: list[dict]) -> set[str]:
    """Conjunto de proteção da camada Externos.

    Um candidato que contenha qualquer token protegido nunca é convertido em variante de
    termo interno. Caso real desta transcrição: "Nick Bostron" (Nick Bostrom) colidia com a
    variante STT "Nick" -> Nyx (RC-621) documentada na KB-RC.
    """
    prot = set()
    for e in externos:
        for campo in ("variante", "canonico"):
            v = (e.get(campo) or "").strip()
            if not v or v.startswith("["):
                continue
            prot.add(L.norm(v))
            prot.update(L.norm(t) for t in v.split() if len(t) > 2)
    return prot


def varrer(termos: dict, obras: list, corpo: str, sementes: list,
           corte: float = 0.80, corte_duplo: float = 0.75,
           guarda: set[str] | None = None, protegidos: set[str] | None = None) -> dict:
    nb = L.norm(corpo)
    guarda = guarda or set()
    protegidos = protegidos or set()
    tokens, suspeitos, grams = janelas(corpo)
    indice = L.superficies(termos, incluir_glossas=True, incluir_sementes=sementes)

    # 1) ocorrências EXATAS de superfícies da base
    freq_janela = collections.Counter()
    for n in range(1, 5):
        for i in range(len(tokens) - n + 1):
            freq_janela[L.norm(" ".join(tokens[i:i + n]))] += 1
    exatas = {}
    for superficie, alvos in indice.items():
        cont = freq_janela.get(superficie, 0)
        if cont:
            exatas[superficie] = dict(cont=cont, alvos=[list(a) for a in alvos],
                                      generico=superficie in L.GENERICOS,
                                      confianca=max((a[2] for a in alvos), default="baixa"))

    canonicas_norm = {sup for sup, alvos in indice.items()
                      if any(papel == "canonico" for _, papel, _ in alvos)}
    dono_canonica: dict[str, set] = {}
    for sup, alvos in indice.items():
        for cod, papel, _ in alvos:
            if papel == "canonico":
                dono_canonica.setdefault(sup, set()).add(cod)

    def remissivo(cod: str) -> bool:
        """Termo cujo único papel é registrar grafia errada e remeter ao canônico."""
        t = termos.get(cod) or {}
        nome = (t.get("termo") or "").lower()
        return ("erro histórico de stt" in nome or "ver " in nome
                or str(t.get("status", "")).lower() in {"remissão", "remissiva", "deprecado"})

    def homografia_ilegitima(variante_norm: str, codigo_semente: str) -> bool:
        """True se a forma é canônica de OUTRO termo que não é remissivo."""
        donos = dono_canonica.get(variante_norm)
        if not donos:
            return False
        cod_base = codigo_semente or ""
        return not any(remissivo(c) or (c and c in cod_base) for c in donos)

    # 2) sementes do Guia realmente presentes (alta precisão)
    sementes_atingidas, suspensas = [], []
    for s in sementes:
        v = L.norm(s["variante"])
        # semente cuja forma É canônica de outro termo da base = homografia: decidir pelo
        # contexto, nunca por substituição (caso real: "Cristo" -> Krishna RC-414 destruiria
        # RC-009 Sophia (Cristo Cósmico)).
        if (s.get("codigo_base") or "") != "EXTERNO" and v in guarda:
            suspensas.append(dict(variante=s["variante"], canonico=s["canonico"],
                                  codigo_base=s.get("codigo_base", ""),
                                  motivo="forma do vocabulário comum pt-BR — só corrige com confirmação contextual"))
            continue
        if (s.get("codigo_base") or "") != "EXTERNO" and homografia_ilegitima(v, s.get("codigo_base", "")):
            suspensas.append(dict(variante=s["variante"], canonico=s["canonico"],
                                  codigo_base=s.get("codigo_base", ""),
                                  motivo="a forma é canônica de outro termo (homografia) — decide o contexto"))
            continue
        # semente interna cuja forma é protegida pela camada Externos é suspensa
        # (caso real: "Nick" -> Nyx RC-621 colide com Nick Bostrom)
        if protegidos and (s.get("codigo_base") or "") != "EXTERNO" \
                and any(t in protegidos for t in ([v] + v.split())):
            suspensas.append(dict(variante=s["variante"], canonico=s["canonico"],
                                  codigo_base=s.get("codigo_base", ""),
                                  motivo="colide com entidade da camada Externos"))
            continue
        cont = len(re.findall(r"\b" + re.escape(v) + r"\b", nb))
        if cont:
            sementes_atingidas.append(dict(variante=s["variante"], canonico=s["canonico"],
                                           codigo_base=s.get("codigo_base", ""),
                                           cont=cont, origem=s.get("origem", ""),
                                           aprovacao=s.get("status_aprovacao", ""),
                                           observacao=s.get("observacao", "")))
    # dedupe: mesma variante+canônico pode vir do Guia e da KB-RC
    vistas, unicas = set(), []
    for s_ in sementes_atingidas:
        k = (L.norm(s_["variante"]), L.norm(s_["canonico"]))
        if k in vistas:
            continue
        vistas.add(k)
        unicas.append(s_)
    sementes_atingidas = unicas
    sementes_atingidas.sort(key=lambda x: -x["cont"])

    # 3) candidatos fuzzy (geração ampla, decisão posterior)
    gkeys = list(grams.keys())
    choices = [L.chave(k) for k in gkeys]
    consultas, meta = [], []
    for superficie, alvos in indice.items():
        if superficie in L.GENERICOS or len(superficie) < 4:
            continue
        for codigo, papel, conf in alvos:
            consultas.append(L.chave(superficie))
            meta.append((superficie, codigo, papel, conf))
    candidatos = []
    if consultas:
        res = process.cdist(consultas, choices, scorer=Levenshtein.normalized_similarity,
                            score_cutoff=0.78, workers=-1, dtype="f4")
        agregado: dict[str, dict] = {}
        for qi, linha in enumerate(res):
            superficie, codigo, papel, conf = meta[qi]
            for ci in linha.nonzero()[0]:
                g = gkeys[ci]
                if g == superficie:
                    continue
                fonetica = float(linha[ci])
                textual = Levenshtein.normalized_similarity(superficie, g)
                nota = max(fonetica, textual)
                if nota < corte:
                    continue
                info = grams[g]
                item = agregado.setdefault(g, dict(achado=info["texto"], n=info["n"], cont=info["cont"],
                                                   contexto=info["contexto"], alvos=[]))
                item["cont"] = max(item["cont"], info["cont"])
                item["alvos"].append(dict(base=superficie, codigo=codigo, papel=papel,
                                          confianca=conf, fonetica=round(fonetica, 2),
                                          textual=round(textual, 2), nota=round(nota, 2)))
                item.setdefault("_guarda", g in guarda)
        for item in agregado.values():
            vistos, unicos = set(), []
            for a in sorted(item["alvos"], key=lambda a: -a["nota"]):
                k = (a["base"], a["codigo"])
                if k in vistos:
                    continue
                vistos.add(k)
                unicos.append(a)
            item["alvos"] = unicos[:5]
            candidatos.append(item)
    candidatos.sort(key=lambda c: (-c["cont"], -c["alvos"][0]["nota"]))

    # 3b) ADJUDICÁVEIS: exigem concordância das duas métricas, alvo de confiança
    #     não-baixa e forma fora do vocabulário comum pt-BR.
    adjudicaveis = []
    for c in candidatos:
        if c.get("_guarda"):
            continue
        # (1) a forma achada JÁ é uma superfície canônica da base: não há o que corrigir.
        #     Sem isto o motor propunha "Javé" (27x) -> "jabe", invertendo a direção.
        if L.norm(c["achado"]) in canonicas_norm:
            continue
        if protegidos:
            toks = [L.norm(t) for t in c["achado"].split() if t]
            if any(t in protegidos for t in toks):
                continue  # forma da camada Externos: não é variante de termo interno
        for t in c["alvos"]:
            if t["confianca"] == "baixa" or min(t["fonetica"], t["textual"]) < corte_duplo:
                continue
            classe = classificar(c["achado"], t["base"])
            # 'variante' só é aceita com o mesmo nº de palavras (evita artefatos de janela);
            # flexão/artigo/truncamento são aceitos com ±1 palavra por serem informativos.
            mesmo_tamanho = len(t["base"].split()) == c["n"]
            if classe == "variante" and not mesmo_tamanho:
                continue
            item = dict(c)
            item["alvo"] = t
            item["classe"] = classe
            adjudicaveis.append(item)
            break
    for item in adjudicaveis:
        cod = item["alvo"]["codigo"]
        t = termos.get(cod)
        item["alvo"]["superficie_casada"] = item["alvo"]["base"]
        item["alvo"]["canonico_display"] = (t["nucleo"] if t else item["alvo"]["base"])

    adjudicaveis.sort(key=lambda c: (-c["cont"], -c["alvo"]["nota"]))

    # 4) entidades do texto AUSENTES da base (candidatas a [NOTA] ou a novo registro)
    base_txt = L.norm(" ".join(t["termo"] + " " + " ".join(t["aliases"] if "aliases" in t else t["glossas"])
                               for t in termos.values()))
    def _campo_obra(o: dict, *nomes) -> str:
        for n in nomes:
            if o.get(n):
                return str(o[n])
        return ""
    bib_txt = L.norm(" ".join(
        f"{_campo_obra(o, 'Título', 'titulo')} {_campo_obra(o, 'Subtítulo', 'subtitulo')} "
        f"{_campo_obra(o, 'Observações', 'nota')}" for o in obras))
    ausentes = {}
    for m in re.finditer(r"[A-ZÀ-Ü][\wÀ-ÿ]*(?:\s+[A-ZÀ-Ü][\wÀ-ÿ]*){0,3}", corpo):
        seq = m.group(0).strip()
        nseq = L.norm(seq)
        if not nseq or seq.strip(".,:;!?\"'()") in PALAVRAS_COMUNS or len(nseq) < 4:
            continue
        if nseq in base_txt or nseq in bib_txt:
            continue
        item = ausentes.setdefault(nseq, dict(forma=seq, cont=0, contexto=""))
        item["cont"] += 1
        if not item["contexto"]:
            i = corpo.find(seq)
            item["contexto"] = corpo[max(0, i - 70):i + len(seq) + 70]
    ausentes_lista = sorted(ausentes.values(), key=lambda x: -x["cont"])

    # 5) pré-filtro do dossê (o que realmente importa para esta transcrição)
    relevantes = set(L.filtrar_relevantes(termos, grams.keys(), incluir_glossas=True,
                                          incluir_sementes=sementes))
    relevantes.update(c["alvo"]["codigo"] for c in adjudicaveis if c["alvo"]["codigo"] in termos)
    relevantes.update(s["codigo_base"] for s in sementes_atingidas if s["codigo_base"] in termos)

    return dict(tokens=len(tokens), suspeitos=len(suspeitos), janelas=len(grams),
                exatas=exatas, sementes_atingidas=sementes_atingidas,
                sementes_suspensas=suspensas,
                candidatos=candidatos, adjudicaveis=adjudicaveis,
                ausentes=ausentes_lista, relevantes=sorted(relevantes))


# --------------------------------------------------------------------------------------
# Saída
# --------------------------------------------------------------------------------------

def relatorio_md(caminho_txt: Path, cabecalho: str, met: dict, var: dict,
                 termos: dict, obras: list, ocup: dict | None, sementes: list,
                 corte_duplo: float = 0.75) -> str:
    exatas_uteis = {k: v for k, v in var["exatas"].items() if not v["generico"] and v["confianca"] != "baixa"}
    linhas = []
    a = linhas.append
    a(f"# Diagnóstico de transcrição — {caminho_txt.name}")
    a("")
    a(f"- **Fonte:** `{caminho_txt}`")
    a(f"- **Base:** `base-terminologica.xlsx` — {len(termos)} termos, {len(obras)} obras; "
      f"**{len(var['relevantes'])}** termos relevantes para este texto")
    a(f"- **Sementes de variantes carregadas:** {len(sementes)} "
      f"({sum(1 for s in sementes if s.get('status_aprovacao') == 'conflito')} marcadas como conflito)")
    a("")
    a("## 1. Estrutura do texto")
    a("")
    a("| indicador | valor |")
    a("|---|---|")
    a(f"| palavras | {met['palavras']:,} |".replace(",", "."))
    a(f"| caracteres | {met['caracteres']:,} |".replace(",", "."))
    a(f"| tipos lexicais distintos | {met['tipos_lexicais']:,} |".replace(",", "."))
    a(f"| parágrafos | {met['paragrafos']} |")
    a(f"| duração estimada (150 ppm) | {met['duracao_estimada_min']} min |")
    a(f"| vírgulas | {met['pontuacao']['virgulas']} |")
    a(f"| pontos | {met['pontuacao']['pontos']} |")
    a(f"| dois-pontos / aspas | {met['pontuacao']['dois_pontos']} / {met['pontuacao']['aspas']} |")
    a(f"| palavras repetidas em sequência (disfluência) | {met['palavras_repetidas_consecutivas']} |")
    a("")
    a("### Diacríticos (amostra de pares mínimos)")
    a("")
    a("| forma | total | já acentuadas | sem acento |")
    a("|---|---|---|---|")
    pares_ordenados = sorted(met["perda_diacriticos"].items(), key=lambda x: -x[1]["sem_acento"])[:10]
    for forma, d in pares_ordenados:
        a(f"| {forma} | {d['total']} | {d['acentuadas']} | {d['sem_acento']} |")
    a("")
    a("## 2. Cobertura da base")
    a("")
    a(f"- superfícies da base presentes literalmente: **{len(var['exatas'])}** "
      f"(úteis, descartando genéricos e glossas: **{len(exatas_uteis)})**")
    a(f"- termos da base sem nenhuma ocorrência literal: "
      f"**{len(termos) - len({c for v in var['exatas'].values() for c, _, _ in v['alvos']})}** de {len(termos)}")
    a("")
    a("### Ocorrências exatas mais frequentes")
    a("")
    a("| ocorrências | superfície | código | papel | confiança |")
    a("|---|---|---|---|---|")
    for superficie, v in sorted(var["exatas"].items(), key=lambda x: -x[1]["cont"])[:30]:
        cod, papel, conf = v["alvos"][0]
        marca = " ⚠️genérico" if v["generico"] else ""
        a(f"| {v['cont']} | {superficie}{marca} | {cod} | {papel} | {conf} |")
    a("")
    a("## 3. Sementes do Guia encontradas no texto (alta precisão)")
    a("")
    if var["sementes_atingidas"]:
        a("| ocorrências | variante no texto | canônico | código | aprovação |")
        a("|---|---|---|---|---|")
        for s in var["sementes_atingidas"]:
            a(f"| {s['cont']} | {s['variante']} | {s['canonico']} | {s['codigo_base']} | {s['aprovacao']} |")
        a("")
        susp = var.get("sementes_suspensas") or []
        if susp:
            a("### 3.1 Sementes suspensas (colisão com Externos ou homografia interna)")
            a("")
            a("Formas que a base propunha substituir automaticamente, mas que ou pertencem a "
              "entidades do mundo real (camada 3) ou são canônicas de outro termo da própria base. "
              "Nenhuma pode ser trocada às cegas: decidem-se pelo contexto.")
            a("")
            a("| variante | canônico que a base propunha | código | motivo da suspensão |")
            a("|---|---|---|---|")
            for s_ in susp:
                a(f"| {s_['variante']} | {s_['canonico']} | {s_['codigo_base']} | {s_['motivo']} |")
    else:
        a("_Nenhuma variante semeada pelo Guia ocorreu neste texto._")
    a("")
    a("## 4. Candidatos adjudicáveis a variante terminológica")
    a("")
    a(f"{len(var['adjudicaveis'])} formas passaram pelo triplo filtro (concordância das duas "
      f"métricas ≥ {corte_duplo}, alvo de confiança não-baixa e forma fora do vocabulário comum). "
      f"Outras {len(var['candidatos'])} formas ficaram acima do corte frouxo de similaridade "
      "e foram descartadas como colisão com vocabulário comum — permanecem em `diagnostico.json`.")
    a("")
    variantes = [c for c in var["adjudicaveis"] if c["classe"] in ("variante", "truncamento")]
    flexoes = [c for c in var["adjudicaveis"] if c["classe"] in ("flexao", "artigo")]
    a(f"### 4.1 Variantes e truncamentos reais ({len(variantes)} itens) — fila de correção")
    a("")
    a("| occ. | forma no texto | classe | canônico proposto | código | forma casada na base | status | fon. | txt. | contexto |")
    a("|---|---|---|---|---|---|---|---|---|---|")
    for c in variantes[:70]:
        t = c["alvo"]
        status = termos.get(t["codigo"], {}).get("status", "")
        ctx = re.sub(r"\s+", " ", c["contexto"])[:80]
        a(f"| {c['cont']} | {c['achado'][:30]} | {c['classe']} | {t.get('canonico_display', t['base'])[:30]} | "
          f"{t['codigo']} | {t.get('superficie_casada', t['base'])[:22]} | {status} | "
          f"{t['fonetica']:.2f} | {t['textual']:.2f} | …{ctx}… |")
    a("")
    a(f"### 4.2 Flexões e artigos ({len(flexoes)} itens) — NÃO são erro")
    a("")
    a("| occ. | forma no texto | classe | canônico | código |")
    a("|---|---|---|---|---|")
    for c in flexoes[:25]:
        t = c["alvo"]
        a(f"| {c['cont']} | {c['achado'][:34]} | {c['classe']} | "
          f"{t.get('canonico_display', t['base'])[:34]} | {t['codigo']} |")
    a("")
    a("## 5. Entidades do texto ausentes da base")
    a("")
    a(f"{len(var['ausentes'])} sequências capitalizadas sem registro — candidatas a "
      "`[NOTA: termo não encontrado na base]` ou a novo registro (camada *Externos*).")
    a("")
    a("| occ. | forma | contexto |")
    a("|---|---|---|")
    for item in var["ausentes"][:40]:
        a(f"| {item['cont']} | {item['forma'][:40]} | …{item['contexto'][:110]}… |")
    a("")
    a("## 6. Saúde da base")
    a("")
    if ocup:
        a(f"- aba **Fichas**: {ocup['total_registros']} registros; das colunas ricas "
          f"({', '.join(ocup['colunas_ricas'])}), "
          f"{ocup['celulas_placeholder']} células são placeholder `(ver ficha completa em termos/)` "
          f"e {ocup['celulas_preenchidas']} têm conteúdo.")
    nucleo = collections.defaultdict(list)
    for cod, t in termos.items():
        nucleo[L.norm(t["nucleo"])].append(cod)
    duplicados = {k: v for k, v in nucleo.items() if len(v) > 1}
    a(f"- núcleos duplicados (mesmo termo, códigos distintos): **{len(duplicados)}**, "
      f"envolvendo {sum(len(v) for v in duplicados.values())} códigos.")
    for k, v in list(sorted(duplicados.items(), key=lambda x: -len(x[1])))[:10]:
        a(f"    - `{k}` → {', '.join(v)}")
    a("")
    return "\n".join(linhas)


def escrever_csv(caminho: Path, linhas: list[dict], campos: list[str]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)


def slug(nome: str) -> str:
    s = L.norm(nome).replace(" ", "-")
    return re.sub(r"-+", "-", s)[:60]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Diagnóstico de transcrição STT contra a base terminológica.")
    ap.add_argument("transcricao", type=Path)
    ap.add_argument("--base", type=Path, default=Path("base-terminologica.xlsx"),
                    help="planilha (fonte legada); ignorada quando --kb é informado")
    ap.add_argument("--kb", type=Path, default=None,
                    help="pasta KB-RC (fonte de verdade: canonico.json + termos/*.md)")
    ap.add_argument("--variantes-kb", type=Path,
                    default=Path("ferramentas/variantes-kb-extraidas.csv"),
                    help="regras variante->canônico extraídas da prosa das fichas (rc_variantes.py)")
    ap.add_argument("--sementes", type=Path, default=Path("ferramentas/sementes-variantes-stt.csv"))
    ap.add_argument("--externos", type=Path, default=Path("ferramentas/externos.csv"),
                    help="camada 3 (entidades do mundo real): sementes + proteção contra fuzzy interno")
    ap.add_argument("--saida", type=Path, default=None)
    ap.add_argument("--corte", type=float, default=0.80,
                    help="corte frouxo de similaridade (geração de candidatos brutos)")
    ap.add_argument("--corte-duplo", type=float, default=0.75,
                    help="corte mínimo das DUAS métricas para um candidato virar adjudicável")
    ap.add_argument("--guarda", type=Path, default=Path("ferramentas/vocabular-guarda-pt.txt"),
                    help="vocabulário comum pt-BR a ignorar")
    args = ap.parse_args(argv)

    raiz = Path(__file__).resolve().parent.parent
    base_path = args.base if args.base.is_absolute() else raiz / args.base
    sem_path = args.sementes if args.sementes.is_absolute() else raiz / args.sementes
    ext_path = args.externos if args.externos.is_absolute() else raiz / args.externos
    txt_path = args.transcricao if args.transcricao.is_absolute() else raiz / args.transcricao
    saida = args.saida or raiz / "analise" / slug(txt_path.stem)
    saida.mkdir(parents=True, exist_ok=True)

    regras_kb: list[dict] = []
    vk = args.variantes_kb if args.variantes_kb.is_absolute() else raiz / args.variantes_kb
    if vk.exists():
        import csv as _csv
        with vk.open(encoding="utf-8-sig", newline="") as fh:
            for linha in _csv.DictReader(fh):
                if linha.get("confianca_mapeamento") in ("alta", "media") \
                        and linha.get("risco_palavra_comum") == "nao":
                    regras_kb.append(dict(variante=linha["variante"], canonico=linha["canonico"],
                                          codigo_base=linha["codigo"], tipo="kb",
                                          origem=f"kb-rc:{linha['arquivo']}:{linha['classe']}",
                                          observacao=linha["evidencia"][:120],
                                          status_aprovacao="aprovada"))

    if args.kb:
        import rc_kb as KB
        kb_path = args.kb if args.kb.is_absolute() else raiz / args.kb
        meta, termos_json, relacoes_lista, obras = KB.carregar_kb(kb_path)
        fichas = KB.carregar_fichas(kb_path)
        termos = KB.como_termos(termos_json, fichas, regras_kb)
        relacoes = {}
        for r in relacoes_lista:
            relacoes.setdefault(r["tipo"], []).append(
                (r["a"], termos.get(r["a"], {}).get("termo", ""), r["b"],
                 termos.get(r["b"], {}).get("termo", ""), r.get("fonte", "")))
        ocup = dict(total_registros=len(fichas),
                    colunas_ricas=["Definição Sintética", "Contexto / Origem",
                                   "Etimologia e Grafias", "Citações-chave", "Observações"],
                    celulas_placeholder=0,
                    celulas_preenchidas=sum(len(f.secoes) for f in fichas.values()))
        ocup["fichas_com_etimologia_grafias"] = sum(1 for f in fichas.values()
                                                    if "Etimologia e Grafias" in f.secoes)
        ocup["com_grafia_preferida"] = sum(1 for f in fichas.values() if f.grafia_preferida)
        ocup["termos_sem_ficha"] = len(termos_json) - len(fichas)
        ocup["fonte"] = f"KB-RC ({meta.get('formato','?')})"
        print(f"[kb] fonte de verdade: {kb_path} — {len(termos_json)} termos, {len(fichas)} fichas, "
              f"{len(regras_kb)} regras de substituição extraídas da prosa")
    else:
        termos, obras, relacoes, ocup = L.carregar_base(base_path)
    sementes = L.carregar_sementes(sem_path) + regras_kb
    cabecalho, corpo = carregar_transcricao(txt_path)
    met = metricas(corpo)
    guarda_path = args.guarda if args.guarda.is_absolute() else raiz / args.guarda
    guarda = carregar_guarda(guarda_path)
    externos = L.carregar_sementes(ext_path)
    if externos:
        print(f"[externos] camada 3: {len(externos)} entidades do mundo real carregadas e protegidas")
    protegidos = proteger_externos(externos)
    sementes = sementes + externos

    var = varrer(termos, obras, corpo, sementes, corte=args.corte,
                 corte_duplo=args.corte_duplo, guarda=guarda, protegidos=protegidos)

    payload = dict(arquivo=str(txt_path), cabecalho=cabecalho, metricas=met,
                   base=dict(termos=len(termos), obras=len(obras),
                             relacoes={k: len(v) for k, v in relacoes.items()},
                             fichas=ocup),
                   sementes=dict(total=len(sementes), atingidas=var["sementes_atingidas"],
                                 suspensas=var.get("sementes_suspensas", [])),
                   cobertura=dict(superficies_presentes=len(var["exatas"]),
                                  termos_relevantes=var["relevantes"]),
                   guarda_carregada=len(guarda), externos=len(externos),
                   protegidos=len(protegidos),
                   exatas=var["exatas"], candidatos_brutos=var["candidatos"],
                   candidatos_adjudicaveis=var["adjudicaveis"], ausentes=var["ausentes"])
    (saida / "diagnostico.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    (saida / "diagnostico.md").write_text(
        relatorio_md(txt_path, cabecalho, met, var, termos, obras, ocup, sementes,
                     corte_duplo=args.corte_duplo), encoding="utf-8")

    propostas = []
    for c in var["adjudicaveis"]:
        for t in [c["alvo"]]:
            propostas.append(dict(variante=c["achado"],
                                  canonico_proposto=t.get("canonico_display", t["base"]),
                                  superficie_casada=t.get("superficie_casada", t["base"]),
                                  codigo_base=t["codigo"], classe=c["classe"],
                                  ocorrencias=c["cont"],
                                  fonetica=t["fonetica"], textual=t["textual"],
                                  confianca=t["confianca"], origem="varredura-automatica",
                                  contexto=re.sub(r"\s+", " ", c["contexto"])[:160],
                                  status_aprovacao="proposta" if c["classe"] in ("variante", "truncamento") else "informativa"))
    for s in var["sementes_atingidas"]:
        propostas.append(dict(variante=s["variante"], canonico_proposto=s["canonico"],
                              superficie_casada=s["variante"],
                              codigo_base=s["codigo_base"], classe="semente-guia", ocorrencias=s["cont"],
                              fonetica=1.0, textual=1.0, confianca="alta",
                              origem=s["origem"], contexto="", status_aprovacao=s["aprovacao"]))
    escrever_csv(saida / "variantes-propostas.csv", propostas,
                 ["variante", "canonico_proposto", "superficie_casada", "codigo_base", "classe",
                  "ocorrencias", "fonetica", "textual", "confianca", "origem", "contexto",
                  "status_aprovacao"])
    escrever_csv(saida / "ausentes-da-base.csv",
                 [dict(forma=i["forma"], ocorrencias=i["cont"],
                       contexto=re.sub(r"\s+", " ", i["contexto"])[:200]) for i in var["ausentes"]],
                 ["forma", "ocorrencias", "contexto"])

    dossie = L.dossie(termos, var["relevantes"],
                      campos=("codigo", "nucleo", "categoria", "status"))
    (saida / "dossie-bloco.txt").write_text(dossie, encoding="utf-8")

    print(f"[ok] diagnóstico escrito em {saida}")
    print(f"     palavras={met['palavras']}  parágrafos={met['paragrafos']}  "
          f"vírgulas={met['pontuacao']['virgulas']}  pontos={met['pontuacao']['pontos']}")
    n_var = sum(1 for c in var["adjudicaveis"] if c["classe"] in ("variante", "truncamento"))
    print(f"     superfícies da base presentes={len(var['exatas'])}  "
          f"candidatos brutos={len(var['candidatos'])}  "
          f"adjudicáveis={len(var['adjudicaveis'])} (variantes/truncamentos={n_var})  "
          f"ausentes={len(var['ausentes'])}")
    print(f"     termos relevantes para o dossê de trabalho={len(var['relevantes'])} "
          f"({len(dossie)//4} tokens aprox.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
