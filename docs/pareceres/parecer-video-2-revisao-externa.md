# Parecer de recepção — vídeo 2: revisão externa "higienizada"

**Projeto:** Transcri-YouTube · **Data:** 16 de setembro de 2026 · **Elaborado por:** Agente 86 (Arena.ai Agent Mode)

**Objeto:** receber e auditar a revisão que o Comandante fez do 2º vídeo, entregue como
`upload/alienigenas-ou-seres-de-outro-universo.docx` e hoje instalada em
`transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos/00-fonte/revisao-comandante.docx` — a revisão que o
Comandante fez do 2º vídeo, produzida fora da esteira da casa, no contexto do teste de "uma outra
ferramenta de transcrição que forneça conteúdo mais higienizado".

**Status: COMPLETO. Bruto oficial recebido em 16/09/2026 (commit `87a3525`) — e ele RETIFICA duas
partes deste parecer.** A auditoria terminológica contra a KB-RC estava certa e continua valendo
(§6). A auditoria de proveniência foi refeita contra o bruto oficial: **8,12%** de divergência, não
9,23% (§4). E o **§3 está RETRATADO**: a pontuação que atribuí ao ASR do YouTube era da minha rota de
captura, não do YouTube — a mesma rota que corrompeu "ovo cósmico" em "novo cósmico". Ver §3, que foi
reescrito como retratação, e §2, que registra a chegada do bruto.

**ESTEIRA EXECUTADA em 16/09/2026**, por despacho do Comandante ("uma esteira normal", sem
comparação de motores): pasta `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos`, bruto oficial instalado, diagnóstico, 3 blocos,
livro-razão com 29 linhas decididas, produto `.docx`, devolução à KB e fonte `Y2026-09-12`
registrada. **Portões G1–G8 `ok`, G9 `n/a`** (a revisão externa é humana, não derivado de
máquina). As três regressões que este parecer apontou foram corrigidas nos blocos — e uma
quarta apareceu na conferência final: `glues`→**gluons** (RC-034), `pósetron`→**pósitron**
(RC-636) e "hoje a parte"→"hoje **à tarde**", que o bruto atesta e muda o sentido da frase de
abertura. Detalhes em `40-devolucao/devolucao-a-kb.md` e `40-devolucao/adjudicacao.md`. Saída bruta do instrumento:
`docs/pareceres/video-2-medicao.md` e `docs/pareceres/video-2-perfil.json` (medidos sobre a captura de
referência — mantidos como evidência do defeito, não como medição do vídeo).

---

## 0. Sumário executivo

**1. Nada foi censurado.** Zero asteriscos nos dois lados. Todas as palavras que uma camada
"higienizadora" costuma remover estão inteiras na revisão: *diabos* (2×2), *esculhambado* (2×2),
*cretinizou-nos*, *imbecilizou-nos*, *coelhos*, *fofoca*, *bom senso*, *mídia*. É o oposto exato do
que o NotebookLM fez no vídeo 1 (`merda`×3 → `m****`, `bandido`×2 → `b******`). **Neste eixo, a
ferramenta nova passa.**

**2. A divergência de 8,12% não é perda — é correção** (medida contra o bruto oficial; eram 9,23%
contra a minha captura, que estava corrompida). Decomposta palavra a palavra (§4): 23 tokens de
corruptelas do ASR consertadas (*julgo*→*jugo*, *mitlogo*→*mitólogo*, *chamanismo*→*xamanismo*,
*acásicos/acáxicos*→*Akáshicos*, *locas/louoca*→*lokas*, *qualia*→*colmeia*, *paraa*→*para a*,
*reu*→*eu*, *colapse*→*colapsa*), 19 tokens de **dêiticos nomeados** — o que o Comandante explicou:
Ellam apontava para a tela e dizia "este aqui"/"aquele ali", e a revisão nomeia o que ele apontava
("o lado antimaterial", "Brahmaloka", "Bhuloka") —, 20 de reescrita de ligação, 4 de números
normalizados e 4 de marcadores orais podados. A revisão é **curadoria doutrinária de qualidade**, não
higienização.

