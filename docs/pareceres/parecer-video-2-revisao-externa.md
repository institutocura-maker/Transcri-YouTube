# Parecer de recepção — vídeo 2: revisão externa "higienizada"

**Projeto:** Transcri-YouTube · **Data:** 16 de setembro de 2026 · **Elaborado por:** Agente 86 (Arena.ai Agent Mode)

**Objeto:** receber e auditar `upload/alienigenas-ou-seres-de-outro-universo.docx` — a revisão que o
Comandante fez do 2º vídeo, produzida fora da esteira da casa, no contexto do teste de "uma outra
ferramenta de transcrição que forneça conteúdo mais higienizado".

**Status: COMPLETO no que depende da casa; BLOQUEADO na camada 1.** A auditoria terminológica contra
a KB-RC está feita e é conclusiva. A auditoria de **proveniência** (o que a ferramenta mudou em
relação ao que foi dito) está feita contra uma **captura de referência**, não contra um bruto
oficial — e essa diferença está declarada em cada achado. Saída bruta do instrumento:
`docs/pareceres/video-2-medicao.md` e `docs/pareceres/video-2-perfil.json`.

---

## 0. Sumário executivo

**1. Nada foi censurado.** Zero asteriscos nos dois lados. Todas as palavras que uma camada
"higienizadora" costuma remover estão inteiras na revisão: *diabos* (2×2), *esculhambado* (2×2),
*cretinizou-nos*, *imbecilizou-nos*, *coelhos*, *fofoca*, *bom senso*, *mídia*. É o oposto exato do
que o NotebookLM fez no vídeo 1 (`merda`×3 → `m****`, `bandido`×2 → `b******`). **Neste eixo, a
ferramenta nova passa.**

**2. A divergência de 9,23% não é perda — é correção.** Decomposta palavra a palavra (§4), ela é:
anotações de áudio do YouTube removidas (`[roncando]`×4, `[limpando a garganta]`×5), correções
ortográficas e terminológicas (*julgo*→*jugo*, *mitlogo*→*mitólogo*, *chamanismo*→*xamanismo*,
*novo cósmico*→*ovo cósmico*, *acásicos/acáxicos*→*Akáshicos*, *locas/louoca*→*lokas*,
*qualia*→*colmeia*) e resolução de dêiticos ("isso aqui" → "o lado antimaterial / Brahmaloka").
A revisão é **curadoria doutrinária de qualidade**, não higienização.

**3. O teto de 5% do portão G9 é da camada 2, e aplicá-lo a este arquivo é erro de categoria.**
Um derivado de máquina não tem motivo para mudar palavra; uma revisão humana tem o dever de mudar.
Se este arquivo entrasse como derivado, o G9 o reprovaria — e estaria errado (§5). **Proposta:
teto por natureza da camada**, e auditoria de *rastreabilidade* (não de divergência) para revisão
de terceiro.

**4. Achado que muda a premissa do vídeo 1: o ASR do YouTube agora entrega texto PONTUADO.**
A captura deste vídeo tem **13,66 sinais por 100 palavras** (144 vírgulas, 99 pontos); o bruto do
vídeo 1 tinha **0,22** (1 vírgula, 15 pontos). Se confirmado no painel, o principal benefício da
camada NotebookLM (pontuar e segmentar) encolhe drasticamente — e o risco dela (censurar) permanece
(§3). Isso reabre a decisão do parecer anterior com dados novos.

**5. Duas regressões na revisão, ambas com canônico na KB** — e ambas com a mesma causa provável: o
corretor ortográfico do editor de texto. *glues* → a KB diz **gluons** (RC-034). *pósetron* → a KB
diz **pósitron** (RC-161, RC-636). É o equivalente doméstico da censura do LLM: uma camada
automática entre o autor e o texto, trocando palavra sem avisar (§6).

**6. Falta a camada 1.** Não há bruto oficial deste vídeo, e o sandbox não alcança o YouTube
(TLS bloqueado; só o fetch de página passa). Sem bruto: G1 não tem o que hashar, G9 não tem contra
que cruzar, e `rc_curadoria.py` não pode aplicar nenhuma variante na KB — a regra da casa é
"**variante sem ocorrência no bruto não entra**". Toda a fila do §7 fica bloqueada por isso (§2).

---

