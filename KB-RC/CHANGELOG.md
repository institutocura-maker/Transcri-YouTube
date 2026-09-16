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
