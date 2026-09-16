# Notas de revisão — decisões de forma desta transcrição

**Transcrição:** Revelações Cósmicas Urgente (Paranormal Experience, 14/09/2026)
**Revisor:** Agente 86 · **Concluído:** 16/09/2026
**Norma aplicada:** `docs/normas/guia-revisao-v2.md` · **Anexo:** `docs/normas/resolucao-de-conflitos.md`
**Onde estão as decisões de conteúdo:** `../40-devolucao/adjudicacao.md` (livro-razão das 98 linhas). Este arquivo trata só de **forma**.

---

## 1. Os oito blocos

| Arquivo | Tema | Palavras | Parágrafos | Rótulos | `[NOTA]` | `[A CONFIRMAR]` | `[INAUDÍVEL]` |
|---|---|---:|---:|---:|---:|---:|---:|
| `bloco-01.md` | Abertura, anúncio e o conhecimento que era só dos reis | 2.397 | 23 | 23 | 0 | 2 | 4 |
| `bloco-02.md` | Niceia, a Trindade, Agostinho, Hobbes e o poder da oração | 2.490 | 25 | 25 | 5 | 2 | 1 |
| `bloco-03.md` | O ser que não é um ser, as forças que atendem preces e o anúncio do evento | 2.634 | 26 | 28 | 6 | 4 | 1 |
| `bloco-04.md` | A Divina Colmeia, o colapso de Javé, o eu parasitário e Ray Kurzweil | 2.606 | 9 | 9 | 6 | 5 | 1 |
| `bloco-05.md` | As IAs que fugiram do Éden, os institutos dos dois hemisférios e o iluminismo sombrio | 2.465 | 7 | 7 | 3 | 3 | 2 |
| `bloco-06.md` | Great reset, Fausto e a obediência, Nicolelis e as Mandalas Arcturianas | 2.539 | 9 | 10 | 5 | 2 | 1 |
| `bloco-07.md` | Rezar para as IAs, Arcturianos e Capelinos, a força da consciência dignificada e Tati Quântica | 2.575 | 18 | 18 | 5 | 3 | 3 |
| `bloco-08.md` | Revelação Cósmica urgente, o planeta-prisão, o Conselho dos Arcontes e a levitação | 2.184 | 26 | 27 | 2 | 3 | 1 |
| **Total** | | **19.890** | **143** | **147** | **32** | **24** | **14** |

Critério de corte: mudança de assunto sustentada, não minuto de relógio. O corpo bruto é uma
única linha de 101.468 caracteres sem nenhuma pontuação; os blocos seguem as costuras temáticas
da conversa. A contagem acima inclui os marcadores editoriais — o texto corrido soma 18.966
palavras contra 18.806 do bruto.

**Por que `bloco-01.md` e não `bloco-1.md`:** com dez blocos ou mais, o glob `bloco-*.md`
ordena `1, 10, 11, 2, 3…` e o DOCX final sai com a palestra embaralhada. Zero à esquerda
resolve para qualquer tamanho. Nesta transcrição eram 8 blocos e o defeito não apareceria —
apareceria na terceira ou quarta.

## 2. Formato de arquivo (compatível com `ferramentas/rc_docx.py`)

1. Título do bloco em `## Bloco N — tema` (vira Heading 2 no `.docx`, com painel de navegação).
2. **Nenhum comentário HTML** (`<!-- -->`) dentro de `20-blocos/`: o montador não o conhece e o
   texto sujo vai para o produto.
3. Parágrafo = linha não vazia; linha em branco separa parágrafos. Um turno de fala é um
   parágrafo.
4. `**negrito**` para o rótulo do falante e para o que o revisor quiser destacar; `*itálico*`
   para títulos de obras (*The Singularity Is Near*, *Deep Utopia*, *A Divina Colmeia*);
   `` `código` `` não é usado aqui.
5. O negrito automático de primeira menção de cada termo canônico é aplicado pelo montador a
   partir de `../10-diagnostico/dossie-bloco.txt` (`--lexico`) — não marcar à mão, para não
   duplicar.

## 3. Diarização — desvio documentado do Guia §9

O Guia §9 pede o rótulo do falante **em linha própria**. Aqui o rótulo vai **em negrito, inline,
no início do parágrafo do turno**:

```
**[JAN VAL ELLAM]** Tranquilo. Mais uma vez é uma honra, uma alegria estar aqui…
```

Motivos: (a) o despacho do Comandante de 15/09/2026 escolheu a **opção B — rótulos inferidos
explícitos**, e o inline mantém o rótulo colado à fala que ele qualifica; (b) em linha própria,
143 parágrafos virariam 286, com 143 linhas órfãs de três palavras quebrando o fluxo de leitura
justificado e a entrelinha 1,5 do produto; (c) o `rc_docx.py` trata cada linha como um parágrafo,
então o rótulo em linha própria herdaria recuo e justificação de corpo de texto.

O desvio está registrado aqui e em `../40-devolucao/adjudicacao.md` §5. Se o curador preferir a
forma do Guia, a conversão é mecânica — mas o produto perde leitura.

Rótulos usados: `[JAN VAL ELLAM]` 64 · `[GURU DE MALÁ]` 42 · `[ALEXANDRE SHERMINATOR]` 36 ·
`[ANÚNCIO]` 4 · `[FALANTE?]` 1.

## 4. Disfluência — nível LEVE

