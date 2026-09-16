# Relatório de curadoria — lote 02

**Data:** 16 de setembro de 2026 · **Curador:** Agente 86 · **Ferramenta:** `ferramentas/rc_termo.py`
**Autorização:** despacho do Comandante *Aprovação do Lote 01 e Padrão Y* (16/09/2026)
**Origem:** `transcricoes/2026-09-14-revelacoes-cosmicas-urgente` · **Fonte:** `Y2026-09-14`
**Estado:** 10 termos criados (RC-947 a RC-956) · padrão Y instituído · 1 variante remanejada · 1 item desbloqueado

---

## 1. O que o despacho autorizou, e o que foi feito

| Determinação | Execução |
|---|---|
| Lote 01 ratificado | nada a fazer; o estado ratificado é o que está em `KB-RC/` desde `13bc65b` |
| CI ativado pelo Comandante (opção A) | conferido: `.github/workflows/qa.yml` em `5744f1f`, **byte-idêntico** a `ferramentas/ci/qa.yml`. Os quatro passos foram simulados localmente antes de qualquer PR (§6) |
| Padrão Y aprovado | `KB-RC/biblio.json` recebeu `Y2026-09-14`; o Guia ganhou o **§2.5**; `rc_indice.py --checar` passou a fiscalizar (§3) |
| URL fornecida | gravada nos três lugares que precisam concordar, conferida na plataforma (§2) |
| Fechar os 10 termos | RC-947 a RC-956 criados com `rc_termo.py`, a partir de especificação escrita e validada (§4) |

---

## 2. A fonte deixou de ser órfã

URL conferida na plataforma em 16/09/2026 — não apenas copiada:

| campo | valor |
|---|---|
| URL | https://www.youtube.com/watch?v=enBUKAWXQRw |
| Título oficial | **ASSISTA ANTES QUE SAIA DO AR - Jan Val Ellam** |
| Canal | PARANORMAL EXPERIENCE (@PARANORMALBR) |
| Publicado / upload | 2026-09-14 / 2026-09-15 |
| Duração | **2:25:50** |
| Plataforma | categoria Education · 162.368 visualizações · 9.935 likes |

**Correção que a conferência produziu:** `metadados.yaml` registrava `duracao_min: 125`, estimativa da
captura. O valor real é 146. Corrigido, com `duracao_real: "2:25:50"` ao lado para deixar visível que
o número veio da plataforma. O título oficial e o `titulo` da captura batem; a `chamada`
("ASSISTA ANTES QUE SAIA DO AR") era, ela própria, o título do vídeo.

**Duas corroborações da revisão vieram de graça**, na descrição oficial: o anúncio da Insider com
cupom PARANORMAL (bloco 1, preservado no corpo por decisão do Comandante) e as *Mandalas Arcturianas*
(bloco 6), que sustentam o termo novo RC-951.

**E um alerta que quase virou erro:** a descrição anuncia **outro evento** — *Conexão com os Guardiões
Espirituais*, Robson Pinheiro, R$ 160 ou 10× R$ 16. Não é o evento de 03/10 no Teatro Santo Agostinho
citado no bloco 3 (Terry Fabris + Robson Pinheiro, anunciado a R$ 180 ou 12× R$ 18,60 no vídeo
"LEMÚRIA ESTÁ em busca URGENTE DE CONTATO"). Conferido: as duas `[NOTA]` de preço do bloco 3
**continuam corretas** — o áudio diz "10 parcelas de R$ 18", que fecha com os R$ 180 daquele evento.
Nenhuma linha do produto foi alterada. O risco de conflate ficou registrado como item **0041** da
fila (informativo) e no campo `nota` do próprio registro Y, que é onde um revisor futuro vai olhar.

---

## 3. Padrão Y — a norma e a fiscalização

`docs/normas/guia-revisao-v2.md` **§2.5** define: código `Y` + data da transmissão; os sete campos de
sempre em `biblio.json` (com o canal em `editora`) mais `tipo`, `url`, `canal`, `data_publicacao`,
`data_upload`, `duracao`/`duracao_min`, `forma_captura`, `confiabilidade`, `slug`,
`midia_arquivada`, `consultado_em`. E as consequências para a revisão: termo de fonte Y **nunca**
nasce `verificado`; `confianca_fonte` é `média`; a evidência se aponta por slug + bloco.

