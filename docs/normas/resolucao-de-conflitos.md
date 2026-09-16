# Resolução dos Conflitos da Base Terminológica

**Documento:** Anexo I do Guia de Revisão e Governança Terminológica — v2
**Elaborado por:** Agente 86 (revisor terminológico)
**Data:** 16 de setembro de 2026
**Status:** submetido à aprovação do Comandante — nenhuma revisão de transcrição começa antes deste despacho
**Fontes de evidência:** `KB-RC/canonico.json` (946 termos, formato canonico-1.1), `KB-RC/biblio.json` (104 obras), `KB-RC/termos/*.md` (820 fichas), `base-terminologica.xlsx` (fonte legada), `Guia - SISTEMA DE REVISÃO E GOVERNANÇA TERMINOLÓGICA.docx` (Guia v1), transcrição *Revelações Cósmicas Urgente – Jan Val Ellam*

---

## 1. Sumário executivo

Os oito conflitos apontados na auditoria estão **todos resolvidos com evidência documental**. Em cinco deles a KB-RC decide sozinha; em dois a KB-RC e o Guia v1 divergem e a KB-RC prevalece; em um (Jeane Miranda) não há conflito de grafia, há **lacuna de registro**.

| # | Conflito | Decisão | Autoridade da decisão | Efeito imediato no pipeline |
|---|---|---|---|---|
| 1 | Asphezian × Asfezion | **Asphezian** | RC-025 + planilha (aba Índice Mestre); "Asfezion" tem **zero** ocorrências na KB | Guia v1 §5.3 corrigido; semente `Asfezion` removida |
| 2 | RC-092 × RC-252 (Quarto Logos × Olm) | **RC-092 = Quarto Logos; RC-252 = Olm** | `canonico.json` + B016 "O Quarto Logos" | Guia v1 §5.1 tinha os códigos **invertidos**; a forma "Olm" passa a ser suspensa por homografia |
| 3 | Brahma × Brama | **Brahma** | RC-037 "Brahma (Brajna)" + Quarentena Terminológica (`NUNCA "Brama"`) | 8 ocorrências nesta transcrição; Guia v1 **não tinha regra** para o erro mais frequente do texto |
| 4 | Jeane Miranda | **Grafia confirmada; falta ficha** | 10 fichas a mencionam; nenhuma a registra | Criar ficha na categoria 1.6 (Figuras humanas) |
| 5 | Len Mion × Lemion | **Len Mion** (canônico); Lemion/Lemon/Lemior/Nemon = grafias STT | RC-074, linha 87 da ficha: "'Lemion/Lemon/Lemior' é grafia STT de Len Mion (Satã, RC-074)" | Guia v1 já decidia certo; a lista de variantes foi ampliada de 2 para 5 formas |
| 6 | radiato × radiata | **radiata / radiatas** (feminino) | RC-631 "Cérebro Radiata", RC-093 "Radiatas", RC-834 "mente radiata" | "radiato" vira variante STT; 15 ocorrências de "radiato" na KB são citações ou títulos curatoriais a sanear |
| 7 | elogismo → ilogismo | **Regra descartada** | "ilogismo" não existe na KB nem no texto (a única ocorrência encontrada é *silogismo*, em RC-009) | Guia v1 §5.4 perde esta linha; sem efeito prático nesta transcrição (0 ocorrências) |
| 8 | Duplicatas na base | **4 remissões confirmadas; 3 pares são complementares, não duplicados** | fichas marcadas `REMISSIVA` (RC-449, RC-769, RC-872, RC-936) | `canonico.json` precisa expor o campo de remissão (hoje só 3 menções a "remiss" em 946 termos) |

**Placar:** 6 decisões a favor da KB-RC, 1 contra o Guia v1 (conflito 1), 1 regra do Guia v1 descartada (conflito 7). Nenhum conflito exigiu decisão por intuição fonética.

---

## 2. Critério de evidência usado

Hierarquia aplicada em todos os oito casos, do mais forte para o mais fraco:

