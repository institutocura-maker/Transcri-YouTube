# Guia de Revisão e Governança Terminológica — v2

**Aplicação:** transcrições automáticas (STT) de palestras, lives e vídeos do YouTube de Jan Val Ellam e material correlato das Revelações Cósmicas.
**Versão:** 2.0 — substitui integralmente o *docs/legado/2026-09-guia-v1/guia-sistema-de-revisao-e-governanca-terminologica-v1.docx* (v1).
**Data:** 16 de setembro de 2026 · **Elaboração:** Agente 86 · **Aprovação:** Comandante
**Anexo I:** `docs/normas/resolucao-de-conflitos.md` (resolução dos oito conflitos da base — leitura obrigatória antes da primeira revisão)

---

## 0. O que mudou da v1 para a v2

| # | Mudança | Motivo |
|---|---|---|
| 1 | **A fonte de verdade passou a ser `KB-RC/`** (`canonico.json` + `biblio.json` + `termos/*.md`). A planilha `docs/legado/2026-09-base-terminologica.xlsx` fica como fonte legada de conferência. | Decisão do despacho. A KB-RC tem 946 termos, 820 fichas e 104 obras; a planilha é um retrato anterior e sem prosa |
| 2 | Os **oito conflitos da base foram resolvidos** e viraram registro formal (§4.3) | Não se revisa transcrição com a base em conflito |
| 3 | Nova seção de **camadas de correção** com ordem de aplicação (§3) | A v1 misturava terminologia, ortografia e números na mesma tabela |
| 4 | Novas regras de **quando NÃO substituir** (§4.2), com classes de variante extraídas da KB (§4.1) | 778 das 1.590 relações variante→canônico da KB são equivalência conceitual, não erro de grafia; substituí-las destruiria o texto |
| 5 | **Camada Externos formalizada** (§5) com busca externa autorizada somente para ela, sempre com fonte e data | Despacho: aprovada com restrição |
| 6 | **Contrato editorial explícito** (§1.2): saídas .md + .docx, sem guia de fontes, anúncios preservados, diarização com rótulos inferidos, disfluência leve | Decisões do Comandante que estavam fora do documento |
| 7 | Seções novas de **pontuação/segmentação** (§8), **números e datas** (§7), **marcadores editoriais** (§12) | O material bruto chega com 1 vírgula e 19 pontos em 18.781 palavras |
| 8 | **Fluxo em 8 blocos** com comandos e dossiê por bloco (§13) e métricas de aceite (§14) | Operacionalizar a revisão |
| 9 | **Governança de retorno à KB** (§15): toda revisão devolve achados à base | A KB é viva; a revisão é também um instrumento de coleta |
| 10 | Regra nova: **citação literal preserva a forma STT** (§4.5) | Sem ela, a Quarentena entraria em conflito com as próprias fichas |

---

## 1. Escopo e produto

### 1.1 Escopo
Correção ortográfica e terminológica de transcrição automática, com padronização dos termos das Revelações Cósmicas, sem reescrita autoral. **O revisor não é coautor**: ele devolve ao texto a forma que o autor teria usado se tivesse digitado.

### 1.2 Contrato editorial (fixo para toda entrega)

| Item | Regra |
|---|---|
| Saídas | **Sempre duas**: `.md` (versionamento — inegociável) e `.docx` (produto de leitura) |
| "Guia de fontes" | **Removido do produto final.** O resumo automático de fontes não aparece no texto revisado; fica apenas nos artefatos de análise |
| Anúncios e trechos promocionais | **Preservados no corpo**, íntegros, marcados com `[ANÚNCIO]` na primeira linha do trecho |
| Diarização | **Opção B** — rótulos inferidos explícitos: `[APRESENTADOR]`, `[JAN VAL ELLAM]`, `[CONVIDADO]` |
| Disfluência | **Nível LEVE** — remover repetições imediatas e vícios ("né", "eh", "uhum"); **preservar sintaxe e identidade oral** |
| Busca externa | **Autorizada somente para a camada Externos** (§5), sempre registrando fonte e data |
| Números e datas | Nunca alterar o que foi dito; divergência verificada vai em `[NOTA]` e para o produtor (§7) |

### 1.3 Produtos de uma revisão completa
1. `transcricoes/<slug>/10-diagnostico/diagnostico.md` + `.json` — radiografia automática.
2. `transcricoes/<slug>/10-diagnostico/variantes-propostas.csv` — fila de decisão.
3. `transcricoes/<slug>/10-diagnostico/ausentes-da-base.csv` — candidatos a novo registro na KB.
4. `transcricoes/<slug>/20-blocos/bloco-NN.md` — os oito blocos revisados (fonte versionável).
5. `<Título> (revisado).docx` — produto de leitura, montado por script.
6. `transcricoes/<slug>/40-devolucao/devolucao-a-kb.md` — achados que a revisão devolve à base (§15).

---

## 2. Fonte de verdade: KB-RC

### 2.1 Estrutura

| Arquivo | Conteúdo | Uso na revisão |
|---|---|---|
| `KB-RC/canonico.json` | 956 termos (formato canonico-1.1) + ≈1.900 relações tipadas | nome canônico, categoria, status, confiança, fontes, relacionados |
| `KB-RC/biblio.json` | 105 obras: 97 códigos B (B001–B098, **falta B095**), 3 ART, 1 PER, 1 EXT, 2 P, **1 Y** (§2.5) | grafia de títulos, datas, ISBN, tipo de obra |
| `KB-RC/termos/*.md` | **830 fichas** com prosa curatorial | definição, contexto, etimologia e grafias, citações-chave, Quarentena |
| `docs/legado/2026-09-base-terminologica.xlsx` | retrato legado (abas Como usar, Índice Mestre, Fichas, Categorias, Bibliografia, Relações, Status) | conferência histórica; **não decide** |

**126 termos do `canonico.json` não têm ficha.** Para eles só se aplica o nome canônico; não há variantes documentadas.

### 2.2 Anatomia da ficha

