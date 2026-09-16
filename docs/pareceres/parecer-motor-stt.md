# Parecer de engenharia — motor de STT na entrada da esteira

**Projeto:** Transcri-YouTube · **Data:** 16 de setembro de 2026 · **Elaborado por:** Agente 86 (Arena.ai Agent Mode)

**Objeto:** decidir se o STT do **NotebookLM** substitui o STT do **YouTube** como matéria-prima em
`transcricoes/<slug>/00-fonte/`, medindo os quatro eixos do despacho de 16/09/2026.

**Status: COMPLETO.** Os dois lados foram medidos com a mesma régua, no mesmo dia, sobre o mesmo
áudio. Saída bruta do instrumento: `docs/pareceres/parecer-motor-stt-medicao.md` (gerada, não
redigida) e `docs/pareceres/perfil-stt.json`.

---

## 0. Sumário executivo

**Veredito: adotar a saída do NotebookLM como TEXTO DE TRABALHO, e nunca como fonte. `00-fonte`
continua sendo o STT cru do YouTube.** Três razões, todas medidas:

**1. A comparação pedida não existe como foi formulada — e isso é a descoberta mais importante do
experimento.** Não há dois motores. Há **um** reconhecimento de fala (o do YouTube) e uma **camada
de reescrita** por cima. A evidência é quantitativa e independente:

| prova | A (YouTube) | B (NotebookLM) | leitura |
|---|---:|---:|---|
| palavras | 18.966 | 18.975 | diferença de **+9 palavras** em 19 mil (+0,05%) |
| divergência lexical (multiconjunto) | — | **3,00%** | 280 palavras de A ausentes em B, 289 de B ausentes em A |
| Jaccard de vocabulário | — | **0,929** | paráfrase derrubaria este número |
| hapax (palavras de ocorrência única) em comum | 1.721 | 1.735 · **93% em comum** | reescrita trocariam justamente estas |
| marcadores orais com contagem **idêntica** | — | **9 de 16** | então 132=132, uhum 31=31, cara 26=26, tipo 25=25, ó 21=21, tô 20=20, sabe 17=17, quer dizer 5=5, sei lá 2=2 |
| repetição "blá blá" | 22 | 22 | mesmo gaguejo, mesmo lugar |

Dois ASR diferentes erram de jeito diferente. Estes erram **igual**. Portanto "trocar o STT do
YouTube pelo do NotebookLM" não é uma opção disponível; a opção real é **pôr ou não pôr um LLM
entre o reconhecimento e o revisor**. O parecer responde a essa.

**2. A camada ganha de forma esmagadora no eixo que mais custa mão de obra hoje, e não ganha nada no
segundo mais caro.** Pontuação e segmentação passam de trabalho de reconstrução a trabalho de
conferência (0,22 → 15,93 sinais por 100 palavras; mediana de 331 → 11 palavras por sentença; 8 →
295 segmentos nativos). Disfluência **não muda**: 40,49 → 40,79 marcas por 1.000 palavras, empate
técnico. O contrato editorial de nível LEVE continua inteiro sobre a mesa do revisor.

**3. A camada edita o conteúdo em silêncio — e censurou palavras que interessam a esta KB.** Cinco
tokens foram mascarados com asterisco, todos inexistentes em A:

| trecho | A (STT cru) | B (NotebookLM) | natureza |
|---|---|---|---|
| "os europeus viam Jesus como um…" | **bandido** | `b******` | censura de palavra substantiva em trecho teológico |
| "não mais um … judeu" | **bandido** | `b******` | idem, segunda ocorrência |
| "especialistas em fazer…" | **merda** | `m****` | censura de palavrão |
| "ih vai dar …" | **merda** | `m****` | idem |
| "fiz … a advogado defesa não fez" | **merda** | `m****` | idem |

`b******` não é palavra da língua portuguesa. Se B entrasse em `00-fonte` como bruto, essas cinco
palavras estariam **perdidas**: o QA G1 confere sha256, não conteúdo, e não há nenhum portão hoje
que compare o produto contra o bruto palavra a palavra. É exatamente o princípio que a casa já
adotou — bruto imutável, decisão registrada — que impede o dano.

