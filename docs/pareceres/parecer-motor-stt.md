# Parecer de engenharia — motor de STT na entrada da esteira

**Projeto:** Transcri-YouTube · **Data:** 16 de setembro de 2026 · **Elaborado por:** Agente 86 (Arena.ai Agent Mode)

**Objeto:** decidir se o STT do **NotebookLM** substitui o STT do **YouTube** como matéria-prima
em `transcricoes/<slug>/00-fonte/`, medindo os quatro eixos do despacho de 16/09/2026.

**Status: PARCIAL — a régua está construída, calibrada e a linha de base (lado A) está medida.
O lado B não pôde ser medido porque o arquivo `Opcao-B.txt` não chegou ao workspace.**

Este parecer não inventa o lado B. Onde falta número, está escrito "aguardando" — nunca um
palpite no lugar de uma medição.

---

## 0. Sumário executivo

Três coisas foram feitas e uma não foi.

**Feitas:**

1. **O instrumento existe e funciona.** `ferramentas/rc_perfil_stt.py` mede os quatro eixos sobre
   qualquer arquivo de STT e, passados dois arquivos, imprime o comparativo A × B com coluna
   "melhor". Roda em 3 s; com `--com-diagnostico` (que executa o motor de diagnóstico da casa
   inteiro sobre cada arquivo) roda em 8 s. Sai em terminal, `--json` e `--md`.
2. **A régua foi calibrada antes de medir — e três defeitos dela teriam falsificado o resultado.**
   Um deles contava o artigo "o" como o marcador oral "ó" e produzia 499 falsos positivos num
   texto de 19 mil palavras; a disfluência total do lado A sairia **71% maior** do que é
   (1.308 marcas em vez de 768). Outro contava equivalência conceitual da KB como corrupção de
   STT e apontava "humano" ×58 como erro do motor. O terceiro lia o CSV de Externos com o
   cabeçalho errado (a primeira linha é comentário) e achava zero entidades. Os três estão
   corrigidos e travados por teste (§2.2).
3. **A linha de base A está medida e publicada** (§3). Números-chave: 18.966 palavras, 0,22 sinais
   de pontuação por 100 palavras, mediana de 331 palavras por sentença, 768 marcas de disfluência,
   taxa de confiança terminológica 0,8262, **175 itens de curadoria** gerados pelo diagnóstico
   (44 propostas a adjudicar + 131 formas ausentes da base).

**Não feita:**

4. **O veredito de integração.** Sem o arquivo B não há comparação, e sem comparação não há
   parecer — há opinião. O que este documento entrega no lugar é o **critério de decisão
   pré-registrado** (§4): os limiares numéricos que B precisa atravessar para ganhar cada eixo,
   fixados *antes* de qualquer número de B existir. Isso tem um propósito metodológico concreto:
   quando B chegar, ninguém (nem eu) poderá mover a trave para o lado que o resultado favorecer.
   O commit deste documento antecede a chegada de B e é a prova auditável disso.

**Resposta à pergunta sobre a pasta `upload/`: sim, e já está implantada** (§6). Ela é a correção
estrutural da falha que travou este experimento: o anexo não chegou e não havia segundo caminho
para entregá-lo.

---

## 1. O que foi pedido e o que conta como resposta

Do despacho de 16/09/2026, quatro eixos e um critério de aceite:

| # | eixo | pergunta do Comandante | como este parecer responde |
|---|---|---|---|
| 1 | pontuação e segmentação | parágrafos razoáveis? pontuação nativa? | densidade de cada sinal por 1.000 palavras, sentenças, palavras/sentença (média, mediana, maior), parágrafos reais |
| 2 | disfluência | repetições imediatas e "né"/"eh" diminuíram? | contagem por marcador oral + repetições de palavra, bigrama, trigrama e prolongamentos, em absoluto e por 1.000 palavras |
| 3 | fidelidade terminológica | alucinou menos ou mais nas entidades dos lotes 01 e 02? | superfícies canônicas presentes × corrupções mapeadas na KB-RC × formas proibidas × entidades Externos, e o volume de curadoria que o `rc_diagnostico.py` gera |
| 4 | integração | trocar o STT reduz a carga das `rc_*` e o esforço manual? | as quatro suposições que a esteira faz sobre a FORMA do arquivo de entrada, testadas uma a uma, com a lista de ferramentas que quebram |

