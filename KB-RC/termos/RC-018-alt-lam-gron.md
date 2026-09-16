+++
# frontmatter curatorial (Onda 2.1) — fonte: registro-mestre
codigo = "RC-018"
nome = "Alt´Lam Gron"
categoria = "Tecnologias & Artefatos"
subcategoria = "5.1 Naves / Tecnologia extraterrestre"
status = "em análise"
fontes = ["B031", "B017", "B018", "B039", "P2021-05-15", "P2020-04-25", "P2023-12-03", "P2018-12-15", "P2022-09-25"]
via = "P7-conhecimento"
confianca_fonte = "baixa"
atualizado = "2026-08-29"
+++
# Alt´Lam Gron — RC-018

## Definição Sintética

**Alt´Lam Gron** é, nas obras do acervo, a nave-entidade vinculada ao sistema de Alt´Lam (`RC-017`) — a estrutura
que hospeda os coletivos rebeldes fora do planeta. Esta ficha existia **só no cadastro** (`dados_termos.py`) desde a
migração: não havia arquivo, e por isso não havia definição. Passa a tê-la, e a definição é a que a fonte oral de
**03/12/2023** entrega: na palestra, a nave é dita **pequenininha**, é o lugar onde uma turma **se astralizou**
depois de «fazer a experiência», e é o ponto onde estão, ao mesmo tempo, os efetivos de uma família, o
processador dela e **uma visita datada** (Sofia, nos anos 2018-19). A Base ganha, com isso, o que nenhuma obra
dava: um endereço funcional para o nome.

## Contexto / Origem

**Materialização (não é criação).** O código RC-018 vivia só no cadastro — linha `("RC-018", "Alt´Lam Gron", Tecnologias & Artefatos,
5.1 Naves / Tecnologia extraterrestre…, `B031`, `B017`, `B018`, `B039`, `P2021-05-15`, `P2020-04-25`, `P2023-12-03`, RC-017; RC-058; RC-062; RC-089, False)` — sem arquivo em `termos/`. A
**Devolutiva do Curador de 29/08/2026 (D-10)** autorizou a virada `ficha=False → ficha=True` «com as 4 grafas e o
censo», dada a quantidade de dado técnico que a fonte entrega sobre o objeto. É uma de **duas** materializações
deste ciclo (a outra é `RC-040`); `RC-444 Família Cromon` foi nominalmente mantida em `ficha=False`.

Com isso:

- a Base passa de **458 para 460 arquivos de ficha** e o cadastro de **457 para 459** linhas `ficha=True`;
- o cadastro continua em **777 termos** (teto curatorial; `RC-778` não consumido) e as **1.856 relações
  permanecem intactas**: 0 aresta(s) tocam RC-018 hoje em `RELACOES` — a rede deste termo é só a que o
  cadastro já registrava, e nenhuma linha foi acrescentada;
- o cadastro lista em `relacionados` os códigos `RC-017`, `RC-058`, `RC-062`, `RC-089`:
  **não há arestas correspondentes** para eles, e três deles nem arquivo têm. Abrir essas arestas é decisão
  curatorial e continua pendente — a ficha declara a lacuna em vez de preenchê-la.

**O que a fonte muda e o que não muda (D-9, sem harmonização):** a fala de 2023 dá **um censo próprio** para o que
está a bordo — `cerca de 900, quase 1000` corrigido em seguida para `938 figuras` — e é a mesma grandeza que os
ciclos anteriores registraram para a **família** (936 em P2022-03-26; 900Q; 13 membros em `RC-491`). As quatro
magnitudes coexistem, cada uma com sua fonte e data; nada é médio, nada é arredondado, e `RC-491` **não** foi
editada por este ciclo.

**Origem do conteúdo da ampliação:** palestra `P2023-12-03 — A Rebelião de Lúcifer ainda por ser Finalizada` (na sala, 03/12/2023), blocos U0004 e U0016 do
`original.txt` — transcrição automatizada, **não conferida com o áudio**. Cada aspa foi recortada byte a byte por
`_gerar_ampliacoes_P2023-12-03.py` sobre o caça-âncoras `_aspas_P2023-12-03.py`; nada foi digitado de memória.