**Contra o critério pré-registrado (§4), o placar foi:** B **ganhou o eixo 1** (4 de 4 limiares),
**perdeu o eixo 2**, **perdeu o eixo 3** pelo limiar composto (342 itens contra o teto de 197) e
**quebra 1 das 4 suposições** de integração. A regra §4.4(a) mandava trocar. A evidência de
proveniência e de censura — que a regra não previa, porque ninguém sabia que era o mesmo ASR —
converte "trocar" em "acrescentar camada com guarda". Registro os dois desfechos: o que a regra
pré-registrada disse, e o que a medição acrescentou a ela.

**Custo de código da adoção recomendada: 5 itens, cerca de um dia, listados em §8.** O maior deles
não é a quebra de integração — é o portão novo que falta (comparar produto × bruto), que é o que
teria pego a censura sozinho.

---

## 1. Identificação dos dois arquivos

| | A — YouTube | B — NotebookLM |
|---|---|---|
| caminho | `transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-bruta.txt` | `Opcao-B.txt` (raiz, commit `6eddae0`, enviado pelo Comandante via upload web do GitHub) |
| sha256 | `34f9bcf418bf6acc7a42b40c71a915a4ac72132eb4b894036711a93823a095fc` | `5aa247f3487752423e1eb4056c0fd54c4af5394a563411d3e5e5b95110e714d7` |
| bytes / linhas | 106.243 · 15 | 109.452 · 300 |
| cabeçalho | linhas 0–11 | linhas 0–11, **idêntico ao de A**, mais um separador `====` na linha 10 |
| corpo | **1 linha** de 101.468 chars | **288 linhas**, um turno de fala por linha |
| fim de linha | CRLF | CRLF |
| estágio na esteira | bruto | solto (leitura de bruto — mesma classe) |

O cabeçalho de B é cópia do de A, inclusive o "Guia de fontes". Isso tem duas consequências que
precisam ficar escritas: a prosa do guia **não** é saída do NotebookLM (é a captura original), e a
presença do marcador "Transcrição Automática" em B é mérito de quem preparou o arquivo, não do
motor — um export futuro do NotebookLM sem o cabeçalho da casa quebraria também essa suposição
(§7, item 3 do custo pré-registrado).

---

## 2. O instrumento e os quatro defeitos de régua

`ferramentas/rc_perfil_stt.py` mede os quatro eixos do despacho sobre qualquer arquivo de STT e, com
dois argumentos, imprime o comparativo com coluna "melhor". Com `--com-diagnostico` executa o motor
da casa inteiro sobre cada lado — é a medida direta de "carga das ferramentas `rc_*`", porque é a
mesma ferramenta que a esteira usa. Roda em 15 s nos dois arquivos.

A régua vem da KB-RC pela mesma porta que o resto da esteira usa: **956 termos, 1.085 superfícies
canônicas, 124 corrupções mapeadas, 5 formas proibidas pela Quarentena (24 com o livro-razão desta
transcrição), 37 formas Externos e 32 canônicos Externos.**

Quatro defeitos da régua foram encontrados e corrigidos **antes de qualquer conclusão**. Os três
primeiros eram meus; o quarto é do motor da casa e continua lá — está documentado em §7 como item de
código.

| # | defeito | efeito se não corrigido | estado |
|---|---|---|---|
| 1 | marcador oral contado no texto normalizado: `norm("ó") == "o"` | 499 falsos positivos; disfluência de A inflada de 768 para 1.308 marcas (**+71%**) | corrigido + teste |
| 2 | `Variações` da ficha (equivalência **conceitual**, Guia §5) contada como corrupção | apontava "humano"×58 e "espirito"×12 como erro de motor; taxa de confiança caía de 0,8262 para 0,6040 | corrigido + teste |
| 3 | `externos.csv` lido sem pular os comentários `#` que antecedem o cabeçalho | zero entidades Externos medidas — justamente a camada que protege "Ray Kurzweil" | corrigido + teste |
| 4 | `rc_diagnostico.py:372` procura **sequências capitalizadas** sem registro na base | num STT pontuado toda inicial de frase é capitalizada: a lista de "ausentes" de B encheu de verbo e advérbio comum (211 formas, das quais só 76 são candidatas reais) | **não corrigido no motor**; o perfil separa os baldes e o parecer registra (§6.3) |