**3. O teto de 5% do portão G9 é da camada 2, e aplicá-lo a este arquivo é erro de categoria.**
Um derivado de máquina não tem motivo para mudar palavra; uma revisão humana tem o dever de mudar.
Se este arquivo entrasse como derivado, o G9 o reprovaria — e estaria errado (§5). **Proposta:
teto por natureza da camada**, e auditoria de *rastreabilidade* (não de divergência) para revisão
de terceiro.

**4. RETRATADO — o ASR do YouTube NÃO pontua; quem pontuou foi a minha rota de captura.**
O bruto oficial tem **0,11 sinais por 100 palavras** (0 vírgulas, 2 pontos, e os dois são os pontos
decimais de "3.000" e "5.000"). A premissa do Guia §8 continua inteira, e a arquitetura de camadas
do vídeo 1 não precisa ser reavaliada. O que o episódio ensina é outro, e vale mais: **captura de
transcrição por fetch de página não é fonte** — a rota devolveu texto pontuado, capitalizado e com uma
palavra corrompida ("ovo cósmico" → "novo cósmico"). Ver §3.

**5. Duas regressões na revisão, ambas com canônico na KB** — e ambas com a mesma causa provável: o
corretor ortográfico do editor de texto. *glues* → a KB diz **gluons** (RC-034). *pósetron* → a KB
diz **pósitron** (RC-161, RC-636). É o equivalente doméstico da censura do LLM: uma camada
automática entre o autor e o texto, trocando palavra sem avisar (§6).

**6. A camada 1 chegou e a fila destravou.** O Comandante subiu `upload/video-2-transcri-youtube.txt`
(commit `87a3525`, sha256 `16c9276ae847dd728b4be0d731132b8848e0b5fad4d9b0ced966121b0939e9a1`,
11.638 bytes, corpo de **1.810 palavras** na linha 12). É o bruto oficial: G1 tem o que hashar, e as
variantes do §7 passam a ter atestação — `rc_curadoria.py` pode aplicá-las (§7).

---

## 1. O que chegou, e o que a plataforma diz

| campo | valor | fonte |
|---|---|---|
| arquivo | `upload/alienigenas-ou-seres-de-outro-universo.docx` → `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos/00-fonte/revisao-comandante.docx` | commit `0ea4388` (upload web do Comandante); migrado da zona de trânsito em 16/09/2026 |
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

## 2. A camada 1: o que faltava, o que chegou, e o que o sandbox não alcança

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

**RESOLVIDO em 16/09/2026:** o Comandante subiu `upload/video-2-transcri-youtube.txt` (commit
`87a3525`) — a cópia do painel, no mesmo formato do vídeo 1 (cabeçalho com título, URL, data e *guia
de fontes*; corpo numa linha só). Números: 11.638 bytes · 12 linhas · sha256
`16c9276ae847dd728b4be0d731132b8848e0b5fad4d9b0ced966121b0939e9a1` · corpo na linha 12 com
**10.008 caracteres e 1.810 palavras** · critério de corpo `linha-mais-longa` com cobertura de 88,3%
(acima do piso de 80% do `rc_leitura.py`, então sem aviso). G1 e a fila de curadoria destravados.

**Uma divergência de registro, para decidir:** o cabeçalho do bruto diz "publicado em **13/09/2026**",
o `.docx` do Comandante diz **12/09/2026** e a página do YouTube diz *uploaded* **2026-09-12**. A casa
fica com a plataforma (12/09) e registra as outras duas datas nos metadados — o vídeo 1 já tinha o
mesmo padrão (live em 14/09, upload em 15/09).

