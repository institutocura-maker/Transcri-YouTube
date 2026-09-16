# Como contribuir — papéis, fluxo e regras

Norma completa: `docs/normas/guia-revisao-v2.md` · estrutura do repositório:
`docs/planos/plano-de-organizacao.md` · conflitos da base resolvidos:
`docs/normas/resolucao-de-conflitos.md`.

## Papéis

| Papel | Escreve em | **Não** escreve em |
|---|---|---|
| **Capturador** | `transcricoes/<slug>/00-fonte/` | qualquer outra pasta |
| **Revisor** | `20-blocos/`, `40-devolucao/`, `90-registro/` | `KB-RC/`, `00-fonte/` |
| **Curador** | `KB-RC/`, `ferramentas/dados/` | blocos revisados |
| **Comandante** | `90-registro/despachos/`, aprovação de PR | — |

### A regra que sustenta tudo

**O revisor propõe; o curador aplica.** Nenhuma alteração entra em `KB-RC/` a partir do trabalho de
revisão — tudo vai para `40-devolucao/` e para `KB-RC/_fila-de-curadoria.csv`. Isso existe porque
uma transcrição é uma fonte nova, não uma autoridade: o que ela revela precisa ser cotejado com as
outras 100 fontes da base antes de virar canônico.

## Fluxo de uma transcrição

```bash
# 1. abrir a pasta (o script valida o slug, grava o hash do bruto e atualiza o catálogo)
python ferramentas/rc_novo.py --slug 2026-10-02-lemuria-terry-fabris \
    --titulo "LEMÚRIA ESTÁ em busca URGENTE DE CONTATO" --canal "Paranormal Experience" \
    --url https://youtu.be/9DvQf6DikA8 --data 2026-10-02 --bruto ~/Downloads/legenda.txt

# 2. conferir os metadados que o script não tem como saber (duração, chamada, falantes)
#    transcricoes/<slug>/00-fonte/metadados.yaml

# 3. diagnóstico contra a fonte de verdade (a saída é descoberta sozinha)
python ferramentas/rc_diagnostico.py transcricoes/<slug>/00-fonte/transcricao-bruta.txt --kb KB-RC

# 4. revisar em blocos — um arquivo por bloco, nome zero-padded
#    transcricoes/<slug>/20-blocos/bloco-01.md …

# 5. adjudicar linha a linha o livro-razão (nenhuma linha pode ficar sem decisão)
python ferramentas/rc_ledger.py transcricoes/<slug> --pendencias
python ferramentas/rc_ledger.py transcricoes/<slug> --marcar "Brama=recusada" \
    --motivo "flexão legítima; o canônico Brahma já está aplicado"
python ferramentas/rc_ledger.py transcricoes/<slug> --recalcular --resumo

# 6. montar o produto e escrever a devolução
python ferramentas/rc_docx.py transcricoes/<slug>/20-blocos/bloco-*.md \
    --lexico transcricoes/<slug>/10-diagnostico/dossie-bloco.txt \
    --saida transcricoes/<slug>/30-produto/transcricao-revisada.docx \
    --titulo "Título da palestra" \
    --validar transcricoes/<slug>/10-diagnostico/variantes-propostas.csv

# 7. portões e catálogo
python ferramentas/rc_qa.py transcricoes/<slug>
python ferramentas/rc_indice.py
```

## Branches e commits

- `main` — só trabalho fechado. Nunca revisão em andamento.
- `rev/<slug>` — uma branch por transcrição.
- `kb/<lote>` — uma branch por lote de curadoria (agrega devoluções de vários vídeos).
- **Um PR por transcrição revisada**, com o template preenchido.
- Commits no imperativo, com o slug quando tocar uma transcrição específica:
  `[lemuria-terry-fabris] bloco 3: Terry Fabris confirmado pelo anúncio oficial`.
- `git mv` para mover; nunca apagar histórico. Legado vai para `docs/legado/` com data.

## Convenções que o QA cobra

| Regra | Portão |
|---|---|
| o bruto nunca é editado | G1 |
| bloco tem `## Bloco N`, rótulo de fala, nome `bloco-NN.md`, sem comentário HTML | G2 |
| nenhuma forma proibida pela Quarentena da KB no texto corrido | G3 |
| nenhuma linha do livro-razão sem decisão | G4 |
| nenhuma variante adjudicada como `aceita` sobrevive | G5 |
| o `.docx` é reproduzível a partir dos `.md` | G6 |
| o catálogo bate com o disco | G7 |
| nada acima de 5 MB, sem `~$*`, sem espaço nem acento em caminho operacional | G8 |

Detalhes e justificativas: `docs/planos/plano-de-organizacao.md` §8.2.

## Ambiente

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ferramentas/requirements.txt
python testes/test_pipeline.py     # fumaça: os scripts importam e o modelo está íntegro
```

O repositório **não** versiona o venv, nem `diagnostico.json`, nem mídia pesada.