**Critério de aceite fixado pelo Comandante:** diagnóstico de viabilidade *antes* de fixar o novo
padrão de entrada. É exatamente o que está sendo feito — e é por isso que o parecer não fecha sem B.

---

## 2. O instrumento

### 2.1 Como mede

```
python ferramentas/rc_perfil_stt.py <arquivo-A> [<arquivo-B>] \
    [--kb KB-RC] [--com-diagnostico] [--md docs/pareceres/...] [--json ...]
```

A régua é a KB-RC carregada pela mesma porta que o resto da esteira usa (`rc_kb.carregar_kb` +
`carregar_fichas` + `como_termos` + `rc_lexicon.superficies`), o que torna os números comparáveis
com os do `rc_diagnostico.py` já publicados. Nesta data: **956 termos, 1.085 superfícies canônicas,
124 corrupções mapeadas, 5 formas proibidas pela Quarentena (24 com o livro-razão da transcrição de
referência), 37 formas Externos e 32 canônicos Externos.**

Duas decisões de medição que mudam o resultado e não são cosméticas:

* **Corrupção é `variante_stt` + semente curada.** O campo `Variações` da ficha é equivalência
  *conceitual* (Guia §5) e não entra. Contá-lo mediria vocabulário comum, não erro de motor.
* **O eixo 3 sabe em que estágio o arquivo está.** Medir um texto curado e um bruto na mesma
  escala seria injusto: o curado já teve as corrupções substituídas. A ferramenta imprime o
  estágio (`bruto`, `curado`, `solto`) e avisa em voz alta quando A e B estão em estágios
  diferentes.

### 2.2 Os três defeitos de régua corrigidos antes de medir

Isto importa para o parecer porque uma régua torta não compara dois motores — ela fabrica um
vencedor.

| defeito | efeito se não corrigido | correção | teste |
|---|---|---|---|
| marcador oral contado no texto normalizado: `L.norm("ó") == "o"` | 499 falsos positivos; disfluência do lado A inflada de 768 para 1.308 marcas (+71%) | "ó" e "hã" são buscados na forma **acentuada** no texto original; os demais, cuja forma sem acento não é palavra da língua ("ne", "ta", "ai"), são buscados no texto normalizado — o que captura tanto o motor que acentua quanto o que não acentua | `'ó' vocativo não é contado como o artigo 'o'`; `'né' é contado com e sem acento` |
| `Variações` da ficha contado como corrupção | "'humano'×58, 'espirito'×12, 'brama'×8" apareciam como erros do motor; taxa de confiança caía de 0,8262 para 0,6040 | só `variante_stt` e sementes; superfície que também é canônica é excluída do conjunto de corrupções | `corrupção não pode ser também canônico`; `campo 'Variações' não entra como corrupção` |
| `externos.csv` lido sem pular os comentários `#` que antecedem o cabeçalho | 0 entidades Externos medidas — a camada que protege "Ray Kurzweil" de virar variante interna ficava invisível | linhas `#` descartadas antes do `DictReader`; contam-se os dois lados (forma canônica e forma corrompida) | `externos.csv é lido apesar dos comentários antes do cabeçalho` |

O teste de fumaça da casa subiu de 105 para **124 verificações, 0 falhas**, e o QA G1–G8 continua
verde (sha256 do bruto intacto: `34f9bcf418bf…`).

### 2.3 Um aviso sobre o fixture sintético