**Decisão que não tomei na primeira versão:** não criei `transcricoes/<slug>/`, porque o slug depende
do título (§1) e a pasta dependia do bruto. A auditoria foi feita na **zona de trânsito** `upload/`,
que é o lugar documentado para isso (Plano de Organização §7). Com o despacho seguinte — "podemos
tratar este 2º vídeo normalmente, uma esteira normal" — a pasta passa a ser o caminho, e a captura de
referência deixa de ser insumo: fica em `docs/pareceres/` como **evidência do defeito de rota** do §3.

---

## 3. RETRATAÇÃO — o ASR do YouTube não pontua; a minha rota de captura pontuou

**O que este parecer afirmou na primeira versão:** que a captura deste vídeo tinha 13,66 sinais por
100 palavras contra 0,22 no bruto do vídeo 1, e que portanto o ASR do YouTube teria passado a
entregar texto pontuado — o que reabriria a decisão sobre a camada derivada. **Está errado.** O bruto
oficial, entregue pelo Comandante no commit `87a3525`, não tem pontuação nenhuma.

| | bruto oficial (Comandante) | minha captura por fetch | revisão do Comandante |
|---|---:|---:|---:|
| palavras | **1.810** | 1.830 | 1.817 |
| vírgulas | **0** | 144 | 206 |
| pontos | **2** (os decimais de "3.000" e "5.000") | 99 | 81 |
| interrogações | **0** | 7 | 6 |
| sinais por 100 palavras | **0,11** | 13,66 | 16,13 |
| "ovo cósmico" | **ovo cósmico** | "novo cósmico" | ovo cósmico |
| `[roncando]`, `[limpando a garganta]` | ausentes | presentes (9) | ausentes |

A rota de fetch de página **reescreveu o texto**: pontuou, capitalizou, separou em linhas de legenda,
acrescentou marcadores de áudio que o bruto oficial não tem e **trocou uma palavra** — "dentro do
**ovo** cósmico" virou "dentro do **novo** cósmico". Os três "indícios" que apresentei na primeira
versão eram, todos, artefatos da mesma rota: a minúscula depois de ponto e as corruptelas preservadas
provavam apenas que a reescrita era conservadora, não que a pontuação fosse do ASR.

**Consequências, todas já aplicadas neste parecer:**

1. **A premissa do Guia §8 continua inteira** — o STT não traz pontuação, pontuar continua sendo
   trabalho. A arquitetura de três camadas do vídeo 1 **não** precisa ser reavaliada; o derivado
   continua valendo o que o parecer anterior mediu.
2. **A fila do §7 perde um item**: `novo cósmico → Ovo Cósmico` (RC-034) era corrupção minha, não do
   ASR. O bruto oficial já diz "ovo cósmico" — não há variante a registrar.
3. **Nenhum achado deste parecer continua apoiado na captura de referência.** A auditoria foi refeita
   contra o bruto oficial (§4) e as duas regressões do §6.1 foram reconfirmadas nele: o bruto diz
   "quarks e **glu**" e "nenhum **pósitron** daqui".
4. **Norma nova, que vale para a casa inteira:** *transcrição obtida por fetch de página não é fonte.*
   É derivado de fidelidade desconhecida — pontua, capitaliza e troca palavra. Serve para descobrir
   que um vídeo existe e para ler o conteúdo; **não** serve para instalar `transcricao-bruta.txt`, nem
   para atestar variante, nem para medir. O bruto só entra por cópia do painel feita por gente
   (o caminho do vídeo 1 e deste) ou por download da legenda. Registrado em `upload/README.md` e nos
   becos sem saída do diário.

**Por que isso importa mais do que o achado retractado:** a casa passou o dia 16/09 construindo uma
arquitetura cuja regra central é "derivado nunca vira fonte". Aqui foi o **agente** que quase instalou
um derivado como fonte — com hash, parecer e fila de curadoria apoiados nele. O G1 teria ficado verde
sobre uma cópia que trocou "ovo" por "novo". A defesa que funcionou foi a mesma de sempre: o
Comandante entregou a fonte, e a fonte desmentiu o derivado.