```
+++                                            <- frontmatter curatorial
codigo = "RC-037"
nome = "Brahma (Brajna)"
categoria = "Seres & Entidades"
subcategoria = "1.1 Divindades / Criadores"
status = "verificado"
fontes = ["B031", "B024", ...]
via = "P6-evidência"
confianca_fonte = "alta"
atualizado = "2026-09-13"
+++
# Brahma (Brajna) — RC-037
> REMISSIVA — ...                              <- quando aplicável
## Definição Sintética
## Contexto / Origem
## Etimologia e Grafias                        <- 406 fichas; 338 com grafia preferida
## Citações-chave                              <- transcrições literais, com data e fonte
## Termos Relacionados
## Ampliação / Atualização por fonte
## Observações
## Quarentena Terminológica                    <- RC-826 a RC-833
## Cautela editorial / Glossário interno
```

**O que cada campo autoriza:**

| Campo | Autoriza |
|---|---|
| `nome` | a forma que vai para o texto |
| `Variações de STT` / `Etimologia e Grafias` | substituição direta da variante pelo canônico |
| `Variações` (sem "de STT") | **nada**: é equivalência conceitual (§4.1, classe `variacao`) |
| `Quarentena Terminológica` | proibição absoluta (`NUNCA …`) |
| `Citações-chave` | conferência de sentido; **não** é dicionário de grafias |
| `REMISSIVA` no cabeçalho | ignorar o verbete e usar o código apontado |

### 2.3 Status e confiança

| Status | O que fazer |
|---|---|
| 🟢 verificado | aplicar sem ressalva |
| 🟠 em análise | aplicar e marcar `[A CONFIRMAR]` na primeira ocorrência do bloco |
| 🔵 candidato / provisório | aplicar apenas com contexto inequívoco; senão, manter a forma dita + `[NOTA]` |
| 🔴 quarentena / cautela editorial | não aplicar: registrar e consultar o curador |

| `confianca_fonte` | O que fazer |
|---|---|
| alta | substituir |
| média | substituir e citar o código na nota de trabalho |
| baixa | **não substituir automaticamente**; decidir por contexto e registrar |

### 2.4 Quarentena Terminológica (norma vigente)

Regras `NUNCA` declaradas pelo curador nas fichas RC-826 a RC-833 (varredura de 31/08/2026 corrigiu 158 ocorrências na própria KB):

- **Sophia** — NUNCA "Sofia"
- **Yel Luzbel** — NUNCA "Luzbel" sozinho, NUNCA "Yosbel"
- **Brahma** — NUNCA "Brama"
- **Aya / Aye** — NUNCA "Aia" / "Aie"

Grafias canônicas confirmadas por RC-836/RC-837: **Awayen, Brahma, Javé, Vishnu, Shiva, Projeto Talm, Val Tam**.

A Quarentena tem precedência sobre qualquer outra regra deste Guia.

### 2.5 Fontes audiovisuais — padrão Y (aprovado em 16/09/2026)