Para provar que o eixo 4 detecta arquivo paragraphado, foi criado
`testes/fixtures/stt-com-paragrafos-sintetico.txt`. **É sintético, escrito à mão, e não é saída de
motor nenhum** — o cabeçalho do próprio arquivo diz isso. Ele existe só para o teste afirmar que o
instrumento acusa a quebra em vez de deixá-la passar em silêncio. Nenhum número dele entra neste
parecer como resultado.

---

## 3. Linha de base A — STT do YouTube (medida, não estimada)

Arquivo: `transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-bruta.txt`
(106.243 bytes, 15 linhas, CRLF, estágio **bruto**).

### Eixo 1 — pontuação e segmentação

| métrica | A (YouTube) | leitura |
|---|---:|---|
| palavras | 18.966 | live de 2h25min |
| sinais por 100 palavras | **0,22** | pontuação praticamente inexistente |
| vírgulas | 7 | 0,37 por 1.000 palavras |
| pontos | 23 | 1,21 por 1.000 — e parte deles é numérico ("2007.") |
| interrogações | 11 | — |
| dois-pontos | 73 | herança do cabeçalho e de marcações internas |
| aspas retas | 117 | — |
| sentenças | 35 | para 18.966 palavras |
| palavras/sentença (média) | **541,9** | não são sentenças: são trechos entre os poucos pontos |
| palavras/sentença (mediana) | 331 | — |
| maior "sentença" | **2.604 palavras** | — |
| parágrafos reais | **4** | e os 4 vêm do cabeçalho; o corpo é **uma** linha |
| palavras/parágrafo | 4.741,5 | — |

Referência interna: o produto final curado desta mesma transcrição tem **151 parágrafos**
(QA G6). Ou seja, entre o bruto (1 linha de corpo) e o produto (151 parágrafos) existe um trabalho
de segmentação que hoje é **100% manual**. Esse é o tamanho do prêmio que o eixo 1 disputa.

### Eixo 2 — disfluência

| métrica | A (YouTube) |
|---|---:|
| marcas totais | **768** |
| por 1.000 palavras | **40,49** |
| repetições de palavra imediata | 115 |
| repetições de bigrama | 25 |
| repetições de trigrama | 9 |
| prolongamentos ("ééé") | 4 |

Marcadores orais, em ordem: então 132 · aí 123 · tá 87 · né 49 · eh 45 · uhum 31 · cara 26 ·
tipo 25 · ó 21 · ah 20 · tô 20 · sabe 17 · olha 13 · quer dizer 5 · hum 3 · sei lá 2.

O contrato editorial desta casa é disfluência **nível LEVE** (remover repetições imediatas e
"né"/"eh"/"uhum", preservar sintaxe e identidade oral). Sobre A, isso significa intervir em
centenas de pontos à mão. Se B já entregar menos marcas, a economia é direta — mas veja a
ressalva de §4.2: menos disfluência também pode ser menos texto.

### Eixo 3 — fidelidade terminológica

| métrica | A (YouTube) |
|---|---:|
| superfícies canônicas da KB presentes | 49 formas distintas, **271 ocorrências** |
| corrupções mapeadas (`variante_stt` + sementes) | 33 formas, **57 ocorrências** (3,01/1.000 palavras) |
| formas proibidas (Quarentena + livro-razão) | 21 formas, 37 ocorrências |
| Externos — forma canônica | 17 formas, 35 ocorrências |
| Externos — forma corrompida | 27 formas, **56 ocorrências** |
| **taxa de confiança** (canônico ÷ canônico+corrupção) | **0,8262** |

Piores corrupções: `brama`×8, `jahe`×6, `javer`×3, `belal`×3, `yahe`×2, `demiurg`×2, `calmeia`×2,
`arcontos`×2.

**A ressalva metodológica mais importante deste parecer.** A KB-RC foi construída *a partir* das
corrupções deste STT: as 90 variantes registradas nos lotes 01 e 02 são, em boa parte, grafias que
o motor do YouTube produziu. A régua é portanto **assimétrica a favor de A** — as corrupções de A
já estão mapeadas (contam no eixo 3), enquanto as de B, sendo novas, não aparecem como corrupção:
aparecem como *forma ausente da base*. Medir só "corrupções mapeadas" daria a B um falso zero.

