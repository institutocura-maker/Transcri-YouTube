# Parecer de viabilidade — Revisão ortográfica e terminológica de transcrições do YouTube

**Projeto:** Transcri-YouTube · **Data:** 15 de setembro de 2026 · **Elaborado por:** Agente 86 (Arena.ai Agent Mode)

**Objeto da análise**
1. `Guia - SISTEMA DE REVISÃO E GOVERNANÇA TERMINOLÓGICA.docx` — a *skill* vinda de outra plataforma;
2. `base-terminologica.xlsx` — ontologia consolidada das Revelações Cósmicas (Jan Val Ellam);
3. `Revelações Cósmicas Urgente – Jan Val Ellam.txt` — primeira transcrição a processar (live do canal Paranormal Experience, 14/09/2026).

---

## 0. Sumário executivo

**Veredito: a proposta é viável e o ativo mais valioso do projeto — a base terminológica — está em condição de uso. Mas o Guia, tal como está escrito, não sobrevive ao contato com esta transcrição: ele pressupõe três condições que não se verificam aqui.** É um problema de arquitetura, não de mérito. Com quatro ajustes (todos de baixo custo), o fluxo passa a ser executável, auditável e repetível.

O que foi feito para chegar a essa conclusão (não é opinião, é medição):

| entrega | caminho |
|---|---|
| Biblioteca de acesso à base (946 termos, 104 obras, 1.887 relações) | `ferramentas/rc_lexicon.py` |
| Varredura automática transcrição × base | `ferramentas/rc_diagnostico.py` |
| Tabela de variantes do Guia convertida em dado (39 pares, 55 superfícies analisadas) | `ferramentas/sementes-variantes-stt.csv` |
| Guarda de vocabulário comum pt-BR (1.844 formas) | `ferramentas/vocabular-guarda-pt.txt` |
| Montagem determinística do DOCX final (Passo 3) | `ferramentas/rc_docx.py` |
| Diagnóstico completo desta transcrição | `analise/revelacoes-cosmicas-urgente-jan-val-ellam/` |
| **Amostra revisada do bloco 1 + DOCX montado** | `…/exemplo-bloco-01.md`, `…/EXEMPLO-saida-bloco-01.docx` |

**Os três pressupostos do Guia que falham aqui**

1. *"Extrair termos, grafias canônicas, etimologia e definições da aba **Fichas**"* → as cinco colunas ricas da aba Fichas (Definição sintética, Contexto/Origem, **Etimologia/Grafias**, Citações-chave, Observações) contêm, em **100% das 820 linhas**, o texto `(ver ficha completa em termos/)`. São **4.100 células vazias de conteúdo**. A pasta `termos/` e o script `ferramentas/build_xlsx.py`, citados na aba "Como usar", **não estão neste repositório**. Ou seja: a fonte que o Passo 1 declara obrigatória não existe aqui.
2. *"Uma única chamada de consulta consolidada"* → o índice inteiro custa ~9.500 tokens; com glossas e relações, ~58.000. Somado à transcrição (~26.000) e ao Guia (~4.000), são ~88.000 tokens de entrada **antes** de produzir ~35.000 tokens de saída. Não cabe num passe único confiável. A boa notícia: **esta transcrição só aciona 78 dos 946 termos** — um dossê filtrado custa **~1.000 tokens**, 9× menos.
3. *"Emissão direta do texto completo integralmente revisado"* → 18.781 palavras não saem inteiras e bem revisadas numa única emissão. O próprio Guia já admite segmentação (item 7.1), mas sugere 2–4 blocos para áudios >45 min; **esta live tem ~125 min**. A montagem final deve ser **programática**, não manual.

**A lacuna que mais dói:** a base guarda *canônicos*; o conhecimento de *variante → canônico* mora apenas nas tabelas do Guia (39 pares). Das 55 superfícies citadas nas seções 5.1/5.2/5.4 do Guia (variantes e canônicos somados), **38 não existem em nenhuma aba da planilha**. Como o Guia proíbe "inventar grafias por intuição" e manda sinalizar `[NOTA: termo não encontrado na base]`, a aplicação literal produziria dezenas de notas — inclusive para erros que a própria base resolveria. Nesta live, um único autor externo (Ray Kurzweil) aparece **9 vezes sob 9 grafias diferentes**, das quais o Guia conhece **uma**.

**O que esta transcrição realmente exige** (ordem de grandeza medida):

| dimensão | volume |
|---|---|
| Pontuação a reconstruir | 1 vírgula e 19 pontos (todos numéricos) em 18.781 palavras |
| Segmentação | 1 parágrafo único de 101.468 caracteres |
| Diarização | ≥ 2 vozes ativas (apresentador e Jan Val Ellam) + 6 pessoas citadas |
| Variantes terminológicas resolvíveis pela base | ~45 ocorrências mapeadas |
| Candidatos levantados pela varredura | 572 brutos → 70 adjudicáveis → **38 variantes/truncamentos** |
| Entidades ausentes da base | **169** sequências próprias (candidatas a `[NOTA]` ou a novo registro) |
| Disfluências | 115 repetições consecutivas; "né" 49, "eh" 45, "uhum" 31, "aí" 123 |