---

## 4. Auditoria da revisão: o que mudou, palavra por palavra

Medido contra o **bruto oficial** (`video-2-medicao-oficial.md`, gerado pelo instrumento):

| métrica | A (bruto oficial) | B (revisão) | leitura |
|---|---:|---:|---|
| palavras | 1.810 | 1.817 | +7 (+0,4%): mesma cobertura de áudio, do primeiro ao último enunciado |
| sinais por 100 palavras | **0,11** | 16,13 | o STT não pontua (§3); a revisão pontuou |
| sentenças · maior sentença | 3 · 1.737 | 85 · 282 | segmentação criada pela revisão |
| divergência lexical | — | **8,12%** | 70 palavras de A ausentes em B, 77 de B ausentes em A |
| Jaccard de vocabulário | — | 0,916 | mesmo léxico, edição pontual |
| hapax em comum | — | 0,922 | |
| marcadores orais idênticos | — | 4 de 6 (67%) | então 8=8, sabe 8=8, tipo 4=4, aí 2=2 |
| disfluências | 27 (14,92/1.000) | 24 (13,21/1.000) | **a revisão quase não trata disfluência** |
| canônicos KB presentes | 12 formas / 26 ocorrências | **16 formas / 31 ocorrências** | o revisor aplicou a base |
| variantes STT · formas proibidas | 0 · 0 | 0 · 0 | nada a substituir, nada proibido |
| tokens mascarados com `*` | **0** | **0** | nenhuma censura |
| veredito do instrumento | — | — | "mesma base de áudio com edição substancial em um dos lados" |

**Decomposição das 70 perdas** — todas conferidas uma a uma no bruto oficial:

| categoria | tokens | exemplos |
|---|---:|---|
| corruptelas do ASR corrigidas | **23** | *julgo*, *mitlogo*, *chamanismo*, *glu*, *positron*, *acásicos*, *acáxicos*, *locas*×2, *louoca*, *qualia*, *paraa*, *reu*, *colapse*, *ancorado*, *esculhamba*+*sem*, *vir*, *reproduzindo* |
| **dêiticos nomeados pelo revisor** | **19** | *aqui*×13, *esse*×4, *isso*×2 — "este aqui"/"aquele ali" ditos apontando para a tela |
| reescrita de ligação | 20 | *e*×2, *a*, *pra*×2, *um*, *ou*, *em*, *como*, *fosse*, *era*, *foi*, *ele*, *eu*, *tinha*, *num*, *grande*, *lenta*, *duas*, *depois*, *essas*, *coisas*, *gente*, *tarde* |
| números normalizados | 4 | `3.000`/`5.000`/"un" → "3 mil"/"5 mil"/"Uns" (valor preservado — Guia §7) |
| marcadores orais podados | 4 | *eh*, *oh*, *né* |

**Decomposição dos 77 acréscimos:** nomes doutrinários que o bruto não traz — *antimaterial*×5,
*material*×3, *lado*×3, *loka(s)*×3, *brahmaloka*×2, *bhuloka*, *universo*×2, *chamado*, *chamamos*,
*colmeia*, *akashicos* —; correções (*xamanismo*, *jugo*, *mitólogo*, *esculhambassem*, *colapsa*,
*ancorada*, *mil*×3, *uns*, *5*, *dois*); artigos e verbos de reescrita (*o*×10, *que*×3, *para*×3,
*tem*×3, *de*, *da*, *do*, *os*, *são*, *com*, *for*, *nossa*, *tudo*, *além*, *nisso*, *lados*,
*parte*, *fossem*, *esses*, *reproduzido*, *servir*); e as **duas regressões do §6.1** (*glues*,
*posetron*).