A métrica simétrica é a **carga terminológica total**, que soma o que o motor dá de trabalho
independentemente de a KB já conhecer a corrupção:

| componente | A (YouTube) |
|---|---:|
| linhas geradas no livro-razão pelo `rc_diagnostico.py` | **132** |
| — das quais `proposta` (exigem decisão do revisor) | **44** |
| — das quais `informativa` (artigo 47, flexão 4 — ruído morfológico) | 51 |
| — das quais semente do Guia já aprovada (é só aplicar) | 36 |
| — das quais "a confirmar" | 1 |
| formas ausentes da base (candidatas a termo novo) | **131** |
| superfícies exatas da KB encontradas | 108 |
| **carga terminológica total (132 + 131)** | **263 itens** |

É contra **263** que B será medido, não contra 57.

### Eixo 4 — integração à esteira

| suposição que a esteira faz hoje | A | detalhe |
|---|:---:|---|
| `rc_novo.py` e `rc_indice.py` medem o corpo como **a linha mais longa** (`max(linhas, key=len)`) | ✅ | a maior linha (101.468 chars) cobre **98,9%** do arquivo |
| `rc_diagnostico.carregar_transcricao` separa o cabeçalho pelo marcador "Transcrição Automática" | ✅ | marcador presente |
| diarização opção B: rótulos **inferidos** pelo revisor | ✅ | nenhum rótulo nativo; o revisor continua inferindo |
| Guia §8: pontuação é corretiva, o STT não traz | ✅ | 2,2 sinais por 1.000 palavras |

**A é 4/4 compatível — por construção, não por mérito.** A esteira foi desenhada em volta de A.
É isso que torna o eixo 4 o eixo decisivo: um motor melhor que não caiba na esteira custa código;
um motor pior que caiba custa curadoria. O parecer tem que dizer qual dos dois preços está na mesa.

---

## 4. Critério de decisão pré-registrado

Fixado em 16/09/2026, **antes** de qualquer número de B existir. B ganha o eixo se atravessar o
limiar; não ganha se ficar abaixo; e nenhum limiar será revisto depois de visto o resultado.

### 4.0 Guarda de comparabilidade (vem antes de tudo)

| guarda | limiar | se falhar |
|---|---|---|
| mesma extensão de áudio | palavras de B entre **90% e 110%** das de A (17.069 a 20.862) | o parecer **não compara motores**: compara recortes. Ferramentas que resumem podem devolver síntese, não transcrição — e aí qualquer métrica de qualidade é ilusão |
| mesmo estágio | ambos em estado **bruto** | comparar bruto com texto curado mede o revisor, não o motor |
| mesmo idioma e diacríticos | perda de diacríticos comparável (A: "nao" 402 sem acento × 8; "voce" 205 × 3; "entao" 132 × 3) | se B não acentua, o eixo 2 usa a contagem sem acento (já prevista no instrumento) e o eixo 3 perde precisão — registrar no veredito |

### 4.1 Eixo 1 — pontuação e segmentação

| limiar | valor | por quê |
|---|---|---|
| sinais por 100 palavras | **> 2,0** (A: 0,22) | dez vezes A já significa pontuação nativa, não corretiva |
| mediana de palavras/sentença | **< 60** (A: 331) | oralidade revisável vive entre 15 e 40 palavras; 60 é o teto generoso |
| maior sentença | **< 200 palavras** (A: 2.604) | uma sentença de 2.604 palavras não é revisável, é um capítulo |
| parágrafos reais | **≥ 100** (A: 4; produto curado: 151) | mesma ordem de grandeza do resultado humano já publicado significa que a segmentação deixou de ser trabalho manual |