Conclusão prática: **terminologia é ~20% do trabalho; normalização sintática (pontuação, parágrafos, disfluência) é ~80%.** O Guia cobre bem os 20% e é omisso sobre os 80%.

---

## 1. Auditoria dos três arquivos

### 1.1 Guia (DOCX) — 8 seções, bem estruturado

Pontos fortes: fluxo em 3 passos claro; governança por status (⚪🟡🟠🟢); sistema de sinalização `[NOTA]` consistente; seção "o que não fazer" que evita loops (herança valiosa da plataforma anterior); política de preservação de trechos promocionais.

Achados de forma e conteúdo:

- **Entidades HTML vazadas no documento:** `&quot;` (14×) e `&apos;` (13×) aparecem no texto visível (ex.: *subtítulo padrão: &quot;Transcrição revisada…&quot;*, *marcas d&apos;água*). Resíduo de conversão — recomendo regenerar o DOCX.
- **Inconsistência de título no Passo 3:** o diagrama diz "GERAÇÃO DO DOCUMENTO TEXTUAL FINAL"; o item 3.3 diz "Gerar Documento **Word** Revisado". Definir o formato contratual (DOCX? MD? ambos?).
- **Números declarados divergem da planilha** (ver 1.2).
- **Regras herdadas de outra plataforma** que aqui perdem o sentido: "proibido fracionar a consulta", "proibido emitir sumários analíticos", "proibido reiniciar o ciclo". Num repositório Git com scripts determinísticos, o antídoto contra loops não é proibir o fracionamento — é **fracionar com montagem programática**.
- **"NÃO recorrer a busca externa"** é uma regra ótima para o cânone ellâmico, mas insustentável para a camada *Externos* (Kurzweil, Bostrom, Gordon Moore, Agostinho de Hipona, Goethe). Ver proposta 6.3.

### 1.2 Base (XLSX) — declarado no Guia × medido na planilha

| Aba | Guia declara | Medido | Situação |
|---|---|---|---|
| Índice Mestre | 946 termos | **946** | ✅ confere |
| Fichas | 650 registros, 14 colunas | **820** registros; 5 colunas ricas = **4.100 placeholders, 0 preenchidas** | ❌ bloqueante para o Passo 1 |
| Relações | 1.898 relações | **1.887** (240 tipos distintos) | ⚠️ deriva pequena |
| Bibliografia | 102 obras (B001–B102) | **104** linhas (102 obras + `P2023-05-21`, `P2024-11-09`) | ⚠️ mistura obras e podcasts |
| Categorias | 40 subdivisões | **40** | ✅ |
| Status | 4 níveis | **4** (🟢 572 · 🟡 212 · 🟠 102 · ⚪ 60) | ✅ |
| Como usar | — | revela: *"as fichas-fonte vivem em Markdown (pasta `termos/` + `indice-mestre.md`)… pode ser regenerada pelo script `ferramentas/build_xlsx.py`"* | ⚠️ esses arquivos **não estão no repositório** |

Distribuição temática dos 946 termos: Conceitos Cosmológicos 277 · Seres & Entidades 264 · Processos & Fenômenos 120 · Eventos & Eras 94 · Lokas & Geografias 56 · Termos Específicos 55 · Tecnologias & Artefatos 42 · Genealogias & Linhagens 38.

Regra de aplicação obrigatória (🟢 + 🟠) atinge **674 termos**; os 272 restantes (🟡/⚪) são, pelo Guia, apenas observacionais.

**Qualidade interna da base** (achados que afetam a revisão):

- **9 núcleos duplicados, envolvendo 19 códigos.** O caso mais grave: `Choque de Realidade` existe **3×** — RC-898 (🟢), RC-936 (🟡) e RC-867 (⚪). A regra "aplique compulsoriamente 🟢/🟠" fica ambígua: qual código referenciar? Também duplicados: `Criaturas-ferramenta` (RC-164/RC-449), `Val Aten` (RC-115/RC-502), `Mônada` (RC-149/RC-937), `Têmis` (RC-305/RC-815), `Rakshasas` (RC-581/RC-872), `Conselho dos Cinco` (RC-043/RC-501), `Favor Divino` (RC-063/RC-332), `Fenômenos Denunciadores do Fim` (RC-203/RC-314).
- **Grafias divergentes entre registros:** RC-037 é `Brahma (Brajna)`, mas RC-781 grafa `Pactos de Javé (Brama / Vishnu / Shiva)`. Na live, o palestrante diz "Brama" 8× e "Brahma" 0× — a decisão canônica muda 8 substituições.
- **Só 2 relações modelam erro de STT** (`erro-stt-de`): RC-497 `Impérial` → RC-087 `Perpérion`; RC-500 `Almaior/Alamaior` → RC-499 `Forno de Awaymaion`. É o embrião certo, mas em escala insuficiente (2 para 946).
- **390 termos têm glossa entre parênteses** e 70 têm formas separadas por `/`. Extração automática de alias a partir daí produz superfícies falsas — ver 4.4.