## 1. O que chegou, e o que a plataforma diz

| campo | valor | fonte |
|---|---|---|
| arquivo | `upload/alienigenas-ou-seres-de-outro-universo.docx` | commit `0ea4388` (upload web do Comandante) |
| sha256 | `d188b7eed166f6005c9c00b011099b1742ac08134424e3154d848c41335784a2` | medido |
| tamanho | 20.138 bytes · 58 parágrafos (28 reais) · 0 tabelas | medido |
| corpo | **1.817 palavras** em 25 parágrafos · 206 vírgulas · 81 pontos · 6 interrogações | medido, cabeçalho separado |
| corpo extraído (versionado) | `docs/pareceres/video-2-revisao-corpo.txt` · sha256 `9fd50e32a8fa077b0ff048263f24e0ea5e3b61eec9896f7fd5805619c21e8c2c` | extraído do `.docx`, sem as 3 linhas de cabeçalho |
| título no arquivo | "Alienígenas ou seres de outro universo?" | cabeçalho do .docx |
| **título no YouTube** | **"Alienígenas e humanos: Eles já estão entre nós?"** | página do vídeo, conferida em 16/09/2026 |
| canal | Jan Val Ellam (`@JanValEllam`) — **não** é o Paranormal Experience | idem |
| URL | `https://www.youtube.com/watch?v=v0gJWn50gg8` | cabeçalho do .docx + página |
| publicado | 2026-09-12 · categoria People & Blogs · 76.950 views · 2.699 likes | página |
| duração | **19:24** | página |
| nota do autor do arquivo | "Trata-se de um trecho da Palestra — A Dramática Fusão dos Universos de Hyren e Hyron" | cabeçalho do .docx |

**Dois fatos de registro:**

* **O título diverge.** O .docx chama de "Alienígenas ou seres de outro universo?"; o vídeo chama-se
  "Alienígenas e humanos: Eles já estão entre nós?". Como o slug vira o nome da pasta e vai para o
  catálogo e para o `biblio.json` (padrão Y, Guia §2.5), **a escolha é do Comandante** — a casa
  registra o título oficial do vídeo e pode manter o título de trabalho como `chamada`.
* **O "trecho" é o vídeo inteiro.** A revisão cobre do primeiro ao último enunciado do vídeo
  ("A terra inteira está sendo visitada…" → "…porque isso já está acontecendo."). O que é trecho é o
  **vídeo** em relação à palestra maior — fato bibliográfico relevante: o vídeo é um corte de
  *A Dramática Fusão dos Universos de Hyren e Hyron*, que a KB conhece pelo tema
  (**B085** *Hyren-Hyron: Universos em Colisão*, 2021, Freitas e Kummer; RC-106 lista
  "Hyren (Druidística)").

---

## 2. A camada 1 está faltando — e o que fiz a respeito

A arquitetura aprovada ontem tem três camadas: **fonte** (bruto imutável, sha256, G1),
**trabalho** (derivado, G9) e **saída** (blocos e produto, G2/G3/G5/G6). O arquivo recebido é
**saída produzida fora da casa**: texto revisado, sem o bruto embaixo. Consequências concretas, não
teóricas:

| o que fica impossível | por quê |
|---|---|
| G1 (bruto intacto) | não há arquivo para hashar — e nada impede que a "higienização" tenha comido palavra |
| G9 (divergência × teto, máscaras) | não há fonte contra que cruzar; o portão responde FALHA por desenho |
| `rc_curadoria.py` aplicar variantes na KB | a regra da casa exige **atestação no bruto**; sem ele, nenhuma variante entra |
| auditar a ferramenta nova | não se distingue o que o motor errou do que o revisor consertou |

**O sandbox não baixa o bruto.** Egresso é restrito: `pypi.org` e `github.com` respondem 200;
`youtube.com`, `video.google.com` e proxies de leitura fecham a conexão TLS. `yt-dlp` instalado e
testado: `SSLError('TLS/SSL connection has been closed (EOF)')` nas três tentativas. A única porta
é o fetch de página da plataforma, que devolve o texto do painel de transcrição — foi o que usei.

**Captura de referência** (não é bruto oficial): `docs/pareceres/captura-referencia-v0gJWn50gg8.txt`

