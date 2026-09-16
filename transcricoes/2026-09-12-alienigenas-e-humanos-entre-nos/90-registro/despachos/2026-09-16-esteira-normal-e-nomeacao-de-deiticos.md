# Despacho de 16/09/2026 — esteira normal para o vídeo 2 e nomeação de dêiticos

| campo | valor |
|---|---|
| data | 16 de setembro de 2026 |
| de | Comandante |
| para | Agente 86 |
| via | mensagem no chat (o `ask_user` com quatro perguntas foi pulado; o Comandante respondeu por extenso) |
| rege | `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos` |
| anexos entregues | `upload/video-2-transcri-youtube.txt` (bruto oficial, commit `87a3525`) · `upload/alienigenas-ou-seres-de-outro-universo.docx` (revisão externa, commit `0ea4388`) |

## 1. O que o Comandante decidiu

1. **Esteira normal.** "Podemos tratar este 2º vídeo normalmente, sem necessidade de comparação, ou
   seja, uma esteira normal." — fica dispensada a comparação entre motores; o vídeo entra como
   bruto → diagnóstico → blocos → adjudicação → produto → devolução → nove portões.
2. **Bruto oficial entregue** no repositório, com a ressalva "só use se for realmente necessário".
   **É necessário:** os portões G1 e G9, o `rc_curadoria.py` e a adjudicação do livro-razão exigem o
   bruto como autoridade sobre o que foi dito. Instalado em `00-fonte/transcricao-bruta.txt`.
3. **A revisão é dele, feita em aplicativo especialista** — e ele está testando outras ferramentas.
   Portanto o `.docx` não é derivado de máquina da casa: é **revisão humana externa**. Consequência
   prática: o campo `derivado:` de `metadados.yaml` fica vazio e o portão **G9 responde `n/a`**; a
   auditoria da revisão vive no parecer, não nos metadados.
4. **Nomeação de dêiticos autorizada e explicada.** O autor apontava para a tela de apresentação e
   dizia "este aqui"/"aquele ali" sem nomear; o Comandante **nomeou** o que ele apontava — a formação
   do universo, com o seu lado material e o antimaterial. As inserções de *Brahmaloka*, *Bhuloka* e
   *lado antimaterial* na revisão são deliberadas, não alucinação.

## 2. Trecho literal (para não se perder a formulação)

> "Ao revisar o vídeo notei que o Ellam dizia algo e não nominava, porque estava apontando para uma
> tela de apresentação, então o que eu fiz, nomeie o que ele estava falando e basicamente está
> relacionado à formação do universo, com seu lado material e o antimaterial, que ela apontava e
> falava este aqui ou aquele ali."

## 3. Como a casa executou

* Mediu o par oficial (bruto × revisão) com o `rc_perfil_stt.py`: **8,12%** de divergência lexical,
  70 perdas e 77 ganhos, veredito "mesma base de áudio com edição substancial". Decomposição no
  parecer §4: as 70 perdas são 23 corruptelas do ASR corrigidas, **19 dêiticos nomeados**, 20
  reescritas de ligação, 4 números normalizados e 4 marcadores orais podados. **Nenhuma categoria é
  supressão de conteúdo.**
* Tratou a nomeação como o Guia v2 §12 manda: **um** `[NOTA]` na primeira ocorrência (bloco 2), com a
  justificativa, a citação do despacho e as fichas (RC-033/RC-038, RC-106/RC-107, RC-077); texto limpo
  nas ocorrências seguintes.
* Conferiu a revisão contra o bruto palavra por palavra e achou **três regressões** que nenhuma régua
  automática propôs: `glues` → **gluons** (RC-034), `pósetron` → **pósitron** (RC-636/RC-161) e
  "hoje a parte" → "hoje **à tarde**". Corrigidas nos blocos, com `[NOTA]`, e propostas para
  Quarentena na fila de curadoria (ids 0049 e 0050).

## 4. O que este despacho encerrou

* A **retratação do §3 do parecer**: o bruto oficial desmentiu a captura por `fetch_page` que o agente
  tinha usado como referência. O ASR do YouTube **não pontua** (0,11 sinais por 100 palavras no corpo
  do bruto); os 13,66 medidos antes eram da rota de captura, que ainda corrompeu "ovo cósmico" em
  "novo cósmico" e inventou anotações de áudio. **Norma nova da casa: transcrição obtida por fetch de
  página não é fonte** — serve para descobrir que um vídeo existe, não para instalar bruto, atestar
  variante nem medir.
* A **fila de curadoria bloqueada**: sem bruto não havia atestação possível (Guia §15); com o bruto
  entregue, as 29 linhas do livro-razão foram decididas e 10 propostas entraram na fila
  (`KB-RC/_fila-de-curadoria.csv`, ids 0042–0051).
* A proposta de variante "novo cósmico" → RC-034, que era corrupção da captura do agente, **não** da
  fala: retirada da fila.

## 5. O que continua em aberto com o Comandante

* **Título e slug** — a casa adotou o oficial ("Alienígenas e humanos: Eles já estão entre nós?",
  slug `2026-09-12-alienigenas-e-humanos-entre-nos`) e registrou o dele ("Alienígenas ou seres de
  outro universo?") como `chamada`. Trocar depois é um `git mv` mais três campos de metadados.
* **Data** — plataforma 12/09, cabeçalho do bruto 13/09, cabeçalho do `.docx` 12/09. Ficou a da
  plataforma; as três estão registradas.
* **Adjudicação das 10 propostas** da fila de curadoria (5 variantes STT, 1 ressalva de falso amigo,
  2 Quarentenas, 1 divergência factual, 1 registro biblio já aplicado) e da proposta de `Jesus` na
  camada 3 (`40-devolucao/externos-novos.csv`).
* **Encargo de varredura de formas quase-canônicas** (parecer §9, alta prioridade): é o que impede que
  um `glues` ou um `pósetron` volte a passar por palavra legítima.