### 1.3 Transcrição — retrato estrutural

| métrica | valor |
|---|---|
| palavras / caracteres | 18.781 / 101.468 |
| duração estimada (150 ppm) | **~125 min** |
| parágrafos | **1** (bloco único, zero quebras de linha) |
| vírgulas / pontos / reticências | **1 / 19 / 0** — e os 19 pontos são numéricos (`60.000`, `13.8`, `Javé 2.0`) |
| dois-pontos / aspas | 73 / 117 (o motor marcou discurso direto, mas não marcou frase) |
| tipos lexicais distintos | 3.171 |
| repetições consecutivas (disfluência) | 115 (ex.: "eu eu eu eu", "não não não não não") |
| diacríticos | **preservados**: perda de ~0–3% nos pares testados (`não` 394/402, `você` 202/205, `então` 129/132). Acentuação não é o problema. |
| cabeçalho | título, canal, chamada comercial, data e um **"Guia de fontes"** (resumo automático de ~850 caracteres, provavelmente gerado por ferramenta) |
| elenco identificável | apresentador (tratado como "guru"), Jan Val Ellam (também chamado "Rogério" e "Jeanval"), e os citados Terry Fabris, Robson Pinheiro, Alê, Mayara Leite, Tati ("Tati Quântica") |
| conteúdo comercial | ~24 menções (Insider, cupom, QR code, evento de 3 de outubro, ingressos) — o Guia manda preservar |

---

## 2. Lacuna crítica: não existe camada de variantes

O Guia determina: *"NÃO inventar, estimar ou padronizar grafias por intuição; termos sem respaldo documental na planilha devem ser sinalizados como não encontrados."* A regra é correta — mas só funciona se a planilha documentar variantes. **Ela não documenta.**

Das 55 superfícies citadas nas tabelas do Guia (5.1 nomes próprios, 5.2 termos técnicos, 5.4 erros STT):

| situação | quantidade | exemplos |
|---|---|---|
| existem na base | 17 (15 no Índice Mestre + 2 só na Bibliografia) | Yel Luzbel, Sophia, Len Mion, Javé, Jan Val Ellam, Olm, Zion, Biodemos, Wyrd, Terra Atlantis |
| **não existem em nenhuma aba** | **38** | Alusbel, Eelusbel, Elusbel, Luz Bel, Uri Alusbel, Demion, Jabé, Javert, Xavé, Yahé, Jean Van Hollen, Yavain Lan, Jean Vaillelin, Jane/Jeanne Miranda, Ohm, radiato, Asfezion, Asfésian, Fessien, Os Deselados, Raymond Czel, Immanuel/Manuel/Emanuel Kant, Sherminator, Sherminetro, churto, degotificação, pressionificou, afitar, elogismo, "quebra dos lágrimas mentais" |

**Consequência operacional:** a regra do Guia, aplicada ao pé da letra, transforma todo erro STT novo em `[NOTA: termo não encontrado na base]`. Nesta live seriam **mais de 30 notas** apenas em nomes próprios — poluição que destrói a legibilidade do produto final.

**Solução proposta (camada 2):** uma tabela de variantes **versionada em CSV no repositório** (e, quando aprovada, refletida numa nova aba do XLSX ou nas relações `erro-stt-de`):

```
variante | canonico | codigo_base | tipo | origem | evidencia | ocorrencias | aprovacao | data
```

Já entregue como **`ferramentas/sementes-variantes-stt.csv`** — os 39 pares do Guia convertidos em dado, com coluna `status_aprovacao` separando `aprovada` (29) de `conflito` (10, ver §3). O script de diagnóstico consome esse arquivo e passa a detectar automaticamente, em qualquer transcrição futura, as variantes já conhecidas: nesta live ele pegou `Sofia`→Sophia (2×), `Yahé`/`Xavé`→Javé (3×), `Sherminetro`→Sherminator (1×), `Manuel Kant`/`Emanuel Kant`→Immanuel Kant (2×), `Raymond Czel`→Ray Kurzweil (1×).

**E o ciclo se fecha:** cada revisão devolve variantes novas para a tabela (a varredura já emite `variantes-propostas.csv` com 77 linhas prontas para triagem: 38 propostas de correção, 7 sementes do Guia confirmadas no texto e 32 informativas). Da segunda transcrição em diante, o sistema fica progressivamente mais preciso — hoje ele precisa redescobrir tudo a cada arquivo.

---

## 3. Conflitos Guia × Base que exigem decisão de governança