1. **Quarentena Terminológica** da ficha — seção presente em RC-826 a RC-833, com regras do tipo `NUNCA "Brama"`, `NUNCA "Sofia"`, `NUNCA "Luzbel" sozinho`, `NUNCA "Aia/Aie"`. É a norma explícita do curador.
2. **Nome do termo em `canonico.json`** — verdade-mestra gerada do registro-mestre; é o que as ferramentas consultam.
3. **Seção "Etimologia e Grafias"** da ficha (406 fichas a possuem; 338 trazem grafia preferida) e o campo de variações de STT.
4. **Prosa da ficha com data e fonte** (ex.: `[P2020-04-25 · …]`, `(U0084)`) — evidência datada vence evidência não datada.
5. **`biblio.json`** — títulos de obras fixam grafias (ex.: B016 "O Quarto Logos").
6. **Planilha `base-terminologica.xlsx`** — fonte legada, usada apenas para conferência.
7. **Guia v1** — menor peso: é derivado, não primário.

Dois princípios complementares:

- **Quando a KB se contradiz**, vence a regra mais específica e mais recente (campo `atualizado` da ficha). Quando não há evidência, a forma fica `[A CONFIRMAR]` e **não se substitui nada**.
- **Citação literal preserva a forma STT.** A KB contém "Brama", "Sofia" e "Lemion" dentro de aspas porque reproduz a fala bruta. A Quarentena rege o **texto editorial**, não as citações. Sem este princípio, o conflito 3 e o conflito 5 pareceriam insolúveis.

---

## 3. Conflito a conflito

### 3.1 Conflito 1 — Asphezian × Asfezion

**O que o Guia v1 diz (§5.3):** "Termos como biodemo/biodemos, radiato/radiata, Wyrd e **Asfezion** (designação de nave/complexo operacional, evitando variações como 'Asfésian' ou 'Fessien') devem ser inseridos rigorosamente em sua forma canônica."

**O que a KB diz:** `canonico.json` RC-025 = **Asphezian**, categoria "Tecnologias & Artefatos", subcategoria "5.1 Naves / Tecnologia extraterrestre", status 🟠 em análise, confiança **baixa**, via P7, fontes B031 e P2018-12-15. A planilha legada traz o mesmo nome. Contagem na KB: **Asphezian 28 ocorrências; Asfezion 0 ocorrências**.

**Decisão:** canônico = **Asphezian** (RC-025). O Guia v1 inverteu a relação: tratou como canônica uma forma que não existe em nenhum registro, e listou como "variação a evitar" justamente a forma canônica ("Asfésian" ≈ Asphezian).

**Aplicação:** semente `Asfezion` retirada do dicionário de correções; `Asphezian` entra como forma canônica. Por ser termo de **confiança baixa e status "em análise"**, toda ocorrência revisada recebe `[A CONFIRMAR]` na primeira aparição do bloco.

**Pendência:** a confiança baixa vem de uma única via (P7). Recomenda-se reexame quando nova palestra mencionar a nave.

### 3.2 Conflito 2 — RC-092 × RC-252 (Quarto Logos × Olm)

**O que o Guia v1 diz (§5.1):** "Ohm / Olm → Ohm (Zion) / Olm (Logos) | Verificar distinção na planilha: **RC-092 (Codificador) vs RC-252 (Quarto Logos)**."

**O que a KB diz:**
- RC-092 = **Quarto Logos (Olm / Codificador de Zian)** — verificado, confiança alta.
- RC-252 = **Olm (Codificador de Zion/Zian)** — verificado, confiança alta.
- B016 = **O Quarto Logos** (obra primária, 217 págs., 1ª ed. 2017, Natal-RN) — trabalhada.

**Decisão:** os códigos do Guia v1 estão **invertidos**. Vale o `canonico.json`: RC-092 é *Quarto Logos*, RC-252 é *Olm*. A glossa "Olm (Logos)" do Guia também está errada — Olm é o **Codificador**, e "Quarto Logos" é o termo cuja glossa contém Olm.

**Aplicação:** a forma "Olm" é agora **suspensa automaticamente** pelo motor (seção 3.1 do diagnóstico: homografia entre RC-092 e RC-252) e só é resolvida por contexto. "Ohm" permanece como variante STT a verificar caso a caso.