Teste de fumaça da casa: **105 → 136 verificações, 0 falhas.** QA G1–G8 verde, bruto de A intacto.

---

## 3. Critérios de decisão pré-registrados — e o resultado contra cada um

Os limiares abaixo foram fixados no commit anterior à chegada de B (`cb291f1`), quando só existia a
linha de base A. Nenhum foi revisto depois de visto o resultado; onde a medição mostrou que o limiar
estava mal especificado, isso está declarado em vez de corrigido em silêncio.

### 3.0 Guarda de comparabilidade

| guarda | limiar | resultado |
|---|---|---|
| mesma extensão de áudio | B entre 90% e 110% das palavras de A (17.069 a 20.862) | **18.975 — PASSA com folga (+0,05%)** |
| mesmo estágio | ambos em estado bruto | **PASSA** (A "bruto", B "solto": mesma classe de leitura) |
| diacríticos comparáveis | perda de diacríticos equivalente | **PASSA** — os dois acentuam |

Sem a guarda, nada do resto valeria: ferramenta que resume devolve síntese, e síntese parece limpa
em toda métrica de qualidade.

### 3.1 Eixo 1 — pontuação e segmentação: **B GANHA, 4 de 4**

| limiar pré-registrado | A | B | resultado |
|---|---:|---:|:---:|
| sinais por 100 palavras **> 2,0** | 0,22 | **15,93** | ✅ 72× |
| mediana de palavras/sentença **< 60** | 331 | **11,0** | ✅ 30× |
| maior sentença **< 200 palavras** | 2.604 | **75** | ✅ |
| segmentação nativa **≥ 100 unidades** | 8 | **295** | ✅ *ver ressalva* |

Detalhe de B: 1.328 sentenças; 1.694 vírgulas (89,28/1.000 palavras); 1.144 pontos (60,29/1.000);
184 interrogações; 64,3 palavras por segmento.

> **Ressalva declarada.** O limiar foi escrito contra "parágrafos separados por linha em branco",
> convenção do produto desta casa. B quebra por linha, sem linha em branco: tem **5** parágrafos
> nesse critério e **295** segmentos no critério de quebra. A métrica foi corrigida no instrumento
> (passou a medir os dois) e aplicada igualmente a A, que tem 8. A substância do limiar — cem ou
> mais unidades de segmentação nativa — é atendida por 295. Registro que o limiar, como estava
> escrito, teria reprovado B por um detalhe de formatação.

Referência interna: o produto final curado desta transcrição tem **151 parágrafos** (QA G6). B
entrega 295 turnos de ~64 palavras — mais fino que o produto. O trabalho do revisor deixa de ser
*descobrir* fronteiras e passa a ser *juntar* turnos.

### 3.2 Eixo 2 — disfluência: **B PERDE**

| limiar pré-registrado | A | B | resultado |
|---|---:|---:|:---:|
| marcas por 1.000 palavras **≤ 20,0** | 40,49 | **40,79** | ❌ |
| repetições de palavra imediata **≤ 57** | 115 | **127** | ❌ |

Totais: 768 × 774 marcas (+0,8%). Marcadores orais: 619 × 611. Bigramas 25 × 26, trigramas 9 × 10,
prolongamentos 4 × 11.

A diferença de 12 repetições a mais em B é ruído de palavras funcionais, não conteúdo novo:
"que" 17→14, "não" 10→13, "blá" 22→22 nos dois. **A camada de reescrita não limpa disfluência** —
ela preserva "tão pequeno, tão pequeno, tão pequeno, tão pequeno" inteiro, o que é fidelidade, não
defeito, mas significa que o contrato de nível LEVE continua custando exatamente o mesmo.

