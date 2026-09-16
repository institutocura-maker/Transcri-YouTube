# 10-diagnostico — saída do motor

Regenerável por `ferramentas/rc_diagnostico.py`, com **uma exceção crítica**:

`variantes-propostas.csv` recebe do revisor as colunas `adjudicacao`, `motivo_adjudicacao` e
`ocorrencias_no_revisado`. É o **livro-razão da revisão**. Rodar o motor por cima dele apaga o
trabalho de adjudicação e faz o QA voltar a cobrar linhas conscientemente recusadas.

Para rodar de novo, grave fora da pasta e compare:

```bash
python ferramentas/rc_diagnostico.py ../00-fonte/transcricao-bruta.txt --kb KB-RC --saida /tmp/diag-novo
```

Arquivos esperados aqui: `diagnostico.md`, `variantes-propostas.csv`, `ausentes-da-base.csv`,
`dossie-bloco.txt`. `diagnostico.json` é regenerável e por isso está no `.gitignore`.