**Pendências:** (a) RC-092 grafa "**Zian**" e RC-252 grafa "**Zion/Zian**" — uniformizar; (b) registrar explicitamente a relação RC-092 ↔ RC-252 (hoje só há `relaciona-se-a` genérico).

### 3.3 Conflito 3 — Brahma × Brama

**O que o Guia v1 diz:** nada. "Brama" e "Brahma" têm **zero ocorrências** no Guia v1 — o erro terminológico mais frequente desta transcrição (8 ocorrências) não tinha regra.

**O que a KB diz:**
- RC-037 = **Brahma (Brajna)** — verificado, confiança alta, 10+ fontes.
- Quarentena Terminológica (fichas RC-826 a RC-833): `NUNCA "Brama"`. A varredura de 31/08/2026 corrigiu **158 ocorrências** na própria KB.
- RC-836/RC-837 confirmam as grafias canônicas Awayen, **Brahma**, Javé, Vishnu, Shiva, Projeto Talm, Val Tam.
- **Resíduo:** RC-781 ainda se chama "Pactos de Javé (**Brama** / Vishnu / Shiva)" — viola a Quarentena no próprio nome.

**Decisão:** canônico = **Brahma**; "Brama" é corruptela proibida.

**Aplicação:** as 8 ocorrências de "Brama" e as 2 de "para Brama" desta transcrição entram na fila de correção como regra de classe `nunca` (confiança de mapeamento alta). Ver §3.8 sobre a dupla candidatura de "para Brama".

**Pendência:** corrigir o nome de RC-781 para "Pactos de Javé (Brahma / Vishnu / Shiva)".

### 3.4 Conflito 4 — Jeane Miranda

**O que o Guia v1 diz (§5.1):** "Jane Miranda, Jeanne Miranda → **Jeane Miranda** | Grafia nominal canônica confirmada."

**O que a KB diz:** Jeane Miranda é mencionada em **10 fichas** (psicógrafa associada a "Os Livros de Yel Luzbel"; uma ficha a compara ao "Processador Val", RC-089; outra fala em "versão paralela"). **Não existe ficha própria** para ela — nem em `KB-RC/termos/`, nem em `canonico.json`.

**Decisão:** não há conflito de grafia (o Guia v1 está certo). Há **lacuna de registro**: uma pessoa real, citada em dez fichas, sem verbete.

**Aplicação:** a grafia "Jeane Miranda" é mantida e protegida; as formas "Jane Miranda" e "Jeanne Miranda" continuam na camada de sementes.

**Ação proposta:** criar ficha na categoria **1.6 (Figuras humanas)** com status inicial "identificada", fontes = as 10 fichas que a citam, e relação `proferida-por`/`recebido-por` com os livros de Yel Luzbel.

### 3.5 Conflito 5 — Len Mion × Lemion

**O que o Guia v1 diz (§5.1):** "Lémion, Demion → **Len Mion** | Duas palavras individualizadas, sem acentuação gráfica."

**O que a KB diz:**
- RC-074 = **Len Mion (Satã)** — verificado, confiança alta.
- A própria ficha RC-074 usa as duas grafias: **"Len Mion" 35 vezes, "Lemion" 24 vezes** — quase sempre dentro de citações literais da fala.
- Linha 87 da ficha resolve a questão de forma explícita: *"**[Lemion = Len Mion (Satã)] (U0084)** «E Lemon fixou os olhos em um dos milhões que estavam vivendo aqui.» — **'Lemion/Lemon/Lemior' é grafia STT de Len Mion (Satã, RC-074)**"*.
- Linha 93 acrescenta mais uma forma: *"o palestrante avalia Len Mion (STT **'Nemon'**) como 'alguém muito pior do que Javé'"*.
- RC-850 ("Alexandre Magno (tirano sob influência de **Lemion**)") e RC-851 ("Qin Shi Huang Di (imperador chinês sob influência de **Lemion**)") trazem a corruptela **no próprio nome e no nome do arquivo**.

**Decisão:** canônico = **Len Mion**. Variantes STT documentadas = **Lemion, Lemon, Lemior, Nemon, Lémion, Demion** (as duas últimas herdadas do Guia v1).

**Aplicação:** a lista de sementes passa de 2 para 6 formas. Citações literais entre aspas **não** são alteradas.

