# CHANGELOG da KB-RC

Histórico de **curadoria**: o que mudou na fonte de verdade, quando, a pedido de qual
transcrição e por decisão de quem. O revisor propõe (em
`transcricoes/<slug>/40-devolucao/`); o curador aplica aqui.

Propostas aguardando aplicação vivem em `_fila-de-curadoria.csv`. Este arquivo só recebe
linha quando a mudança **foi aplicada**.

Formato de cada entrada:

```
## AAAA-MM-DD — <assunto do lote>
- <código> <o que mudou> — origem: <slug da transcrição ou despacho>
```

---

## 2026-09-16 — abertura do registro de curadoria

Nenhuma alteração aplicada ainda. Este arquivo foi criado pela migração do repositório
(`docs/planos/plano-de-organizacao.md`, fase 4) para que a KB-RC passe a ter histórico
próprio, separado do histórico das transcrições.

Estado da base nesta data:

| item | valor |
|---|---|
| termos em `canonico.json` | 946 (formato canonico-1.1) |
| fichas em `termos/` | 820 |
| termos sem ficha | 126 |
| obras em `biblio.json` | 104 (97 códigos B, B001–B098 **com a falta de B095**, 3 ART, 1 PER, 1 EXT, 2 P) |
| regras de substituição extraídas da prosa | 299 (`ferramentas/dados/variantes-kb-extraidas.csv`) |
| entidades na camada Externos | 37 (`ferramentas/dados/externos.csv`) |
| propostas pendentes na fila | 38 (`_fila-de-curadoria.csv`) |

### Estado da base depois do lote 02 (16/09/2026)

| item | antes | depois |
|---|---|---|
| termos em `canonico.json` | 946 | **956** (RC-947 a RC-956) |
| fichas em `termos/` | 820 | **830** |
| termos sem ficha | 126 | 126 (nenhum termo novo nasceu sem ficha) |
| obras em `biblio.json` | 104 | **105** — primeira fonte audiovisual, `Y2026-09-14` (padrão Y, Guia §2.5) |
| variantes STT nas fichas | 62 | **90** (84 no lote 01, +7 dos termos novos, −1 remanejada) |
| relações tipadas | 1.887 | **1.915** |
| itens na fila | 38 pendentes | 41: **26 aplicados**, 14 pendentes, 1 informativo |

Nenhum termo novo nasceu como `verificado`: fonte Y é STT único, sem pontuação — entram como
`provisório` (9) ou `candidato` (1, o Tom Teltan, cuja grafia segue `[A CONFIRMAR]`).

### Pendências anteriores a este arquivo

Registradas para não se perderem — vieram do Anexo I
(`docs/normas/resolucao-de-conflitos.md` §6) e foram assumidas pelo Comandante em 16/09/2026:

- 10 ações residuais da resolução dos oito conflitos da base;
- ficha de **Jeane Miranda** a criar;
- código **B095** ausente em `biblio.json`;
- 126 termos sem ficha em `termos/`.

A elas somam-se os itens 11 a 18 propostos pela revisão de
`2026-09-14-revelacoes-cosmicas-urgente` (ver `_fila-de-curadoria.csv`).

## 2026-09-16 — lote 01: variantes STT devolvidas por `2026-09-14-revelacoes-cosmicas-urgente`

Curadoria: Agente 86. Ferramenta: `ferramentas/rc_curadoria.py` (atestação no bruto antes de gravar).

- RC-699 acrescentadas "espírito mantado" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0011 da fila (1 ocorrência no bruto)
- RC-479 acrescentadas "Jah Baal", "Belal" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0012 da fila (4 ocorrências no bruto)
- RC-474 acrescentadas "arcontos", "erontes" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0013 da fila (3 ocorrências no bruto)
- RC-001 acrescentadas "Xavé", "Yahé", "Javer", "Jahé" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0014 da fila (12 ocorrências no bruto)
- RC-009 acrescentadas "Cosmo Rock" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0015 da fila (1 ocorrência no bruto)
- RC-037 acrescentadas "Brama" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0016 da fila (8 ocorrências no bruto)
- RC-104 acrescentadas "Virgin" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0017 da fila (1 ocorrência no bruto)
- RC-102 acrescentadas "Chiva" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0018 da fila (1 ocorrência no bruto)
- RC-048 acrescentadas "Demiurg" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0019 da fila (2 ocorrências no bruto)
- RC-397 acrescentadas "tirtancaras" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0020 da fila (1 ocorrência no bruto)
- RC-756 acrescentadas "Ganexa", "Ganeixa" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0021 da fila (3 ocorrências no bruto)
- RC-174 acrescentadas "calmeia" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0022 da fila (2 ocorrências no bruto)
- RC-494 acrescentadas "dinastia das Sofias" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0024 da fila (1 ocorrência no bruto)
- RC-596 acrescentadas "arces", "arcos" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0039 da fila (2 ocorrências no bruto)
- RC-176 acrescentadas "circuito coméico" — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0040 da fila (1 ocorrência no bruto)

## 2026-09-16 — lote 02: 10 termos novos (padrão Y)

Curadoria: Agente 86. Ferramenta: `ferramentas/rc_termo.py` a partir de `_lote-02-termos.json`. Autorização: Despacho do Comandante de 16/09/2026 — 'Aprovação do Lote 01 e Padrão Y': convenção Y aprovada, URL fornecida, autorizados os 10 novos termos.

Fonte registrada: **Y2026-09-14** em `biblio.json`. `canonico.json` foi de 946 para 956 termos; `relacoes` ganhou 28 arestas.

- RC-947 **Eu Parasitário (de Javé)** (Processos & Fenômenos / 4.2 Fenômenos espirituais / mediúnicos; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0001 da fila
- RC-948 **/Kaggen (nome san de Javé)** (Seres & Entidades / 1.1 Divindades / Criadores; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0002 da fila
- RC-949 **Tom Teltan** (Seres & Entidades / 1.6 Figuras humanas (históricas/míticas); status candidato) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0003 da fila
- RC-950 **Avalokiteshvara** (Seres & Entidades / 1.1 Divindades / Criadores; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0004 da fila
- RC-951 **Arcturianos** (Seres & Entidades / 1.3 Extraterrestres / Raças cósmicas; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0005 da fila
- RC-952 **Constituição Setenária** (Conceitos Cosmológicos / 2.3 Dimensões / Planos de existência; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0006 da fila
- RC-953 **Circuito Colmeico** (Conceitos Cosmológicos / 2.2 Leis e princípios cósmicos; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0007 da fila
- RC-954 **Planeta de Expiação e Provas** (Lokas & Geografias / 3.3 Localidades terrestres; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0008 da fila
- RC-955 **Javé 2.0** (Seres & Entidades / 1.1 Divindades / Criadores; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0009 da fila
- RC-956 **Força da Consciência Dignificada** (Conceitos Cosmológicos / 2.6 Ética / Carma / Compromissos; status provisório) — origem: 2026-09-14-revelacoes-cosmicas-urgente, item 0010 da fila