## Etimologia e Grafias

- **Canônico da Base:** *Alt´Lam Gron* — com **acento agudo** (`´`, U+00B4), não crase, não cedilha: é a grafia do
  cadastro e ela preside o nome da ficha.
- **Na fonte oral (P2023-12-03)** o nome aparece **degradação a baixo pelo STT em três formas** —
  `Alto Longró`, `Alto Langron`, `Alto Longron` — nunca como o par `Alt´Lam` + `Gron` do cadastro. `[REVISAR → CHANCELA 10/09/2026 · F039-L5: AGUARDA-ÁUDIO (três formas STT preservadas; cluster paralelo em RC-036: ALTA LANGRON/ALTO LONGBRON) — ver nota]`:
  nenhuma delas promotiona a grafia canônica, e nenhuma hipótese etimológica é feita a partir do TXT.
- **Vetado** (devolutiva de 29/08/2026, D-4): nenhuma das máscaras do STT (`p****`, `m****`, `b******`, `e******`)
  transita para esta ficha. As nove ocorrências ficam na apostila, com a moldura, onde o leitor vê que são máscara.

## Ampliação
### P2023-12-03 (A Rebelião de Lúcifer ainda por ser Finalizada)

- **[P2023-12-03 · ALT´LAM GRON NA FALA DE 03/12/2023]** «fizeram a experiência Alto Longró e se astralizaram junto. Se astralizaram, não é? Termina sendo. Passaram a viver dentro dessa nave e essa nave pulou umita para cima e continuou flutuando sobre o Oceano Atlântico Norte. Até hoje ela tá lá. E cerca de 900, quase 1000 seres dentro da nave, que é o» (U0004) — **Selo temporal (D-9/D-10):** fórmula oral de 03/12/2023, transcrita como dita — grafia degradada do STT preservada, nenhuma cifra arredondada, nenhuma divergência harmonizada. · ⚠️ **sem ganho de anterioridade**: a ficha já tem fonte oral **mais antiga ou igual** (`P2020-04-25`); a entrada desta fonte é de **conteúdo**, não de data.
- **[P2023-12-03 · A NAVE, O CENSO E A VISITA DATADA]** «Sofia esteve aqui nos anos 2018, 19 lá em Alto Longron, ou seja, na tal nave pequenininha dos Wall, onde cerca de 938 figuras aí estão e o processador Vol está lá.» (U0004) — D-10: materialização autorizada. A fonte entrega o que o cadastro não tinha: a grafia em quatro formas, o censo da nave (~1.000 → 938 a bordo, uns 600 e poucos na Terra) e **um evento datado** — a presença de Sofia ali em 2018-19. Nada é harmonizado com os 936/984 de ciclos anteriores: divergência selada (D-9).

### P2018-12-15 (Terra Atlantis – Aprofundamento)

- **[Alt Lam Gron, a alteração de 19.700 anos] (U0003)** «Essa ilha foi vista durante milênos como essa essa mudança, essa camuflagem que a nave esfer aplicou a ela mesmo numa alteração chamada Al Langron lá na antiguidade.» — Alt Lam Gron (RC-018): a camuflagem 'Al Langron' que a nave esfera aplicou a si mesma há 19.700 anos, entre Inglaterra e Irlanda.

### P2022-09-25 (O Contexto Espiritual da Construção de Brasília)