* sha256 `8bae5bb66d557f8e474196193fe771ca1a36a0741f930ea764281ccff5aea47d` · 10.688 bytes ·
  355 linhas · 1.830 palavras;
* obtida em 16/09/2026 pelo **fetch da página do YouTube**, reproduzida pelo agente a partir do
  texto renderizado. O hash certifica **esta cópia**, não a saída do YouTube;
* **limitação declarada:** termina com um `M.` solto — artefato do fim do painel. A revisão do
  Comandante não tem esse `M.`, o que indica que o texto dele termina onde o vídeo termina;
* evidência de que é ASR cru, não reescrita: preserva as anotações de áudio do YouTube
  (`[roncando]`×4, `[limpando a garganta]`×5) e as corruptelas (`Un 3.000 anos`, `ficávam`,
  `mitlogo`, `julgo`, `paraa`, `esculhamba sem`, `locas`, `louoca`, `glu`, `reu`, `acásicos`);
* **todo achado deste parecer que depende dela está marcado "a confirmar"** — a conferência definitiva
  exige a captura oficial.

**O que resolve em 30 segundos:** abrir o vídeo → *Mostrar transcrição* → copiar → colar num `.txt`,
como o Comandante fez no vídeo 1. Aí a casa instala `00-fonte/transcricao-bruta.txt`, grava o sha256,
o G1 fica verde, o G9 passa a ter contra que cruzar e a fila de curadoria destrava.

**Decisão que não tomei:** não criei `transcricoes/<slug>/`. O slug depende do título (§1), a pasta
depende do bruto (§2) e o precedente da casa é explícito — entrega do Comandante não muda de lugar
por conta do agente. A auditoria inteira foi feita na **zona de trânsito** `upload/`, que é exatamente
o lugar documentado para isso (Plano de Organização §7; o próprio `rc_perfil_stt` reconhece o estágio
"solto — arquivo fora de `transcricoes/`").

---

## 3. O achado que muda a premissa: o ASR do YouTube pontua

| | vídeo 1 (bruto, 14/09) | vídeo 2 (captura, 12/09) |
|---|---:|---:|
| sinais por 100 palavras | **0,22** | **13,66** |
| vírgulas | 1 | 144 |
| pontos | 15 | 99 |
| anotações de áudio | nenhuma | `[roncando]`, `[limpando a garganta]` |

Três indícios de que a pontuação é do próprio ASR, e não de quem capturou:

1. **minúscula depois de ponto** — "os mesmos discos voadores de sempre. que seja, porque é, mas a
   história é muito complexa". Revisor humano ou LLM capitaliza; ASR não;
2. **as anotações de áudio sobrevivem** — camada de reescrita as remove (foi o que o NotebookLM fez);
3. **as corruptelas sobrevivem todas** — `Un 3.000`, `mitlogo`, `paraa`, `glu`, `reu`.

**Consequência para a decisão de ontem.** O parecer do motor STT deu ao derivado NotebookLM a vitória
no eixo 1 (pontuação/segmentação) com placar 4/4 — mas medido contra um bruto **sem pontuação**. Se o
YouTube agora pontua na origem, o ganho do derivado encolhe para 13,66 → 15,98 sinais/100 palavras
(neste vídeo) e para segmentação de linhas de legenda, enquanto o risco documentado dele (censura de
vocabulário, microedição que quebra casamento com a KB) continua inteiro. **A relação custo-benefício
da camada derivada precisa ser reavaliada com um bruto novo** — e a ferramenta que o Comandante está
testando pode tornar a camada desnecessária.

**A confirmar pelo Comandante:** abrir o painel de transcrição de um vídeo recente e ver se vem
pontuado. Se vier, o Guia §8 precisa de uma terceira redação: pontuação nativa **na fonte**, não só
no derivado.

---

## 4. Auditoria da revisão: o que mudou, palavra por palavra

Instrumento: `rc_perfil_stt.py`, eixo de proveniência. Captura (A) × revisão (B):

