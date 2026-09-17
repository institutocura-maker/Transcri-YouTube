# Relatório de curadoria — lote 03 (vídeo 2)

| campo | valor |
|---|---|
| data | 17 de setembro de 2026 |
| origem | `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos` (fonte `Y2026-09-12`) |
| decisão | **despacho do Comandante de 17/09/2026** — os 10 itens da fila do vídeo 2 APROVADOS |
| curador que aplicou | Agente 86 |
| ferramentas | `rc_curadoria.py --aplicar` (parte mecânica, com atestação no bruto antes de gravar) + edição de ficha documentada (Quarentena e Cautela, que a ferramenta não aplica) |
| itens | 0042 a 0051 · todos `aplicada` em `_fila-de-curadoria.csv` |
| verificação | `rc_qa.py --tudo` (G3 passa de 6 → 8 formas proibidas nesta pasta, 0 ocorrências) · `testes/test_pipeline.py` 158 verificações, 0 falhas |

Lote 01 = variantes STT do vídeo 1 (16/09). Lote 02 = 10 termos novos do vídeo 1 (16/09).
**Lote 03 = vídeo 2 inteiro.** O `rc_curadoria.py` rotula a entrada automática de CHANGELOG como
"lote 01" porque conta lotes **por transcrição**; na numeração da KB este é o terceiro.

---

## 1. O que foi aplicado — variantes STT (mecânico, `rc_curadoria.py`)

| Item | Ficha | Variante(s) gravada(s) | Ocorr. no bruto |
|---|---|---|---:|
| 0043 | RC-077 Lokas | locas | 2 |
| 0044 | RC-077 Lokas | louoca | 1 |
| 0045 | RC-034 Big Bang | glu | 1 |
| 0046 | RC-577 Xamanismo Cósmico | chamanismo — **parcial**, ver §3 | 1 |
| 0047 | RC-548 Arquivos Mentais | acásicos · acáxicos | 2 |

Efeito nas fichas: RC-077 e RC-034 ganharam a seção **Etimologia e Grafias** (não tinham) com
"Grafia preferida" e "Variações STT capturadas", mais a seção **Atualização** com a entrada datada e
a evidência do item; RC-577 e RC-548 já tinham a seção e receberam a linha de variações. Campo
`atualizado` do front-matter das quatro fichas: `2026-09-17`.

**Atestação.** Todas as cinco formas foram conferidas no **corpo** do bruto oficial
(`00-fonte/transcricao-bruta.txt`, sha256 `16c9276a…`) — nunca na captura por *fetch* de página, que
a norma nova (Guia v2 §2.6, regra 8) rebaixou a não-fonte:

| forma | trecho do bruto |
|---|---|
| `locas` (2×) | "esse aqui tem milhões de **locas** o que é **locas**" |
| `louoca` | "cada **louoca** é um buraquinho daquele" |
| `glu` | "singularidade com quarks e **glu** que ao explodir criou matéria e antimatéria" |
| `chamanismo` | "o que a gente entende como sendo **chamanismo** resultou desse processo" |
| `acásicos` / `acáxicos` | "isso aqui são os registros **acásicos ou acáxicos**" — o autor hesita entre as duas formas na mesma frase |

## 2. O que foi aplicado — Quarentena de formas quase-canônicas (manual)

Defesa chamada de "crítica" pelo Comandante: o corretor ortográfico do editor troca termo técnico por
forma quase-canônica, e nenhuma régua automática da casa pegava.

| Item | Ficha | Seção criada | Regra |
|---|---|---|---|
| 0049 | **RC-034** Big Bang | `## Quarentena Terminológica` | **gluons** — NUNCA "glues" |
| 0050 | **RC-636** Duas Pulsações da Criação | `## Quarentena Terminológica` | **pósitron** — NUNCA "pósetron" |

As duas seções registram a origem do defeito: no vídeo 2 o bruto dizia "quarks e glu" e "nenhum
pósitron daqui" — ou seja, **no segundo caso o ASR estava certo e o editor estragou**. O portão G3
lerá essas Quarentenas em qualquer transcrição futura (`rc_qa.formas_proibidas` extrai `NUNCA "…"` de
todas as fichas): nesta pasta a varredura passou de 6 para 8 formas, e na do vídeo 1 de 25 para 27,
com 0 ocorrências nas duas.

## 3. O que foi aplicado — cautelas editoriais (manual)

