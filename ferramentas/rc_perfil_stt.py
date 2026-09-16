# -*- coding: utf-8 -*-
"""rc_perfil_stt — perfil comparativo de motores de STT sobre o mesmo áudio.

Nasceu do despacho de 16/09/2026: comparar o STT do YouTube (já revisado, referência da casa) com o
STT do NotebookLM sobre o MESMO áudio, para decidir qual entra na pasta `00-fonte` da esteira.

Mede quatro eixos, sempre com números e nunca com impressão:

  1. **Pontuação e segmentação** — densidade de cada sinal por 1.000 palavras, sentenças,
     palavras por sentença, parágrafos reais.
  2. **Disfluência** — marcadores orais e repetições imediatas (palavra, bigrama, trigrama),
     em valor absoluto e por 1.000 palavras.
  3. **Fidelidade terminológica** — contra a KB-RC: canônicos presentes, variantes STT já
     mapeadas presentes (quanto menos, melhor: são as corrupções que custaram curadoria),
     formas proibidas pela Quarentena, entidades da camada Externos.
  4. **Veredito de integração** — o arquivo cabe nas suposições que as ferramentas `rc_*`
     fazem hoje? O que quebraria, e em silêncio?

O eixo 4 é o que importa para a decisão: um motor melhor que não caiba na esteira custa código, e
um motor pior que caiba custa curadoria. A ferramenta diz qual dos dois preços está na mesa.

Com `--com-diagnostico`, roda o motor de diagnóstico inteiro (`rc_diagnostico.py`) em pasta
temporária para cada arquivo e compara o volume de trabalho que cada um geraria — é a medida mais
direta de "carga das ferramentas rc_*", porque é a mesma ferramenta que a esteira usa.

Uso:
    python ferramentas/rc_perfil_stt.py upload/opcao-b.txt
    python ferramentas/rc_perfil_stt.py transcricoes/<slug>/00-fonte/transcricao-bruta.txt \\
        upload/opcao-b.txt --md docs/pareceres/parecer-stt-notebooklm.md
    python ferramentas/rc_perfil_stt.py A.txt B.txt --com-diagnostico
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import median

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc_kb as KB  # noqa: E402
import rc_lexicon as L  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent

# Marcadores orais. A contagem NÃO pode ser feita sempre no texto normalizado: L.norm derruba
# acentos, e "ó" vira "o" (artigo, 499 falsos positivos) e "hã" vira "ha" ("há", verbo haver).
# Para esses dois a busca é na forma ACENTUADA, no texto original; para os demais (cuja forma sem
# acento não é palavra da língua) busca-se no texto normalizado, o que captura tanto o motor que
# acentua ("né") quanto o que não acentua ("ne").
MARCADORES_ORAIS = ["né", "eh", "uhum", "hum", "ah", "ó", "tá", "tô", "aí", "então", "tipo",
                    "sabe", "cara", "quer dizer", "hã", "sei lá", "olha", "vamos dizer"]
FORMAS_RISCOSAS = {"o", "ha"}  # forma normalizada que colide com palavra comum


def contar_marcador(marcador: str, texto: str, normalizado: str) -> int:
    forma = L.norm(marcador)
    if forma in FORMAS_RISCOSAS:
        return len(re.findall(rf"(?<![\w]){re.escape(marcador)}(?![\w])", texto, re.I))
    return len(re.findall(L.fronteira(forma), normalizado))
PONTUACAO = [(",", "vírgula"), (".", "ponto"), ("?", "interrogação"), ("!", "exclamação"),
             (":", "dois-pontos"), (";", "ponto-e-vírgula"), ("—", "travessão"),
             ("–", "meia-risca"), ("…", "reticências"), ("...", "reticências (3 pontos)"),
             ('"', "aspas retas"), ("“", "aspas curvas"), ("(", "parêntese")]
ROTULOS_FALA = [
    re.compile(r"^\s*\[[A-ZÀ-Ú0-9 ?.\-]{2,40}\]\s*", re.M),          # [GURU DE MALÁ]
    re.compile(r"^\s*\*\*\[[A-ZÀ-Ú0-9 ?.\-]{2,40}\]\*\*", re.M),      # **[NOME]**
    re.compile(r"^\s*[A-ZÀ-Ú][A-ZÀ-Ú a-z]{2,30}:\s", re.M),           # Nome: fala
    re.compile(r"^\s*(?:Speaker|Falante|Orador)\s*\d*\s*[:\-]\s*", re.M | re.I),
]


# ----------------------------------------------------------------------- leitura


def ler(caminho: Path) -> dict:
    """Lê o arquivo preservando o que importa medir: bytes reais, fins de linha, linhas."""
    dados = caminho.read_bytes()
    texto = dados.decode("utf-8-sig", errors="replace")
    linhas = texto.splitlines()
    return {
        "caminho": caminho,
        "bytes": len(dados),
        "crlf": texto.count("\r\n"),
        "lf": texto.count("\n") - texto.count("\r\n"),
        "texto": texto,
        "linhas": linhas,
        "nao_vazias": [l for l in linhas if l.strip()],
    }


def paragrafos(linhas: list[str]) -> list[str]:
    """Parágrafos reais: blocos de linhas não vazias separados por linha em branco.

    Não é o mesmo que "linhas não vazias": num STT com quebra dura a cada fala, cada linha é um
    parágrafo; num texto corrido sem linha em branco, o arquivo inteiro é um parágrafo.
    """
    grupos, atual = [], []
    for l in linhas:
        if l.strip():
            atual.append(l.strip())
        elif atual:
            grupos.append(" ".join(atual))
            atual = []
    if atual:
        grupos.append(" ".join(atual))
    return grupos


def palavras(texto: str) -> list[str]:
    return re.findall(r"[\w'’]+", texto, re.U)


# ------------------------------------------------------- eixo 1: pontuação/segmentação


def eixo_pontuacao(texto: str, paras: list[str], linhas: list[str] | None = None) -> dict:
    """Pontuação e segmentação.

    Duas medidas de segmentação, porque os motores quebram o texto de jeitos diferentes:
    `paragrafos` conta blocos separados por linha em branco (a convenção do produto desta casa),
    e `segmentos_por_quebra` conta linhas não vazias (a convenção de um STT que dá uma linha por
    turno de fala). Um motor pode entregar 288 turnos e **nenhum** parágrafo em branco — medir só
    o segundo faria parecer que ele não segmentou nada.
    """
    pls = palavras(texto)
    n = max(len(pls), 1)
    linhas = linhas if linhas is not None else texto.splitlines()
    segmentos = sum(1 for l in linhas if l.strip())
    cont = {nome: texto.count(simb) for simb, nome in PONTUACAO}
    sentencas = [s.strip() for s in re.split(r"[.!?…]+", texto) if s.strip()]
    por_sent = [len(palavras(s)) for s in sentencas] or [0]
    return {
        "palavras": len(pls),
        "contagem": cont,
        "densidade_por_1000": {k: round(v * 1000 / n, 2) for k, v in cont.items()},
        "sinais_por_100_palavras": round(sum(cont[k] for k in ("vírgula", "ponto", "interrogação",
                                                                "exclamação")) * 100 / n, 2),
        "sentencas": len(sentencas),
        "palavras_por_sentenca": round(sum(por_sent) / len(por_sent), 1),
        "mediana_palavras_por_sentenca": round(median(por_sent), 1),
        "maior_sentenca_palavras": max(por_sent),
        "paragrafos": len(paras),
        "palavras_por_paragrafo": round(n / max(len(paras), 1), 1),
        "paragrafos_por_1000_palavras": round(len(paras) * 1000 / n, 2),
        "segmentos_por_quebra": segmentos,
        "palavras_por_segmento": round(n / max(segmentos, 1), 1),
    }


# ------------------------------------------------------------- eixo 2: disfluência


def eixo_disfluencia(texto: str) -> dict:
    nb = L.norm(texto)
    pls = [L.norm(p) for p in palavras(texto)]
    n = max(len(pls), 1)
    orais = {m: contar_marcador(m, texto, nb) for m in MARCADORES_ORAIS}
    rep1 = sum(1 for i in range(len(pls) - 1) if pls[i] == pls[i + 1] and len(pls[i]) > 1)
    big = [f"{pls[i]} {pls[i+1]}" for i in range(len(pls) - 1)]
    rep2 = sum(1 for i in range(len(big) - 1) if big[i] == big[i + 1] and len(big[i]) > 3)
    tri = [f"{big[i]} {pls[i+2]}" for i in range(len(pls) - 2)]
    rep3 = sum(1 for i in range(len(tri) - 1) if tri[i] == tri[i + 1] and len(tri[i]) > 5)
    # prolongamentos: mesma letra três vezes ou mais ("ééé", "aaa")
    prolong = len(re.findall(r"(.)\1{2,}", texto))
    total = sum(orais.values()) + rep1 + rep2 + rep3
    return {
        "marcadores_orais": orais,
        "total_marcadores": sum(orais.values()),
        "repeticoes_palavra": rep1,
        "repeticoes_bigrama": rep2,
        "repeticoes_trigrama": rep3,
        "prolongamentos": prolong,
        "total_disfluencias": total,
        "por_1000_palavras": round(total * 1000 / n, 2),
    }


# --------------------------------------------------- eixo 3: fidelidade terminológica


def superficies_kb(kb: Path) -> dict:
    """Régua derivada da KB-RC, pela mesma porta que o resto da esteira usa.

    Duas decisões que mudam o número final e não são cosméticas:

    * **canônicos** vêm de `rc_lexicon.superficies` (o índice invertido da casa), não de uma
      montagem própria — assim a contagem é comparável com o que o `rc_diagnostico` relata.
    * **corrupções** são só `variante_stt` + sementes curadas. O campo `Variações` da ficha é
      equivalência CONCEITUAL (Guia §5) e não entra: contar "humano" ou "espírito" como corrupção
      de STT seria medir vocabulário comum e inflar o eixo 3 dos dois lados.
    """
    meta, termos, _rel, _obras = KB.carregar_kb(str(kb))
    fichas = KB.carregar_fichas(str(kb))
    termos_ricos = KB.como_termos(termos, fichas)
    indice = L.superficies(termos_ricos, incluir_glossas=False,
                           incluir_sementes=L.carregar_sementes(str(RAIZ / "ferramentas" / "dados"
                                                                     / "sementes-variantes-stt.csv")))
    canonicos = {sup: alvos[0][0] for sup, alvos in indice.items()
                 if any(p == "canonico" for _, p, _c in alvos) and len(sup) > 2}
    variantes = {sup: alvos[0][0] for sup, alvos in indice.items()
                 if sup not in canonicos and len(sup) > 2
                 and any(p in ("variante_stt", "semente") for _, p, _c in alvos)}
    proibidas_kb = {}
    for f in fichas.values():
        for m in re.finditer(r'NUNCA\s+\**"([^"\n]+?)"\**', f.quarentena or ""):
            proibidas_kb.setdefault(L.norm(m.group(1).strip()), f"Quarentena de {f.codigo}")
    externos = set()
    externos_canonicos = set()
    arq = RAIZ / "ferramentas" / "dados" / "externos.csv"
    if arq.exists():
        # o CSV tem comentários "#" ANTES do cabeçalho — lê-los como campo quebra o DictReader
        with arq.open(encoding="utf-8-sig", newline="") as fh:
            corpo = [l for l in fh if not l.lstrip().startswith("#")]
        for linha in csv.DictReader(corpo):
            v = (linha.get("variante") or "").strip()
            c = (linha.get("canonico") or "").strip()
            if len(v) > 2:
                externos.add(L.norm(v))
            if len(c) > 2:
                externos_canonicos.add(L.norm(c))
    return {"canonicos": canonicos, "variantes": variantes, "proibidas": proibidas_kb,
            "externos": externos, "externos_canonicos": externos_canonicos,
            "n_termos": len(termos), "n_fichas": len(fichas), "origem": str(kb)}


def regua_para(regua_base: dict, caminho: Path, kb: Path) -> dict:
    """Régua base + as formas proibidas do livro-razão, quando o arquivo pertence a uma transcrição.

    Sem isso o eixo 3 mediria só a Quarentena (5 formas) e deixaria de fora as 24 variantes que o
    revisor adjudicou como aceitas — que são justamente as que o QA G3 fiscaliza.
    """
    regua = dict(regua_base)
    pasta = None
    for pai in caminho.resolve().parents:
        if pai.name == "transcricoes":
            break
        if (pai / "10-diagnostico").is_dir():
            pasta = pai
            break
    if pasta is not None:
        try:
            import rc_qa
            regua["proibidas"] = {L.norm(f): mot for f, mot in
                                  rc_qa.formas_proibidas(pasta, kb).items()}
            regua["pasta_ledger"] = str(pasta.relative_to(RAIZ))
        except Exception as exc:  # régua nunca pode derrubar a medição
            regua["aviso_ledger"] = f"livro-razão não lido ({exc}); só Quarentena"
    return regua


def contar(conjunto: dict | set, nb: str) -> tuple[int, int, list]:
    """(formas distintas achadas, ocorrências totais, amostra com código)."""
    itens = conjunto.items() if isinstance(conjunto, dict) else ((x, "") for x in conjunto)
    achadas, ocorrencias, amostra = 0, 0, []
    for forma, cod in itens:
        if not forma:
            continue
        n = len(re.findall(L.fronteira(forma), nb))
        if n:
            achadas += 1
            ocorrencias += n
            amostra.append((forma, cod, n))
    amostra.sort(key=lambda x: -x[2])
    return achadas, ocorrencias, amostra[:12]


def eixo_terminologia(texto: str, regua: dict) -> dict:
    nb = L.norm(texto)
    can_d, can_o, can_a = contar(regua["canonicos"], nb)
    var_d, var_o, var_a = contar(regua["variantes"], nb)
    pro_d, pro_o, pro_a = contar(regua["proibidas"], nb)
    ext_d, ext_o, _ext_a = contar(regua["externos"], nb)
    exc_d, exc_o, _exc_a = contar(regua.get("externos_canonicos", set()), nb)
    n = max(len(palavras(texto)), 1)
    return {
        "canonicos_distintos": can_d, "canonicos_ocorrencias": can_o, "canonicos_amostra": can_a,
        "variantes_stt_distintas": var_d, "variantes_stt_ocorrencias": var_o,
        "variantes_stt_amostra": var_a,
        "proibidas_distintas": pro_d, "proibidas_ocorrencias": pro_o, "proibidas_amostra": pro_a,
        "externos_distintos": ext_d, "externos_ocorrencias": ext_o,
        "externos_canonicos_distintos": exc_d, "externos_canonicos_ocorrencias": exc_o,
        "corrupcoes_por_1000_palavras": round(var_o * 1000 / n, 2),
        "taxa_fiducia": round(can_o / max(can_o + var_o, 1), 4),
    }


# --------------------------------------------- eixo 5: proveniência (A × B, precisa dos dois)


def assinatura(texto: str) -> Counter:
    """Multiconjunto de palavras normalizadas — a impressão digital do fluxo de fala."""
    return Counter(L.norm(w) for w in palavras(texto))


def eixo_proveniencia(a: dict, b: dict) -> dict:
    """Os dois arquivos vêm do MESMO reconhecimento de fala ou de motores independentes?

    A pergunta parece acadêmica e não é: se B for o mesmo ASR do YouTube com uma camada de
    reescrita por cima, então "trocar de motor" é a decisão errada — a decisão certa é sobre pôr ou
    não pôr um LLM entre o reconhecimento e o revisor, e o risco passa a ser edição silenciosa do
    bruto, não qualidade de escuta. Sem este eixo, o parecer compararia ouvidos que são o mesmo
    ouvido e atribuiria ao motor errado o que é mérito (ou dano) da camada de reescrita.

    Mede três coisas independentes:
      divergência lexical  — palavras que um tem e o outro não (multiconjunto, sem alinhamento);
      sobreposição de tipos — Jaccard e hapax em comum (paráfrase derruba os dois);
      marcadores orais     — quantos têm contagem IDÊNTICA nos dois (mesmo ASR repete igual).
    """
    ca: Counter = a["assinatura"]
    cb: Counter = b["assinatura"]
    na, nb = sum(ca.values()), sum(cb.values())
    removidas = ca - cb
    acrescentadas = cb - ca
    divergencia = (sum(removidas.values()) + sum(acrescentadas.values())) / max(na, 1)
    tipos_a, tipos_b = set(ca), set(cb)
    jaccard = len(tipos_a & tipos_b) / max(len(tipos_a | tipos_b), 1)
    hapax_a = {w for w, n in ca.items() if n == 1}
    hapax_b = {w for w, n in cb.items() if n == 1}
    hapax_comuns = len(hapax_a & hapax_b) / max(len(hapax_a), 1)
    ma, mb = a["disfluencia"]["marcadores_orais"], b["disfluencia"]["marcadores_orais"]
    identicos = [m for m in ma if ma.get(m) == mb.get(m) and ma.get(m, 0) > 0]
    taxa_ident = len(identicos) / max(len([m for m in ma if ma[m] > 0]), 1)
    # máscara de profanidade/PII: a camada de reescrita pode CENSURAR o texto ("merda" -> "m****"),
    # e asterisco não é palavra da língua — se entrar no produto, entra como lixo tipográfico
    masc_a = re.findall(r"\w*\*{2,}\w*", a.get("texto_bruto", ""))
    masc_b = re.findall(r"\w*\*{2,}\w*", b.get("texto_bruto", ""))
    if divergencia <= 0.05 and taxa_ident >= 0.5:
        veredito = ("MESMO reconhecimento de fala com camada de reescrita por cima "
                    "(pontuação/segmentação e edição pontual) — não são dois motores")
    elif divergencia <= 0.15:
        veredito = "mesma base de áudio com edição substancial em um dos lados"
    else:
        veredito = "reconhecimentos independentes — a comparação de motor é válida como tal"
    return {
        "palavras_a": na, "palavras_b": nb,
        "removidas": sum(removidas.values()), "acrescentadas": sum(acrescentadas.values()),
        "divergencia": round(divergencia, 4),
        "jaccard_tipos": round(jaccard, 4),
        "hapax_comuns": round(hapax_comuns, 4),
        "marcadores_iguais": len(identicos), "taxa_marcadores_iguais": round(taxa_ident, 3),
        "marcadores_iguais_lista": sorted(identicos),
        "top_removidas": [f"{w}×{n}" for w, n in removidas.most_common(12)],
        "top_acrescentadas": [f"{w}×{n}" for w, n in acrescentadas.most_common(12)],
        "mascarados_a": len(masc_a), "mascarados_b": len(masc_b),
        "amostra_mascarados_b": masc_b[:8],
        "veredito": veredito,
    }


# ------------------------------------------------- eixo 4: veredito de integração


def eixo_integracao(arq: dict) -> dict:
    """As suposições que a esteira faz hoje, testadas contra este arquivo."""
    texto, linhas = arq["texto"], arq["linhas"]
    maior = max((len(l) for l in linhas), default=0)
    corpo_linha = max(linhas, key=len) if linhas else ""
    cobertura = len(corpo_linha) / max(len(texto), 1)
    marcador = "Transcrição Automática" in texto
    rotulos = {}
    for i, padrao in enumerate(ROTULOS_FALA):
        achados = padrao.findall(texto)
        if achados:
            rotulos[f"padrão {i + 1}"] = len(achados)
    # um ou dois achados são falso positivo ("Falei:" casa com "Nome: fala"); diarização nativa
    # de verdade aparece dezenas de vezes num arquivo de 2 horas
    diarizacao = any(v >= 3 for v in rotulos.values())
    sinais = sum(texto.count(s) for s in (",", ".", "?", "!"))
    pls = max(len(palavras(texto)), 1)
    densidade = sinais * 1000 / pls
    # Três desfechos, e a diferença entre os dois últimos é o que decide o parecer:
    #   ok       — a suposição continua valendo;
    #   codigo   — a suposição quebra e custa alteração nas ferramentas (preço pago uma vez);
    #   superada — a premissa da norma deixa de valer porque o motor já entrega o que a norma
    #              mandava o revisor fazer à mão (o trabalho manual desaparece; não é defeito).
    quebras = [
        # corrigido em 16/09/2026 (rc_leitura.py): a cascata é marcador → linha mais longa →
        # arquivo inteiro COM AVISO. O que sobra é o resíduo do critério 3: sem marcador e sem linha
        # dominante, o corpo inclui o cabeçalho — o instrumento avisa, mas não separa.
        ("rc_novo.py / rc_indice.py medem o corpo pelo critério único de rc_leitura.py "
         "(marcador → linha mais longa → arquivo inteiro, com aviso)",
         "ok" if (marcador or cobertura >= 0.8) else "codigo",
         (f"marcador presente: corpo separado do cabeçalho" if marcador else
          f"a maior linha cobre {cobertura:.1%} do arquivo"
          + ("" if cobertura >= 0.8 else
             " — cai no critério 3 (arquivo inteiro): o corpo inclui o cabeçalho, medição "
             "contaminada; rc_leitura AVISA em metadados.yaml, mas ainda não separa"))),
        ("rc_diagnostico.carregar_transcricao separa cabeçalho pelo marcador "
         "'Transcrição Automática' (pendência: parecer-motor-stt §8 item 2)",
         "ok" if marcador else "codigo",
         "marcador presente" if marcador else "sem marcador: o arquivo inteiro vira corpo e o "
                                              "cabeçalho sai vazio"),
        ("diarização opção B (rótulos inferidos pelo revisor)",
         "superada" if diarizacao else "ok",
         f"rótulos nativos detectados ({rotulos}): inferir vira conferir" if diarizacao
         else "sem rótulos nativos: o revisor continua inferindo"),
        ("Guia §8 (pontuação é corretiva, o STT não traz)",
         "superada" if densidade >= 5 else "ok",
         f"{densidade:.1f} sinais por 1.000 palavras"
         + (" — pontuação praticamente ausente" if densidade < 5
            else " — pontuação nativa: a norma passa a ser de conferência, não de reconstrução")),
    ]
    return {
        "maior_linha_chars": maior,
        "cobertura_corpo_por_linha": round(cobertura, 4),
        "marcador_cabecalho": marcador,
        "rotulos_nativos": rotulos,
        "diarizacao_nativa": diarizacao,
        "sinais_por_1000": round(sinais * 1000 / pls, 2),
        "quebras": [{"suposicao": s, "tipo": t, "compativel": t != "codigo", "detalhe": d}
                    for s, t, d in quebras],
        "ferramentas_afetadas": [
            "rc_novo.py — mede o bruto (bytes, linhas, sha256, corpo) e grava metadados.yaml",
            "rc_indice.py — coluna palavras_brutas do catálogo vem da linha mais longa",
            "rc_diagnostico.py — separação de cabeçalho pelo marcador",
            "metadados.yaml — campos corpo_linha, corpo_caracteres, corpo_palavras, pontuacao_original",
            "rc_qa.py G1 — sha256 do bruto (não muda, mas o bruto passa a ter outra forma)",
            "Guia §8 e §9 — pontuação e diarização deixam de ser corretivas se o motor já as traz",
        ],
    }


# ------------------------------------------------------------------- diagnóstico


def carregar_guarda() -> set:
    """Vocabulário comum pt-BR da casa (o mesmo que o rc_diagnostico usa para não propor substituição)."""
    arq = RAIZ / "ferramentas" / "dados" / "vocabular-guarda-pt.txt"
    if not arq.exists():
        return set()
    return {L.norm(l.strip()) for l in arq.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")}


def classificar_ausentes(linhas: list[dict], texto_norm: str, guarda: set) -> dict:
    """Separa o joio do trigo na lista de "ausentes da base".

    O `rc_diagnostico` procura **sequências capitalizadas** sem registro na base. A heurística é boa
    num STT que não pontua; num STT que pontua, toda inicial de frase é capitalizada e a lista enche
    de verbo e advérbio comuns ("Infelizmente", "Claro", "Desintegrou"). Sem esta separação, o eixo 3
    pune o motor justamente por aquilo que ele fez de melhor.

    Quatro baldes, do mais ruidoso ao que interessa:
      n_grama   janela de 2-4 palavras — não é entidade, é recorte;
      comum     palavra única que está no vocabulário-guarda da casa;
      capital   palavra única que também ocorre em minúscula no texto (inicial de frase);
      real      o que sobra — candidata de verdade a termo novo ou a [NOTA].
    """
    formas = [(l.get("forma", ""), int(l.get("ocorrencias") or 0)) for l in linhas]
    multi, comum, capital, real = [], [], [], []
    for f, n in formas:
        if not f.strip():
            continue
        if " " in f.strip():
            multi.append((f, n))
        elif L.norm(f) in guarda:
            comum.append((f, n))
        elif len(re.findall(rf"(?<!\w){re.escape(L.norm(f))}(?!\w)", texto_norm)) > n:
            capital.append((f, n))
        else:
            real.append((f, n))
    res = {}
    for nome, grupo in (("n_grama", multi), ("comum", comum), ("capital", capital), ("real", real)):
        res[nome] = {"formas": len(grupo), "ocorrencias": sum(n for _, n in grupo),
                     "amostra": [f for f, _ in sorted(grupo, key=lambda x: -x[1])[:12]]}
    res["total_formas"] = len(formas)
    res["total_ocorrencias"] = sum(n for _, n in formas)
    return res


# artigos, preposições e conjunções que o motor de diagnóstico gruda na janela — não fazem parte
# da grafia da entidade, e contá-los inflaria a dispersão ("do paraíso original" ≠ "paraíso original")
_STOP = {"o", "a", "os", "as", "um", "uma", "do", "da", "dos", "das", "de", "d", "e", "no", "na",
         "nos", "nas", "em", "esse", "essa", "este", "esta", "aquele", "aquela", "que", "se", "ao",
         "aos", "para", "pra", "por", "com", "seu", "sua", "seus", "suas", "ele", "ela", "meu",
         "minha", "nosso", "nossa", "como", "mais", "mas", "ou", "ja", "é", "eh", "né", "ne", "tem"}


def nucleo_grafia(variante: str) -> str:
    toks = [t for t in L.norm(variante).split() if t]
    while toks and toks[0] in _STOP:
        toks.pop(0)
    while toks and toks[-1] in _STOP:
        toks.pop()
    return " ".join(toks)


def dispersao_de_grafias(linhas: list[dict]) -> dict:
    """Quantas grafias diferentes cada motor produziu para a MESMA entidade.

    Vem do próprio livro-razão do `rc_diagnostico` (colunas `variante` e `canonico_proposto`), com as
    formas normalizadas e sem os artigos que a janela gruda — então não sofre o artefato de
    capitalização nem o de recorte. Entra só o que é proposta de verdade (status_aprovacao
    "proposta" ou "aprovada"); linhas "informativa" são artigo e flexão, ruído morfológico.
    É a medida mais direta de "alucinou menos ou mais nas entidades", que foi o que o despacho pediu.
    """
    por_alvo: dict[str, set] = {}
    for l in linhas:
        if (l.get("status_aprovacao") or "").strip() == "informativa":
            continue
        alvo = (l.get("canonico_proposto") or "").strip()
        nucleo = nucleo_grafia(l.get("variante") or "")
        if alvo and nucleo:
            por_alvo.setdefault(alvo, set()).add(nucleo)
    ordenado = sorted(por_alvo.items(), key=lambda x: -len(x[1]))
    return {"entidades": len(por_alvo),
            "grafias_distintas": sum(len(v) for v in por_alvo.values()),
            "media_por_entidade": round(sum(len(v) for v in por_alvo.values())
                                        / max(len(por_alvo), 1), 2),
            "piores": [(alvo, sorted(v)) for alvo, v in ordenado[:8]]}


def rodar_diagnostico(caminho: Path, kb: Path) -> dict:
    """Roda o motor de diagnóstico da esteira em pasta temporária e resume o volume de trabalho."""
    with tempfile.TemporaryDirectory(prefix="perfil-stt-") as tmp:
        cmd = [sys.executable, str(RAIZ / "ferramentas" / "rc_diagnostico.py"), str(caminho),
               "--kb", str(kb), "--saida", tmp]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(RAIZ), timeout=1800)
        res = {"exit": proc.returncode, "erro": proc.stderr[-600:] if proc.returncode else ""}
        out = Path(tmp)
        cand = list(out.rglob("variantes-propostas.csv"))
        if cand:
            with cand[0].open(encoding="utf-8-sig", newline="") as fh:
                linhas = list(csv.DictReader(fh))
            res["linhas_ledger"] = len(linhas)
            res["por_classe"] = dict(Counter((l.get("classe") or "?") for l in linhas))
            # "adjudicável" é a coluna status_aprovacao, não um chute meu: o rc_diagnostico marca
            # "proposta" o que exige decisão do revisor (variante, truncamento) e "informativa" o
            # resto. É esse o número que mede esforço manual de curadoria.
            res["propostas"] = sum(1 for l in linhas
                                   if (l.get("status_aprovacao") or "").strip() == "proposta")
            res["informativas"] = sum(1 for l in linhas
                                      if (l.get("status_aprovacao") or "").strip() == "informativa")
            res["por_status"] = dict(Counter((l.get("status_aprovacao") or "(vazio)").strip()
                                             or "(vazio)" for l in linhas))
        aus = list(out.rglob("ausentes-da-base.csv"))
        if aus:
            with aus[0].open(encoding="utf-8-sig", newline="") as fh:
                linhas_aus = list(csv.DictReader(fh))
            res["ausentes_da_base"] = len(linhas_aus)
            res["ausentes_classificados"] = classificar_ausentes(
                linhas_aus, L.norm(caminho.read_text(encoding="utf-8-sig", errors="replace")),
                carregar_guarda())
        if cand:
            res["dispersao"] = dispersao_de_grafias(linhas)
        md = list(out.rglob("diagnostico.md"))
        if md:
            t = md[0].read_text(encoding="utf-8")
            for chave, padrao in (("sementes_atingidas", r"Sementes atingidas\D*(\d+)"),
                                  ("superficies_exatas", r"ocorrências EXATAS\D*(\d+)")):
                m = re.search(padrao, t, re.I)
                if m:
                    res[chave] = int(m.group(1))
        return res


# ------------------------------------------------------------------------ saída


ESTAGIOS = {
    "00-fonte": ("bruto", "STT cru: corrupções e formas proibidas SÃO esperadas — é a matéria-prima"),
    "10-diagnostico": ("diagnóstico", "saída de ferramenta, não texto de revisão"),
    "20-blocos": ("curado", "texto em revisão: formas proibidas devem tender a zero (QA G3)"),
    "30-produto": ("curado", "produto final: formas proibidas DEVEM ser zero (QA G3)"),
    "40-devolucao": ("curado", "devolução ao Comandante: formas proibidas DEVEM ser zero"),
    "90-registro": ("registro", "metadados/livro-razão"),
}


def estagio(caminho: Path) -> tuple[str, str]:
    """Em que estágio da esteira este arquivo mora — muda como se lê o eixo 3.

    Comparar um bruto com um texto curado seria injusto: o curado já teve as corrupções
    substituídas. A ferramenta diz em voz alta qual dos dois está medindo.
    """
    for parte in caminho.resolve().parts:
        if parte in ESTAGIOS:
            return ESTAGIOS[parte]
    return ("solto", "arquivo fora de transcricoes/ (ex.: upload/) — leitura de BRUTO, "
                      "é o caso do experimento de motor")


def classe_de_leitura(estagio: str) -> str:
    """Agrupa estágios pela forma de ler o eixo 3: cru, curado ou outro."""
    return {"bruto": "cru", "solto": "cru", "curado": "curado"}.get(estagio, "outro")


def perfil(caminho: Path, kb: Path, regua: dict, com_diag: bool) -> dict:
    arq = ler(caminho)
    paras = paragrafos(arq["linhas"])
    corpo = arq["texto"]
    est, leitura = estagio(caminho)
    return {
        "arquivo": str(caminho),
        "nome": caminho.name,
        "estagio": est, "leitura_estagio": leitura,
        "bytes": arq["bytes"], "crlf": arq["crlf"], "lf": arq["lf"],
        "linhas": len(arq["linhas"]), "linhas_nao_vazias": len(arq["nao_vazias"]),
        "paragrafos_reais": len(paras),
        "estrutura": eixo_pontuacao(corpo, paras, arq["linhas"]),
        "pontuacao": eixo_pontuacao(corpo, paras, arq["linhas"]),
        "assinatura": assinatura(corpo),
        "texto_bruto": corpo,
        "disfluencia": eixo_disfluencia(corpo),
        "terminologia": eixo_terminologia(corpo, regua),
        "integracao": eixo_integracao(arq),
        "diagnostico": rodar_diagnostico(caminho, kb) if com_diag else None,
    }


def fmt(n) -> str:
    return f"{n:,}".replace(",", ".") if isinstance(n, int) else str(n)


def imprimir(p: dict) -> None:
    e, d, t, i = p["pontuacao"], p["disfluencia"], p["terminologia"], p["integracao"]
    print(f"\n{'=' * 78}\n{p['nome']}  ({fmt(p['bytes'])} bytes · {p['linhas']} linhas · "
          f"{p['paragrafos_reais']} parágrafos reais · CRLF {p['crlf']}/LF {p['lf']})\n{'=' * 78}")
    print(f"    estágio na esteira: {p['estagio']} — {p['leitura_estagio']}")
    print(f"\n[1] PONTUAÇÃO E SEGMENTAÇÃO — {fmt(e['palavras'])} palavras")
    print(f"    sinais por 100 palavras: {e['sinais_por_100_palavras']}")
    print(f"    sentenças: {fmt(e['sentencas'])} · palavras/sentença: "
          f"{e['palavras_por_sentenca']} (mediana {e['mediana_palavras_por_sentenca']}, "
          f"maior {fmt(e['maior_sentenca_palavras'])})")
    print(f"    parágrafos: {fmt(e['paragrafos'])} · palavras/parágrafo: {e['palavras_por_paragrafo']}")
    for k, v in e["contagem"].items():
        if v:
            print(f"      {k:<22} {fmt(v):>7}  ({e['densidade_por_1000'][k]}/1.000 palavras)")
    print(f"\n[2] DISFLUÊNCIA — {fmt(d['total_disfluencias'])} marcas "
          f"({d['por_1000_palavras']} por 1.000 palavras)")
    print(f"    repetições: palavra {fmt(d['repeticoes_palavra'])} · bigrama "
          f"{fmt(d['repeticoes_bigrama'])} · trigrama {fmt(d['repeticoes_trigrama'])} · "
          f"prolongamentos {fmt(d['prolongamentos'])}")
    top = sorted(d["marcadores_orais"].items(), key=lambda x: -x[1])[:10]
    print("    marcadores orais: " + " · ".join(f"{m} {fmt(n)}" for m, n in top if n))
    print(f"\n[3] FIDELIDADE TERMINOLÓGICA (contra a KB-RC)")
    print(f"    canônicos presentes: {fmt(t['canonicos_distintos'])} formas distintas, "
          f"{fmt(t['canonicos_ocorrencias'])} ocorrências")
    print(f"    variantes STT mapeadas presentes: {fmt(t['variantes_stt_distintas'])} formas, "
          f"{fmt(t['variantes_stt_ocorrencias'])} ocorrências "
          f"({t['corrupcoes_por_1000_palavras']}/1.000 palavras)")
    print(f"    formas proibidas (Quarentena + livro-razão): {fmt(t['proibidas_distintas'])} formas, "
          f"{fmt(t['proibidas_ocorrencias'])} ocorrências")
    print(f"    Externos — forma canônica: {fmt(t['externos_canonicos_distintos'])} formas, "
          f"{fmt(t['externos_canonicos_ocorrencias'])} ocorrências · "
          f"forma corrompida: {fmt(t['externos_distintos'])} formas, "
          f"{fmt(t['externos_ocorrencias'])} ocorrências")
    print(f"    taxa de confiança (canônico ÷ canônico+variante): {t['taxa_fiducia']:.4f}")
    if t["variantes_stt_amostra"]:
        print("    piores corrupções: " + ", ".join(
            f"'{f}'×{n}" for f, c, n in t["variantes_stt_amostra"][:8]))
    print(f"\n[4] INTEGRAÇÃO À ESTEIRA")
    print(f"    maior linha: {fmt(i['maior_linha_chars'])} chars = "
          f"{i['cobertura_corpo_por_linha']:.1%} do arquivo")
    print(f"    marcador 'Transcrição Automática': {'sim' if i['marcador_cabecalho'] else 'não'}")
    print(f"    rótulos de fala nativos: {i['rotulos_nativos'] or 'nenhum'} "
          f"→ diarização nativa: {'sim' if i['diarizacao_nativa'] else 'não'}")
    marca_tipo = {"ok": "compatível", "codigo": "CUSTA CÓDIGO", "superada": "PREMISSA SUPERADA"}
    for q in i["quebras"]:
        print(f"      [{marca_tipo[q['tipo']]:<18}] {q['suposicao']}\n{'':<25}{q['detalhe']}")
    if p["diagnostico"]:
        dg = p["diagnostico"]
        print(f"\n[5] DIAGNÓSTICO DA ESTEIRA (rc_diagnostico.py, exit {dg['exit']})")
        for k in ("linhas_ledger", "propostas", "informativas", "ausentes_da_base",
                  "superficies_exatas", "sementes_atingidas"):
            if k in dg:
                print(f"    {k}: {fmt(dg[k])}")
        if dg.get("ausentes_classificados"):
            ac = dg["ausentes_classificados"]
            print(f"    ausentes da base, separando o joio do trigo "
                  f"({ac['total_formas']} formas no total):")
            for k, rot in (("n_grama", "janela de 2-4 palavras (recorte, não entidade)"),
                           ("comum", "palavra única do vocabulário comum"),
                           ("capital", "inicial de frase (a palavra também ocorre em minúscula)"),
                           ("real", "CANDIDATA REAL a termo novo")):
                b = ac[k]
                print(f"      {rot:<56} {b['formas']:>4} formas · {b['ocorrencias']:>4} occ")
        if dg.get("dispersao"):
            dp = dg["dispersao"]
            print(f"    dispersão de grafias: {dp['grafias_distintas']} grafias para "
                  f"{dp['entidades']} entidades (média {dp['media_por_entidade']})")
            for alvo, vs in dp["piores"][:5]:
                print(f"      {alvo[:34]:<36} {len(vs)} grafias: {', '.join(vs[:6])}")
        if dg.get("por_status"):
            print("    por status_aprovacao: " + ", ".join(f"{k} {fmt(v)}" for k, v in
                                                           sorted(dg["por_status"].items())))
        if dg.get("por_classe"):
            print("    por classe: " + ", ".join(f"{k} {fmt(v)}" for k, v in
                                                 sorted(dg["por_classe"].items())))
        if dg.get("erro"):
            print("    erro: " + dg["erro"][:300])


def comparar(a: dict, b: dict) -> None:
    print(f"\n{'=' * 78}\nCOMPARATIVO — {a['nome']} (A) × {b['nome']} (B)\n{'=' * 78}")
    if classe_de_leitura(a["estagio"]) != classe_de_leitura(b["estagio"]):
        print(f"  [ATENÇÃO] leituras incompatíveis: A={a['estagio']}, B={b['estagio']}. "
              f"Medir um bruto contra um texto curado mede o revisor, não o motor.")
    linhas = tabela_comparativa(a, b)  # fonte única: terminal e markdown mostram os mesmos números
    print(f"\n{'métrica':<44}{'A':>12}{'B':>12}{'Δ B−A':>12}   melhor")
    print("-" * 92)
    for rot, va, vb, criterio in linhas:
        try:
            delta = round(vb - va, 4)
        except TypeError:
            delta = "—"
        if criterio == "—" or not isinstance(delta, (int, float)) or delta == 0:
            melhor = "—"
        else:
            melhor = "B" if (delta > 0) == (criterio == "maior") else "A"
        print(f"{rot:<44}{fmt(va):>12}{fmt(vb):>12}{str(delta):>12}   {melhor}")
    if a.get("assinatura") and b.get("assinatura"):
        pv = eixo_proveniencia(a, b)
        print(f"\n[6] PROVENIÊNCIA — os dois lados vêm do mesmo reconhecimento de fala?")
        print(f"    divergência lexical: {pv['divergencia']:.2%} "
              f"({fmt(pv['removidas'])} palavras de A ausentes em B, "
              f"{fmt(pv['acrescentadas'])} palavras de B ausentes em A)")
        print(f"    vocabulário: Jaccard {pv['jaccard_tipos']:.3f} · hapax em comum "
              f"{pv['hapax_comuns']:.3f}")
        print(f"    marcadores orais com contagem IDÊNTICA: {pv['marcadores_iguais']} "
              f"({pv['taxa_marcadores_iguais']:.0%}) → {', '.join(pv['marcadores_iguais_lista'])}")
        print(f"    maiores perdas em B: {', '.join(pv['top_removidas'][:10])}")
        print(f"    maiores acréscimos em B: {', '.join(pv['top_acrescentadas'][:10])}")
        print(f"    tokens mascarados com asterisco: A {pv['mascarados_a']} · B {pv['mascarados_b']}"
              + (f" → {', '.join(pv['amostra_mascarados_b'])}" if pv["mascarados_b"] else ""))
        print(f"    VEREDITO: {pv['veredito']}")
    ka = sum(1 for q in a["integracao"]["quebras"] if q["compativel"])
    kb_ = sum(1 for q in b["integracao"]["quebras"] if q["compativel"])
    tot = len(a["integracao"]["quebras"])
    sa = sum(1 for q in a["integracao"]["quebras"] if q["tipo"] == "superada")
    sb = sum(1 for q in b["integracao"]["quebras"] if q["tipo"] == "superada")
    print(f"\ncompatibilidade com a esteira: A {ka}/{tot} · B {kb_}/{tot} "
          f"(premissas superadas: A {sa}, B {sb})")
    rotulo = {"codigo": "B CUSTA CÓDIGO  ", "superada": "B SUPERA PREMISSA"}
    for q in b["integracao"]["quebras"]:
        if q["tipo"] != "ok":
            print(f"  [{rotulo[q['tipo']]}] {q['suposicao']}\n{'':<21}{q['detalhe']}")


def tabela_comparativa(a: dict, b: dict) -> list[tuple]:
    """Linhas (rótulo, valor A, valor B, critério de melhor) do comparativo.

    Fonte única: o terminal (`comparar`) e o markdown (`para_markdown`) imprimem exatamente estas
    linhas. Duas listas separadas já produziram um relatório markdown mais curto que a medição.
    """
    linhas = [
        ("bytes", a["bytes"], b["bytes"], "—"),
        ("linhas", a["linhas"], b["linhas"], "—"),
        ("parágrafos (separados por linha em branco)", a["paragrafos_reais"],
         b["paragrafos_reais"], "—"),
        ("segmentos por quebra de linha", a["pontuacao"]["segmentos_por_quebra"],
         b["pontuacao"]["segmentos_por_quebra"], "maior"),
        ("palavras", a["pontuacao"]["palavras"], b["pontuacao"]["palavras"], "—"),
        ("sinais por 100 palavras", a["pontuacao"]["sinais_por_100_palavras"],
         b["pontuacao"]["sinais_por_100_palavras"], "maior"),
        ("sentenças", a["pontuacao"]["sentencas"], b["pontuacao"]["sentencas"], "maior"),
        ("palavras/sentença", a["pontuacao"]["palavras_por_sentenca"],
         b["pontuacao"]["palavras_por_sentenca"], "menor"),
        ("maior sentença (palavras)", a["pontuacao"]["maior_sentenca_palavras"],
         b["pontuacao"]["maior_sentenca_palavras"], "menor"),
        ("disfluências totais", a["disfluencia"]["total_disfluencias"],
         b["disfluencia"]["total_disfluencias"], "menor"),
        ("disfluências/1.000 palavras", a["disfluencia"]["por_1000_palavras"],
         b["disfluencia"]["por_1000_palavras"], "menor"),
        ("repetições de palavra", a["disfluencia"]["repeticoes_palavra"],
         b["disfluencia"]["repeticoes_palavra"], "menor"),
        ("marcadores orais", a["disfluencia"]["total_marcadores"],
         b["disfluencia"]["total_marcadores"], "menor"),
        ("canônicos KB presentes", a["terminologia"]["canonicos_ocorrencias"],
         b["terminologia"]["canonicos_ocorrencias"], "maior"),
        ("corrupções STT presentes", a["terminologia"]["variantes_stt_ocorrencias"],
         b["terminologia"]["variantes_stt_ocorrencias"], "menor"),
        ("corrupções/1.000 palavras", a["terminologia"]["corrupcoes_por_1000_palavras"],
         b["terminologia"]["corrupcoes_por_1000_palavras"], "menor"),
        ("formas proibidas", a["terminologia"]["proibidas_ocorrencias"],
         b["terminologia"]["proibidas_ocorrencias"], "menor"),
        ("taxa de confiança", a["terminologia"]["taxa_fiducia"],
         b["terminologia"]["taxa_fiducia"], "maior"),
    ]
    if a.get("diagnostico") and b.get("diagnostico"):
        da, db = a["diagnostico"], b["diagnostico"]
        for k, rot in (("linhas_ledger", "linhas no livro-razão"),
                       ("propostas", "propostas a adjudicar"),
                       ("ausentes_da_base", "ausentes da base (lista bruta)")):
            if k in da and k in db:
                linhas.append((rot, da[k], db[k], "menor"))
        if "ausentes_classificados" in da and "ausentes_classificados" in db:
            linhas.append(("candidatas REAIS a termo novo",
                           da["ausentes_classificados"]["real"]["formas"],
                           db["ausentes_classificados"]["real"]["formas"], "menor"))
            linhas.append(("ruído na lista de ausentes (n-grama + comum + capital)",
                           sum(da["ausentes_classificados"][k]["formas"]
                               for k in ("n_grama", "comum", "capital")),
                           sum(db["ausentes_classificados"][k]["formas"]
                               for k in ("n_grama", "comum", "capital")), "menor"))
        if "dispersao" in da and "dispersao" in db:
            linhas.append(("dispersão de grafias (formas distintas)",
                           da["dispersao"]["grafias_distintas"],
                           db["dispersao"]["grafias_distintas"], "menor"))
            linhas.append(("dispersão: média de grafias por entidade",
                           da["dispersao"]["media_por_entidade"],
                           db["dispersao"]["media_por_entidade"], "menor"))
        if "ausentes_da_base" in da and "ausentes_da_base" in db:
            # a métrica simétrica do parecer: não depende de a KB já conhecer a corrupção, porque
            # corrupção inédita aparece como "ausente da base" e entra na soma do mesmo jeito
            linhas.append(("CARGA TERMINOLÓGICA TOTAL (livro-razão + ausentes)",
                           da["linhas_ledger"] + da["ausentes_da_base"],
                           db["linhas_ledger"] + db["ausentes_da_base"], "menor"))
    return linhas


def veredito(vb, va, criterio: str) -> str:
    try:
        delta = round(vb - va, 4)
    except TypeError:
        return "—"
    if criterio == "—" or delta == 0:
        return "—"
    return "B" if (delta > 0) == (criterio == "maior") else "A"


def para_markdown(perfis: list[dict], base: dict) -> str:
    """Markdown do perfil. Os números vêm do mesmo cálculo que a saída de terminal — nada é redigido
    à mão aqui, para que o relatório não possa divergir da medição."""
    hoje = datetime.now().strftime("%Y-%m-%d")
    out = [f"# Perfil de motores de STT — medição de {hoje}", "",
           f"Gerado por `ferramentas/rc_perfil_stt.py` (régua: KB-RC com {base['n_termos']} termos, "
           f"{len(base['canonicos'])} superfícies canônicas, {len(base['variantes'])} corrupções "
           f"mapeadas).", ""]
    for p in perfis:
        out += [f"## {p['nome']}", "", "```text", _texto_do_perfil(p).rstrip(), "```", ""]
    if len(perfis) == 2:
        a, b = perfis
        out += [f"## Comparativo — {a['nome']} (A) × {b['nome']} (B)", "",
                "| métrica | A | B | Δ B−A | melhor |", "|---|---:|---:|---:|:---:|"]
        for rot, va, vb, crit in tabela_comparativa(a, b):
            try:
                delta = f"{round(vb - va, 4):g}"
            except TypeError:
                delta = "—"
            out.append(f"| {rot} | {fmt(va)} | {fmt(vb)} | {delta} | {veredito(vb, va, crit)} |")
        pv = eixo_proveniencia(a, b)
        out += ["", "### Proveniência — os dois lados vêm do mesmo reconhecimento de fala?", "",
                "| medida | valor |", "|---|---:|",
                f"| divergência lexical | {pv['divergencia']:.2%} "
                f"({fmt(pv['removidas'])} de A ausentes em B · {fmt(pv['acrescentadas'])} de B "
                f"ausentes em A) |",
                f"| Jaccard de vocabulário | {pv['jaccard_tipos']:.3f} |",
                f"| hapax em comum | {pv['hapax_comuns']:.3f} |",
                f"| marcadores orais com contagem idêntica | {pv['marcadores_iguais']} "
                f"({pv['taxa_marcadores_iguais']:.0%}) |",
                f"| tokens mascarados com asterisco | A {pv['mascarados_a']} · "
                f"B {pv['mascarados_b']} |",
                "", f"**Veredito:** {pv['veredito']}.", ""]
        ka = sum(1 for q in a["integracao"]["quebras"] if q["compativel"])
        kb_ = sum(1 for q in b["integracao"]["quebras"] if q["compativel"])
        tot = len(a["integracao"]["quebras"])
        sa = sum(1 for q in a["integracao"]["quebras"] if q["tipo"] == "superada")
        sb = sum(1 for q in b["integracao"]["quebras"] if q["tipo"] == "superada")
        out += ["", f"Compatibilidade com a esteira: **A {ka}/{tot}** · **B {kb_}/{tot}** "
                f"(premissas superadas: A {sa}, B {sb}).", ""]
        for q in b["integracao"]["quebras"]:
            if q["tipo"] == "codigo":
                out += [f"- **B CUSTA CÓDIGO** `{q['suposicao']}` — {q['detalhe']}"]
            elif q["tipo"] == "superada":
                out += [f"- **B SUPERA A PREMISSA** `{q['suposicao']}` — {q['detalhe']} "
                        f"(trabalho manual que deixa de existir; não é defeito)"]
        if a["diagnostico"] and b["diagnostico"]:
            out += ["", "### Carga do `rc_diagnostico.py` (mesma ferramenta da esteira)", "",
                    "| saída | A | B |", "|---|---:|---:|"]
            for k in ("linhas_ledger", "ausentes_da_base", "sementes_atingidas"):
                if k in a["diagnostico"] and k in b["diagnostico"]:
                    out.append(f"| {k} | {fmt(a['diagnostico'][k])} | {fmt(b['diagnostico'][k])} |")
        out.append("")
    return "\n".join(out) + "\n"


def _texto_do_perfil(p: dict) -> str:
    """Captura a saída de `imprimir(p)` para embutir no markdown — mesma fonte, zero divergência."""
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        imprimir(p)
    return buf.getvalue()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Perfil comparativo de motores de STT.")
    ap.add_argument("arquivos", type=Path, nargs="+", help="um ou dois arquivos de STT")
    ap.add_argument("--kb", type=Path, default=RAIZ / "KB-RC")
    ap.add_argument("--com-diagnostico", action="store_true",
                    help="roda rc_diagnostico.py em cada arquivo (lento, mas é a medida real de carga)")
    ap.add_argument("--json", type=Path, default=None, help="grava o perfil completo em JSON")
    ap.add_argument("--md", type=Path, default=None,
                    help="grava o perfil em markdown (tabela comparativa + perfis por arquivo)")
    args = ap.parse_args(argv)

    for a in args.arquivos:
        if not a.exists():
            raise SystemExit(f"[recusado] arquivo inexistente: {a}")
    base = superficies_kb(args.kb)
    print(f"[régua] KB-RC: {base['n_termos']} termos · {len(base['canonicos'])} superfícies "
          f"canônicas · {len(base['variantes'])} corrupções mapeadas (variante_stt + sementes) · "
          f"{len(base['proibidas'])} proibidas na Quarentena · {len(base['externos'])} formas "
          f"Externos · {len(base['externos_canonicos'])} canônicos Externos")
    perfis = []
    for a in args.arquivos:
        regua = regua_para(base, a, args.kb)
        if regua.get("pasta_ledger"):
            print(f"[régua] livro-razão de {regua['pasta_ledger']}: "
                  f"{len(regua['proibidas'])} formas proibidas no total")
        if regua.get("aviso_ledger"):
            print(f"[régua] AVISO: {regua['aviso_ledger']}")
        p = perfil(a, args.kb, regua, args.com_diagnostico)
        p["regua"] = {"proibidas": len(regua["proibidas"]),
                      "pasta_ledger": regua.get("pasta_ledger", ""),
                      "aviso_ledger": regua.get("aviso_ledger", "")}
        imprimir(p)
        perfis.append(p)
    if len(perfis) == 2:
        comparar(perfis[0], perfis[1])
    if args.json:
        # a assinatura (multiconjunto de ~3 mil tipos) é meio de cálculo, não resultado: sai do JSON
        enxutos = [{k: v for k, v in p.items() if k not in ("assinatura", "texto_bruto")}
                   for p in perfis]
        args.json.write_text(json.dumps(enxutos, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\n[ok] perfil gravado em {args.json}")
    if args.md:
        args.md.parent.mkdir(parents=True, exist_ok=True)
        args.md.write_text(para_markdown(perfis, base), encoding="utf-8")
        print(f"[ok] relatório markdown gravado em {args.md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