**B ganha o eixo 1 se atender aos quatro.** Se atender só a pontuação e não a segmentação (ou
vice-versa), o eixo é declarado **parcial** e o veredito de §4.4 desconta isso.

### 4.2 Eixo 2 — disfluência

| limiar | valor | por quê |
|---|---|---|
| marcas por 1.000 palavras | **≤ 20,0** (A: 40,49) | metade do trabalho manual do contrato nível LEVE |
| repetições de palavra imediata | **≤ 57** (A: 115) | idem, no componente mais caro de remover |

**Ressalva obrigatória:** se B ganhar o eixo 2 com queda de palavras próxima do limite inferior da
guarda (§4.0), o parecer deve dizer que a vitória pode ser **supressão de conteúdo**, não limpeza.
Disfluência menor com texto muito menor não é mérito — é corte. Nesse caso o eixo 2 é anulado.

### 4.3 Eixo 3 — fidelidade terminológica

| limiar | valor | por quê |
|---|---|---|
| **carga terminológica total** (linhas no livro-razão + ausentes da base) | **≤ 197 itens** (A: 263; redução de 25%) | é a métrica simétrica, imune ao viés de a KB ter sido construída sobre A |
| taxa de confiança | **> 0,8262** (A) | mais canônico, menos corrupção — mas só vale como evidência secundária, pelo viés acima |
| formas proibidas presentes | **≤ 37 ocorrências** (A) | o motor não pode produzir as formas que a Quarentena e o livro-razão vetam |
| Externos corrompidos | **< 56 ocorrências** (A) | nomes próprios do mundo real são o teste mais duro de alucinação fonética |

**B ganha o eixo 3 se a carga terminológica total ficar ≤ 197.** Os outros três limiares são
evidência de apoio e não decidem sozinhos.

### 4.4 Eixo 4 — veredito de integração

Regra composta, porque é aqui que a decisão realmente mora:

1. **Se B for 4/4 compatível** e ganhar 2 ou mais eixos entre 1–3 → **trocar**, sem custo de código.
2. **Se B quebrar a suposição da "linha mais longa"** (cobertura da maior linha < 80%) → a troca
   exige alteração em: `rc_novo.py` (medição do corpo), `rc_indice.py` (coluna `palavras_brutas`),
   campos `corpo_linha`/`corpo_caracteres`/`corpo_palavras`/`pontuacao_original` do
   `metadados.yaml`, Guia §8 e §9, e os testes 3 e 12 do pipeline. Custo estimado: **meio dia de
   código**, uma vez, e o resultado é uma esteira que deixa de depender da forma do arquivo —
   ganho estrutural permanente.
3. **Se B quebrar também o marcador de cabeçalho** (ausência de "Transcrição Automática") → soma-se
   o ajuste em `rc_diagnostico.carregar_transcricao` (critério de separação passa a ser posição ou
   regex de cabeçalho, não marcador literal). Custo adicional pequeno, mesmo padrão de correção.
4. **Veredito final:** trocar se **(a)** B ganhar o eixo 1 completo, **ou** **(b)** B ganhar o eixo 3
   pelo limiar de 197, **e** em ambos os casos o custo de código for o dos itens 2 e 3 — que é
   finito, conhecido e pago uma única vez. **Não trocar** se B ganhar apenas o eixo 2: limpeza de
   disfluência é o que a esteira já faz bem e barato, e é o eixo mais fácil de fingir suprimindo texto.

---

## 5. O que já se pode afirmar sobre o eixo 4, mesmo sem B

Uma descoberta que vale independentemente do resultado do experimento, porque é um defeito latente
da esteira atual:

> **Duas ferramentas diferentes usam dois critérios diferentes para decidir o que é o corpo do
> arquivo — e uma delas produz métricas erradas em silêncio.**

* `rc_novo.py:71` e `rc_indice.py:62`: corpo = `max(linhas, key=len)`.
* `rc_diagnostico.carregar_transcricao`: corpo = o que vem depois do marcador "Transcrição Automática".

