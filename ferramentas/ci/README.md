# `ferramentas/ci/` — configuração pronta do GitHub Actions

## Por que não está em `.github/workflows/`

O Agente 86 empurra este repositório através de um **GitHub App** cuja permissão não inclui
`workflows`. Sem essa permissão, qualquer push que crie ou altere `.github/workflows/*` é recusado:

```
! [remote rejected] (refusing to allow a GitHub App to create or update workflow
  `.github/workflows/qa.yml` without `workflows` permission)
```

Para não deixar o repositório sem CI nem forçar uma concessão de permissão que talvez não seja
desejada, o workflow vive aqui, versionado e pronto para instalar.

## Como ativar (uma das três opções)

**Opção 1 — quem tem acesso direto ao repositório faz o push:**

```bash
mkdir -p .github/workflows
cp ferramentas/ci/qa.yml .github/workflows/qa.yml
git add .github/workflows/qa.yml
git commit -m "Ativa o CI: oito portões + catálogo em toda abertura de PR"
git push
```

**Opção 2 — conceder a permissão ao App.** Em *Settings → Integrations → GitHub Apps*, dar
**Read and write** em *Workflows* ao app usado pela Arena; depois pedir ao Agente para repetir o
push. A partir daí o próprio Agente mantém o workflow.

**Opção 3 — sem CI, por enquanto.** Os portões rodam localmente com um comando:

```bash
python ferramentas/rc_qa.py --tudo && python ferramentas/rc_indice.py --checar
```

A diferença é só *quem* roda e *quando*: o CI roda em **clone fresco**, que é o único teste capaz
de pegar divergência entre o repositório e a cópia de trabalho — exatamente o que aconteceu no
incidente de normalização de fim de linha de 16/09/2026 (relatado em
`docs/planos/plano-de-organizacao.md` §14.2). Sem CI, rode os portões também num clone fresco:

```bash
git clone <repo> /tmp/fresco && cd /tmp/fresco
python ferramentas/rc_qa.py --tudo && python ferramentas/rc_indice.py --checar
```

## O que o workflow faz

`qa.yml` — gatilho em push para `main` e em toda abertura de PR:

| Passo | Comando |
|---|---|
| 1 | `pip install python-docx openpyxl rapidfuzz numpy` |
| 2 | `python ferramentas/rc_qa.py --tudo` — os oito portões em cada transcrição |
| 3 | `python ferramentas/rc_indice.py --checar` — catálogo em dia |
| 4 | `python testes/test_pipeline.py` — fumaça das ferramentas |

Falhou qualquer um dos três: o PR não deveria ser mesclado. O corpo do PR tem o modelo
`.github/PULL_REQUEST_TEMPLATE.md` com os três comandos para colar o resultado.