Fiscalização automática em `rc_indice.py --checar` (passo do CI), nos dois sentidos:

- a partir de `30-produto`, a transcrição tem de ter URL, e a URL tem de estar em `biblio.json`;
- o campo `slug` do registro Y tem de apontar de volta para a pasta;
- **antes** de `30-produto` é aviso, não erro — pasta recém-criada por `rc_novo.py` não pode nascer
  reprovada, pela mesma razão que os portões têm o estado `N/A`.

Testes negativos conferidos: URL trocada por uma não registrada → exit 1 com a mensagem certa;
registro Y apontando para outra pasta → exit 1 nomeando o conflito. Foi assim que a transcrição de
referência chegou à devolução com `url: null`; agora o mesmo esquecimento não passa do catálogo.

---

## 4. Os dez termos

Especificação escrita em `KB-RC/_lote-02-termos.json` — a ferramenta não improvisa conteúdo: ela
valida e grava o que estiver especificado, e recusa tudo se qualquer item falhar.

| Código | Termo | Categoria / subcategoria | Status | Por que esse status |
|---|---|---|---|---|
| RC-947 | Eu Parasitário (de Javé) | Processos & Fenômenos / 4.2 | provisório | o autor nomeia e define ("a gente chama 'eu parasitário'"), 3 ocorrências |
| RC-948 | /Kaggen (nome san de Javé) | Seres & Entidades / 1.1 | provisório | externo verificado (Bleek & Lloyd, 1870); uso RC em fonte única |
| RC-949 | Tom Teltan | Seres & Entidades / 1.6 | **candidato** | grafia `[A CONFIRMAR]`, não localizada em base nem fonte externa |
| RC-950 | Avalokiteshvara | Seres & Entidades / 1.1 | provisório | grafia consagrada; forma do bruto muito instável (3 variantes) |
| RC-951 | Arcturianos | Seres & Entidades / 1.3 | provisório | lacuna real: a base tinha Capela e nada de Arcturus |
| RC-952 | Constituição Setenária | Conceitos Cosmológicos / 2.3 | provisório | expressão já usada na prosa de RC-474 e RC-706 sem verbete |
| RC-953 | Circuito Colmeico | Conceitos Cosmológicos / 2.2 | provisório | neologismo definido pelo autor ("eu chamo de circuito colmeico") |
| RC-954 | Planeta de Expiação e Provas | Lokas & Geografias / 3.3 | provisório | termo kardecista assumido pelo autor, com atribuição explícita |
| RC-955 | Javé 2.0 | Seres & Entidades / 1.1 | provisório | designação oral e irônica; risco de leitura como versão de software |
| RC-956 | Força da Consciência Dignificada | Conceitos Cosmológicos / 2.6 | provisório | declarada pelo autor como "uma tese minha e de alguns espíritos" |

Nenhum nasceu `verificado`: uma fonte audiovisual, STT sem pontuação, não sustenta promoção — o §2.5
diz isso e a fila de promoção fica para quando houver obra primária ou segunda fonte.

Cada ficha traz definição, contexto com o bloco, grafia preferida, variantes (e variantes STT quando o
bruto as teve), citação literal com ponteiro para o slug, termos relacionados tipados, a fonte Y e
observações de cautela. `canonico.json` foi de 946 para **956** termos; `relacoes`, de 1.887 para
**1.915** arestas. `rc_termo.py` fez o round-trip: releu as dez fichas com `rc_kb` e conferiu código,
nome, variantes STT, fontes e status — divergência teria revertido tudo.

Variantes STT que nasceram com os termos: `Kaagen`/`kaagem` (RC-948), `avaloque texwara`/`avalo
testivara`/`avaloxivara` (RC-950), `constituição centenária` (RC-952), `circuito coméico` (RC-953) —
**7 novas, menos 1 remanejada**: a base foi de 84 variantes STT (lote 01) para **90**. O número do
lote 01 continua 84 no relatório dele, que é retrato daquele momento, não estado atual.