**Pendências:** (a) RC-850 e RC-851 deveriam renomear o campo `nome` para "…sob influência de Len Mion" e manter "Lemion" como variante; (b) a ficha RC-074 carrega nota de revisão pendente (`CHANCELA 2026-09-06 · F042-VARREDURA: ISOLAMENTO`) que o curador deve fechar.

### 3.6 Conflito 6 — radiato × radiata × radiatas

**O que o Guia v1 diz (§5.3):** lista "radiato/radiata" como par a resolver pela coluna `etimologia_grafias`, sem decidir.

**O que a KB diz:**
- RC-631 = **Cérebro Radiata** (verificado, confiança média).
- RC-093 = **Radiatas** (categoria 1.7 Híbridos / Seres de transição; em análise, confiança baixa).
- RC-834: "Sofia: criada do genoma de Virgno, **mente radiata**, anjos incorruptíveis".
- Contagem bruta na KB: *radiata* 84, *radiatas* 27, *radiato* 15 — mas as 15 de "radiato" estão em **citações literais** (RC-009, RC-565) e em **títulos curatoriais de citação** (RC-631 linha 75: "[O radiato superado pelos bilatérios]" citando «cérebro **radiata** de Sofia»), além de RC-771 (campo Quarentena de cautela editorial).

**Decisão:** canônico = **radiata / radiatas** (feminino, concordando com "mente radiata", "cérebro radiata"). "radiato" é forma STT/curational a sanear.

**Aplicação:** "radiato" entra como variante STT de RC-631/RC-093. Nesta transcrição não há ocorrência de nenhuma das formas — decisão preventiva.

**Pendência:** revisar os títulos curatoriais que grafam "radiato" (RC-631 l.75, RC-009 l.424, RC-565 l.48) sem tocar nas citações entre aspas.

### 3.7 Conflito 7 — elogismo → ilogismo

**O que o Guia v1 diz (§5.4, tabela de erros brutos):** "elogismo → **ilogismo** | Correção conceitual de vício de raciocínio."

**O que a KB diz:** nada. "ilogismo" **não existe** como termo, variante ou grafia em `canonico.json`, `biblio.json` ou nas 820 fichas. A única correspondência textual encontrada é a palavra **silogismo** ("não há silogismo possível"), em RC-009. "elogismo" também não existe.

**Decisão:** **descartar a regra.** "Ilogismo" não é palavra portuguesa dicionarizada nem termo da Revelação Cósmica; a regra produzia uma correção que transformaria texto comum em neologismo inexistente.

**Aplicação:** linha removida do dicionário de sementes. Se a forma aparecer em alguma transcrição futura, o procedimento é marcar `[A CONFIRMAR]` e ouvir o áudio — não substituir.

**Efeito nesta transcrição:** nenhum (0 ocorrências das duas formas).

### 3.8 Conflito 8 — Duplicatas e remissões

Levantamento completo feito ficha a ficha:

| Canônico | Duplicata/remissão | Situação real | Providência |
|---|---|---|---|
| RC-898 Choque de Realidade (verificado, média) | RC-936 "Choque de realidade" (provisório) | **REMISSIVA** declarada na ficha | manter RC-898; RC-936 é histórico |
| RC-898 | RC-867 "Choque de Realidade (o perpétuo espanto dos donos da verdade)" (candidato, baixa) | verbete paralelo **sem ficha** | fundir em RC-898 ou criar remissão |
| RC-164 Criaturas-ferramenta | RC-449 (mesmo nome, verificado, alta) | **REMISSIVA** — "duplicata absorvida por RC-164 [F045-MERGE 07-09-2026]" | nada a fazer além de expor no JSON |
| RC-115 Val Aten | RC-502 | remissão | idem |
| RC-149 Mônada | RC-937 | remissão | idem |
| RC-581 Rakshasas | RC-872 | **REMISSIVA** | idem |
| RC-043 Conselho dos Cinco | RC-501 | remissão | idem |
| RC-314 Fenômenos Denunciadores do Fim | RC-203 | remissão | idem |
| — | RC-769 Corpos Fenva | **REMISSIVA** | registrar alvo no JSON |
| RC-305 Têmis × RC-815 "Temis (Têmis) como Mãe-de-Pandora (Co-clonadora)" | **não é duplicata** | RC-815 é um aspecto/tese distinta | manter ambos; uniformizar "Temis" → "Têmis" no nome de RC-815 |
| RC-063 × RC-332 | **não é duplicata** | verbetes complementares | manter |