Sobre A os dois critérios coincidem (a linha 12 tem 101.468 chars e começa depois do marcador), e
por isso ninguém notou. Sobre um STT paragraphado, `max(linhas, key=len)` devolve **um parágrafo**
— o maior — e grava em `metadados.yaml` um `corpo_palavras` que seria uma fração do real, sem erro,
sem exceção, sem aviso. O QA G1 confere o sha256 do bruto, não a coerência da medição: passaria verde.

**Recomendação, independente de B ganhar ou perder:** unificar o critério num único lugar
(`rc_lexicon` ou um módulo de leitura de bruto) com fallback em cascata — marcador, depois linha
mais longa, depois arquivo inteiro — e com um aviso explícito quando a cobertura da maior linha for
abaixo de 80%. O `rc_perfil_stt.py` já calcula essa cobertura; transformá-la em guarda da esteira é
trabalho pequeno e remove uma classe inteira de erro silencioso.

---

## 6. A pasta `upload/` — resposta à pergunta do Comandante

**Opinião: faz falta, e não como conveniência — como correção de uma falha que já ocorreu.** O
anexo `Opcao-B.txt` não chegou e não havia segundo caminho de entrega; o experimento parou e nenhum
dos dois lados podia dizer onde o arquivo estava.

**Implantada nesta data:**

| item | estado |
|---|---|
| `upload/` criada | ✅ |
| `upload/README.md` (versionado) | ✅ regras, formatos aceitos, quatro vias de entrega, o que acontece quando o arquivo chega |
| `.gitignore`: `/upload/*` + `!/upload/README.md` | ✅ verificado com `git check-ignore` |

**Por que ignorada pelo git, se a casa versiona até o bruto?** Porque `upload/` é **zona de
trânsito**, não arquivo. O ciclo é:

```
upload/<arquivo>  →  rc_perfil_stt.py  →  parecer  →  aprovado?
                                                      ↓ sim
                              transcricoes/<slug>/00-fonte/  →  versionado, com sha256
                                                                 no metadados.yaml e
                                                                 fiscalizado pelo QA G1
```

Nada que seja fonte de verdade pode morar só em `upload/`. Se a pasta fosse versionada, ela viraria
um segundo depósito de brutos fora do controle do QA — que é exatamente o problema que o sha256 do
G1 existe para impedir.

**As quatro vias de entrega** (detalhe em `upload/README.md`): reanexar no chat; colar o texto;
link público (busco com `fetch_page`; Drive precisa estar como "qualquer pessoa com o link"); ou
commit direto do Comandante com `git add -f upload/<arquivo>`, que vence o ignore.

---

## 7. O que falta para fechar este parecer

**Um arquivo.** `Opcao-B.txt` — a transcrição do NotebookLM sobre o mesmo áudio
(`https://www.youtube.com/watch?v=enBUKAWXQRw`, 2h25min50s).

Assim que ele existir em qualquer lugar acessível, a execução é esta, e o parecer é completado com
os números reais no mesmo turno:

```bash
python ferramentas/rc_perfil_stt.py \
    transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-bruta.txt \
    upload/opcao-b.txt \
    --com-diagnostico \
    --md docs/pareceres/parecer-motor-stt-medicao.md \
    --json docs/pareceres/perfil-stt.json
```

Verificações que serão feitas antes de escrever qualquer conclusão: guarda de comparabilidade
(§4.0) → eixos 1 a 3 contra os limiares de §4.1–§4.3 → quebras de integração de §4.4 → veredito.

---

## 8. Na geladeira, conforme ordem expressa

Registrado para não se perder: os **14 itens pendentes** da fila de curadoria (8 `correcao-ficha`,
5 `divergencia-factual`, 1 `novo-registro-biblio` 0033) e a **segunda transcrição tradicional**
estão suspensos por decisão do Comandante de 16/09/2026, com foco total neste experimento. As
pendências residuais da KB (Jeane Miranda, B095) seguem com o Comandante. Nada disso foi tocado
neste turno.