### 3.3 Eixo 3 — fidelidade terminológica: **B PERDE pelo limiar composto, ganha nos três acessórios**

| limiar pré-registrado | A | B | resultado |
|---|---:|---:|:---:|
| carga terminológica total **≤ 197 itens** | **263** | **342** | ❌ |
| taxa de confiança **> 0,8262** | 0,8262 | **0,8476** | ✅ |
| formas proibidas **≤ 37 ocorrências** | 37 | **10** | ✅ |
| Externos corrompidos **< 56 ocorrências** | 56 | **51** | ✅ |

Composição da carga (o que o `rc_diagnostico.py` gera sobre cada arquivo):

| componente | A | B |
|---|---:|---:|
| linhas no livro-razão | 132 | 131 |
| — propostas a adjudicar | 44 | 47 |
| — informativas (artigo/flexão) | 51 | 48 |
| — sementes do Guia já aprovadas | 36 | 36 |
| formas ausentes da base (bruto) | 131 | **211** |
| **carga total** | **263** | **342** |

Placar completo da tabela comparativa (26 métricas, em `parecer-motor-stt-medicao.md`): **B melhor
em 11, A melhor em 9, empate/sem critério em 6.** A leitura que interessa não é o placar, é o
padrão: B ganha tudo que é **forma** (pontuação, segmentação, sentença) e A ganha tudo que é
**volume de curadoria** — em boa parte porque a régua da casa conta mais candidatos quando o texto é
pontuado (§5).

### 3.4 Eixo 4 — integração: **B é 3 de 4; uma quebra custa código, uma premissa foi superada**

| suposição da esteira | A | B | desfecho em B |
|---|:---:|:---:|---|
| `rc_novo.py`/`rc_indice.py` medem o corpo como a linha mais longa | ✅ 98,9% | ❌ **3,9%** | **CUSTA CÓDIGO** — `corpo_palavras` sairia fracionário, sem erro e sem aviso |
| `rc_diagnostico` separa cabeçalho pelo marcador "Transcrição Automática" | ✅ | ✅ | compatível (por cópia do cabeçalho, não por mérito do motor) |
| diarização opção B (rótulos inferidos pelo revisor) | ✅ nenhum | ✅ nenhum | compatível — B **não** traz nome de falante; traz 288 turnos sem rótulo |
| Guia §8 (pontuação é corretiva, o STT não traz) | ✅ 2,2/1.000 | **159,3/1.000** | **PREMISSA SUPERADA** — a norma passa a ser de conferência |

Os três estados importam: "custa código" é preço pago uma vez; "premissa superada" é trabalho manual
que **deixa de existir**. Confundir os dois levaria a recusar B por "incompatibilidade" exatamente
no ponto em que ele mais ajuda.

---

## 4. A pergunta literal do despacho: B alucinou menos ou mais nas entidades dos lotes 01 e 02?

**Resposta: praticamente igual, com vantagem pequena de B — e a diferença que aparece nos totais é
da régua, não do motor.** Contagem de ocorrências das formas canônicas e das variantes STT
registradas na KB, nos termos dos dois lotes:

| código | termo | canônico A | canônico B | corrupto A | corrupto B |
|---|---|---:|---:|---:|---:|
| RC-947 | Eu Parasitário | 12 | 12 | 0 | 0 |
| RC-948 | /Kaggen | 0 | 0 | 3 | 3 |
| RC-949 | Tom Teltan | 2 | 2 | 0 | 0 |
| RC-950 | Avalokiteshvara | 0 | 0 | 3 | 2 |
| RC-952 | Constituição Setenária | 2 | 2 | 2 | 2 |
| RC-953 | Circuito Colmeico | 0 | 0 | 1 | 0 |
| RC-954 | Planeta de Expiação e Provas | 2 | **0** | 0 | 0 |
| RC-955 | Javé 2.0 | 2 | 2 | 0 | 0 |
| RC-956 | Força da Consciência Dignificada | 4 | 4 | 0 | 0 |
| RC-001 | Javé | 60 | 60 | 12 | 10 |
| RC-037 | Brahma | 0 | 0 | 8 | 8 |
| RC-048 | Demiurgo | 8 | 8 | 2 | **0** |
| RC-474 | Arcontes | 10 | 10 | 3 | 2 |
| RC-479 | Belial | 10 | 8 | 4 | 3 |
| RC-756 | Ganesha | 0 | 0 | 3 | **4** |
| **total** | | **113** | **109** | **51** | **43** |