| métrica | A (captura) | B (revisão) | leitura |
|---|---:|---:|---|
| palavras | 1.830 | 1.817 | −13 (−0,7%): mesma cobertura de áudio |
| divergência lexical | — | **9,23%** | 91 palavras de A ausentes em B, 78 de B ausentes em A |
| Jaccard de vocabulário | — | 0,910 | mesmo léxico, edição pontual |
| hapax em comum | — | 0,917 | |
| marcadores orais idênticos | — | 4 de 6 (67%) | então 8=8, sabe 8=8, tipo 4=4, aí 2=2 |
| disfluências | 26 (14,21/1.000) | 24 (13,09/1.000) | **a revisão NÃO trata disfluência** |
| sinais por 100 palavras | 13,66 | 15,98 | pontuação refinada, não criada |
| canônicos KB presentes | 26 | **31** | +5: o revisor aplicou a base |
| variantes STT / formas proibidas | 0 / 0 | 0 / 0 | nada a substituir |
| tokens mascarados com `*` | **0** | **0** | nenhuma censura |
| veredito do instrumento | — | — | "mesma base de áudio com edição substancial em um dos lados" |

**Decomposição das 91 perdas** (todas conferidas uma a uma):

| categoria | tokens | exemplos |
|---|---:|---|
| anotações de áudio do YouTube | 14 | `[roncando]`×4, `[limpando a garganta]`×5 (limpando+garganta) |
| dêiticos resolvidos em termo doutrinário | ~19 | *aqui*×13, *esse*×4, *isso*×2 → "o lado antimaterial", "Brahmaloka", "Bhuloka" |
| corruptelas corrigidas | ~12 | *julgo*, *mitlogo*, *chamanismo*, *paraa*, *reu*, *esculhamba*, *sem*, *colapse*, *ancorado*, *glu*, *un*, *loca/louoca* |
| normalização de números | 3 | `3.000`/`5.000` → "3 mil"/"5 mil" (valor preservado — dentro do Guia §7) |
| artigos/preposições de reescrita | ~10 | *a*×6, *pra*×2, *e*×2 |
| marcadores orais podados | 2 | *eh*, *oh* |
| artefato da captura | 1 | o `M.` final (§2) |

**Decomposição dos 78 acréscimos:** termos doutrinários explícitos (*antimaterial*×5, *material*×3,
*lado*×3, *loka(s)*×3, *brahmaloka*×2, *bhuloka*, *akashicos*), correções (*jugo*, *mitólogo*,
*xamanismo*, *esculhambassem*, *colapsa*, *ancorada*, *ovo*, *glues*, *posetron*), artigos de
reescrita (*o*×10, *que*×3, *para*×3, *tem*×3, *da*×2) e *mil*×3 da normalização numérica.

**Leitura.** Nenhuma categoria é supressão de conteúdo. A revisão faz três coisas que a casa também
faz: **corrige o ASR contra a KB**, **explicita dêiticos** ("esse aqui" → "o lado antimaterial") e
**normaliza números**. O que ela **não** faz é tratar disfluência (24 marcas remanescentes, nível
acima do Guia §10) nem inserir marcadores editoriais — ou seja, sobra trabalho para a esteira, e é
trabalho pequeno.

---

## 5. Consequência arquitetural: teto de divergência é por natureza de camada

O G9 foi calibrado ontem com teto de 5% para o **derivado de máquina**: um texto que se declara
"o mesmo áudio, reescrito para legibilidade" não tem motivo legítimo para trocar palavra, e quando
troca, é censura ou microedição — foi o que pegou `merda`/`bandido` e o RC-954 zerado.

Este arquivo é outra coisa: **revisão humana**. Divergir é o trabalho. Medido com a régua da camada
2, um texto excelente reprova (9,23% > 5%) — e um portão que reprova o bom trabalho ensina as pessoas
a ignorar o portão.

**Proposta de norma (Guia §2.6, item 3) — teto por natureza:**

| natureza da camada | teto de divergência | o que se audita |
|---|---|---|
| derivado de máquina (mesmo ASR) | **≤ 5%** (como está) | divergência + máscaras: qualquer troca de palavra é suspeita |
| revisão de terceiro (humana ou de outra ferramenta) | **sem teto** | **rastreabilidade**: cada mudança classificada (correção KB / ortografia / disfluência / número / inserção doutrinária) e nenhuma sem classificação |
| saída da casa (blocos) | já coberto | G3 (formas proibidas), G5 (variantes aceitas), G6 (reprodutibilidade) |

Implementação pequena: `derivado.natureza: maquina | revisao-externa` no `metadados.yaml`; com
`revisao-externa`, o G9 troca o teste de teto pelo **relatório de divergência decomposto** (é o que
a §4 deste parecer fez à mão e pode virar saída do portão) e continua **falhando** em máscara de
asterisco não restaurada — censura é inaceitável em qualquer camada.