| Item | Ficha | Seção criada | Regra |
|---|---|---|---|
| 0048 | **RC-894** Qualia como Processamento Humano | `## Cautela editorial` | "qualia" exige validação de contexto: no vídeo 2 é corruptela de **colmeia** (RC-174) |
| 0046 | **RC-577** Xamanismo Cósmico | `## Cautela editorial` | "chamanismo" nem sempre é Xamanismo Cósmico: no sentido genérico a substituição **não** se aplica |

São os dois casos em que a varredura automática casa a forma e erra o sentido. O RC-577 já trazia
`chamanismo` como variante STT desde a pré-curadoria de `P2022-12-17` — ou seja, o risco não era
hipotético: sem a cautela, qualquer ocorrência futura viraria "Xamanismo Cósmico" por substituição.
O Comandante confirmou a aceitação parcial "mantendo a integridade doutrinária sem forçar um conceito
onde ele não foi aplicado".

## 4. O que foi decidido sem gravar na KB

| Item | Decisão |
|---|---|
| 0042 | `Y2026-09-12` em `biblio.json` — já aplicada em 16/09/2026 (é o registro que o `rc_indice.py` exige, Guia §2.5) |
| 0051 | Data oficial **2026-09-12**, a da plataforma. O cabeçalho do bruto traz 13/09/2026 e o do `.docx` revisado, 12/09/2026; as três ficam registradas em `00-fonte/metadados.yaml` e na nota da fonte Y |
| título | Oficial mantido em `titulo` e no slug; o do Comandante ("Alienígenas ou seres de outro universo?") em `chamada` |
| camada 3 | `Jesus` → Jesus de Nazaré gravado em `ferramentas/dados/externos.csv` como **semente de proteção** (38 entidades). A KB tem RC-072 e RC-800 para a leitura RC do nome; a camada 3 protege a grafia contra casamento automático |

## 5. Instrumento: um defeito achado ao aplicar o lote

Ao gravar as Quarentenas e rerodar o G3, apareceu um caso que o instrumento não cobria: a `[NOTA]` do
*pósitron* (bloco 3) **cita a notação da ficha RC-636**, que tem colchete dentro —
«o jogo de pósitrons [STT 'positelétron']». `MARCADOR_RE` e `NOTA_RE` fechavam o marcador no primeiro
`]`, então o rabo da nota voltava a ser corpo: saía sem itálico no `.docx`, entrava na contagem de
palavras (1.874 em vez de 1.865) e — o risco real — uma forma proibida citada como evidência **depois**
do colchete interno daria falso positivo no G3, punindo o revisor por documentar.

Corrigido em `ferramentas/rc_docx.py`: os dois regexes toleram um nível de aninhamento
(`(?:[^\[\]]|\[[^\]]*\])*`). Quatro verificações novas em `testes/test_pipeline.py` travam o
comportamento — inclusive duas que garantem que `glues` e `pósetron` estão entre as formas proibidas
derivadas da KB. Produto regenerado; contagem corrigida em `metadados.yaml`, catálogo, CHANGELOG e nos
documentos da pasta.

**Limitação de instrumento registrada (não corrigida neste turno):** `rc_qa.ler_metadados` não lê
listas aninhadas — `revisao.despachos` volta vazio e `falantes` volta com **só o último** item, nas
duas transcrições (vídeo 1 idem). Nenhum portão depende desses campos hoje, mas um portão futuro que
quiser contar falantes ou conferir despachos leria errado em silêncio. Enquanto isso, campos que o QA
precisa ler ficam em linha única (`curadoria_aplicada`, por exemplo, foi gravado assim).

## 6. Estado final

* Fila de curadoria: **51 itens**, 36 `aplicada`, 14 `pendente` (todas do vídeo 1), 1 `informativa`.
  Pendências do vídeo 2: **zero**.
* `KB-RC/CHANGELOG.md`: duas entradas para 17/09/2026 — a mecânica (5 variantes, gravada pelo
  `rc_curadoria.py`) e a manual (Quarentenas, cautelas, camada 3, data).
* Portões nas duas transcrições: G1–G8 `ok`, G9 `ok` (vídeo 1) / `n/a` (vídeo 2).
* Catálogo: `40-devolvida` nas duas pastas · fonte Y conferida.
* Pacote do vídeo 2 **fechado**, como pedido no fecho do despacho.