| # | Item | Guia diz | Base diz | Recomendação |
|---|---|---|---|---|
| 1 | Nave/complexo | canônico **Asfezion**, evitar "Asfésian"/"Fessien" | **RC-025 Asphezian** (🟠 em análise) | decidir a grafia e corrigir os dois lados |
| 2 | Códigos Ohm/Olm | "RC-092 (Codificador) vs RC-252 (Quarto Logos)" | **invertido**: RC-092 = `Quarto Logos (Olm / Codificador de Zian)`; RC-252 = `Olm (Codificador de Zion/Zian)` | corrigir o Guia |
| 3 | Brahma | — | RC-037 `Brahma (Brajna)` **vs** RC-781 `…(Brama / Vishnu / Shiva)` | uniformizar (impacta 8 ocorrências nesta live) |
| 4 | Jeane Miranda | canônico `Jeane Miranda` (de Jane/Jeanne) | **não existe no Índice Mestre** (só menção em observações da Bibliografia) | criar registro |
| 5 | Len Mion | canônico `Len Mion`; variantes "Lémion, Demion" | RC-074 `Len Mion (Satã)` ✔, mas RC-850/RC-851 usam **"Lemion"** como glossa | uniformizar a glossa |
| 6 | Radiato/Radiata | termos canônicos "radiato/radiata" | RC-093 `Radiatas` (plural) e RC-631 `Cérebro Radiata` | definir singular/plural canônico |
| 7 | ilogismo | correção de "elogismo" → **ilogismo** | inexistente na base; forma não corrente em português | validar com o autor ou trocar por "ilogicidade/ilógico" |
| 8 | Duplicados | "fonte exclusiva da verdade" | 9 núcleos duplicados / 19 códigos, com **status divergentes** | fundir ou marcar o registro preferencial |

Esses 8 pontos são decisões de 15 minutos — mas, sem elas, o revisor (humano ou agente) improvisa, e improvisar é exatamente o que o Guia proíbe.

---

## 4. O que o teste-piloto mediu

Rodei a varredura completa (`rc_diagnostico.py`) sobre os três arquivos. Resultados que importam para a decisão:

### 4.1 Cobertura: a base é muito maior que qualquer transcrição

- **875 dos 946 termos** não têm nenhuma ocorrência literal nesta live.
- **78 termos** são relevantes → o dossê filtrado gerado (`dossie-bloco.txt`) tem 4,4 KB (~**1.000 tokens**), contra ~9.500 tokens do índice inteiro e ~58.000 do conjunto completo com glossas e relações.
- Implicação direta para o Passo 1: substituir "consultar a planilha inteira, uma vez" por **"gerar o dossê filtrado da transcrição"** — mais barato, mais preciso e repetível por script.

### 4.2 Correções que a base resolve sozinha (amostra medida)

| forma na transcrição | canônico | código | occ. |
|---|---|---|---|
| Jeanval / Jean Valan / Janva Elan / Jean Val | **Jan Val Ellam** | RC-071 | 12+ (o canônico aparece **0×**) |
| Jahé / Jah / Javer / Xavé / Yahé | **Javé** | RC-001 | 15 |
| Brama | **Brahma** | RC-037 | 8 |
| Belal | **Belial** | RC-479 | 3 |
| arcontos | **Arcontes** | RC-474 | 2 |
| Demiurg | **Demiurgo** | RC-048 | 2 |
| Ganexa | **Ganesha** | RC-756 | 2 |
| Sofia | **Sophia** | RC-009 | 2 |
| Chiva (+ "Brama Virgin Chiva") | **Shiva** (+ Brahma, Vishnu, Shiva = Trimurti) | RC-102 / RC-104 | 1 |
| tirtancaras | **Tirthankaras** | RC-397 | 1 |
| dinastia das Sofias | **Dinastia das Sophias** | RC-494 | 1 |
| bilatério | **Bilatérios** | RC-035 | 1 |
| calmeia / calmeias | **colmeia / colmeias** — e o livro é `A Divina Colmeia` | B044 | 4 |
| Inquisição Trimortiana | **Inquisição Trimurtiana** | B022 | 1 |
| Quetz | **Quetzalcóatl** | RC-463 | 1 |
| Édo | **Éden** | — | 1 |
| perespírito | **perispírito** | — | 1 |
| crustácio | **crustáceo** | — | 1 |
| corps | **corpos** | — | 1 |
| cílica | **sílica** (Corpos de Sílica) | RC-645/RC-699 | 1 |
| Sherminetro | **Sherminator** | semente do Guia | 1 |

Dois casos demonstram o valor do cruzamento *base + contexto*: **"Brama Virgin Chiva"** só se resolve como **"Brahma, Vishnu, Shiva"** porque a base tem a Trimurti (RC-104) e a Bibliografia confirma o livro citado na mesma frase (`Inquisição Trimurtiana`, B022); e **"A Divina Calmeia"** vira **`A Divina Colmeia`** (B044) porque a obra está catalogada.