---

## 6. Verificação contra a KB-RC — a fonte de verdade decide

### 6.1 Duas regressões na revisão (corrigir)

| na revisão | a KB diz | evidência |
|---|---|---|
| "com quarks e **glues**" | **gluons** | RC-034 *Big Bang*: "sopa de quarks e gluons" (B031; P2025-03-15); a ficha já documenta o STT "quarques" como variante de *quarks* |
| "nenhum **pósetron** daqui" | **pósitron** | RC-161: "o jogo de pósitrons [STT 'positelétron']" (P2024-11-09); RC-636: "os pósitrons, que são os elétrons antimateriais do universo vizinho". A **captura estava certa**: "nenhum pósitron daqui, que é o antielétron" |

**Causa provável, e é um risco novo para a casa:** corretor ortográfico do editor de texto. `gluons`
→ *glues* e `pósitron` → *pósetron* não são erros de ouvido nem de doutrina — são substituições
automáticas de um dicionário que não conhece o termo técnico. É o equivalente doméstico da censura do
LLM: **uma camada automática entre o autor e o texto, trocando palavra sem avisar**. A casa acabou de
aprender a se defender disso no derivado (G9); falta se defender no produto.

**Proposta de contenção (encargo §9):** varredura de **formas quase-canônicas** — token fora do
dicionário pt-BR cuja distância de edição para uma superfície da KB seja 1–2 (glues↔gluons,
pósetron↔pósitron). Sai como camada do `rc_diagnostico` e vira linha na fila, não substituição
automática.

### 6.2 Um termo sem canônico registrado (decidir)

"**Registros Akáshicos**" — a revisão grafou assim; a KB atesta as duas formas, sem termo canônico:

* RC-161 *Memória Quântica dos Elétrons*: "o registro **akáshico**" (B024 p. 98) e "identifica os
  **registros akáshicos** com a memória coletiva dos elétrons";
* RC-548 *Arquivos Mentais*: "O passado está marcado nos **registros akásicos (ou akáshicos)**"
  (B075 p. 102);
* a citação de P2024-11-09 preservada em RC-161 mantém a forma STT: "os famosos registros acásicos".

Não há `nome` de termo com *Akásh* no `canonico.json`. **Decisão de curadoria:** registrar
*Registros Akáshicos* como termo novo (com *akásicos* como variante STT documentada) ou manter como
expressão dentro de RC-161. Enquanto não decidir, a forma do texto fica como está — é atestada.

### 6.3 Uma colisão de homógrafos (registrar com suspensão)

A captura diz: "Esse aqui tem milhões de **locas**. O que é locas? Sabe uma **qualia** que tem
aqueles buraquinhos? Cada **louoca** é um buraquinho daquele." A revisão leu: "…milhões de **lokas**.
O que são lokas? Sabe uma **colmeia** que tem aqueles buraquinhos? Cada **loka** é um buraquinho
daquele."

* **`lokas` está certo**: RC-077, `nome = "Lokas"`. `locas`/`louoca` são variantes STT novas.
* **`colmeia` está certo pelo contexto** e pela KB: RC-174 *Colmeia Universal* e RC-176 *Modelo
  Colmeia*, com a definição do próprio autor — "eu chamo de **circuito colmeico** o fato de que há um
  ser alfa que manda e o rebanho obedece. A imagem é a da colmeia — a abelha-rainha manda e as
  operárias obedecem". O vídeo diz, literalmente: "uma grande colmeia que tem uma abelha rainha e o
  resto é abelha operária. Tem um ser alfa, o resto obedece."
* **mas `Qualia` é termo legítimo da KB** — `canonico.json`: *"Qualia como Processamento Humano"*.
  Registrar `qualia → Colmeia` como variante STT sem suspensão faria o fuzzy propor *qualia*→*colmeia*
  em todo texto filosófico. É o caso clássico das **11 suspensões automáticas** por homografia do
  lote 01.
* **eco do vídeo 1:** lá o NotebookLM trocou "as **calmeias** começaram a colapsar" por "colmeias" em
  1 de 2 ocorrências, e o lote 01 registrou `calmeia → RC-174` (item 0022, aplicado). O ASR erra essa
  palavra de forma sistemática — *calmeia*, *qualia* — e agora há duas fontes atestando.

