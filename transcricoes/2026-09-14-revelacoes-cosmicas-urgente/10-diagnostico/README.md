# 10-diagnostico — saída do motor

Tudo aqui é **regenerável** por `ferramentas/rc_diagnostico.py`, com uma exceção crítica.

| Arquivo | Natureza | Regenerar? |
|---|---|---|
| `diagnostico.md` | relatório da varredura (snapshot de 16/09/2026) | sim, sem perda |
| `ausentes-da-base.csv` | 145 candidatos a novo registro na KB | sim, sem perda |
| `dossie-bloco.txt` | léxico de trabalho: 90 termos relevantes (≈1.153 tokens) | sim, sem perda |
| `variantes-propostas.csv` | **NÃO É SÓ SAÍDA DO MOTOR** | **não regenerar por cima** |
| `diagnostico.json` | idem `diagnostico.md`, em JSON | regenerável — por isso está no `.gitignore` |

## Por que `variantes-propostas.csv` não pode ser sobrescrito

O motor escreve 12 colunas. O revisor acrescentou três:

- **`adjudicacao`** — a decisão humana: `aceita`, `aceita-parcial`, `recusada`, `informativa`,
  `protecao`, `superada`
- **`motivo_adjudicacao`** — a justificativa escrita, linha a linha
- **`ocorrencias_no_revisado`** — quantas vezes a variante sobrevive no texto revisado

Este arquivo é o **livro-razão da revisão**: 98 linhas, nenhuma sem decisão. Rodar o motor por
cima dele apaga o trabalho de adjudicação e ainda faz o QA do `rc_docx.py` voltar a cobrar as 20
linhas que foram conscientemente recusadas.

### Se for preciso rodar o diagnóstico de novo

```bash
# saída para fora da pasta, e depois se compara
python ferramentas/rc_diagnostico.py \
    transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-bruta.txt \
    --kb KB-RC --saida /tmp/diag-novo
```

Conferido em 16/09/2026, depois da migração de pastas: a nova rodada reproduz **exatamente** as
mesmas métricas (100 superfícies da base presentes · 790 candidatos brutos · 61 adjudicáveis ·
145 ausentes · 90 termos no dossiê · 98 linhas de variantes). Se um dia divergir, a divergência é
notícia — ou o motor mudou, ou o bruto foi tocado (o portão G1 existe para isso).