### 4.3 Precisão da detecção automática: boa para triagem, ruim para substituir

| etapa | volume |
|---|---|
| janelas analisadas (1–4 palavras com token suspeito) | 33.947 |
| candidatos acima do corte frouxo de similaridade | **572** |
| após triplo filtro (duas métricas ≥ 0,75 + alvo de confiança + vocabulário comum) | **70** |
| variantes/truncamentos reais (fila de correção) | **38** |
| flexões e artigos (informativo, não é erro) | 32 |

Redução de **18.781 palavras → 38 candidatos com contexto**: ganho de ~490× no espaço de busca. Mas a precisão da fila é de **~45%**; os falsos positivos sobreviventes são instrutivos: `drama`→Rama, `Gordon`→Mordon, `destina`→Despina, `piora`→Pirra, `esperou`→Espheron, `corpo físico`→Corpo Búdico, `é profundo`→Eu Profundo. E os descartados pelo filtro eram piores ainda: `morreu`→Noreia, `melhor`→Melkor, `entra`→Indra, `seis`→Zeus, `Jó`→João, `abelha`→Capela, `IA`→IEEA.

> **Conclusão de projeto:** substituição 100% automática é insegura e violaria o próprio Guia ("não alterar a linha de raciocínio"). O desenho correto é **script levanta evidência → revisor (agente ou humano) decide com contexto → script confere a saída**. Foi exatamente assim que o protótipo foi construído.

### 4.4 Armadilha das glossas (importante para quem automatizar)

Extrair alias automaticamente dos parênteses da base cria superfícies falsas:

- `Suserania Universal (herança prometida a **Rockma/Sofia**)` → gerou a superfície "Sofia", que **colide frontalmente** com a regra do Guia `Sofia → Sophia` (RC-009).
- `Antares (Sistema)` → gerou "Sistema"; `Quarentena Sideral / Cósmica` → gerou "Cósmica"; `Terminal Nervoso do Criador (humano)` → gerou "humano"; `Disciplina dos 3As (respiração, mente, alinhamento)` → gerou "mente".
- Resultado medido: das 67 superfícies da base "presentes" no texto, **apenas 38 são úteis**; as demais são vocabulário comum capturado por glossa.

Por isso `rc_lexicon.py` classifica cada superfície por confiança (`alta` / `media` / `baixa`) e, por padrão, **não** aproveita glossas como alias. Quando a camada `termos/` em Markdown for importada, esse problema desaparece — mais um argumento para trazê-la ao repositório.

### 4.5 Termos genéricos exigem guarda

**241 dos 946 núcleos** têm uma única palavra, e vários são vocabulário corrente: `Deus` (108 ocorrências na live), `Deuses`, `Criador`, `Mente`, `Conceito`, `Sistema`, `Caos`, `Transição`, `Cognição`. Sem guarda, o negrito obrigatório de primeira menção e a "substituição compulsória" produziriam absurdos. `ferramentas/vocabular-guarda-pt.txt` (1.844 formas) e a lista `GENERICOS` em `rc_lexicon.py` cumprem esse papel; ambas são ampliáveis.

### 4.6 O caso Kurzweil: por que a camada de variantes é indispensável

Um único autor externo, **9 ocorrências, 9 grafias diferentes**:

`Raymond Kzwell` · `Ray Kzwell` · `Raymond Cselva` · `Raymond K` · `Ray Curser` · `Ray Cur` · `Ray Curzell` · `Raymond Curs` · `Raymond Czel`

O Guia conhece **uma** delas ("Raymond Czel → Ray Kurzweil"). Nenhum sistema resolve isso sem um dicionário de variantes alimentado continuamente — e sem permitir consulta externa controlada para grafias de nomes do mundo real (Kurzweil, Bostrom, Gordon Moore, Nvidia, Hipona, Goethe).

---

## 5. Lacunas de escopo do Guia para esta transcrição

### 5.1 Pontuação e segmentação — o maior volume de trabalho, e o Guia é omisso
1 vírgula e 19 pontos em 18.781 palavras. O motor marcou discurso direto (73 dois-pontos, 117 aspas) mas não marcou limites de frase. **Reconstruir sintaxe é a maior parte do esforço**, e é também a parte de maior risco de alterar sentido. O Guia precisa de uma seção própria: critérios de frase/parágrafo, limite de tamanho, tratamento de frases interrompidas, política de travessão e de aspas em discurso direto.

### 5.2 Diarização (quem fala)
Há pelo menos duas vozes ativas e seis pessoas citadas. Sem áudio, atribuir turnos é inferência. Três opções: (a) sem rótulos, texto corrido; (b) rótulos inferidos `[APRESENTADOR]` / `[JAN VAL ELLAM]` onde a evidência é forte; (c) rótulos apenas nas trocas de turno evidentes (pergunta/resposta). **A amostra do bloco 1 foi produzida com a opção (b)** para você avaliar visualmente.