Leituras que valem mais que o total:

* **/Kaggen é corrompido de forma idêntica nos dois** (3 ocorrências de `kaagen`/`kaagem`). Um
  segundo ASR não erraria o mesmo nome raro do mesmo jeito — é a mesma escuta.
* **RC-048 Demiurgo: B eliminou os dois truncamentos `demiurg`** que A trazia. A camada de reescrita
  completa palavra truncada — ganho real.
* **RC-756 Ganesha: B piorou** (4 grafias contra 3, `ganexa` incluído). A camada também inventa.
* **RC-954 sumiu em B por uma microedição:** A diz "planeta de expiação **e** provas"; B diz
  "planeta de expiação **em** provas". Uma preposição trocada derrubou o casamento com o canônico do
  lote 02. É o retrato do risco: a edição é pequena demais para notar lendo, e grande o bastante
  para quebrar a automação.
* **RC-953:** A traz "as calmeias começaram a colapsar"; B harmonizou para "as colmeias". Aqui a
  camada corrigiu uma corrupção — mas corrigiu **uma** das duas ocorrências, o que produz
  inconsistência interna, exatamente o que a curadoria existe para evitar.

Dispersão de grafias por entidade (do livro-razão, sem artigos grudados pela janela): A **75 grafias
para 58 entidades** (média 1,29); B **77 para 63** (média **1,22**). B espalha por mais entidades,
mas com menos variantes por entidade.

---

## 5. Onde a régua mente: o quarto defeito, quantificado

O `rc_diagnostico` procura **sequências capitalizadas** sem registro na base. Num STT que não pontua,
a heurística é ótima: maiúscula só aparece em nome próprio. Num STT pontuado, toda inicial de frase
é maiúscula. Separando os baldes — a lógica está implementada em `rc_perfil_stt.classificar_ausentes`:

| balde | A | B |
|---|---:|---:|
| janela de 2–4 palavras (recorte, não entidade) | 71 formas · 87 occ | 83 formas · 98 occ |
| palavra única do vocabulário comum (guarda de 1.884 formas) | 8 · 15 | 26 · 59 |
| inicial de frase (a palavra também ocorre em minúscula no texto) | 11 · 21 | 26 · 44 |
| **candidata real a termo novo** | **41 formas · 52 occ** | **76 formas · 100 occ** |

Mesmo depois da limpeza B apresenta 1,9× mais candidatas — e ainda assim parte do resíduo é artefato:
entre as 76 estão "Desintegrou", "Oremos", "Acreditem", "Estudando", "Resoluções", verbos e
substantivos capitalizados de ocorrência única que a heurística não distingue de nome próprio. As
candidatas genuínas que B acrescenta são entidades reais que A grafou de outro jeito ou não
capitalizou: Trump, Fausto, Matrix, Miami, Trácia, Cristian, Yahvé, Frankstein.

**Conclusão honesta do eixo 3:** não há evidência de que B alucine **mais** entidades. Há evidência
sólida de que a régua da casa **conta mais candidatos** quando o texto é pontuado. O limiar composto
de 197 itens, aplicado sobre uma métrica contaminada por capitalização, reprovou B por um efeito da
virtude de B. Registro o resultado pré-registrado como **derrota no eixo 3** e registro também que a
métrica precisa da versão 2 (ciente de inicial de frase) antes de ser usada de novo — correção que
vale para os dois lados e que está orçada em §8, item 2.