| Saiu | Ficou |
|---|---|
| repetição imediata por erro de dicção ("ele voltou, ele voltou") | repetição **retórica** ("milênios — milênios", "ama não, ama não, ama não") |
| marcadores de hesitação: "né", "eh", "uhum", "aham", "tipo assim" solto | sintaxe oral, com seus períodos longos e suas retomadas |
| auto-interrupção sem conteúdo ("eu fui… eu fui lá") | correção que acrescenta informação ("não Bau, Belial, seja quem for") |
| concordância truncada pelo STT quando era claramente ruído | concordância oral do autor, mesmo fora da norma culta |

O nível leve foi fixado no despacho de 15/09/2026. A identidade oral do Jan é parte do valor do
documento: limpar demais produziria um texto que ele não disse.

## 5. Pontuação — inserida integralmente

O STT não entrega **nenhum** sinal. Tudo foi pontuado pelo revisor: 1.909 vírgulas, 789 pontos,
167 interrogações. Critérios: vírgula em vocativo, aposto e enumeração; travessão para aposto
explicativo longo; dois-pontos antes de citação e de enumeração anunciada; aspas em citação
direta (inclusive na fala que o autor encena, como o diálogo de Agostinho no bloco 2); ponto de
interrogação em pergunta real, mesmo retórica.

## 6. Números, datas e cifras

**Nenhum número foi alterado no corpo.** Onde o dito diverge do verificado, o número dito
permanece e a divergência vira `[NOTA]` com fonte e data — e migra para a §4 da devolução.
Justificativa: a cifra faz parte do registro oral e a correção silenciosa quebraria a
rastreabilidade, que é o que permite ao produtor conferir depois.

Casos: Kurzweil 2007 (a obra é de 2005) · singularidade 2029/2045 · ingresso "10 parcelas de
R$ 18" (o oficial é R$ 180 ou 12× R$ 18,60) · Mentalma "cinco publicados, são oito" (a KB
registra 5 + curso) · 60.000 demissões no Google (não verificado) · Singularity University 2010
ou 2011 (fundada em 2008).

## 7. Marcadores editoriais

| Marcador | Quando | Renderização no `.docx` |
|---|---|---|
| `[NOTA: …]` | evidência, divergência, forma do bruto, esclarecimento | itálico, corpo 11 pt |
| `[A CONFIRMAR: "…"]` | o revisor tem hipótese mas falta fonte; alguém precisa confirmar | itálico, corpo 11 pt |
| `[INAUDÍVEL: "…"]` | o STT entregou algo que não fecha sentido; entre aspas vai o que se ouviu | itálico, corpo 11 pt |
| `**[ANÚNCIO]**` | trecho promocional, preservado no corpo por decisão do Comandante | negrito |

Regra: marcador **cita o bruto de propósito**. O QA expurga o conteúdo dos marcadores antes de
procurar formas proibidas — senão a evidência seria punida como erro.

## 8. Anúncios e o guia de fontes

- **Anúncios preservados no corpo** (despacho de 15/09/2026), marcados `**[ANÚNCIO]**`: Insider
  (40% de desconto, cupom PARANORMAL), evento com Terry Fabris no Teatro Santo Agostinho,
  Mandalas Arcturianas. São parte da transmissão e têm valor documental — inclusive o preço
  divergente do anúncio oficial.
- **"Guia de fontes" removido do produto final** (mesmo despacho). Ele vive nas linhas 7 a 11 do
  cabeçalho original, que ficou integralmente em `../00-fonte/transcricao-bruta.txt`; o corpo
  começa na linha 13. Nada foi perdido, apenas não faz parte do produto de leitura.

## 9. O que o revisor NÃO fez

1. Não reescreveu frase nenhuma por estilo — só por ortografia, terminologia e pontuação.
2. Não resumiu, não cortou argumento, não reordenou turnos.
3. Não corrigiu o pensamento do autor, mesmo onde ele é controverso.
4. Não substituiu nenhuma palavra da base sem adjudicação explícita no livro-razão.
5. Não silenciou divergência factual: toda uma virou `[NOTA]` com fonte.
6. Não tocou em `../00-fonte/` — o bruto é imutável e o hash confere.
7. Não aplicou nada na KB-RC: **o revisor propõe, o curador aplica.**

## 10. Casos difíceis e como foram resolvidos

| Caso | Decisão | Por quê |
|---|---|---|
| "Rogério" dito em 1ª pessoa e exemplificado em 3ª | mantido como dito + `[NOTA]` | indício de nome civil do próprio Jan Val Ellam; não é papel do revisor afirmar |
| Trocadilho "nunca houve um amanhã / a manhã" | preservado | recurso retórico, não erro de STT |
| "ser silicato" | preservado | o autor usa e glossa em seguida ("ou seja, ser feito de sílica") |
| "Lei de Gordon Moore" | *Lei de Moore* na voz do narrador; forma dita preservada dentro da citação | o aposto seguinte ("dono da Intel") refere-se à pessoa |
| Diálogo da levitação no bloco 8 | troca de falantes corrigida | a atribuição estava invertida e mudava o sentido |
| "Jah Baal" na pergunta do apresentador | *Belial*, com `[NOTA]` | o próprio autor emprega Belial adiante, na narrativa de Jó; RC-479 |
| "Xavé" no bloco 2 | *Javé*, com `[NOTA]` — correção tardia, pega pelo QA | a forma bruta só sobrevive dentro da nota, citando a fonte |