### 6.4 O que a revisão acertou contra a KB (conferido, nada a fazer)

`lokas` (RC-077) · `Brahmaloka` (RC-038; RC-106 *Universo Antimaterial*) · `Bhuloka` (RC-033;
RC-107 *Universo Material*) · `ovo cósmico` no lugar de "novo cósmico" (RC-034: "É ainda o 'Ovo
Cósmico' do mito chinês: P'an Ku (Brahma)") · `xamanismo` · `jugo` · `mitólogo` · `entropia`
(RC-160) · `singularidade`, `big bang`, `quarks` · `memória quântica dos elétrons` (RC-161) ·
`loop mental` · `externalização` (princípio).

### 6.5 Diagnóstico da casa sobre a revisão (números do motor)

```
palavras=1825  parágrafos=26  vírgulas=206  pontos=81
superfícies da base presentes=21  candidatos brutos=197  adjudicáveis=33
(variantes/truncamentos=7)  ausentes=5
```

**5 ausentes contra 145 no vídeo 1** — e ainda assim são ruído: 2 são inicial de frase
("Detalhe", "Nenhum" — o **4º defeito de régua**, `rc_diagnostico.py:372`, pendente), 2 são artefato
da linha de cabeçalho que entrou na medição, e **1 é candidato real: "Registros Akáshicos"** (§6.2).
Em texto limpo o defeito de régua é 80% do ruído — mais um argumento para o item 2 do §8 do parecer
anterior.

**Falso positivo perigoso na fila, que só adjudicação humana pega:**

| a fila propõe | o que aconteceria se aplicado |
|---|---|
| `colmeia` → **Colmeia Universal** (RC-174, superfície casada *calmeia*) | "Sabe uma **Colmeia Universal** que tem aqueles buraquinhos?" — destrói a frase. A palavra do texto **já é** a correta |
| `antimaterial` → **Antimundo / antimatéria** (RC-527, truncamento, 5 ocorrências) | o termo certo é RC-106 *Universo Antimaterial*, não RC-527 |
| `ainda` → **Brahma** (superfície *anda*) | ruído fonético puro |

Confirma a norma vigente (Guia §14): "**a fila fuzzy é triagem de recall, nunca decisão**". Acrescento
o caso ao Guia §4.2 (*quando NUNCA substituir*): **variante cujo canônico é foneticamente idêntico à
forma correta do texto** — a fila vai propor sempre, e a resposta é sempre *recusada/proteção*.

---

## 7. Fila de curadoria proposta — **bloqueada até existir bruto**

`rc_curadoria.py` não aplica variante sem ocorrência atestada no bruto (regra da casa, Guia §15 e
`CONTRIBUTING`). Nenhuma destas linhas pode entrar em `KB-RC/_fila-de-curadoria.csv` enquanto
`00-fonte/transcricao-bruta.txt` não existir. Ficam aqui, prontas:

| # | tipo | forma | canônico | evidência |
|---|---|---|---|---|
| 1 | nova variante STT | `locas`, `louoca` | RC-077 Lokas | "milhões de locas… Cada louoca é um buraquinho" |
| 2 | nova variante STT **com suspensão por homografia** | `qualia` | RC-174 Colmeia Universal | §6.3 — colide com *Qualia como Processamento Humano* |
| 3 | nova variante STT | `acásicos`, `acáxicos` | Registros Akáshicos (a registrar, §6.2) | "os registros acásicos ou acáxicos" |
| 4 | nova variante STT | `novo cósmico` | RC-034 Ovo Cósmico | "ficaram dentro do novo cósmico" |
| 5 | nova variante STT | `glu` | gluons (RC-034) | "com quarks e glu" |
| 6 | nova variante STT | `mitlogo` | mitólogo | "Nenhum mitlogo consegue" |
| 7 | nova variante STT | `julgo` | jugo | "se libertaram do julgo dos deuses" |
| 8 | nova variante STT | `chamanismo` | xamanismo | "o que a gente entende como sendo chamanismo" |
| 9 | nova variante STT | `paraa`, `reu`, `esculhamba sem`, `ficávam`, `Un` | para a, (o) eu, esculhambassem, ficavam, Uns | corruptelas de ligação |
| 10 | novo termo (decisão) | Registros Akáshicos | — | §6.2 |
| 11 | novo registro bibliográfico | *A Dramática Fusão dos Universos de Hyren e Hyron* (palestra) | — | cabeçalho do .docx; tema = B085 |
| 12 | novo registro Y | vídeo `v0gJWn50gg8` (padrão Y, Guia §2.5) | — | §1 — canal Jan Val Ellam, 2026-09-12, 19:24 |

**O que este vídeo acrescenta à KB como fonte** (para quando o bruto existir): atesta RC-174/RC-176
(circuito colmeico, com a fórmula "ser alfa, o resto obedece"), RC-106/RC-107 (dois universos,
material e antimaterial, e a fusão), RC-161 (memória quântica dos elétrons = registros akáshicos;
"nenhum elétron morre, o que se modifica é a memória quântica"), RC-636 (pósitrons como elétrons
antimateriais), RC-034 (singularidade, sopa de quarks e gluons, ovo cósmico), RC-160 (entropia como
quem finaliza), RC-070 (isolamento cósmico: "ficamos isolados… condicionados a pensar que somos os
únicos"), além do princípio da **externalização** e do **loop mental** como mecanismo do colapso.

---

## 8. O que sobra para a esteira fazer neste texto

A revisão do Comandante adiantou o que a casa faria nos blocos. Sobra, medido:

1. **2 correções** (§6.1): `glues`→gluons, `pósetron`→pósitron;
2. **disfluência nível LEVE** (Guia §10): 24 marcas remanescentes — 13,09 por 1.000 palavras. O vídeo 1
   entrou com 40,49; este texto está melhor, mas acima do que a norma pede;
3. **marcadores editoriais** (Guia §12): nenhum `[NOTA]`, nenhum `[A CONFIRMAR]` — as inserções
   doutrinárias (*Brahmaloka*, *Bhuloka*, "o lado antimaterial") são interpretação do revisor e
   merecem `[NOTA]` com a evidência da KB, porque **não estão na captura**;
4. **diarização**: dispensável — monólogo, falante único (Jan Val Ellam);
5. **anúncios**: não há (o vídeo não tem trecho promocional; a descrição tem os links do canal, que
   não entram no corpo — Guia §1.2);
6. **conversão para o formato da casa**: `.docx` → blocos `.md` (o contrato de versionamento é
   inegociável) e remontagem do `.docx` por `rc_docx.py`, para o G6 poder garantir reprodutibilidade.

---

## 9. Encargos de código que este turno revelou

| # | item | onde | prioridade |
|---|---|---|---|
| 1 | `derivado.natureza` (máquina × revisão externa) e G9 decompondo divergência em vez de aplicar teto cego | `rc_qa.py`, Guia §2.6 | **alta** — sem isso o G9 reprova trabalho bom |
| 2 | varredura de **formas quase-canônicas** (distância 1–2 de superfície KB, fora do dicionário) | `rc_diagnostico.py` | **alta** — pega `glues`/`pósetron` e o próximo corretor |
| 3 | `rc_leitura.py` separar cabeçalho no critério 3 (sem marcador, sem linha dominante) | `rc_leitura.py` | média — o instrumento avisa, mas ainda mede o cabeçalho junto |
| 4 | `rc_novo.py --bruto` opcional + `bruto.status: pendente-captura`, com G1 respondendo **N/A** em vez de FALHA | `rc_novo.py`, `rc_qa.py` | média — pasta em captura é estado legítimo, não erro |
| 5 | item 2 do parecer anterior: `rc_diagnostico.py:372` ciente de inicial de frase | `rc_diagnostico.py` | média — 80% do ruído em texto limpo |
| 6 | reconciliar as duas réguas de contagem (`split()` × `PALAVRA_RE`) | `rc_leitura.py`, `rc_diagnostico.py` | baixa — documentada no Guia §2.6 item 6 |

Feito neste turno, sem custo: os **vereditos do eixo 4 do `rc_perfil_stt.py` estavam mentindo** —
diziam que `rc_novo`/`rc_indice` medem o corpo pela linha mais longa, o que deixou de ser verdade
hoje de manhã com o `rc_leitura.py`. Atualizados para descrever o código real, inclusive o resíduo do
critério 3. Testes: **154 verificações, 0 falhas**.

---

## 10. Nota operacional

* **O workspace foi reclonado neste turno** e a branch local nasceu na base (`3adc6b6`), com o
  trabalho do dia no disco como *untracked*. Recuperado sem perda: backup em `/tmp` antes,
  `git reset --hard` para a ponta remota `0ea4388` depois, árvore conferida (154 testes, 9 portões
  verdes). O clone veio com `remote.origin.fetch` restrito a `main` — corrigido, e a branch agora
  rastreia `origin/arena/01a0a743-transcri-youtube`.
* **O push voltou a funcionar.** O commit de ontem (`4e01d97`, arquitetura de três camadas + G9) subiu
  junto com os dois que estavam presos localmente. A branch está 22 commits à frente de `origin/main`;
  **nenhum PR foi aberto** — a decisão é do Comandante.
* **Este turno não criou pasta de transcrição, não mexeu em `KB-RC/` e não moveu o arquivo do
  Comandante.** A auditoria vive em `docs/pareceres/` e o arquivo continua em `upload/`, de onde só
  sai com destino decidido.

---

## Como reproduzir tudo o que está neste parecer

```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -r ferramentas/requirements.txt

# 1. extrair o corpo do .docx (descartando as 3 linhas de cabeçalho)
/tmp/venv/bin/python -c "from docx import Document; u=[p.text for p in \
Document('upload/alienigenas-ou-seres-de-outro-universo.docx').paragraphs if p.text.strip()]; \
open('docs/pareceres/video-2-revisao-corpo.txt','w',encoding='utf-8').write(chr(10).join(u[3:])+chr(10))"

# 2. os quatro eixos + proveniência: captura de referência × revisão
/tmp/venv/bin/python ferramentas/rc_perfil_stt.py \
    docs/pareceres/captura-referencia-v0gJWn50gg8.txt \
    docs/pareceres/video-2-revisao-corpo.txt \
    --md docs/pareceres/video-2-medicao.md --json docs/pareceres/video-2-perfil.json

# 3. motor da casa contra a KB-RC (ausentes, adjudicáveis, dossiê)
/tmp/venv/bin/python ferramentas/rc_diagnostico.py \
    docs/pareceres/video-2-revisao-corpo.txt --kb KB-RC --saida /tmp/diag-video2

# 4. as evidências da KB que decidem o §6
grep -rn "sopa de quarks e gluons" KB-RC/termos/RC-034-big-bang.md   # gluons, não "glues"
grep -rn "Pósitrons" KB-RC/termos/RC-636-*.md                        # pósitron, não "pósetron"
grep -o '"nome": "[^"]*ualia[^"]*"' KB-RC/canonico.json              # Qualia É termo da KB
grep -n "nome" KB-RC/termos/RC-077-lokas.md | head -3                # Lokas
grep -rn "akásicos\|akáshicos" KB-RC/termos/RC-548-*.md KB-RC/termos/RC-161-*.md
```

---

## 11. Decisões pendentes do Comandante

1. **O bruto oficial** — copiar a transcrição do painel do YouTube (30 s) e entregar. Destrava G1, G9
   e toda a fila do §7. Sem ele, a casa tem uma revisão boa e nenhuma forma de auditá-la.
2. **Título e slug** — "Alienígenas e humanos: Eles já estão entre nós?" (oficial) ou "Alienígenas ou
   seres de outro universo?" (do arquivo)? O slug vira nome de pasta e vai para o catálogo e o
   `biblio.json`.
3. **Natureza da camada** (§5) — o arquivo entra como **revisão externa** (sem teto de divergência,
   com auditoria de rastreabilidade) ou como **derivado de trabalho** (teto, e então 9,23% reprova)?
   Proponho o primeiro, com `derivado.natureza: revisao-externa`.
4. **Quem termina o texto** (§8) — a casa converte para blocos `.md`, aplica as 2 correções, a
   disfluência leve e os `[NOTA]` nas inserções doutrinárias, e remonta o `.docx`? Ou o Comandante
   prefere manter a revisão dele como está, com este parecer anexado?
5. **A premissa do §3** — confirmar no painel se o YouTube agora pontua. Se sim, o Guia §8 muda de
   novo e a camada derivada do vídeo 1 precisa ser reavaliada com dados novos.
