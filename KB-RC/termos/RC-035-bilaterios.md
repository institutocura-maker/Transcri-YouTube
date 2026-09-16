+++
# frontmatter curatorial (Onda 2.1) — fonte: registro-mestre
codigo = "RC-035"
nome = "Bilatérios"
categoria = "Seres & Entidades"
subcategoria = "1.7 Híbridos / Seres de transição"
status = "em análise"
fontes = ["B031", "P2019-08-25", "P2024-05-04", "P2025-02-16", "P2024-04-13", "P2021-05-15", "P2020-04-25", "P2023-12-03", "P2022-05-07"]
via = "P7-conhecimento"
confianca_fonte = "baixa"
atualizado = "2026-08-29"
+++
# Bilatérios — RC-035

## Definição Sintética

A Base cataloga **Bilatérios** como classe de seres em estágio de transição (Seres & Entidades / 1.7), e não como termo anatômico: é o cadastro quem assim o classifica, e a ficha não reinterpreta a classificação. O que a fonte oral de 03/12/2023 acrescenta é um uso — a afirmação, no meio de um raciocínio sobre cérebros, de que o modelo humano seria bilatério. Fica registrado com endereço. A tensão entre o uso da fala (atributo de cérebro) e a categoria do cadastro (classe de seres) é declarada `[REVISAR → CHANCELA 10/09/2026 · F040-L5: TENSÃO REGISTRADA (uso da fala × categoria do cadastro; não fundir) — ver nota]`, não resolvida.

## Contexto / Origem

**Materialização (não é criação).** `RC-035` vivia só no cadastro: linha em `ferramentas/dados_termos.py`, `ficha=False`, sem arquivo em `termos/`. A virada foi autorizada pelo despacho do Curador de 29/08/2026, na linha que trata das ordens nomeadas sem arquivo, e executada pelo Motor Único em `ciclos/P2023-12-03/`.

Com isso:

* a Base ganha um **arquivo**; 0 termos novos e **0 relações novas** por este ciclo;
- o cadastro lista 3 código(s) em `relacionados`: 1 com aresta correspondente em `RELACOES` e 0 sem arquivo de ficha. A ficha **declara** a lacuna em vez de preenchê-la — abrir aresta é decisão curatorial;
- as fontes já registradas no cadastro são `B031`, `P2024-05-04`, `P2025-02-16`, `P2024-04-13`, `P2021-05-15`, `P2020-04-25`, `P2023-12-03`.

**Origem do conteúdo da ampliação:** palestra `P2023-12-03 — A Rebelião de Lúcifer ainda por ser Finalizada` (03/12/2023, na sala). Transcrição automatizada, **não conferida com o áudio**; cada aspa foi recortada do `original.txt` pelo índice de âncoras do motor e conferida byte a byte pelo portão B. Nada foi digitado de memória.

## Observações sobre o Estado da Malha

* **[REVISAR → ENCERRADO 2026-09-06 · F040-L4: RATIFICADO — divergência registrada, não costurada — ver nota] — uso da fala × categoria do cadastro.** A frase de 03/12/2023 trata bilatério como atributo de cérebro; o cadastro o lista como classe de seres. A divergência é registrada, não costurada, e nenhuma ficha de anatomia foi tocada (D-7: obsolescência anatômica mora em `RC-631`/`RC-632`).
* **Trava aplicável**: D-7 (anatomia sem código novo) · D-4 (nenhuma máscara transita) · veto de trânsito por nomear classe de seres.

## Ampliação
### P2023-12-03 (A Rebelião de Lúcifer ainda por ser Finalizada)

- **[P2023-12-03 · BILATÉRIOS NA FALA DE 03/12/2023]** «O nosso é bilatério.» (U0038) — **Selo temporal (D-9/D-10):** fórmula oral de 03/12/2023, transcrita como dita — grafia degradada do STT preservada, nenhuma cifra arredondada, nenhuma divergência harmonizada. · ⚠️ **sem ganho de anterioridade**: a ficha já tem fonte oral **mais antiga ou igual** (`P2020-04-25`); a entrada desta fonte é de **conteúdo**, não de data.

### P2022-05-07 (Shiva, o Projeto Talm e os Mistérios de Awaylengam)

- **[Bilatérios — antes do cérebro, o corpo] (U0003)** «Então, primeiro, antes de surgir, desculpa, um cérebro bilatério, teve que surgir um corpo bilatério.» — a bilateralidade corporal (produto de Awaylengan) precede a cerebral; ver RC-093.

## Fontes
| Obra (sigla) | Título | Página | Tipo |
|---|---|---|---|
| P2022-05-07 | Shiva, o Projeto Talm e os Mistérios de Awaylengam (palestra) | — | transcrição automatizada; citação |
| P2023-12-03 | A Rebelião de Lúcifer ainda por ser Finalizada (palestra) | — | transcrição automatizada; citação |
| B031 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |

## Termos Relacionados
| Termo | Código | Tipo de relação |
|---|---|---|
| Biodemos | RC-036 | **sem aresta** em `RELACOES`; arquivo existe |
| Radiatas | RC-093 | **sem aresta** em `RELACOES`; arquivo existe |
| Cérebro Radiata | RC-631 | ← distingue-se-de |
| Fornos Replicadores (naves/estações de semeadura de vida do Projeto Talm; Awayen, Awaylengan e Awaymaion) | RC-771 | ← relaciona-se-a |
| Forno de Awaylengan (forno de Shiva — o primeiro a funcionar) | RC-837 | associado |

## Ampliação
### P2019-08-25 (Os Três Fornos Replicadores do Projeto Talm)

- **[P2019-08-25 · A FONTE ORAL FUNDADORA DOS BILATÉRIOS — O NIDANA B]** (predata P2023-12-03 em 4 anos):
- "nesse último bilhão de anos surgiu os primeiros seres bilatérios. Até então só tinha radiatas é isso. Radiatas são seres cérebro onde só gira um sistema fechado. Bilatérios são seres que têm um cérebro, mas que tem duas componentes rodando. Chamado hemisfério direito, hemisfério esquerdo" (STT);
- a origem: o **Nidana B** (junção Awaylengan + Awaymaion): "criaram Nidana B, ou seja, o ovo cov" (STT) — nova versão do código que juntou a experiência dos dois fornos;
- a consequência na Terra: "já eram seres bilaterais, porque a tal molécula mãe" (STT) que foi lançada aqui "já vinha como sendo Nidana B" — a explosão cambriana e a evolução até os humanos;
- **Materialização decidida por Devolutiva O-3** — em vez de criar um código duplicado (RC-838), a fonte fundadora de 2019 amplia a ficha **RC-035 Bilatérios** já existente (correção do dossiê O-2, que por erro de busca não a localizara).



> Notas de processo: 3 bloco(s) arquivado(s) VERBATIM em `notas/fichas/RC-035.md` (migração 2.4 — 12/09/2026). Histórico de mutirão/governança — consultar lá, não reescrever.