**Decisão:** apenas **4 fichas** são formalmente remissivas (RC-449, RC-769, RC-872, RC-936). Os demais casos são remissões implícitas na prosa. Dois pares que pareciam duplicados (RC-305/RC-815 e RC-063/RC-332) **não são**.

**Problema estrutural:** `canonico.json` traz apenas 3 menções a remissão em 946 termos, e RC-449 aparece no JSON com o **mesmo nome e o mesmo status** do canônico RC-164. Qualquer ferramenta que leia só o JSON trata duplicata absorvida como termo vivo.

**Ação proposta:** acrescentar ao formato canonico o campo `remissiva_para` (código) e `status: "remissão"`, e regerar o JSON. Enquanto isso não ocorre, o pipeline usa as fichas (que declaram `REMISSIVA`) e não o JSON para decidir duplicatas.

---

## 4. Achados adicionais (não constavam dos oito conflitos)

Descobertos durante a verificação de evidência. Todos afetam o pipeline.

### 4.1 RC-781 viola a Quarentena e tem referências cruzadas erradas
Nome atual: "Pactos de Javé (**Brama** / Vishnu / Shiva)". Além da grafia proibida, a ficha afirma que Vishnu/Krishna = RC-102 e Shiva = RC-148; na verdade **RC-102 = Shiva** e **RC-148 = Agentes da Vida Universal**. Corrigir nome e cross-refs.

### 4.2 RC-142 (Yel Luzbel) está incompleta
Termo verificado, confiança alta, central para a Quarentena (`NUNCA "Luzbel" sozinho`, `NUNCA "Yosbel"`), mas a ficha **não tem Definição Sintética nem Etimologia e Grafias**. É a ficha que mais precisa de complementação.

### 4.3 `biblio.json` tem 97 códigos B, não 102
Contagem real: 104 registros = **97 B-codes (B001–B098, falta B095)**, 3 ART (curadoria), 1 PER (Revista Plus Ultra), 1 EXT (Nuctemeron, fonte externa), 2 P (palestras). O Guia v1 fala em "102 obras B001-B102". Corrigir o texto do Guia e investigar B095.

### 4.4 "Valores Supremos da Consciência" não está na KB
Na transcrição: *"eu tenho um programa no YouTube chamado Valores Supremos da Consciência"*. Não é livro: é **programa/série do autor no YouTube**, ausente de `biblio.json` e de `canonico.json`. Proposta: novo registro bibliográfico (tipo PER/programa).

### 4.5 "Sherminetro" não é *Terminator*
Hipótese inicial descartada pelo contexto: *"vamos aproveitar aqui meu querido Sherminetro para falar das mandalas arcturianas"*. É **apelido com que Jan se dirige ao apresentador**. Registrado em `ferramentas/externos.csv` como `[A CONFIRMAR]` — nenhuma alteração sem confirmação do produtor.

### 4.6 "Nick" (Nyx, RC-621) colide com Nick Bostrom
A KB documenta "Nick" como variante STT de **Nyx**. Nesta transcrição, "Nick" é **Nick Bostrom** (*"Nick Bostron no seu livro chamado Utopia Profunda"*). O motor agora **suspende** a semente automaticamente (diagnóstico §3.1). Regra geral incorporada ao Guia v2: entidade da camada Externos nunca vira variante de termo interno.

### 4.7 "a vista" colide com Avesta (RC-595)
A KB documenta `Avesta. STT: AESTA, a vesta`. No texto: *"se você pagar a vista você vai ter…"* — português comum. A forma foi para o vocabulário de guarda. Regra geral: variante STT documentada que coincide com expressão comum do português só se aplica com confirmação contextual.