---

## Anexo A — saída integral do instrumento sobre o lado A

Reprodutível com o comando de §7 (omitindo o segundo arquivo). Os números do §3 saem daqui; se um
dia divergirem, o que vale é esta execução.

```text
[régua] KB-RC: 956 termos · 1085 superfícies canônicas · 124 corrupções mapeadas (variante_stt + sementes) · 5 proibidas na Quarentena · 37 formas Externos · 32 canônicos Externos
[régua] livro-razão de transcricoes/2026-09-14-revelacoes-cosmicas-urgente: 24 formas proibidas no total

==============================================================================
transcricao-bruta.txt  (106.243 bytes · 15 linhas · 4 parágrafos reais · CRLF 15/LF 0)
==============================================================================
    estágio na esteira: bruto — STT cru: corrupções e formas proibidas SÃO esperadas — é a matéria-prima

[1] PONTUAÇÃO E SEGMENTAÇÃO — 18.966 palavras
    sinais por 100 palavras: 0.22
    sentenças: 35 · palavras/sentença: 541.9 (mediana 331, maior 2.604)
    parágrafos: 4 · palavras/parágrafo: 4741.5
      vírgula                      7  (0.37/1.000 palavras)
      ponto                       23  (1.21/1.000 palavras)
      interrogação                11  (0.58/1.000 palavras)
      dois-pontos                 73  (3.85/1.000 palavras)
      meia-risca                   2  (0.11/1.000 palavras)
      aspas retas                117  (6.17/1.000 palavras)
      aspas curvas                 1  (0.05/1.000 palavras)

[2] DISFLUÊNCIA — 768 marcas (40.49 por 1.000 palavras)
    repetições: palavra 115 · bigrama 25 · trigrama 9 · prolongamentos 4
    marcadores orais: então 132 · aí 123 · tá 87 · né 49 · eh 45 · uhum 31 · cara 26 · tipo 25 · ó 21 · ah 20

[3] FIDELIDADE TERMINOLÓGICA (contra a KB-RC)
    canônicos presentes: 49 formas distintas, 271 ocorrências
    variantes STT mapeadas presentes: 33 formas, 57 ocorrências (3.01/1.000 palavras)
    formas proibidas (Quarentena + livro-razão): 21 formas, 37 ocorrências
    Externos — forma canônica: 17 formas, 35 ocorrências · forma corrompida: 27 formas, 56 ocorrências
    taxa de confiança (canônico ÷ canônico+variante): 0.8262
    piores corrupções: 'brama'×8, 'jahe'×6, 'javer'×3, 'belal'×3, 'yahe'×2, 'demiurg'×2, 'calmeia'×2, 'arcontos'×2

[4] INTEGRAÇÃO À ESTEIRA
    maior linha: 101.468 chars = 98.9% do arquivo
    marcador 'Transcrição Automática': sim
    rótulos de fala nativos: nenhum
      [compatível ] rc_novo.py / rc_indice.py medem o corpo como **a linha mais longa**
                   a maior linha cobre 98.9% do arquivo
      [compatível ] rc_diagnostico.carregar_transcricao separa cabeçalho pelo marcador 'Transcrição Automática'
                   marcador presente
      [compatível ] diarização opção B (rótulos inferidos pelo revisor)
                   sem rótulos nativos: o revisor continua inferindo
      [compatível ] Guia §8 (pontuação é corretiva, o STT não traz)
                   2.2 sinais por 1.000 palavras — pontuação praticamente ausente

[5] DIAGNÓSTICO DA ESTEIRA (rc_diagnostico.py, exit 0)
    linhas_ledger: 132
    propostas: 44
    informativas: 51
    ausentes_da_base: 131
    superficies_exatas: 108
    por status_aprovacao: a confirmar 1, aprovada 36, informativa 51, proposta 44
    por classe: artigo 47, flexao 4, semente-guia 37, truncamento 5, variante 39
```
