# Protótipo de análise — congelado em 2026-09-15

Primeira tentativa de diagnóstico da transcrição *Revelações Cósmicas Urgente*, feita **antes** de
a KB-RC assumir o posto de fonte de verdade (despacho do Comandante de 15/09/2026). Rodava contra
a planilha `base-terminologica.xlsx`.

**Não é o diagnóstico vigente.** O vigente está em
`transcricoes/2026-09-14-revelacoes-cosmicas-urgente/10-diagnostico/`.

| Arquivo | O que é |
|---|---|
| `diagnostico.md` | relatório da varredura contra a planilha |
| `variantes-propostas.csv` | fila de decisão da época, sem a coluna `adjudicacao` |
| `ausentes-da-base.csv` | candidatos a novo termo, calculados contra a planilha |
| `dossie-bloco.txt` | léxico de trabalho da época |
| `exemplo-bloco-01.md` | primeiro esboço de bloco revisado, usado para calibrar o formato |
| `EXEMPLO-saida-bloco-01.docx` | o mesmo esboço montado em DOCX |

## Por que foi guardado

1. Documenta o **antes e o depois** da troca de fonte de verdade: comparando os dois
   `variantes-propostas.csv` vê-se o que a prosa das 820 fichas acrescentou ao motor
   (299 regras de substituição que a planilha não tinha).
2. `exemplo-bloco-01.md` foi o molde que definiu o formato dos 8 blocos finais — formato que o
   `rc_docx.py` implementa e que o portão G2 do QA cobra.
3. Princípio P10 do Plano de Organização: nada se apaga, legado é arquivado com data.