---

## 5. Dois remanejamentos que a criação dos termos exigiu

**Variante que mudou de ficha.** No lote 01, `circuito coméico` foi gravada em **RC-176** (Modelo
Colmeia) porque não havia canônico próprio — a fila dizia "RC-176 é a ficha hospedeira". Criado
**RC-953 Circuito Colmeico**, a variante foi movida para lá e RC-176 recebeu remissiva em
`## Atualização`, dizendo para onde foi e por quê. É o único caso de variante que trocou de ficha;
está coberto por teste.

**Item desbloqueado.** O 0023 (`constituição centenária`) estava bloqueado exatamente por falta de
canônico. Com RC-952 criado, a variante já nasceu na ficha dele; o item foi marcado `aplicada` com o
motivo escrito na própria coluna `evidencia`. `corpo rátmico` continua fora — não ocorre no bruto.

**Um bug que o termo /Kaggen revelou.** O portão G3 casava formas proibidas com `\b…\b`, e `\b` só
existe entre caractere de palavra e não-palavra. Para uma forma que **começa em barra** — `/Kaggen` —
o `\b` inicial nunca casa: em "de /Kaggen" os dois lados são não-palavra. Ou seja, o portão deixaria
passar exatamente a forma que deveria pegar, e o mesmo valeria para a atestação de curadoria e para a
contagem de sobrevivências do livro-razão. Corrigido com `rc_lexicon.fronteira()`, que usa
`(?<!\w)`/`(?!\w)` nas bordas que não são de palavra, adotado nos três lugares. A disciplina anterior
está preservada e testada: "Demiurg" continua sem casar dentro de "Demiurgo", "enoteísmo" dentro de
"henoteísmo". Sem o RC-948, o defeito seguiria invisível.

---

## 6. Verificação

| O quê | Resultado |
|---|---|
| `testes/test_pipeline.py` | **105 verificações, 0 falhas** (seções 10 e 11 novas: curadoria e padrão Y) |
| `rc_qa.py --tudo` | G1–G8 verdes; G1 com sha256 `34f9bcf4…` (bruto intocado por este lote) |
| `rc_indice.py --checar` | catálogo em dia, **fonte Y conferida**; dois testes negativos reprovam como devem |
| CI simulado localmente | os quatro passos do workflow, na ordem, com `qa.json` válido |
| `.github/workflows/qa.yml` × `ferramentas/ci/qa.yml` | `diff` vazio — cópias idênticas |
| Round-trip das fichas | `rc_kb` relê as dez: código, nome, variantes STT, fontes e status conferem |
| Markdown das fichas | nenhuma ficha nova com defeito; RC-176 sem defeito novo após o remanejamento |

---

## 7. O que continua na fila

41 itens: **26 aplicados** (15 no lote 01, 11 neste), **14 pendentes**, **1 informativo** (0041).

| Grupo | Itens | O que falta |
|---|---|---|
| correcao-ficha | 0025–0032 (8) | reescrita de prosa, uma ficha por vez, com a fonte na mão. Inclui o falso amigo RC-649 × Kurzweil, as fichas das pessoas reais do canal e "Mentalma: 5 ou 8 livros?" |
| divergencia-factual | 0034–0038 (5) | já tratadas no produto como `[NOTA]`; na KB viram alerta de Quarentena ou nada — a critério do Comandante |
| novo-registro-biblio | 0033 (1) | *Valores Supremos da Consciência*, programa do autor no YouTube — agora cabe no padrão Y, mas precisa do URL do programa |

O padrão Y resolveu o que travava os dez termos. O item 0033 é o próximo da mesma fila: é um programa
audiovisual, então é `Y`+data — falta só o link, que o Comandante tem e o Agente não.

**Encargo permanente registrado neste lote:** o workflow existe em duas cópias e o Agente só pode
editar uma. `diff .github/workflows/qa.yml ferramentas/ci/qa.yml` precisa continuar vazio; se um dia
deixar de estar, o CI passa a verificar outra coisa do que o repositório documenta — e o selo continua
verde.