A base nasceu de livros (B###) e palestras (P####-MM-DD). Transcrição de YouTube não é nenhuma das
duas coisas, e citar uma fonte que não existe envenena a base — por isso o **padrão Y**, aprovado
pelo Comandante em despacho de 16/09/2026.

**Código:** `Y` + data da transmissão ao vivo (ou da publicação, se não for live) — `Y2026-09-14`.
O código é da **fonte**, não do vídeo: se o mesmo conteúdo reaparecer em outro canal, é outra fonte.

**Campos obrigatórios no registro de `biblio.json`:**

| Campo | Conteúdo |
|---|---|
| `codigo`, `titulo`, `subtitulo`, `editora`, `ano`, `status`, `nota` | os sete campos de sempre — `editora` recebe o canal, `status` usa o vocabulário existente (`trabalhada` quando a transcrição já foi revisada e devolvida) |
| `tipo` | `audiovisual-youtube` |
| `url` | o link. **Sem URL não há registro**: link é a única mídia que este repositório guarda (Plano §7) |
| `canal`, `data_publicacao`, `data_upload` | o canal e as duas datas — publicação e upload costumam diferir |
| `duracao`, `duracao_min` | conferidas na plataforma, não estimadas |
| `forma_captura` | como o texto foi obtido (`youtube-autosub`, `whisper`, legenda oficial…) |
| `confiabilidade` | em geral `média — STT`; sobe a `alta` com legenda oficial ou conferência contra o áudio |
| `slug` | onde a transcrição vive no repositório |
| `midia_arquivada` | `false` — e assim continua; vídeo jamais entra no Git comum |
| `consultado_em` | data da última conferência do link |

**Consequências para a revisão:**

- termo novo nascido de fonte Y entra como **provisório** ou **candidato**, nunca como verificado:
  uma única fonte audiovisual, sem pontuação e com nomes próprios instáveis não sustenta promoção.
  A promoção vem com obra primária ou segunda fonte;
- `confianca_fonte` de fonte Y é **média** (§2.3: substituir e citar o código na nota de trabalho);
- a ficha registra em `## Fontes` o código Y e, em `## Observações`, o bloco da transcrição onde o
  termo aparece — o ponteiro para a evidência é o slug + bloco, não a minutagem do vídeo;
- o mesmo URL vai em três lugares, que precisam concordar: `biblio.json`, `00-fonte/metadados.yaml`
  e `00-fonte/midia/README.md`;
- **a conferência é automática desde 16/09/2026**: `rc_indice.py --checar` (passo do CI) recusa o
  catálogo de transcrição que, a partir de `30-produto`, não tenha URL, ou cuja URL não esteja em
  `biblio.json` como fonte Y — e confere no sentido inverso (o `slug` do registro Y tem de apontar
  para a pasta). Antes de `30-produto` é aviso, não erro: pasta recém-criada não pode nascer
  reprovada, pela mesma razão que os portões têm o estado `N/A`.

**Primeira fonte Y:** `Y2026-09-14` — *ASSISTA ANTES QUE SAIA DO AR - Jan Val Ellam*, canal
PARANORMAL EXPERIENCE, 2:25:50, slug `2026-09-14-revelacoes-cosmicas-urgente`. Originou o lote 02
de curadoria: 10 termos novos (RC-947 a RC-956).

---

### 2.6 Camadas de texto — bruto, derivado e saída (norma de 16/09/2026)

Uma pasta de transcrição guarda **até três textos**. Confundir as camadas é o erro mais caro deste
fluxo: o que a casa assina é a saída, mas o único irrefutável é o bruto.

| camada | arquivo canônico | natureza | portão |
|---|---|---|---|
| fonte | `00-fonte/transcricao-bruta.txt` | saída do STT, **imutável** | G1 (sha256) |
| trabalho | `00-fonte/transcricao-pontuada.txt` | **derivado** de outra ferramenta (NotebookLM e afins) | G9 |
| saída | `20-blocos/bloco-NN.md` + `30-produto/*.docx` | texto revisado, assinado | G2, G3, G5, G6 |

Regras:

1. **Derivado nunca vira fonte.** Ele é conveniência de trabalho — pontuação nativa, segmentação por
   turno, menos lacunas. Se o derivado se perde, o que sobrevive é o bruto; por isso o bruto é
   imutável e o derivado é **medido**.
2. **Registro obrigatório** em `00-fonte/metadados.yaml`, bloco `derivado:`: `arquivo`,
   `ferramenta`, `sha256`, `divergencia_maxima` (teto padrão `0.05`) e `palavras_mascaradas`
   (lista de `mascara` → `restaurar_para`). Sem registro o G9 responde `N/A` e a camada não existe
   oficialmente — não é derivado, é arquivo solto.
3. **Teto de divergência.** O G9 mede divergência lexical derivado × bruto (palavras do bruto
   ausentes **+** palavras a mais, sobre o total das duas contagens). Acima do teto aquilo não é
   reescrita do mesmo áudio, é outro texto: a revisão volta ao bruto. Referência medida nesta
   transcrição: **3,00%** (18.806 × 18.815 palavras), com 93% dos *hapax* comuns e 9 de 16
   marcadores orais em contagem idêntica — é o mesmo ASR do YouTube sob uma camada de reescrita, não
   um segundo motor (ver `docs/pareceres/parecer-motor-stt.md`).
4. **Palavra mascarada se restaura do bruto, e o asterisco nunca chega à saída.** Camadas de
   segurança de terceiros mascaram vocabulário (`merda` → `m****`, `bandido` → `b******`), inclusive
   em trecho teológico ("os europeus viam Jesus como um b******"). O revisor confere cada máscara no
   bruto, escreve a palavra real no bloco e registra o par no `metadados.yaml`. O G9 localiza as
   máscaras **pelo contexto no bruto** — não por comprimento+inicial, que dá falso positivo — e
   falha nos quatro modos de estragar: derivado trocado (sha256), divergência acima do teto, palavra
   não restaurada, asterisco no texto revisado, máscara sem registro.
5. **Onde começa o corpo** tem uma resposta só, em `ferramentas/rc_leitura.py`: (i) marcador
   `Transcrição Automática` → corpo é o que vem depois dele; (ii) sem marcador, a linha mais longa,
   se cobrir ≥ 80% dos caracteres do arquivo; (iii) nada disso, o arquivo inteiro **com aviso**
   gravado em `metadados.yaml` (`aviso_corpo`, `criterio_corpo`). Arquivo paragraphado não é mais
   medido como se o corpo fosse o parágrafo mais longo — nesse erro silencioso o derivado desta
   transcrição teria 771 palavras em vez de 18.815, com o QA verde.
6. **Duas réguas de contagem coexistem** e nenhuma está errada: `rc_leitura` conta palavras por
   `PALAVRA_RE` (`[\wÀ-ÿ']+`, que separa em hífen e barra) e é a régua do `metadados.yaml`
   (18.806 no bruto); `rc_diagnostico` conta por `split()` (18.781 no mesmo corpo). A divergência do
   item 3 é imune a isso porque compara bruto e derivado **com a mesma régua**. Qualquer número
   citado em relatório deve dizer de qual instrumento veio.
7. Nomes ASCII, sem espaço e sem acento (Plano de Organização). O cabeçalho do vídeo (título, canal,
   URL) fica **fora** do corpo e fora do produto (§1.2).
8. **Texto obtido por *fetch* de página não é camada nenhuma: não é fonte** (norma de 16/09/2026,
   nascida do vídeo 2). O transcript do painel do YouTube lido por `fetch_page` em
   `v0gJWn50gg8` foi conferido contra o bruto oficial entregue depois: 1,22% de divergência lexical,
   mas **pontuado** (144 vírgulas contra zero do bruto), **capitalizado**, com **anotações de áudio
   que o bruto não tem** (`[roncando]`, `[limpando a garganta]`) e ao menos **uma palavra corrompida**
   ("ovo cósmico" → "novo cósmico"). É um derivado de fidelidade desconhecida e não verificável.
   Serve para **identificar** o vídeo (título, canal, duração, descrição, data); **nunca** para
   instalar bruto, atestar variante STT, propor termo nem medir motor. Se o bruto não existe, ele não
   existe: a fila de curadoria fica bloqueada (§15) e a pasta espera o arquivo — que chega por
   `upload/` (via A, B ou D do `upload/README.md`) ou por commit do Comandante. O que o *fetch*
   devolveu fica em `docs/pareceres/` como **evidência do defeito da rota**, com sha256, e é citado
   como tal.

---

## 3. As cinco camadas de correção (ordem de aplicação)

Aplicar nesta ordem. Camada posterior não desfaz camada anterior.

| Camada | O quê | Instrumento | Quem decide |
|---|---|---|---|
| 1 | **Terminologia canônica KB-RC** (nomes, conceitos, obras) | `canonico.json` + fichas + Quarentena | regra + revisor |
| 2 | **Variantes STT documentadas** (Brama→Brahma, Yahé→Javé) | `ferramentas/dados/variantes-kb-extraidas.csv` (1.590 pares; 299 regras de substituição) | revisor, com contexto |
| 3 | **Externos** (autores, obras, empresas, pessoas do mundo real) | `ferramentas/dados/externos.csv` (41 entidades) — busca externa autorizada | revisor, com fonte e data |
| 4 | **Números, datas e valores** | §7 — nunca alterar o dito | produtor |
| 5 | **Ortografia, pontuação, segmentação e disfluência** | §6, §8, §10 | revisor |

---

## 4. Regras de substituição terminológica

### 4.1 Classes de variante (o que a KB realmente documenta)

O extrator `rc_variantes.py` lê a prosa das 820 fichas e classifica cada par variante→canônico. **A classe determina a ação** — este é o ponto mais importante do Guia v2.

| Classe | O que é | Ocorrências extraídas | Ação |
|---|---|---|---|
| `nunca` | proibição da Quarentena (`NUNCA "Brama"`) | 6 | **substituir sempre** (texto editorial) |
| `deprecada` | termo registrado como erro histórico com remissão (RC-497 Impérial → Perpérion RC-087; RC-500 Almaior/Alamaior → Forno de Awaymaion RC-499) | — | substituir e citar o código canônico |
| `stt` | campo "Variações de STT" da ficha (ex.: RC-087 documenta *Perpério, Perfério, Perpéria, Perpérian*) | 621 | substituir quando o contexto for o termo |
| `stt_contextual` | padrão `X (STT «y»)` na prosa: o alvo é o nome imediatamente anterior | 134 | substituir com confirmação contextual |
| `stt_mapeado` | mapeamento explícito "y = X" na prosa | 42 | substituir |
| `corruptela` | forma corrompida apontada pelo curador | 7 | substituir com confirmação contextual |
| `oral` | forma falada aceita | 2 | manter; não "corrigir" |
| `variacao` | **equivalência conceitual** (ex.: Javé como variação de Criador) | **778** | **NUNCA substituir** |
| (marcação) `referencia_oral` | alvo longo (>4 palavras) = título de conceito, não grafia (ex.: "Eva" → *Sequência Formativa da Racionalidade Humana*) | 613 | reconhecer, não trocar |

Duas marcações de risco atravessam todas as classes:

- **`risco_palavra_comum = sim`** — a variante é palavra do português (ex.: *Tem* → Têmis; *a vista* → Avesta; *caos* → Javé como Caos Personificado). Só se aplica com contexto inequívoco.
- **homografia** — a variante é canônica de outro termo (ex.: *Olm* é RC-252 e aparece na glossa de RC-092; *Cristo* é figura cristã e variante STT de Krishna RC-414). O motor **suspende** e o revisor decide.

### 4.2 Quando NUNCA substituir

1. **Classe `variacao`** (equivalência conceitual). Trocar "Criador" por "Javé" altera doutrina, não ortografia.
2. **Citação literal entre aspas** — preserva a forma STT (§4.5).
3. **Entidade da camada Externos** — "Nick" de Nick Bostrom nunca vira Nyx (RC-621).
4. **Forma do vocabulário comum** (`ferramentas/dados/vocabular-guarda-pt.txt`, 1.878 entradas) sem contexto inequívoco.
5. **Termo de status 🔴 ou confiança baixa** sem evidência adicional.
6. **Números, datas, valores e nomes de pessoas reais não confirmados** (§7, §5).
7. **Quando a decisão exigir conhecimento que o texto não dá** — marcar `[A CONFIRMAR]`, nunca chutar.

### 4.3 Registro formal de decisão (oito conflitos resolvidos)

Reproduz o §5 do Anexo I. É a tabela de bolso do revisor.

| Forma no texto | Forma canônica | Código | Classe | Ação |
|---|---|---|---|---|
| Asfezion, Asfésian, Fessien | **Asphezian** | RC-025 | grafia errada do Guia v1 | substituir + `[A CONFIRMAR]` (confiança baixa) |
| Brama | **Brahma** | RC-037 | `nunca` | substituir |
| Lemion, Lemon, Lemior, Nemon, Lémion, Demion | **Len Mion** | RC-074 | variante STT | substituir |
| radiato | **radiata / radiatas** | RC-631, RC-093 | variante STT | substituir |
| Jane Miranda, Jeanne Miranda | **Jeane Miranda** | ficha a criar (1.6) | nome próprio | substituir |
| elogismo | — | — | **regra descartada** | não substituir; `[A CONFIRMAR]` + áudio |
| Olm / Ohm | **decidir por contexto**: Olm (RC-252) ou Quarto Logos (RC-092) | RC-252/RC-092 | homografia | suspenso |
| duplicatas | usar o **canônico**: RC-898, RC-164, RC-115, RC-149, RC-581, RC-043, RC-314 | — | remissão | citar sempre o canônico |

Códigos invertidos no Guia v1 e agora corrigidos: **RC-092 = Quarto Logos**, **RC-252 = Olm** (a v1 dizia o contrário).

### 4.4 Casos de estudo desta transcrição

| Forma no texto | Proposta automática | Decisão correta | Por quê |
|---|---|---|---|
| "chamado **Brama** pelos arianos" (8×) | Brahma (RC-037) | **Brahma** | Quarentena: `NUNCA "Brama"` |
| "o ser a quem obedeciam era o **Yahé** ou Javé" | Javé (RC-001) | **Javé** | variante STT documentada; o texto já traz as duas formas |
| "esses seres **Brama Virgin Chiva**" | Virgin → RC-104 | **Brahma, Vishnu, Shiva** | a tríade é a glossa de RC-781; "Virgin" = Vishnu |
| "Krishna tomou a devoção da Índia **para Brama**" | Ishvara (RC-691, via "para Bragna") | **para Brahma** | RC-691 documenta "para Bragna" = Para Brajna; aqui o dativo é de Brahma. O motor propõe, o revisor decide |
| "se você pagar **a vista**" | Avesta (RC-595) | **à vista** | português comum; a KB documenta "a vesta" como STT de Avesta |
| "**Nick** Bostron no seu livro Utopia Profunda" | Nyx (RC-621) | **Nick Bostrom**, *Deep Utopia* (2024) | camada Externos; confirmado em Wikipedia/Bertrand (16/09/2026) |
| "meu querido **Sherminetro**" | Terminator | **[A CONFIRMAR]** | contexto mostra apelido do apresentador, não o filme |
| "**choques de realidade**" (2×) | Choque de Realidade (RC-867/RC-898) | decidir: conceito nomeado ou plural genérico | RC-898 é o canônico; RC-867/RC-936 são paralelo/remissiva |
| "**cristão**", "**cristã**", "o **Cristo**" | Krishna (RC-414) | **manter** | homografia suspensa; Krishna só se o contexto for o avatar hindu |

### 4.5 Citação literal preserva a forma STT

A própria KB grafa "Brama", "Sofia" e "Lemion" **dentro de aspas**, porque reproduz a fala bruta (RC-074 usa "Len Mion" 35× e "Lemion" 24×). Regra:

- **Texto editorial** (o que o revisor escreve): forma canônica, sempre.
- **Citação literal** (entre aspas, com data e fonte): forma tal como foi dita; a corruptela pode ser sinalizada com `[sic]` quando induzir erro de leitura.
- **Título curatorial de citação** (o cabeçalho que o curador escreve acima da citação): forma canônica.

---

## 5. Camada Externos (autores, obras, empresas e pessoas do mundo real)

**Única camada com busca externa autorizada.** Toda entrada registra **fonte e data**.

Arquivo: `ferramentas/dados/externos.csv` — colunas `variante,canonico,codigo_base,tipo,origem,observacao,status_aprovacao`.

Regras:

1. Entidade externa **protege** a forma: ela nunca vira variante de termo interno (o motor suspende a colisão).
2. `status_aprovacao = a confirmar` exige validação com o produtor antes de qualquer alteração no texto.
3. Divergência factual (ano, cargo, autoria) **não se corrige no corpo**: vai em `[NOTA]` e para o produtor (§7).
4. Estrangeirismo mantém grafia original, em itálico no .docx (*Deep Utopia*, *Dark Enlightenment*).

Entradas já validadas nesta transcrição (consulta de 16/09/2026):

| Forma no texto | Canônico | Fonte registrada |
|---|---|---|
| Raymond Kzwell, Raymond Kurzweil | **Ray Kurzweil** | Wikipedia: *The Singularity Is Near* |
| "livro a Singularidade… em 2007" | ***The Singularity Is Near*** (2005) | Wikipedia/Penguin — **ano divergente: 2005, não 2007** |
| Nick Bostron | **Nick Bostrom** | Wikipedia: Nick Bostrom |
| Dark Utopia / Utopia Profunda | ***Deep Utopia: Life and Meaning in a Solved World*** (Ideapress, maio/2024, ISBN 9781646871643) | Bertrand.pt / Wikipedia |
| Terry Fabris | **Terry Fabris** (grafia confirmada) | YouTube: *LEMÚRIA ESTÁ em busca URGENTE DE CONTATO – Terry Fabris* (upload 24/08/2026) — o mesmo vídeo anuncia o evento presencial com Robson Pinheiro, 3 de outubro, ingresso R$ 180 ou 12× R$ 18,60 |
| Manuel Kant, Emanuel Kant | **Immanuel Kant** | conhecimento geral do revisor |
| Goethe, Faust, Mephistopheles | **Goethe**, *Fausto*, **Mefistófeles** | conhecimento geral do revisor |
| Agostinho | **Agostinho de Hipona** (*credo ut intelligam*) | conhecimento geral do revisor |
| Gordon Moore / "lei de Gordon Moore" | **Gordon Moore** / **Lei de Moore** | conhecimento geral — a live diz "dono da Intel"; correto é cofundador |
| Sherminetro | **[A CONFIRMAR]** — apelido do apresentador | transcrição (contexto) |
| Tati Quântica, Paranormal Experience, Siddhartha/Sidarta Galutama | a confirmar | produtor / contexto (**Sidarta Galutama** = Siddhartha Gautama) |

---

## 6. Ortografia e gramática pt-BR

1. **Maiúscula inicial** em nomes próprios e em conceitos canônicos registrados como tal na KB (*Choque de Realidade*, *Ato de Verdade*, *Nova Espiritualidade*). Conceito usado genericamente fica em minúscula ("um choque de realidade entre os dois").
2. **Hífen** conforme o registro canônico: *Criaturas-ferramenta* (RC-164), *Yel Luzbel* **sem** hífen (Guia v1 §5.1).
3. **Crase**: obrigatória em "à vista", "à medida que", "às vezes"; proibida antes de masculino, verbo e pronome.
4. **Estrangeirismo** em itálico no .docx; sem itálico no .md (usar \`código\` apenas para formas técnicas).
5. **Diacríticos**: o STT desta casa preserva acentos (perda medida: 8 em 402 "não", 3 em 205 "você"). Ainda assim, conferir *só/sô*, *já/já*, *até/ate* em homógrafos.
6. **Números por extenso** até dez, exceto datas, valores e medidas.
7. **Não inventar** acento, hífen ou maiúscula em termo da KB sem registro: na dúvida, `[A CONFIRMAR]`.

---

## 7. Números, datas e valores

Regra de ouro: **o revisor não corrige o que o autor disse; ele reporta.**

| Situação | Procedimento |
|---|---|
| Número ininteligível no STT ("10,18") | buscar o valor real na fonte externa (camada 3) e marcar `[NOTA: o anúncio oficial do evento indica 12× de R$ 18,60; no áudio, "dez, dezoito"]` |
| Divergência factual verificada (Kurzweil: 2005, não 2007) | manter o dito no corpo + `[NOTA]` + item na devolução ao produtor |
| Data de palestra/obra | conferir com `biblio.json` (97 B-codes + 2 P) |
| Valor monetário de anúncio | preservar exatamente como anunciado (§11) |
| Numeral ordinal/capítulo | conferir com a ficha da obra |

Nenhum número é alterado sem fonte registrada.

---

## 8. Pontuação e segmentação

> **Atualizado em 16/09/2026.** Havendo **derivado pontuado** (§2.6), pontuação e segmentação vêm
> prontas dele e esta seção deixa de ser *criação* para ser **conferência**: o padrão passa a ser
> aceitar a pontuação nativa e intervir só com motivo. Sem derivado, as regras abaixo continuam
> sendo o trabalho manual, na íntegra. Foi essa a razão da adoção do texto pontuado como camada de
> trabalho: mediana de sentença 331 → 11 palavras, maior sentença 2.604 → 75, segmentos 8 → 295
> (295 são as linhas não vazias do arquivo inteiro, cabeçalho incluído — a régua do `rc_perfil_stt`;
> só o corpo são 287, pela do `rc_leitura`).

O bruto desta transcrição: **18.806 palavras em 1 parágrafo, com 1 vírgula e 15 pontos** (71 dois-pontos, 117 aspas) — régua do `rc_leitura`; o `rc_diagnostico` reporta 18.781 na sua régua própria (§2.6, item 6). Sem derivado, a segmentação é a maior parte do trabalho.

1. **Parágrafo novo** a cada mudança de assunto, de interlocutor ou de movimento argumentativo.
2. **Vírgula** em: aposto, vocativo, oração intercalada, adjunto deslocado, enumeração. Não separar sujeito de verbo.
3. **Dois-pontos** preservados quando introduzem citação ou enumeração do autor.
4. **Aspas** para citação literal (§4.5) e para o que o autor põe entre aspas ("os que estão entre aspas morrendo").
5. **Ponto de interrogação/interrogação retórica** apenas quando a entonação do áudio confirmar; senão, ponto final.
6. **Não criar** travessão de diálogo: a diarização usa rótulos (§9).
7. Frases de mais de ~60 palavras podem ser divididas **somente** onde já há conjunção coordenativa; nunca reescrever a ordem.
8. **Nenhuma intervenção de pontuação pode alterar palavra** (com derivado). Pontuar é o trabalho; reescrever é censura — foi assim que a camada de reescrita zerou a variante RC-954 ("expiação **e** provas" → "**em** provas") e trocou "calmeias" por "colmeias" em 1 de 2 ocorrências. Palavra que muda sem registro é o que o G9 chama de divergência, e ela tem teto (§2.6, item 3).
9. A métrica de aceite da **saída** continua valendo: ≥ 1 vírgula a cada 25 palavras, medida no produto revisado (§14), nunca no bruto.

---

## 9. Diarização — opção B (rótulos inferidos explícitos)

> **Atualizado em 16/09/2026.** O derivado pontuado já **segmenta por turno de fala** (287
> segmentos de corpo contra 1 parágrafo no bruto), então a diarização deixa de exigir que o revisor descubra onde
> começa cada fala: a fronteira vem dada. O que continua sendo trabalho da casa é **nomear** o
> falante, por inferência — o derivado não sabe quem é quem. A forma do rótulo também mudou,
> conforme despacho do Comandante: **negrito inline no início do parágrafo do turno**, e não mais
> caixa alta em linha própria. O desvio praticado nos blocos 01–08 desta transcrição fica assim
> incorporado à norma.

Forma vigente:

```
**[GURU DE MALÁ]** Então você acha que a gente tá vivendo um choque de realidade?

**[JAN VAL ELLAM]** Tá. E não é de hoje.
```

Forma anterior (aceita em material já publicado, não usar em revisão nova):

```
[APRESENTADOR] Então você acha que a gente tá vivendo um choque de realidade?

[JAN VAL ELLAM] Tá. E não é de hoje.
```

Regras:

1. Rótulo em **negrito inline**, entre colchetes, no início do parágrafo do turno — um parágrafo por turno, mesmo que a fala seja curta. Nomes de falantes desta transcrição, conforme despacho: `[GURU DE MALÁ]`, `[ALEXANDRE SHERMINATOR]`, `[JAN VAL ELLAM]`.
2. Inferência por: vocativo ("meu querido"), tema (doutrina = Jan), papel (pergunta = apresentador), mudança de estilo.
3. **Inferência duvidosa** → `[FALANTE?]` antes do rótulo.
4. Trecho sem identificação possível → `[SEM DIARIZAÇÃO]`.
5. Rótulos não entram no texto falado: são metadados de leitura — por isso vão em negrito, fora do corpo da frase, e por isso o G2 não os confunde com conteúdo.
6. Convidados nomeados: `[TERRY FABRIS]`, `[ROBSON PINHEIRO]` — grafia conforme camada Externos.
7. A segmentação herdada do derivado é **conferida**, não aceita às cegas: a mesma camada que acerta o turno também suprimiu "full megante" e trocou "cabeça" por "cadecia". Fronteira de turno duvidosa se resolve ouvindo; lacuna `[INAUDÍVEL]` é decisão editorial do revisor (§12), não do derivado.

---

## 10. Disfluência — nível LEVE

| Remover | Preservar |
|---|---|
| repetição imediata ("apresenta apresenta", 115 ocorrências de palavras repetidas consecutivamente) | repetição enfática deliberada ("não morre, não morre mesmo") |
| "né" (49×), "eh" (45×), "uhum" (31×) isolados | "né" com função de pergunta real no fim de frase dirigida ao interlocutor |
| falso início abandonado ("eu… eu vou") | hesitação que carrega sentido ("é… difícil dizer") |
| "tipo" (25×) e "sabe" (17×) como muleta | "tipo" com sentido lexical ("um tipo de cérebro") |
| marcador de backchannel do ouvinte no meio da fala do autor | resposta curta do interlocutor em turno próprio |

**Proibido:** reordenar palavras, trocar conectivo, "melhorar" a frase, converter oralidade em norma escrita. A sintaxe oral é identidade do autor. "Aí", "então" (132×), "cara" (26×) e "tá" (87×) permanecem.

---

## 11. Anúncios e trechos promocionais

**Preservar no corpo, integralmente** — incluindo valores, condições, datas, cupons e chamadas de ação. Tratamento:

1. `[ANÚNCIO]` na primeira linha do trecho.
2. Números e valores conferidos com a fonte oficial quando disponível (camada 3) — divergência vai em `[NOTA]`, nunca em substituição silenciosa.
3. Nome de produto/canal/empresa segue a grafia da camada Externos.
4. Nenhum anúncio é resumido, encurtado ou movido para apêndice.

Exemplo real deste material: evento presencial de 3 de outubro com Robson Pinheiro e Terry Fabris, ingresso anunciado como "R$ 180 ou 12× de R$ 18,60" na fonte oficial, dito no áudio como "dez… dezoito" — manter o dito + `[NOTA]` com o valor oficial e a fonte.

---

## 12. Marcadores editoriais

| Marcador | Uso | Obrigatório quando |
|---|---|---|
| `[NOTA: …]` | esclarecimento do revisor, divergência factual, referência cruzada | número/data divergente; termo de confiança baixa |
| `[A CONFIRMAR]` | forma não confirmada na KB nem em fonte externa | entidade externa não validada; termo 🔵/🟠 |
| `[INAUDÍVEL]` | trecho ininteligível no áudio | nunca inventar palavra |
| `[sic]` | forma incorreta preservada dentro de citação literal | citação que pode induzir erro |
| `[ANÚNCIO]` | abertura de trecho promocional | sempre |
| `[FALANTE?]`, `[SEM DIARIZAÇÃO]` | diarização incerta | §9 |
| `[APRESENTADOR]`, `[JAN VAL ELLAM]` | turnos de fala | §9 |

Marcadores saem em itálico no .docx (o `rc_docx.py` já faz isso).

---

## 13. Fluxo de trabalho em 8 blocos

### 13.1 Preparação (uma vez por transcrição)

```bash
# ambiente
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -r ferramentas/requirements.txt

# 1) extrair as relações variante -> canônico da prosa das fichas
python ferramentas/rc_variantes.py --kb KB-RC --transcricao "<Título>.txt"

# 2) diagnóstico com a KB-RC como fonte de verdade
#    SEM --saida: a ferramenta descobre sozinha transcricoes/<slug>/10-diagnostico/ a partir do
#    caminho do bruto. Passar --saida "transcricoes/<slug>" joga os arquivos na raiz da pasta e
#    deixa diagnostico.json fora do padrão do .gitignore (135 KB regeneráveis versionados).
python ferramentas/rc_diagnostico.py transcricoes/<slug>/00-fonte/transcricao-bruta.txt --kb KB-RC
```

Saídas usadas no dia a dia: `diagnostico.md` (leitura), `variantes-propostas.csv` (fila de decisão), `ausentes-da-base.csv` (novos registros), `dossie-bloco.txt` (recorte enxuto da base, ≈1.153 tokens).

Havendo **derivado** (§2.6) — texto pontuado de outra ferramenta, por exemplo:

```bash
# 3) colocar o derivado no lugar certo e registrá-lo: ele mora em 00-fonte/, nunca na raiz
git mv Opcao-B.txt transcricoes/<slug>/00-fonte/transcricao-pontuada.txt
sha256sum transcricoes/<slug>/00-fonte/transcricao-pontuada.txt   # -> derivado.sha256 no metadados.yaml

# 4) conferir a camada de trabalho ANTES de revisar uma linha sequer
python ferramentas/rc_qa.py transcricoes/<slug> --portao G9
```

O G9 na preparação responde três perguntas de uma vez: o derivado é o arquivo registrado (sha256),
ele é o mesmo áudio (divergência ≤ teto) e o que ele mascarou está mapeado. Rodar isso depois de
revisar oito blocos custa caro; rodar antes custa dez segundos. As máscaras que o G9 listar vão para
`derivado.palavras_mascaradas` no `metadados.yaml` com a palavra do bruto ao lado — é a lista de
Find&Replace que deixa de ser manual.

### 13.2 Divisão em 8 blocos

Dividir por **fronteiras de assunto**, não por contagem fixa de palavras: cada bloco deve começar e terminar num ponto de virada temática. Para 18.781 palavras, isso dá blocos de ~2.350 palavras (≈16 minutos de áudio cada).

### 13.3 Rotina por bloco (repetir 8×)

1. Ler o bloco inteiro sem editar (compreensão).
2. Ouvir/conferir os trechos marcados `[INAUDÍVEL]` e `[A CONFIRMAR]`.
3. Aplicar as camadas na ordem do §3.
4. Adjudicar cada linha da fila `variantes-propostas.csv` que caia no bloco: **aceitar / recusar / decidir por contexto**, registrando o motivo.
5. Segmentar parágrafos e pontuar (§8); diarizar (§9); podar disfluência leve (§10). Com derivado (§2.6), os três já vêm prontos: conferem-se, restaurando do bruto toda palavra mascarada que cair no bloco.
6. Marcar anúncios (§11) e inserir marcadores (§12).
7. Gravar `transcricoes/<slug>/20-blocos/bloco-NN.md`.
8. Revisão de fechamento do bloco: ler em voz alta; nada de termo canônico sem conferência na ficha.

### 13.4 Montagem final

```bash
python ferramentas/rc_docx.py transcricoes/<slug>/20-blocos/*.md \
    --lexico transcricoes/<slug>/10-diagnostico/dossie-bloco.txt \
    --saida "<Título> (revisado).docx" \
    --titulo "<Título>" \
    --subtitulo "Transcrição revisada — padronização terminológica conforme as Revelações Cósmicas" \
    --validar transcricoes/<slug>/10-diagnostico/variantes-propostas.csv
python ferramentas/md_para_docx.py transcricoes/<slug>/40-devolucao/devolucao-a-kb.md --saida transcricoes/<slug>/40-devolucao/devolucao-a-kb.docx
```

O `--lexico` aplica negrito na **primeira menção** de cada termo canônico; `--validar` confere se alguma forma proibida sobreviveu no produto final.

---

## 14. Controle de qualidade e métricas de aceite

| Verificação | Meta | Como medir |
|---|---|---|
| Forma proibida da Quarentena no produto final | **0** | `--validar` do `rc_docx.py`; `grep -c "Brama\|Sofia\|Yosbel\|Aia\|Aie"` |
| Variantes STT de alta confiança não resolvidas | **0** | `variantes-propostas.csv` sem linhas `status_aprovacao=proposta` pendentes |
| Termo 🔵/provisório aplicado sem `[A CONFIRMAR]` | **0** | varredura dos marcadores |
| Entidade externa alterada sem fonte+data | **0** | auditoria de `externos.csv` |
| Número/data alterado no corpo | **0** | diff contra o bruto: nenhuma linha numérica muda sem `[NOTA]` |
| Anúncio resumido ou removido | **0** | conferência §11 |
| Repetição imediata remanescente | ≤ 5 em todo o texto | métrica `palavras_repetidas_consecutivas` (bruto: 115) |
| Parágrafos | ≥ 120 (bruto: 1) | métrica `paragrafos` |
| Virgulas/pontos proporcionais | ≥ 1 vírgula a cada 25 palavras | métrica `pontuacao` |
| Dossiê por bloco | ≤ 2.000 tokens | `dossie-bloco.txt` |
| Divergência lexical derivado × bruto | ≤ `derivado.divergencia_maxima` (padrão 0,05) | portão **G9** |
| Palavra mascarada no derivado sem restauração | **0** | portão **G9** |
| Asterisco de censura na saída (`20-blocos/`, `30-produto/`) | **0** | portão **G9**; `grep -c '\*\*\*\*'` |
| Derivado sem sha256 registrado | **0** | portão **G9** |

**Precisão esperada dos instrumentos** (medida nesta transcrição): camada de sementes/Quarentena ≈ 100% após as 11 suspensões automáticas; fila fuzzy ≈ 40% — **ela é triagem de recall, nunca decisão**. Subir o corte de similaridade destrói recall (0,85 → 11 propostas e só 4 das 10 variantes-chave; 0,90 → 4 propostas e 2 de 10), por isso o padrão permanece 0,75–0,80 com adjudicação humana obrigatória.

---

## 15. Governança: devolução à KB-RC

Toda revisão produz `transcricoes/<slug>/40-devolucao/devolucao-a-kb.md`, com quatro seções:

1. **Novos termos propostos** — formas do texto ausentes da base (145 nesta transcrição), com contexto, código sugerido, categoria e confiança.
2. **Novas variantes STT** — corruptelas observadas que a KB ainda não documenta, com a citação literal e a data da fonte.
3. **Correções na KB** — fichas com erro, cross-ref quebrada, nome violando a Quarentena, campo faltante.
4. **Novos registros bibliográficos** — obras, programas e canais citados (ex.: *Valores Supremos da Consciência*, programa de YouTube do autor, ausente de `biblio.json`).

Regras de governança:

- Nenhuma alteração na KB é feita pelo revisor: **propõe-se, o curador aplica**.
- Toda proposta cita evidência (arquivo, linha, data, fonte).
- Duplicata nova segue o padrão já usado: cabeçalho `REMISSIVA` + indicação do canônico (como RC-449 → RC-164, F045-MERGE de 07/09/2026).
- Termo deprecado segue o padrão RC-497/RC-500: nome com "— erro histórico de STT (ver …)".
- Variante STT documentada no padrão RC-087: `Variações de STT: Perpério, Perfério, Perpéria, Perpérian`.
- Proibição absoluta só entra via **Quarentena Terminológica** na ficha, com a forma `NUNCA "…"`.

---

## 16. Apêndice A — Ferramentas

| Script | Função | Saída |
|---|---|---|
| `ferramentas/rc_kb.py` | carrega `KB-RC` (camada 1): termos, fichas, relações, obras | objetos em memória |
| `ferramentas/rc_variantes.py` | extrai variante→canônico da **prosa** das fichas, classifica por classe e confiança de mapeamento | `variantes-kb-extraidas.csv` |
| `ferramentas/rc_lexicon.py` | normalização, chave fonética, índice de superfícies, sementes, dossiê | — |
| `ferramentas/rc_diagnostico.py` | varredura completa: exatas, sementes, fuzzy adjudicável, ausentes | `transcricoes/<slug>/*` |
| `ferramentas/rc_docx.py` | monta o .docx revisado (negrito de 1ª menção, validação) | `<Título> (revisado).docx` |
| `ferramentas/md_para_docx.py` | converte documentos de governança (.md → .docx) | `.docx` |
| `ferramentas/rc_qa.py` | os **nove** portões de qualidade, por transcrição ou `--tudo` | stdout, `--json` para o CI |
| `ferramentas/rc_leitura.py` | onde começa o corpo de um STT: critério único em cascata (§2.6, item 5), usado por `rc_novo`, `rc_indice` e `rc_qa` | dict de medição + aviso quando precisa chutar |
| `ferramentas/rc_indice.py` | catálogo das transcrições + fiscalização do padrão Y (§2.5) | `transcricoes/_indice.csv` e `.md` |
| `ferramentas/rc_novo.py` | cria a pasta de transcrição nova a partir de `transcricoes/_modelo/` | `transcricoes/<slug>/` |
| `ferramentas/rc_ledger.py` | livro-razão da adjudicação: pendências, decisões, sobrevivências | `10-diagnostico/variantes-propostas.csv` |
| `ferramentas/rc_curadoria.py` | aplica a fila: variante STT só entra se atestada no bruto | fichas + fila + `CHANGELOG.md` |
| `ferramentas/rc_termo.py` | cria termo novo a partir de especificação validada (§2.5) | ficha + `canonico.json` + fila + `CHANGELOG.md` |

Arquivos de controle: `ferramentas/dados/vocabular-guarda-pt.txt` (1.878 formas comuns), `ferramentas/dados/sementes-variantes-stt.csv`, `ferramentas/dados/externos.csv` (34 entidades), `ferramentas/dados/variantes-kb-extraidas.csv` (1.590 pares).

## 17. Apêndice B — Diagnóstico de referência desta transcrição

*Revelações Cósmicas Urgente – Jan Val Ellam*, executado em 16/09/2026 com `--kb KB-RC`:

- 18.781 palavras (régua `split()` do `rc_diagnostico`; 18.806 na régua `PALAVRA_RE` do `rc_leitura`, que é a gravada em `metadados.yaml` — §2.6, item 6) · 101.468 caracteres · 3.171 tipos lexicais · ≈125 minutos de áudio
- 1 parágrafo · 1 vírgula · 15 pontos · 71 dois-pontos · 117 aspas
- 115 palavras repetidas consecutivamente · marcadores orais: então 132, aí 123, tá 87, né 49, eh 45, uhum 31, cara 26
- 96 superfícies da base presentes · 783 candidatos brutos · 61 adjudicáveis (31 na fila de substituição) · 145 entidades ausentes
- 372 sementes carregadas → 32 atingidas, **11 suspensas** (homografia, guarda ou colisão com Externos)
- 90 termos relevantes para o dossiê de trabalho (≈1.153 tokens)

Fila de substituição (31 itens, extraída de `variantes-propostas.csv`): Brama→Brahma (8), Belal→Belial (3), Javer→Javé (3), choques de realidade→Choque de Realidade (2), atos de verdade→Ato de Verdade (2), para Brama→[decidir: Brahma] (2), Demiurg→Demiurgo (2), arcontos→Arcontes (2), Xavé→Javé, Chiva→Shiva, dinastia das Sofias→Dinastia das Sophias, criatura ferramenta→Criaturas-ferramenta, tirtancaras→Tirthankaras, arcos/arces→[decidir: Archeons de Ereon], Virgin→[decidir: Vishnu] + 16 propostas de baixa adesão a adjudicar.

**Suspendidas (não substituir):** Olm (homografia RC-092/RC-252), Cristo→Krishna (homografia), caos→Javé como Caos Personificado (vocabulário comum), Nick→Nyx (Externos), Shiva→Shiva como Primeiro Demo (homografia), Yel→Elm, Midana→Nidana, WD→Wyrd/Urd, Terra Atlântis→Terra Atlantis, morre→Morlens, anda→Anda.

## 18. Apêndice C — Pendências da KB que afetam a revisão

Do Anexo I, §6: RC-781 (nome "Brama" + cross-refs erradas) · RC-142 incompleta · Jeane Miranda sem ficha · `canonico.json` sem campo de remissão · Len Mion nos nomes de RC-850/RC-851 · Zian/Zion (RC-092/RC-252) · Temis/Têmis (RC-815) · *Valores Supremos da Consciência* ausente de `biblio.json` · "radiato" em títulos curatoriais · B095 ausente.

Nenhuma pendência bloqueia a revisão; todas devem ser devolvidas ao curador ao final.
