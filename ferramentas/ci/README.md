# `ferramentas/ci/` — configuração do GitHub Actions

## Estado: CI ATIVO desde 16/09/2026

O Comandante instalou o workflow em `.github/workflows/qa.yml` (commit `5744f1f`, *Ativando CI:
workflow de QA do Agente 86*), byte-idêntico ao `qa.yml` desta pasta. Ele roda em todo PR que toque
`transcricoes/**`, `KB-RC/**`, `ferramentas/**`, `docs/**` ou o próprio workflow, e em todo push na
`main`.

| Passo | Comando |
|---|---|
| 1 | `pip install -r ferramentas/requirements.txt` |
| 2 | `python testes/test_pipeline.py` — fumaça das ferramentas |
| 3 | `python ferramentas/rc_qa.py --tudo` — os oito portões em cada transcrição |
| 4 | `python ferramentas/rc_indice.py --checar` — catálogo em dia + padrão Y |
| 5 | `python ferramentas/rc_qa.py --tudo --json > qa.json` — artefato legível (não bloqueia) |

## O encargo que fica: duas cópias, um conteúdo

O Agente 86 empurra este repositório por um GitHub App **sem a permissão `workflows`** — qualquer
push que crie ou altere `.github/workflows/*` é recusado:

```
! [remote rejected] (refusing to allow a GitHub App to create or update workflow
  `.github/workflows/qa.yml` without `workflows` permission)
```

Por isso o workflow existe em dois lugares e **precisa continuar igual nos dois**:

- `.github/workflows/qa.yml` — o que o GitHub executa. Só quem tem acesso direto ao repositório edita;
- `ferramentas/ci/qa.yml` — a cópia versionada que o Agente mantém. É daqui que sai qualquer mudança.

Mudou uma, mudou a outra. Se divergirem, o CI passa a verificar outra coisa do que o repositório
documenta — e ninguém percebe, porque o selo continua verde. Para conferir:

```bash
diff .github/workflows/qa.yml ferramentas/ci/qa.yml && echo "cópias idênticas"
```

Alternativa definitiva: conceder *Read and write* em **Workflows** ao app (Settings → Integrations →
GitHub Apps). Aí o Agente mesmo instala e mantém, e a duplicação deixa de ser necessária.

## Sem CI, o equivalente manual

```bash
python ferramentas/rc_qa.py --tudo && python ferramentas/rc_indice.py --checar
python testes/test_pipeline.py
```

De preferência num **clone fresco** (`git clone <repo> /tmp/fresco`), que é o único teste capaz de
pegar divergência entre o repositório e a cópia de trabalho — exatamente o que aconteceu no incidente
de normalização de fim de linha de 16/09/2026 (`docs/planos/plano-de-organizacao.md` §14.2).