---

## 6. Arquitetura recomendada

Não é "trocar o arquivo de `00-fonte`". É separar **fonte** de **texto de trabalho**:

```
00-fonte/
  transcricao-bruta.txt           ← STT cru do YouTube. IMUTÁVEL, sha256, portão G1.
                                     Continua sendo a autoridade sobre o que foi dito.
  transcricao-pontuada.txt        ← saída do NotebookLM. DERIVADO de trabalho, versionado,
                                     com sha256 próprio e proveniência registrada.
  metadados.yaml                  ← ganha: motor_derivado, data_derivado, sha256_derivado,
                                     divergencia_lexical, palavras_mascaradas
```

Com um portão novo no QA — **G9, divergência** — que compara o produto final contra o bruto pelo
multiconjunto de palavras e exige que toda diferença esteja registrada: teto sugerido de 5% (o
medido hoje é 3,00%), mais lista nominal das perdas. Sobre este experimento, o G9 teria apontado
sozinho: `merda ×3` e `bandido ×2` removidos, cinco tokens de asterisco inseridos, "expiação e
provas" → "expiação em provas".

Por que não simplesmente adotar B como bruto: porque então a autoridade sobre o que Jan Val Ellam
disse passaria a ser um LLM que mascara palavra, e a casa não teria como conferir. O sha256 do G1
continuaria verde sobre um texto que já não é a fonte.

Por que não recusar B e continuar como está: porque 295 segmentos e 15,93 sinais por 100 palavras
são, em trabalho humano, a maior economia disponível nesta esteira — a revisão dos 8 blocos gastou a
maior parte do esforço reconstruindo pontuação e descobrindo onde um turno termina, e isso B já
entrega.

**O revisor passa a trabalhar assim:** leitura e curadoria sobre o texto pontuado; conferência de
qualquer trecho duvidoso, entidade, palavrão ou palavra rara **contra o bruto**; divergências
registradas no livro-razão como já se faz hoje. A disfluência continua sendo tratada à mão (eixo 2
empatado), e a terminologia continua dependendo da KB (eixo 3 praticamente inalterado).

---

## 7. Riscos que a adoção cria, com o gatilho de cada um

| risco | evidência nesta medição | contenção |
|---|---|---|
| censura silenciosa de vocabulário | 5 tokens mascarados (`m****` ×3, `b******` ×2) | portão G9 + conferência contra o bruto; asterisco nunca entra no produto |
| microedição que quebra casamento com a KB | "expiação **e** provas" → "**em** provas" (RC-954 zerado) | idem; divergência lexical registrada em `metadados.yaml` |
| correção parcial, gerando inconsistência | "calmeias" → "colmeias" em 1 de 2 ocorrências | curadoria continua decidindo por termo, não por ocorrência |
| acréscimo de palavra | "num circuito" → "num num circuito" | G9 pega como acréscimo não registrado |
| export futuro sem o cabeçalho da casa | o cabeçalho de B foi copiado de A à mão | `rc_novo.py` passa a aceitar bruto sem marcador (cascata em §8, item 1) |
| depender de serviço de terceiro sem contrato | NotebookLM é caixa-preta; a camada pode mudar de comportamento sem aviso | a medição de proveniência fica como rotina: rodar `rc_perfil_stt.py` a cada captura nova e conferir divergência e mascarados antes de revisar |

---

## 8. Custo de código, item a item

| # | item | onde | tamanho |
|---|---|---|---|
| 1 | critério de corpo em cascata (marcador → linha mais longa → arquivo inteiro) + guarda que avise quando a cobertura da maior linha ficar abaixo de 80% | `rc_novo.py:71`, `rc_indice.py:62`, `metadados.yaml`, testes 3 e 12 | meio dia |
| 2 | heurística de "sequências capitalizadas" ciente de inicial de frase (a lógica já está pronta em `rc_perfil_stt.classificar_ausentes`) | `rc_diagnostico.py:372` | ~15 linhas |
| 3 | campos de proveniência do derivado | `rc_novo.py`, `metadados.yaml`, `rc_indice.py` | pequeno |
| 4 | **portão G9 — divergência produto × bruto** | `rc_qa.py` | pequeno; é o item de maior retorno |
| 5 | Guia §8 (pontuação vira conferência), §9 (segmentação nativa por turno; diarização continua inferida) e nova seção sobre derivados de STT | `docs/normas/guia-revisao-v2.md` + `.docx` | redação |