**A observação do Comandante explica o maior bloco de mudanças.** Do despacho de 16/09/2026: *"ao
revisar o vídeo notei que o Ellam dizia algo e não nominava, porque estava apontando para uma tela de
apresentação, então o que eu fiz, nomeie o que ele estava falando e basicamente está relacionado à
formação do universo, com seu lado material e o antimaterial, que ela apontava e falava este aqui ou
aquele ali."* É exatamente o que a medição mostra: 19 dêiticos perdidos, 5 *antimaterial* + 3
*material* + 3 *lado* + 2 *Brahmaloka* + *Bhuloka* ganhos. Não é acréscimo de doutrina por
interpretação livre — é **nomeação do referente ostensivo**, e a KB confirma os nomes
(RC-106 *Universo Antimaterial (Brahmaloka)*, RC-107 *Universo Material (Bhuloka)*).

O que a casa faz com isso, e por quê: o Guia §12 pede marcador editorial para intervenção do revisor
que não está na fonte. Nomear o que o autor apontou é intervenção legítima e documentada — mas o
leitor do produto final não pode confundir a palavra do autor com a do revisor. Tratamento proposto:
`[NOTA]` na **primeira** ocorrência de cada nome inserido (Brahmaloka, Bhuloka, lado
material/antimaterial), explicando que o autor apontava para a tela e o revisor nomeou o referente,
com a ficha da KB ao lado. Nas ocorrências seguintes, texto limpo.

**Leitura final.** Nenhuma categoria é supressão de conteúdo. A revisão faz três das cinco camadas do
Guia §3 (ortografia/gramática, terminologia contra a KB, segmentação e pontuação) e **não** faz as
outras duas: disfluência (24 marcas remanescentes, acima do nível LEVE do §10) e marcadores
editoriais (zero `[NOTA]`, zero `[A CONFIRMAR]`). O que sobra para a esteira é pequeno e está no §8.

---

## 5. Consequência arquitetural: teto de divergência é por natureza de camada

O G9 foi calibrado ontem com teto de 5% para o **derivado de máquina**: um texto que se declara
"o mesmo áudio, reescrito para legibilidade" não tem motivo legítimo para trocar palavra, e quando
troca, é censura ou microedição — foi o que pegou `merda`/`bandido` e o RC-954 zerado.

Este arquivo é outra coisa: **revisão humana**. Divergir é o trabalho. Medido com a régua da camada
2, um texto excelente reprova (8,12% > 5%) — e um portão que reprova o bom trabalho ensina as pessoas
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

## 7. Fila de curadoria proposta — **destravada: o bruto oficial chegou**

`rc_curadoria.py` não aplica variante sem ocorrência atestada no bruto (regra da casa, Guia §15 e
`CONTRIBUTING`). Com `upload/video-2-transcri-youtube.txt` entregue (commit `87a3525`) e instalado em
`transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos/00-fonte/transcricao-bruta.txt`, todas as
linhas abaixo passam a ter atestação — conferida uma a uma no corpo do bruto. **O item 4 da primeira
versão foi retirado**: `novo cósmico` era corrupção da minha captura, não do ASR (§3); o bruto oficial
já diz "ovo cósmico".

| # | tipo | forma | canônico | evidência |
|---|---|---|---|---|
| 1 | nova variante STT | `locas`, `louoca` | RC-077 Lokas | "milhões de locas… Cada louoca é um buraquinho" |
| 2 | nova variante STT **com suspensão por homografia** | `qualia` | RC-174 Colmeia Universal | §6.3 — colide com *Qualia como Processamento Humano* |
| 3 | nova variante STT | `acásicos`, `acáxicos` | Registros Akáshicos (a registrar, §6.2) | "os registros acásicos ou acáxicos" |
| ~~4~~ | ~~`novo cósmico` → RC-034 Ovo Cósmico~~ | **RETIRADO** | — | corrupção da captura por fetch, não do ASR: o bruto oficial diz "ovo cósmico" (§3) |
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

**Feito neste turno:**

