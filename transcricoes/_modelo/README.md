# Modelo de pasta de transcrição

**Não editar aqui.** Este diretório é o esqueleto que `ferramentas/rc_novo.py` copia para criar uma
transcrição nova:

```bash
python ferramentas/rc_novo.py \
    --slug 2026-10-02-lemuria-terry-fabris \
    --titulo "LEMÚRIA ESTÁ em busca URGENTE DE CONTATO" \
    --canal "Paranormal Experience" \
    --url https://youtu.be/9DvQf6DikA8 \
    --data 2026-10-02 \
    --bruto ~/Downloads/legenda.txt
```

O script valida o slug, copia esta árvore, substitui os marcadores `{{…}}`, grava o SHA-256 do
bruto em `metadados.yaml` e acrescenta a linha no catálogo `../_indice.csv`.

## Os estágios

| Pasta | Conteúdo | Quem escreve | Editável depois? |
|---|---|---|---|
| `00-fonte/` | bruto imutável, metadados, mídia | capturador | **nunca** (hash travado no portão G1) |
| `10-diagnostico/` | saída do motor, fila de decisão | `rc_diagnostico.py` | só pelo motor; **o ledger não se regenera por cima** |
| `20-blocos/` | a revisão propriamente dita | revisor | sim, até fechar |
| `30-produto/` | o que se lê | `rc_docx.py` | só pelo montador (portão G6 confere) |
| `40-devolucao/` | o que volta para a KB-RC | revisor | sim, até o curador aplicar |
| `90-registro/` | memória do processo e despachos | revisor + Comandante | *append-only* |

Regras completas: `docs/planos/plano-de-organizacao.md` (§3 a §6) e `docs/normas/guia-revisao-v2.md`.