O item 1 vale **mesmo que B nunca seja adotado**: é um defeito latente da esteira atual. Hoje
`rc_novo.py`/`rc_indice.py` tomam o corpo como `max(linhas, key=len)` e `rc_diagnostico` o separa
pelo marcador — dois critérios diferentes para a mesma pergunta. Sobre A eles coincidem (a linha 12
tem 101.468 chars) e ninguém notou. Sobre qualquer arquivo paragraphado, o primeiro devolve **um
parágrafo** e grava `corpo_palavras` fracionário em silêncio, com o QA verde.

---

## 9. `upload/` — e o lugar do `Opcao-B.txt`

**A pasta foi implantada** (`upload/README.md` versionado; `.gitignore` com `/upload/*` e
`!/upload/README.md`, verificado com `git check-ignore`). É zona de trânsito: o que for aprovado
migra para `transcricoes/<slug>/00-fonte/` e passa a ser versionado com sha256, sob o alcance do QA.
Nada que seja fonte de verdade pode morar só ali — se a pasta fosse versionada, viraria um segundo
depósito de brutos fora do controle do G1.

**Ironia útil:** o arquivo acabou chegando pela quarta via documentada no README — commit direto do
Comandante pela interface web do GitHub (`6eddae0`, "Add files via upload"). Só que o upload web
grava na **raiz**, não em `upload/`. Então `Opcao-B.txt` está hoje num lugar que o Plano de
Organização não prevê: arquivo de uma transcrição específica fora de `transcricoes/<slug>/`.

**Recomendação, para decisão do Comandante** (não movi o arquivo por conta própria — é entrega dele
e o destino depende da arquitetura aprovada):

* se a arquitetura de §6 for aprovada → `git mv Opcao-B.txt transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-pontuada.txt`, com os campos de proveniência em `metadados.yaml`;
* se for recusada → mover para `upload/` com `git rm --cached`, mantendo o histórico e o sha256 registrados neste parecer.

Para upload futuro pela web do GitHub, o caminho pode ser digitado na interface
(`upload/nome-do-arquivo.txt`), o que já cai na zona de trânsito prevista.

---

## 10. Na geladeira, conforme ordem expressa

Os **14 itens pendentes** da fila de curadoria (8 `correcao-ficha`, 5 `divergencia-factual`,
1 `novo-registro-biblio` 0033) e a **segunda transcrição tradicional** seguem suspensos por decisão
do Comandante de 16/09/2026. As pendências residuais da KB (Jeane Miranda, B095) continuam com ele.
Nada disso foi tocado neste turno.

---

## 11. O que proponho como próximo passo

1. **Decisão do Comandante** sobre a arquitetura de §6 (derivado ao lado do bruto) — é o que destrava
   tudo o mais.
2. Se aprovada: itens 1, 2 e 4 de §8 (código), depois item 5 (Guia), e só então a segunda transcrição
   entra já no padrão novo.
3. **Rotina permanente:** toda captura nova passa por `rc_perfil_stt.py` antes da revisão — 15 segundos
   que dizem se o arquivo é o que parece, quanto vai custar em curadoria e se a camada de reescrita
   censurou alguma coisa.

Comando que reproduz tudo o que está neste parecer:

```bash
python ferramentas/rc_perfil_stt.py \
    transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-bruta.txt \
    Opcao-B.txt \
    --com-diagnostico \
    --md docs/pareceres/parecer-motor-stt-medicao.md \
    --json docs/pareceres/perfil-stt.json
```
