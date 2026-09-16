# Adjudicação — Alienígenas e humanos: Eles já estão entre nós? (Jan Val Ellam)

Pasta `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos` · 16/09/2026 · Agente 86.
Livro-razão: `10-diagnostico/variantes-propostas.csv` (29 linhas, todas decididas — portão G4 `ok`).

**Condição desta adjudicação:** a matéria dos blocos não é o bruto, é a **revisão externa** do
Comandante (`00-fonte/revisao-comandante.docx`). O bruto oficial foi usado como autoridade sobre o
que foi dito — foi contra ele que cada decisão abaixo foi conferida. Divergência lexical entre os
dois: **8,12%** (`docs/pareceres/video-2-medicao-oficial.md`).

---

## 1. Fila automática (motor `rc_diagnostico.py` + `rc_lexicon.py`)

| decisão | linhas | o que significa aqui |
|---|---:|---|
| `informativa` | 19 | candidatos de classe *artigo*/*flexão* cuja forma no texto já está correta (ex.: "um loop mental" → RC-924, "e antimatéria" → RC-527). Nada a substituir; registradas para auditoria da varredura |
| `recusada` | 6 | falsos positivos — tabela §3 |
| `protecao` | 2 | "colmeia" (forma já correta, RC-174) e "YouTube" (camada 3, ocorrência no cabeçalho) |
| `aceita` | 1 | `locas` → **Lokas** (RC-077), atestada 2× no corpo do bruto |
| `aceita-parcial` | 1 | `chamanismo` → grafia *xamanismo* aplicada; o termo RC-577 (Xamanismo Cósmico) **não** se aplica |

Nenhuma linha `superada`. Nenhuma linha ficou em `proposta`: o portão G4 não fecha com decisão em
aberto, e desta vez a matéria já vinha revisada — sobrou para a casa conferir, não corrigir em massa.

---

## 2. Correções aplicadas nos blocos

### Bloco 1 — Abertura: os portais e as três fases do trânsito

| onde | de → para | camada do Guia | motivo |
|---|---|:---:|---|
| §1, 1º parágrafo | "falar hoje **a parte**" → "falar hoje **à tarde**" `[NOTA]` | 1 | o bruto atesta "hoje à tarde"; "a parte" não existe na língua e desloca o sentido. **Regressão do editor, a única que muda significado** |
| §1, 1º parágrafo | — `[NOTA]` de proveniência | 5 | o vídeo é trecho da palestra "A Dramática Fusão dos Universos de Hyren e Hyron" (B085); informação do revisor, não fala do autor |
| §1, 2º parágrafo | "**dia-a-dia**" → "**dia a dia**" | 1 | ortografia corrente; o bruto já grafava sem hífen |
| §1, 3º parágrafo | "E quando **pontes, pontes** de luz" → "E quando **pontes** de luz" | 4 | falso início abandonado — remoção prevista no nível LEVE (Guia §10) |

### Bloco 2 — Do fechamento dos portais à colmeia dos lokas

| onde | de → para | camada | motivo |
|---|---|:---:|---|
| §2, "a ciência chama de singularidade" | "quarks e **glues**" → "quarks e **gluons**" `[NOTA]` | 2 | RC-034 registra a "sopa de quarks e gluons" (B031; P2025-03-15); o bruto diz "quarks e glu". `glues` é troca do corretor do editor |
| §2, "O universo antimaterial" | — `[NOTA]` de nomeação de dêiticos | 5 | o autor apontava para a tela; o revisor nomeou o referente (despacho de 16/09/2026). Fichas RC-033/RC-038, RC-106/RC-107, RC-077 |
| §2, "é uma grande colmeia" | "**abelha rainha**" → "**abelha-rainha**" | 2 | RC-175 registra **Abelha-Rainha**; é também a prática do lote 01 |

O bloco já trazia da revisão externa: *xamanismo*, *lokas*, *Bhuloka*, *Brahmaloka*, *loop mental*,
*princípio da externalização*, *mitólogo*, *colapsa* — conferidos um a um contra o bruto e mantidos.

### Bloco 3 — A fusão dos dois universos: caos A e caos B, os elétrons e o que espera as gerações

| onde | de → para | camada | motivo |
|---|---|:---:|---|
| §3, "regras" | "**pré-estabelecidas**" → "**preestabelecidas**" | 1 | Acordo de 1990: prefixo terminado em vogal + palavra iniciada por vogal diferente não leva hífen |
| §3, "nada se perde" | "nenhum **pósetron** daqui" → "nenhum **pósitron** daqui" `[NOTA]` | 2 | RC-636: "o jogo de **pósitrons** [STT 'positelétron']", "os elétrons antimateriais do universo vizinho". **O bruto estava certo**; a regressão é inteira do editor |
| §3, "Isso aqui são os Registros Akáshicos" | mantido | 2 | RC-548 aceita "akásicos (ou akáshicos)" [B075 p. 102]; no bruto, "registros acásicos ou acáxicos" |

---

## 3. Falsos positivos e recusas (6 linhas `recusada`)

| variante | proposta do motor | por que recusada |
|---|---|---|
| `ainda` | Brahma (RC-037) | ruído fonético: casa na superfície "anda" ("Brahma anda"). *ainda* é advérbio comum |
| `universos paralelos` | Universo Paralelo (RC-108) | flexão legítima: plural de uso comum. Flexionar não é corromper — mesmo caso de "Brama" no lote 01 |
| `bilhões de estrelas` | Filhos das Estrelas (RC-222) | falso positivo por janela de palavras: o bruto faz aritmética ("3.000, 5.000 bilhões de estrelas") |
| `cósmico` | Quarentena Sideral / Cósmica (RC-342) | adjetivo comum em "ovo cósmico" (RC-034) |
| `criador caiu` | Tikun Cósmico (RC-514) | casa em "o eu do criador caiu aqui": narrativa, não o termo |
| `dimensionais.` | Val dos Corpos Perdidos / Dimensionados (RC-133) | **candidato gerado no cabeçalho**, não no corpo: o "guia de fontes" resumido do bruto diz "portais dimensionais". Fica como evidência do item 2 do parecer §9 — `rc_diagnostico.py` mede o arquivo inteiro quando não há marcador de corpo |

Protegidas (2): `colmeia` — substituir por "Colmeia Universal" destruiria a frase, a forma do texto já
é a da família RC-174/176/953; `YouTube` — entidade da camada 3, ocorrência no cabeçalho (URL).

---

## 4. Correções manuais não propostas pelo motor

Nenhuma das três regressões do editor foi proposta por qualquer régua da casa — todas foram achadas
conferindo o `.docx` contra o bruto, palavra por palavra:

1. `glues` → **gluons** (RC-034)
2. `pósetron` → **pósitron** (RC-636/RC-161)
3. "hoje a parte" → "hoje **à tarde**" (atestado no bruto)

Mais três de ortografia/hífen que o motor não cobre: *dia a dia*, *abelha-rainha*,
*preestabelecidas*. É o argumento do parecer §9 pela **varredura de formas quase-canônicas**: uma
palavra que difere do canônico por uma letra ou um acento passa por legítima em G3, G5 e G6.

---

## 5. Decisões de forma (desvios documentados do Guia v2)

| decisão | fundamento |
|---|---|
| **Números por extenso mantidos** ("3 mil", "5 mil", "Uns") | o bruto traz `3.000`/`5.000`/`un`; a revisão normalizou **sem alterar valor** — permitido pela política de números do Guia §7. Nenhuma `[NOTA]` foi necessária porque não há divergência de valor, só de grafia |
| **"lokas" em minúscula no corpo** | a prosa das próprias fichas grafa "as lokas" (RC-033, RC-038, RC-066). Guia §3 regra 7: não inventar maiúscula sem registro — aqui o registro é minúsculo |
| **Disfluência LEVE: 1 remoção, 1 preservação** | removido o falso início "pontes, pontes"; **preservada** a repetição enfática "O antimaterial é improvisado, tudo. Tudo é improvisado, início, meio e fim" (anáfora deliberada — Guia §10, coluna "preservar") |
| **Marcadores orais preservados** | *então* 8×, *sabe* 8×, *tipo* 4×, *aí* 2× — todos com função lexical ou idiomática ("sabe-se lá de onde", "Sabe uma colmeia…?", "um tipo de vitamina"). O Guia §10 proíbe converter oralidade em norma escrita |
| **Um rótulo por bloco** | monólogo de um só falante, 25 parágrafos: `**[JAN VAL ELLAM]**` abre cada bloco (Guia §9, opção B). Alexandre Sherminator é citado no encerramento mas não fala |
| **Revisão externa não é `derivado:`** | o portão G9 fiscaliza derivados de máquina. Este texto é revisão humana: a autoridade continua sendo o bruto, e a auditoria ficou no parecer, não nos metadados de derivado |

---

## 6. Ajustes nas ferramentas feitos durante esta revisão

1. **`ferramentas/rc_perfil_stt.py`** — passou a medir o **corpo** pelo critério único do
   `rc_leitura.py`, e não o arquivo inteiro. Era a terceira régua de corpo da casa e a mais
   perigosa, porque ninguém a via: no vídeo 2, o cabeçalho do bruto (o "guia de fontes" resumido,
   167 palavras pontuadas) contaminava a medição e o instrumento devolvia **14,37%** de divergência
   onde o corpo tem **8,12%**, além de anunciar 6,6 sinais de pontuação por 1.000 palavras que o ASR
   nunca produziu. O eixo 4 continua olhando o arquivo inteiro (é a pergunta dele: "onde começa o
   corpo?"), agora com `texto_integral` separado de `texto`.
2. **`docs/normas/guia-revisao-v2.md` §13.1** — o comando do diagnóstico ensinava
   `--saida "transcricoes/<slug>"`, que joga os arquivos na raiz da pasta e deixa
   `diagnostico.json` (135 KB regeneráveis) **fora** do padrão do `.gitignore`. Corrigido para rodar
   sem `--saida`: a ferramenta descobre `10-diagnostico/` a partir do caminho do bruto.

Testes após os dois ajustes: **154 verificações, 0 falhas**.

---

## 7. O que esta revisão NÃO fez

* **Não censurou nada.** Zero tokens mascarados com `*` no bruto e na revisão; as sondas
  (*diabos*, *esculhamb-*, *cretiniz-*, *imbeciliz-*, *coelhos*) estão preservadas nos dois lados.
  O "o que diabos é isso" do bloco 1 e o "esculhambassem" do bloco 2 estão no produto.
* **Não reescreveu.** Nenhuma reordenação de palavra, nenhum conectivo trocado, nenhuma oralidade
  convertida em norma escrita. A sintaxe do autor ficou como o revisor externo a deixou.
* **Não marcou `[A CONFIRMAR]` nem `[INAUDÍVEL]`.** Não há trecho duvidoso: o bruto oficial é
  completo, do primeiro ao último enunciado, e a revisão cobre os dois extremos.
* **Não comparou motores.** Por despacho, o vídeo 2 entrou como **esteira normal**; a auditoria da
  revisão externa ficou registrada no parecer, fora do fluxo.