### 5.3 Disfluências
115 repetições consecutivas, mais "né" (49), "eh" (45), "uhum" (31), "aí" (123), "então" (132). O Guia manda corrigir "aglutinações indevidas e truncamentos" mas não define política para hesitações. Proponho três níveis contratuais: **fiel** (mantém tudo), **leve** (remove repetições imediatas e marcadores de hesitação, preserva "né/tá" e a sintaxe oral), **limpo** (reformula para leitura fluida). Minha recomendação para este acervo: **leve** — preserva a voz do autor sem cansar o leitor.

### 5.4 Números, datas e grandezas
O Guia já alerta para "bilhões vs milhões", mas o problema é mais amplo. Casos reais desta live: `13.8 8 bilhões de anos` (idade do universo → 13,8 bilhões); `2 3 anos` (→ 2 a 3 anos); `60.000 pessoas` (Google); `61 livros` e `10 a 12` em espanhol; `40%`; `R$ 18`; `10,18`; `em 2007 um autor chamado Raymond Kzwell lançou um livro chamado A singularidade está próxima` — *The Singularity Is Near* é de **2005**; `6.000 pessoas assistindo`; `Javé 2.0`. Proponho regra: **números nunca são "consertados" em silêncio** — ou se mantém o falado, ou se corrige com `[NOTA: transcrição original trouxe "X"; corrigido para "Y" pelo contexto]`.

### 5.5 Estrangeirismos, nomes e obras externas (camada *Externos*)
Levantamento desta live (nenhum item consta da base):

| forma na transcrição | forma correta | tipo |
|---|---|---|
| Raymond Kzwell, Ray Kzwell, Raymond Cselva, Raymond K, Ray Curser, Ray Cur, Ray Curzell, Raymond Curs, Raymond Czel | **Ray Kurzweil** | autor |
| A singularidade está próxima | **The Singularity Is Near** (2005) | obra |
| Nick Bostron, Utopia Profunda | **Nick Bostrom**, **Deep Utopia** | autor/obra |
| Gordon Moore, lei de Gordon war | **Gordon Moore**, **Lei de Moore** | autor/conceito |
| Nvid | **Nvidia** | empresa |
| Agostinho de Pona, cédo de Agostinho | **Agostinho de Hipona**, **credo** | autor/termo |
| Emanuel Kant, Manuel Kant, Emanuel Kante | **Immanuel Kant** | autor |
| "Mefistófiles que é o javist romance de de de g" | **Mefistófeles**, **romance *Fausto*, de Goethe** | personagem/obra |
| dark enlightment | **dark enlightenment** | conceito |
| Sidarta | **Siddhartha Gautama** | figura |
| EA (no lugar de IA) | **IA** | sigla |
| Qcode / Qcodes | **QR code / QR codes** | termo |
| Matrix, Intel, Google, Instagram, YouTube, USP, Unicamp, MIT, Harvard, Trump, Elon Musk | — | externos |
| Terry Fabris, Robson Pinheiro, Alê, Mayara Leite, Tati Quântica, Sherminator, Guru de Malá | — | pessoas do canal |
| Valores Supremos da Consciência | **programa do autor no YouTube** (não é livro) | obra/programa |

Sem uma camada *Externos*, todos os itens acima viram `[NOTA: termo não encontrado na base]` — tecnicamente fiel ao Guia, editorialmente inservível.

### 5.6 Artefatos de plataforma e conteúdo comercial
O cabeçalho traz um **"Guia de fontes"** (resumo automático de ~850 caracteres, tom jornalístico, com afirmações que não são do autor — ex.: "parasitismo cognitivo", "singularidade autônoma"). O item 7.3 do Guia manda expurgar artefatos de ferramentas; o item 7.4 manda preservar anúncios. O resumo automático é artefato ou é conteúdo? Proponho: **preservar os anúncios no corpo** (como o Guia manda) e **mover o "Guia de fontes" para um anexo** ou suprimi-lo, por ser texto gerado por máquina e não fala do autor. Decisão sua.

---

## 6. Proposta de arquitetura

### 6.1 Estrutura de pastas

```
Transcri-YouTube/
├── base-terminologica.xlsx            # fonte de verdade canônica (camada 1)
├── Guia - SISTEMA DE REVISÃO ....docx  # norma editorial (a atualizar: v2)
├── ferramentas/
│   ├── requirements.txt
│   ├── rc_lexicon.py                  # acesso à base + normalização + chave fonética
│   ├── rc_diagnostico.py              # varredura transcrição × base
│   ├── rc_docx.py                     # montagem do DOCX final + QA
│   ├── sementes-variantes-stt.csv     # camada 2: variantes aprovadas (39 pares do Guia)
│   ├── externos.csv                   # camada 3: nomes/obras/conceitos do mundo externo (a criar)
│   └── vocabular-guarda-pt.txt        # camada 4: vocabulário comum (1.844 formas)
├── termos/                            # ← IMPORTAR: fichas-fonte em Markdown (hoje ausentes)
└── transcricoes/<slug-do-video>/
    ├── 00-bruto.txt
    ├── 10-diagnostico/{diagnostico.md,diagnostico.json,variantes-propostas.csv,ausentes-da-base.csv,dossie-bloco.txt}
    ├── 20-blocos/b01.md … b08.md      # blocos revisados
    ├── 30-revisado.md                 # texto consolidado
    ├── 40-final.docx                  # produto entregue
    └── 50-notas.md                    # anexo de ocorrências não mapeadas
```

