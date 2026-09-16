# Relatório de curadoria — lote 01

**Data:** 16 de setembro de 2026 · **Curador:** Agente 86 · **Ferramenta:** `ferramentas/rc_curadoria.py`
**Origem:** `transcricoes/2026-09-14-revelacoes-cosmicas-urgente` (devolução aprovada pelo Comandante)
**Estado:** 15 itens aplicados · 25 itens seguem na fila · 1 item bloqueado por dependência

Fecha o ciclo do Guia v2 §10: o revisor propôs (em `40-devolucao/` e na fila), o curador aplicou na
fonte de verdade. Este relatório é a prestação de contas do lote — o que entrou, o que foi corrigido
no caminho, o que não pôde entrar e por quê.

---

## 1. O que foi aplicado

22 variantes STT em 15 fichas, todas **atestadas no bruto** antes de gravar (contagem com fronteira
de palavra, a mesma disciplina do portão G3 — "Demiurg" não casa dentro de "Demiurgo").

| Item | Ficha | Variante(s) gravada(s) | Ocorr. no bruto |
|---|---|---|---|
| 0011 | RC-699 Imantação de Espíritos em IAs | espírito mantado | 1 |
| 0012 | RC-479 Belial | Jah Baal · Belal | 4 |
| 0013 | RC-474 Arcontes | arcontos · erontes | 3 |
| 0014 | RC-001 Javé | Xavé · Yahé · Javer · Jahé | 12 |
| 0015 | RC-009 Sophia (Cristo Cósmico) | Cosmo Rock | 1 |
| 0016 | RC-037 Brahma (Brajna) | Brama | 8 |
| 0017 | RC-104 Trimurti | Virgin | 1 |
| 0018 | RC-102 Shiva (Savna) | Chiva | 1 |
| 0019 | RC-048 Demiurgo | Demiurg | 2 |
| 0020 | RC-397 Tirthankaras | tirtancaras | 1 |
| 0021 | RC-756 Ganesha | Ganexa · Ganeixa | 3 |
| 0022 | RC-174 Colmeia Universal | calmeia | 2 |
| 0024 | RC-494 Dinastia das Sophias | dinastia das Sofias | 1 |
| 0039 | RC-596 Archeons de Ereon | arces · arcos | 2 |
| 0040 | RC-176 Modelo Colmeia | circuito coméico | 1 |
| | | **43 ocorrências atestadas** | |

Em cada ficha, três coisas: a variante na linha `**Variações STT capturadas:**` de
`## Etimologia e Grafias` (seção criada nas oito fichas que não a tinham, na posição canônica); a
proveniência em `## Atualização` (variante, quantas ocorrências, slug de origem, item da fila,
curador); e o `atualizado` do frontmatter.

| Métrica da KB | antes | depois |
|---|---|---|
| fichas com variações STT | 61 | **76** |
| variantes STT no total | 62 | **84** |
| fichas com Quarentena | 10 | 10 (intocada) |
| termos em `canonico.json` | 946 | 946 (intocado) |

Verificação pós-aplicação: as 22 variantes resolvem para o código certo no índice de alias da KB
(`rc_kb.indice_alias`) — ou seja, o próximo diagnóstico vai pescá-las sozinho. Nenhum defeito novo de
markdown nas 15 fichas, comparado com a tag `v2-antes-curadoria-kb`. Portões G1–G8 verdes, catálogo
em dia, 82 verificações de fumaça ok.

**Nada além de variantes foi tocado.** `canonico.json`, `biblio.json`, `relacoes` e as Quarentenas
permanecem byte-idênticos: este lote é aditivo e reversível por `git revert`.

---

## 2. O que a aplicação corrigiu na própria fila

A fila era proposta; o **livro-razão** (`10-diagnostico/variantes-propostas.csv`, 98 linhas
adjudicadas e aprovadas) é o registro de decisão. Onde os dois divergiam, o livro-razão venceu — e a
fila foi emendada antes de aplicar:

