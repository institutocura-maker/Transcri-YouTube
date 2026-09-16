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