### 6.2 Fluxo proposto por transcrição (7 etapas)

| # | etapa | ferramenta | produto |
|---|---|---|---|
| 1 | ingestão e identificação do vídeo (título, canal, data, URL, duração) | manual/script | `00-bruto.txt` |
| 2 | **diagnóstico** (métricas, cobertura, candidatos, ausentes, dossê filtrado) | `rc_diagnostico.py` | pasta `10-diagnostico/` |
| 3 | **triagem** das variantes propostas → aprovar/rejeitar; alimentar `sementes-variantes-stt.csv` e `externos.csv` | revisor | CSVs atualizados |
| 4 | **revisão por blocos** (~2.300–2.600 palavras ≈ 15 min de áudio), com o dossê filtrado + regras como contexto | agente | `20-blocos/bNN.md` |
| 5 | **montagem** do texto consolidado e do DOCX com a tipografia do Guia | `rc_docx.py` | `30-revisado.md`, `40-final.docx` |
| 6 | **QA automático**: nenhuma variante aprovada sobreviveu? negrito só na 1ª menção? notas dentro do limite? contagem de palavras compatível (±3%)? | `rc_docx.py --validar` | log de QA |
| 7 | **devolução à base**: variantes novas, termos ausentes e conflitos encontrados | revisor | PR/commit na base |

### 6.3 As quatro camadas de conhecimento

1. **Canônico** — `base-terminologica.xlsx` (e, idealmente, `termos/*.md`). Só a base cria canônicos.
2. **Variantes STT** — CSV versionado; cresce a cada transcrição; distingue `aprovada` / `proposta` / `conflito`.
3. **Externos** — CSV novo para o mundo fora do cânone ellâmico (autores, obras, empresas, pessoas do canal). Remove ~90% dos `[NOTA]` indevidos. **Aqui proponho uma exceção controlada à proibição de busca externa:** consulta permitida *apenas* para esta camada, sempre registrada no CSV com a fonte e a data.
4. **Guarda** — vocabulário comum pt-BR que nunca deve ser tratado como termo.

### 6.4 Política de notas `[NOTA]`
Manter as três etiquetas do Guia, com dois acréscimos: (a) **teto de 5 notas por bloco** — acima disso, o padrão remete ao anexo `50-notas.md`; (b) nova etiqueta `[NOTA: nome externo — grafia confirmada em <fonte>, <data>]` para a camada *Externos*, distinguindo "não sei" de "sei, mas não está no cânone".

### 6.5 Guia v2 — o que eu reescreveria
Manter: governança por status, etiquetas `[NOTA]`, proibição de inventar grafias, preservação de anúncios.
Alterar: Passo 1 ("dossiê filtrado por transcrição" no lugar de "consulta única consolidada"); Passo 3 ("montagem programática em blocos"); números das abas; os conflitos do §3; as entidades HTML.
Acrescentar: § Pontuação e segmentação; § Diarização; § Disfluências (3 níveis); § Números e grandezas; § Camada Externos; § QA e devolução à base.

---

## 7. Custos estimados

| item | valor |
|---|---|
| blocos necessários (125 min ÷ ~15 min) | **8** |
| entrada por bloco (bruto ~13 KB + dossê 4,4 KB + regras ~3 KB) | ~6–7 mil tokens |
| saída por bloco (texto revisado + notas) | ~4–6 mil tokens |
| turnos de trabalho | 8 de revisão + 1 de montagem/QA + 1 de consolidação na base |
| custo evitado pelo dossê filtrado | de ~9.500 para ~1.000 tokens de contexto terminológico por bloco (**−89%**) |
| tentativa em passe único (o que o Guia propõe) | ~88 mil tokens de entrada + ~35 mil de saída → **falha provável** |

---

## 8. Riscos e mitigações