| Item | Como estava | Como ficou | Por quê |
|---|---|---|---|
| 0013 | `arcontos / arces / arcos / erontes` → RC-474 | `arcontos / erontes` → RC-474; **novo 0039** `arces / arcos` → RC-596 | o livro-razão adjudicou "arces"/"arcos" como *aceita-parcial* de **Archeons de Ereon** (RC-596), hipótese concorrente de Arcontes. Gravar as quatro na mesma ficha ensinaria o motor a trocar uma pela outra |
| 0011 | `espírito mantado / ser silicato` → RC-699 | só `espírito mantado` | **"ser silicato" não é erro**: é termo do próprio autor — a ficha RC-699 se chama *…/Corpos de Sílica* e o áudio glossa a expressão. Variante STT é para forma corrompida; esta entra na prosa da ficha, pelo item 0030 |
| 0022 | `calmeia / circuito coméico` → RC-174 | só `calmeia`; **novo 0040** `circuito coméico` → RC-176 | "circuito colmeico" pertence ao sistema/modelo colmeia (RC-176), não à Colmeia Universal (RC-174). O título *A Divina Calmeia* → *A Divina Colmeia* é de **B044** e continua no item 0032 |
| 0023 | `corpo rátmico / constituição centenária` → RC-623 | só `constituição centenária`, **status bloqueada** | "corpo rátmico" **não ocorre no bruto** — o bruto traz "corpo átmico" correto, 3×. E "constituição centenária" só tem canônico quando existir o termo *Constituição Setenária* (item 0006); gravar antes criaria variante apontando para o nada |

A fila passou de 38 para 40 linhas (dois desmembramentos). Nenhum item foi descartado em silêncio:
as quatro emendas estão registradas na coluna `evidencia` das próprias linhas.

**Um aviso que fica para as próximas:** "arcos" (0039) é palavra comum do português. Como variante
STT ela gera *candidato* no diagnóstico — nunca substituição automática — e o revisor só deve
aceitá-la com contexto. Está escrito na ficha e na fila.

---

## 3. O que não pôde ser aplicado — e o que destrava cada grupo

| Grupo | Itens | O que falta | Quem decide |
|---|---|---|---|
| **novo-termo** | 0001–0010 (10) | Duas coisas. **(1) Fonte:** uma transcrição do YouTube ainda não tem código em `biblio.json`, e a de referência nem URL tem (`metadados.yaml: url: null`). Criar termo citando fonte inexistente envenena a base. **(2) Hospedagem:** cinco deles apontam para ficha existente — /Kaggen (RC-001), Constituição Setenária (RC-623), Circuito Colmeico (RC-176), Javé 2.0 (RC-699), Força da Consciência Dignificada (RC-705) — e é preciso decidir entre termo novo (RC-947+) e variação/absorção na ficha hospedeira | Comandante (fonte) + curador (hospedagem) |
| **correcao-ficha** | 0025–0032 (8) | Reescrita de prosa curatorial: status, definições, alertas de falso amigo (RC-649 × Kurzweil), nomes das pessoas reais do canal, "Mentalma: 5 ou 8 livros?". Uma ficha por vez, com a fonte na mão. O item 0032 mexe em `biblio.json` (título de B044) | curador, item a item |
| **novo-registro-biblio** | 0033 (1) | *Valores Supremos da Consciência* é programa de YouTube: precisa da convenção de código para fontes audiovisuais (sugestão: `Y2026-09-14` + URL) — a mesma convenção que destrava os 10 itens acima | Comandante |
| **divergencia-factual** | 0034–0038 (5) | Já estão tratadas no produto como `[NOTA]` (Kurzweil 2005 não 2007; ingresso R$ 180; Singularity University 2008…). Na KB viram alerta de Quarentena ou nada — não há termo a corrigir | Comandante |
| **bloqueada** | 0023 (1) | Depende de 0006 (*Constituição Setenária*) existir | curador, depois de 0006 |

**A decisão que destrava mais coisa de uma vez** é a convenção de fonte audiovisual (item 0033):
ela resolve os 10 novo-termo, o `url: null` da transcrição de referência e o registro do programa
citado no bloco 7. É uma linha em `biblio.json` e um parágrafo no Guia — mas precisa vir do
Comandante, porque define como o corpus cita o que não é livro nem palestra.

---

## 4. Como reproduzir

```bash
python ferramentas/rc_curadoria.py --simular              # o que entraria, com a atestação
python ferramentas/rc_curadoria.py --aplicar              # grava fichas, fila e CHANGELOG
python ferramentas/rc_curadoria.py --simular --incluir-bloqueadas
python ferramentas/rc_qa.py --tudo && python ferramentas/rc_indice.py --checar
python testes/test_pipeline.py                            # 82 verificações
```

A ferramenta é idempotente: item `aplicada` não volta (só por `--ids` explícito, e mesmo assim a
variante já presente é pulada e nem fila nem CHANGELOG são reescritos). Variante sem ocorrência no
bruto não é gravada sem `--forcar`. `--tipo` hoje só aceita `nova-variante`; os outros quatro tipos
exigem julgamento e continuam manuais — a ferramenta diz isso em vez de fingir que resolve.