- **[A cidadela de Alt'Lam Gron e a nave Esferon] (U0003)** «Na verdade é a nave Esferon com cerca de 900 e pou seres lá dentro que até hoje existe, como eu disse, e fica a oeste da Irlanda.» — a nave Esferon/Alto Langron (RC-018 Alt'Lam Gron): "essa cidadela de Alangron, que a nave esfer dos V, passou a existir então com 983 membros, sendo 115 da família V, 617 L e por aí vai" (U0003: «000 anos, essa cidadela de Alangron, que a nave esfer dos V, passou a existir então com 983 membros, sendo 115 da família V, 617 L e por aí vai.»); Ielreasil e Iel Breasiel (STT "Iel Breasiel/El Breziel/Yel Brasil") "não se astralizaram, também não se submeteram a tal experiência gr" — "Desde 22.000 anos, essa cidadela de Alangron... passou a existir"; "a ilha que os rebeldes viviam nela... passou a ser conhecida como a terra de Brass, o lugar de Br" (U0003: «Aquela ilha voadora que mudava de lugar e que da Irlanda se enxergava, passou a ser conhecida como a terra de Brass, o lugar de Br, para onde Br ia quando ele não tava na Irlanda.»).


## Fontes
| Obra (sigla) | Capítulo | Página | Tipo (citação/paráfrase) |
|---|---|---|---|
| P2022-09-25 | O Contexto Espiritual da Construção de Brasília (palestra) | — | transcrição automatizada; citação |
| P2018-12-15 | Terra Atlantis – Aprofundamento (palestra) | — | transcrição automatizada; citação |
| P2023-12-03 | A Rebelião de Lúcifer ainda por ser Finalizada (palestra) | — | transcrição automatizada; citação |
| B031 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B017 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B018 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B039 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| P2021-05-15 · P2020-04-25 | — | — | fontes orais já registradas no cadastro antes deste ciclo |

## Termos Relacionados
| Termo | Código | Tipo de relação |
|---|---|---|
| Alt´Lam | RC-017 | listado no cadastro como relacionados, **sem aresta** em `RELACOES`; **sem arquivo** |
| Alt´Lam | RC-017 | par nomeador — `RC-017` também está **sem arquivo**; nenhum dos dois recebeu materialização |
| Espheron | RC-058 | listado no cadastro como relacionados, **sem aresta** em `RELACOES`; arquivo existe (P5d) |
| Experiência Gron | RC-062 | listado no cadastro como relacionados, **sem aresta** em `RELACOES`; **sem arquivo** |
| Ion Crom | RC-069 | associado |
| Processador Val | RC-089 | listado no cadastro como relacionados, **sem aresta** em `RELACOES`; arquivo existe |
| Processador Val | RC-089 | a fala põe o processador da família **dentro** da nave: mesma cena, duas fichas |
| Val Eno | RC-123 | associado |
| Val Tam | RC-132 | associado |
| Cidades Voadoras | RC-234 | associado |

## Observações

* **[REVISAR → CHANCELA 2026-09-06 · F041-L5: ISOLAMENTO (orfandade 1× no corpus — precedentes Olga/deibir) — ver nota] — o censo é da fala, não da Base.** «938 figuras» e «uns 600 e poucos» na Terra pertencem a um só
  fôlego de 03/12/2023 e não foram reconciliados com os 936/900Q dos ciclos anteriores nem com os 13 membros de
  `RC-491`. Registrar a divergência datada é o serviço desta ficha; resolvê-la é decisão curatorial.
* **[REVISAR → ENCERRADO 2026-09-06 · F042-VARREDURA: RATIFICADO — registro de fala/leitura do autor ratificado — ver nota] — evento datado.** A visita («Sofia esteve aqui nos anos 2018, 19») é a única data *recente* que esta
  fonte aplica a um objeto da malha; não virou relação, não virou cronologia da ficha e não foi confrontada com as
  datas de aparição já registradas em outras fichas.
* Esta ficha **não** afirma que a nave exista fisicamente no Atlântico Norte: transcreve, com endereço, a afirmação
  de que ela «pulou umita para cima e continuou flutuando» como a fonte a disse, em 2023.


> Notas de processo: 3 bloco(s) arquivado(s) VERBATIM em `notas/fichas/RC-018.md` (migração 2.4 — 12/09/2026). Histórico de mutirão/governança — consultar lá, não reescrever.