| risco | prob. | impacto | mitigação |
|---|---|---|---|
| Hipercorreção: trocar palavra comum por termo exótico da base (`melhor`→Melkor) | alta | grave | guarda de vocabulário + dupla métrica + proibição de substituir sem contexto; QA por amostragem |
| Alterar sentido ao pontuar 18,7 mil palavras sem áudio | alta | grave | política de disfluência contratada; frase curta; nunca fundir duas ideias em uma; revisão por blocos curtos |
| Substituir grafia por intuição (o que o Guia proíbe) | média | grave | só substitui o que está na base ou em CSV aprovado; resto vira `[NOTA]` |
| `[NOTA]` em excesso poluir o texto | alta | médio | camada *Externos* + teto de notas por bloco + anexo |
| Conflito Guia × Base não resolvido | já ocorreu | médio | §3 deste parecer: 8 decisões pendentes |
| Duplicados na base gerarem referência ambígua | já ocorre | médio | fusão/marcação de registro preferencial |
| Perda de fidelidade na montagem entre blocos | média | médio | montagem programática + contagem de palavras ±3% + QA de variantes sobreviventes |
| Atribuir fala ao interlocutor errado | média | médio | diarização conservadora (opção a/c) ou rótulos só em pergunta-resposta |
| Contexto insuficiente para a base inteira | alta | médio | dossê filtrado por transcrição (já implementado) |
| Números/datas "consertados" em silêncio | média | alto | regra de nota obrigatória em alteração numérica |

---

## 9. Recomendações imediatas (checklist)

- [ ] **1.** Importar para o repositório a pasta `termos/` (fichas Markdown) e o `ferramentas/build_xlsx.py` — sem eles, a coluna *Etimologia/Grafias* permanece vazia e o Passo 1 do Guia fica sem fonte.
- [ ] **2.** Decidir os conflitos do §3 (8 pontos de decisão; 10 linhas marcadas como `conflito` no CSV de sementes).
- [ ] **3.** Aprovar a criação das camadas **Variantes STT** e **Externos** (CSVs versionados) e a exceção de busca externa restrita a *Externos*.
- [ ] **4.** Definir o contrato editorial: formato de saída (DOCX/MD/ambos), nível de disfluência (fiel/leve/limpo), diarização (a/b/c), destino do "Guia de fontes" e dos anúncios.
- [ ] **5.** Validar a amostra do bloco 1 (`EXEMPLO-saida-bloco-01.docx`) como padrão visual.
- [ ] **6.** Rodar as 8 etapas de revisão desta live conforme o fluxo 6.2.
- [ ] **7.** Emitir o **Guia v2** com as seções novas (pontuação, diarização, disfluência, números, externos, QA).
- [ ] **8.** Tratar as duplicidades da base (começar por `Choque de Realidade`, RC-867/RC-898/RC-936).
- [ ] **9.** Padronizar a Bibliografia: separar obras (B###) de podcasts/palestras (P####) em abas distintas.
- [ ] **10.** Definir convenção de nomenclatura de arquivos e de metadados mínimos por vídeo (URL, canal, data, duração, participantes).

---

## 10. Decisões que preciso de você

1. **Contrato editorial de saída** — DOCX, Markdown ou ambos? Mantém o "Guia de fontes" no cabeçalho, move para anexo ou remove?
2. **Diarização e disfluência** — rótulos de falante (como na amostra) ou texto corrido? Nível fiel, leve ou limpo?
3. **Camadas novas e busca externa** — aprova criar `Externos` e permitir consulta externa *só* para nomes/obras do mundo real, com registro de fonte e data?
4. **Ordem de execução** — quer que eu comece já a revisão completa desta live (8 blocos), ou prefere primeiro fechar Guia v2 + correções da base?

---

## Anexo A — Como reproduzir este diagnóstico

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ferramentas/requirements.txt

# 1. diagnóstico completo da transcrição contra a base
python ferramentas/rc_diagnostico.py "Revelações Cósmicas Urgente – Jan Val Ellam.txt"

# 2. montagem do DOCX final a partir dos blocos revisados + QA de variantes
python ferramentas/rc_docx.py analise/<pasta>/blocos/*.md \
    --lexico analise/<pasta>/dossie-bloco.txt \
    --saida "40-final.docx" \
    --titulo "Revelações Cósmicas Urgente — Jan Val Ellam" \
    --subtitulo "Transcrição revisada — Padronização terminológica conforme a Revelação Cósmica de Jan Val Ellam" \
    --validar analise/<pasta>/variantes-propostas.csv
```

## Anexo B — Arquivos gerados nesta análise

| arquivo | conteúdo |
|---|---|
| `analise/revelacoes-cosmicas-urgente-jan-val-ellam/diagnostico.md` | diagnóstico legível (6 seções) |
| `…/diagnostico.json` | diagnóstico completo para máquinas (inclui os 572 candidatos brutos) |
| `…/variantes-propostas.csv` | 77 linhas prontas para triagem (variante, canônico, código, classe, contexto, aprovação) |
| `…/ausentes-da-base.csv` | 169 entidades do texto sem registro na base |
| `…/dossie-bloco.txt` | os 78 termos relevantes para esta transcrição (contexto de trabalho) |
| `…/exemplo-bloco-01.md` | amostra revisada do bloco 1 (~570 palavras do bruto) |
| `…/EXEMPLO-saida-bloco-01.docx` | amostra montada com a tipografia do Guia (justificado, 1,5, 12 pt) |