* os **vereditos do eixo 4 do `rc_perfil_stt.py` estavam mentindo** — diziam que `rc_novo`/`rc_indice`
  medem o corpo pela linha mais longa, o que deixou de ser verdade hoje de manhã com o
  `rc_leitura.py`. Atualizados para descrever o código real;
* **`rc_perfil_stt.py` passou a medir o corpo pelo critério único** (`rc_leitura`), e não o arquivo
  inteiro. Era a **terceira régua de corpo** da casa e a mais perigosa, porque ninguém a via: no vídeo
  2 o cabeçalho traz o "Guia de fontes" resumido (167 palavras sobre um corpo de 1.810, pontuado por
  ser resumo automático), e o instrumento devolveu **14,37%** de divergência onde o corpo tem
  **8,12%**, além de anunciar "pontuação nativa" do ASR com 6,6 sinais por 1.000 palavras inventados
  pelo cabeçalho. O eixo 4 continua olhando o arquivo inteiro — é a pergunta dele ("onde começa o
  corpo?") — mas agora com `texto_integral` separado de `texto`;
* com isso o instrumento passa a dizer a verdade sobre o vídeo 2: bruto **0,11** sinais por 100
  palavras → Guia §8 **compatível** (o STT não pontua); revisão 16,13 → premissa superada, como é
  esperado de um texto revisado.

Testes: **154 verificações, 0 falhas**.

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
  Comandante.** A auditoria vive em `docs/pareceres/`; o arquivo migrou de `upload/` para
  `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos/00-fonte/revisao-comandante.docx`, de onde só
  sai com destino decidido.

---

## Como reproduzir tudo o que está neste parecer

```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -r ferramentas/requirements.txt

# 1. extrair o corpo do .docx (descartando as 3 linhas de cabeçalho)
/tmp/venv/bin/python -c "from docx import Document; u=[p.text for p in \
Document('transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos/00-fonte/revisao-comandante.docx').paragraphs if p.text.strip()]; \
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

## 11. Decisões — o que o despacho de 16/09 já respondeu, e o que sobra

**Respondidas pelo Comandante** (despacho: *"podemos tratar este 2º vídeo normalmente, sem necessidade
de comparação, ou seja, uma esteira normal"*):

1. **Bruto oficial** — entregue (`upload/video-2-transcri-youtube.txt`, commit `87a3525`). Instalado
   em `00-fonte/transcricao-bruta.txt`; G1 verde; fila de curadoria com atestação.
2. **Comparação entre motores** — dispensada. O vídeo 2 entra como **esteira normal**: bruto →
   diagnóstico → blocos → produto → devolução → nove portões. A auditoria deste parecer fica como
   registro do teste que o Comandante fez, não como etapa do fluxo.
3. **Natureza da camada** — resolvida na prática: o texto do Comandante não é derivado de máquina, é
   **revisão**. Entra como matéria dos blocos (`20-blocos/`), não como `derivado:` em metadados; o G9
   responde `N/A` nesta pasta e o §5 fica como proposta de norma para quando houver revisão de
   terceiro de novo.
4. **Os dêiticos nomeados** — justificados pelo autor da revisão (§4). Entram no texto com `[NOTA]` na
   primeira ocorrência de cada nome, como o Guia §12 pede.

**Sobram duas, e só duas:**

* **título e slug** — o YouTube diz "Alienígenas e humanos: Eles já estão entre nós?"; o `.docx` diz
  "Alienígenas ou seres de outro universo?". A casa adotou o oficial para o slug
  (`2026-09-12-alienigenas-e-humanos-entre-nos`) e registrou o do Comandante como título de trabalho;
  trocar depois é um `git mv` mais três campos de metadados.
* **data** — o cabeçalho do bruto diz 13/09/2026, o `.docx` diz 12/09/2026 e a plataforma diz
  *uploaded* 2026-09-12. A casa ficou com a plataforma e registrou as três (§2).
