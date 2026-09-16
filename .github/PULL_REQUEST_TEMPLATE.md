## Transcrição

slug: `AAAA-MM-DD-titulo-curto` · status: `XX-…` → `YY-…`
vídeo: <url> · canal: <canal> · duração: <min>

## Números

| | |
|---|---|
| blocos | |
| palavras brutas → revisadas | |
| `[NOTA]` / `[A CONFIRMAR]` / `[INAUDÍVEL]` | |
| linhas do livro-razão decididas | |

## Qualidade

- [ ] `python ferramentas/rc_qa.py transcricoes/<slug>` — **G1 a G8 verdes**
- [ ] `30-produto/transcricao-revisada.docx` regenerado a partir dos `.md` (G6)
- [ ] nenhuma linha de `10-diagnostico/variantes-propostas.csv` sem `adjudicacao` (G4)
- [ ] `00-fonte/transcricao-bruta.txt` intacto — o sha256 confere com `metadados.yaml` (G1)
- [ ] `python ferramentas/rc_indice.py` rodado; catálogo atualizado neste PR

## Devolução à KB-RC

| tipo | quantidade |
|---|---|
| novos termos propostos | |
| novas variantes STT | |
| correções de ficha | |
| novos registros bibliográficos | |
| divergências factuais reportadas ao produtor | |

- [ ] itens consolidados em `KB-RC/_fila-de-curadoria.csv` (IDs: …)
- [ ] `40-devolucao/externos-novos.csv` preenchido, se houver entidade externa nova

**Lembrete:** o revisor **propõe**; quem aplica na KB-RC é o curador. Este PR não deve
conter alteração em `KB-RC/` — exceto a fila de curadoria.

## Despachos

- [ ] despacho(s) do Comandante aplicado(s): `90-registro/despachos/AAAA-MM-DD-…md`
- [ ] desvios de forma do Guia documentados em `20-blocos/notas-de-revisao.md`

## Para o curador / para o produtor

<o que precisa de decisão de outra pessoa: grafias a confirmar, cifras divergentes,
nomes sem fonte. Se não houver nada, escrever "nada pendente".>