### 4.8 "para Brama" tem dupla candidatura
O motor casou "para Brama" com a superfície `para bragna` (RC-691, Ishvara), porque a ficha RC-691 cita *«Desde que para Bragna fez isso»* = grafia STT de **Para Brajna**. No contexto real — *"Krishna tomou toda a devoção que existia na Índia para Brama"* — a leitura correta é **Brahma** (RC-037), dativo. Decisão: **Brahma**; o caso virou exemplo didático no Guia v2 (o motor propõe, o revisor decide).

### 4.9 "Virgin" é Vishnu, não Virgno
No trecho *"esses seres Brama Virgin Chiva"* a tríade é **Brahma, Vishnu, Shiva** (exatamente a glossa de RC-781). O motor propôs RC-104; a leitura correta vem da tríade. Registrado como caso de estudo.

### 4.10 O campo "Variações" mistura duas coisas diferentes
Das 1.590 relações variante→canônico extraídas da prosa das fichas, **778 são equivalências conceituais** (ex.: Javé como variação de Criador) e não erros de grafia. Substituir automaticamente por essa classe destruiria o texto. O extrator passou a classificar cada par (`nunca`, `stt`, `stt_contextual`, `deprecada`, `corruptela`, `oral`, `variacao`) e a marcar a confiança do mapeamento: **299 pares** são regra de substituição; **613** são referência oral (reconhecimento, não troca); **507** são conceituais (nunca trocar).

### 4.11 126 termos não têm ficha
`canonico.json` lista 946 termos; existem 820 fichas. Os 126 restantes não têm "Etimologia e Grafias" nem variantes documentadas — para eles o revisor só pode aplicar o nome canônico.

---

## 5. Registro formal de decisão

Tabela a ser incorporada ao Guia v2 (§4.3) e às sementes do motor.

| Forma proibida / variante | Forma canônica | Código | Classe | Ação do revisor |
|---|---|---|---|---|
| Asfezion, Asfésian, Fessien | Asphezian | RC-025 | grafia errada (Guia v1) | substituir; `[A CONFIRMAR]` na 1ª ocorrência (confiança baixa) |
| Brama | Brahma | RC-037 | `nunca` (Quarentena) | substituir sempre, exceto em citação literal |
| Lemion, Lemon, Lemior, Nemon, Lémion, Demion | Len Mion | RC-074 | variante STT | substituir no texto editorial |
| radiato | radiata / radiatas | RC-631, RC-093 | variante STT | substituir no texto editorial |
| Jane Miranda, Jeanne Miranda | Jeane Miranda | (criar ficha 1.6) | nome próprio | substituir |
| elogismo | — | — | **regra descartada** | não substituir; `[A CONFIRMAR]` + ouvir áudio |
| Olm / Ohm | decidir por contexto: Olm (RC-252) ou Quarto Logos (RC-092) | RC-252 / RC-092 | homografia | **suspenso** — nunca trocar às cegas |
| Sofia | Sophia | RC-009 | `nunca` (Quarentena) | substituir |
| Luzbel (sozinho), Yosbel | Yel Luzbel | RC-142 | `nunca` (Quarentena) | substituir |
| Aia, Aie | Aya, Aye | RC-031 | `nunca` (Quarentena) | substituir |
| Yahé, Xavé, Jabé, Javert, Javer | Javé | RC-001 | variante STT | substituir |
| Chiva, Chiva/Shiva variantes | Shiva | RC-102 | variante STT | substituir |
| Virgin (na tríade Brama/Virgin/Chiva) | Vishnu | RC-104/RC-781 | variante STT | substituir por contexto da tríade |
| Nick (quando = Nick Bostrom) | Nick Bostrom | EXTERNO | camada Externos | **protegido** — nunca trocar por Nyx |
| a vista (pagar à vista) | — | RC-595 (falso positivo) | guarda | não substituir |
| Cristo (como figura cristã) | Cristo | RC-414 (falso positivo) | homografia/guarda | **suspenso** — só Krishna se o contexto for o avatar hindu |

---

## 6. Ações residuais propostas

| # | Ação | Onde | Prioridade | Dependência |
|---|---|---|---|---|
| 1 | Corrigir nome de RC-781 para "Pactos de Javé (Brahma / Vishnu / Shiva)" e refazer as cross-refs (Vishnu/Krishna ≠ RC-102; Shiva ≠ RC-148) | `KB-RC/termos/RC-781*.md` | alta | curador |
| 2 | Completar RC-142 (Yel Luzbel) com Definição Sintética e Etimologia e Grafias | `KB-RC/termos/RC-142*.md` | alta | curador |
| 3 | Criar ficha de Jeane Miranda (categoria 1.6, status "identificada") | `KB-RC/termos/` | alta | curador |
| 4 | Expor `remissiva_para` e `status: "remissão"` no formato canonico e regerar `canonico.json` | `ferramentas/dados_termos.py` + JSON | alta | curador/ferramentas |
| 5 | Uniformizar "Len Mion" nos nomes de RC-850/RC-851 (manter "Lemion" como variante) | fichas + nomes de arquivo | média | curador |
| 6 | Uniformizar Zian/Zion entre RC-092 e RC-252; uniformizar "Têmis" no nome de RC-815 | fichas | média | curador |
| 7 | Registrar "Valores Supremos da Consciência" (programa de YouTube do autor) em `biblio.json` | `KB-RC/biblio.json` | média | curador |
| 8 | Saneamento de "radiato" em títulos curatoriais (RC-631 l.75, RC-009 l.424, RC-565 l.48) sem tocar citações | fichas | baixa | curador |
| 9 | Investigar B095 (código ausente) e corrigir a contagem de obras no Guia | `KB-RC/biblio.json` | baixa | curador |
| 10 | Confirmar com o produtor: grafia de "Sherminetro", "Tati Quântica", "Sherminetro/Sherminator", canal "Paranormal Experience" | `ferramentas/externos.csv` | média | produtor |

Nenhuma destas ações bloqueia a revisão da transcrição: as decisões do §5 já são suficientes para operar.

---

## 7. Reprodução

```bash
# 1. extrair as relações variante -> canônico da prosa das 820 fichas
python ferramentas/rc_variantes.py --kb KB-RC \
    --transcricao "Revelações Cósmicas Urgente – Jan Val Ellam.txt"
#    -> ferramentas/variantes-kb-extraidas.csv (1.590 pares; 299 regras de substituição)

# 2. diagnóstico com a KB-RC como fonte de verdade (a planilha é ignorada)
python ferramentas/rc_diagnostico.py "Revelações Cósmicas Urgente – Jan Val Ellam.txt" \
    --kb KB-RC --saida analise/revelacoes-cosmicas-urgente-jan-val-ellam-kb
#    -> diagnostico.md / .json, variantes-propostas.csv, ausentes-da-base.csv, dossie-bloco.txt
```

**Números do diagnóstico de referência (16/09/2026):** 18.781 palavras · 96 superfícies da base presentes · 783 candidatos brutos · 61 adjudicáveis (31 na fila de substituição) · 145 entidades ausentes da base · 90 termos relevantes para o dossiê de trabalho (≈1.153 tokens) · 372 sementes carregadas, 32 atingidas, **11 suspensas** por homografia, guarda ou colisão com Externos.

**Efeito mensurável da troca de fonte de verdade (planilha → KB-RC):** superfícies detectadas 67 → 96; variantes/truncamentos na fila 38 → 55 (antes do endurecimento das guardas); entidades "ausentes da base" 169 → 145. A KB-RC reconhece mais e erra menos.

**Calibração do corte de similaridade** (medida nesta transcrição, 10 variantes-chave como referência):

| `--corte-duplo` | propostas na fila | variantes-chave preservadas | leitura |
|---|---|---|---|
| 0,75 (padrão) | 32 | 10/10 | recall máximo; exige adjudicação |
| 0,80 | 27 | 9/10 (perde Xavé→Javé, coberto pela camada de sementes) | melhor equilíbrio |
| 0,85 | 11 | 4/10 | perda inaceitável de recall |
| 0,90 | 4 | 2/10 | inutiliza a varredura |

Conclusão: **o corte não é o instrumento de precisão — a adjudicação contextual é**. Precisão medida da fila automática nesta transcrição: ≈40% (13 correções claras em 32 propostas); precisão da camada de sementes/Quarentena: ≈100% (após as 11 suspensões). Por isso o Guia v2 mantém o corte frouxo e torna obrigatória a decisão humana por contexto.
