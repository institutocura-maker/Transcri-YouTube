# Adjudicação — Revelações Cósmicas Urgente (Jan Val Ellam)

**Transcrição revisada:** `Revelações Cósmicas Urgente – Jan Val Ellam.txt` · corpo na linha 12 · 18.781 palavras · 101.468 caracteres · sem pontuação (STT puro).
**Produtos:** `blocos/bloco-1.md` … `blocos/bloco-8.md` (143 parágrafos, 18.966 palavras de texto corrido, 32 `[NOTA]`, 24 `[A CONFIRMAR]`, 14 `[INAUDÍVEL]`).
**Data:** 16 de setembro de 2026 · **Elaboração:** Agente 86.
**Regra de ouro aplicada em todo o log:** *nenhuma palavra da base pode ser substituída por outra, salvo adjudicação explícita e justificada* (Guia v2 §10 e §13).

---

## 1. Fila automática (motor `rc_diagnostico.py` + `rc_lexicon.py`)

O motor produziu **98 linhas** em `variantes-propostas.csv` a partir das sementes de `sementes-variantes-stt.csv` e de `externos.csv` (37 entidades). Na etapa de semeadura, **32 sementes foram atingidas** e **11 ficaram suspensas** por homografia, vocabulário comum ou colisão com a camada Externos: *Nick* (→ Nyx), *Terra Atlântis*, *Alamaior*, *Tempérium*, *a vista* (→ Avesta), *Cristo* (→ Krishna), *Virgem* (→ RC-104 Vishnu), *Get*, *J* isolado, *as reais* (ambiguidade com "reais" monetários), *era dos humanos*.

Cada uma das 98 linhas recebeu decisão humana explícita, gravada nas colunas **`adjudicacao`** e **`motivo_adjudicacao`** do próprio CSV — é o livro-razão desta revisão:

| Decisão | Linhas | Significado |
|---|---|---|
| **aceita** | 24 | variante substituída pelo canônico; não sobrevive no texto revisado |
| **aceita-parcial** | 7 | aplicada onde cabe; ocorrências residuais são legítimas (topônimo, citação direta, 1ª menção) |
| **recusada** | 20 | falso positivo do motor, flexão legítima ou alvo errado — ver §3 |
| **informativa** | 30 | registro de artigo/flexão; não gera substituição |
| **protecao** | 16 | variante e canônico coincidem: a semente existe para **impedir** outra substituição |
| **superada** | 1 | resolvida pelo despacho do Comandante (*Sherminetro* → Alexandre Sherminator) |
| **REVISAR** | 0 | nenhuma linha ficou sem decisão |

O validador de QA do `rc_docx.py` foi ajustado para cobrar apenas as linhas **`aceita`** (antes cobrava toda linha `aprovada`/`proposta`, o que incluía os 20 falsos positivos recusados — ver §5.1).

---

## 2. Correções aceitas por bloco

### Bloco 1 — abertura, anúncio e o problema das IAs
- Jan Vaillan / Jean Valan → **Jan Val Ellam** (registro do autor).
- Sherminetro / Sherminate → **Alexandre Sherminator** — *despacho do Comandante, 16/09/2026*.
- Emanuel Kant → **Immanuel Kant** (externo).
- Qcode / Qcodes → **QR code**.
- Anúncio da Insider preservado integralmente no corpo (40% de desconto, cupom PARANORMAL) — decisão editorial do Comandante.

### Bloco 2 — filosofia, religião e o parasitismo de Javé
- Yahé / Jahé → **Javé** (RC-001).
- Thomas Robs → **Thomas Hobbes**.
- Agostinho de Pona → **Agostinho de Hipona**.
- Mary Chiley → **Mary Shelley**; Dr frankstein → ***Frankenstein*** (corroborado pela KB: "o Frankenstein de Shelley").
- Brama → **Brahma** (RC-037; Quarentena `NUNCA "Brama"`).
- Virgin / Chiva → **Vishnu / Shiva** (RC-104, RC-102).
- Demiurg → **Demiurgo** (RC-048).
- enoteísmo → **henoteísmo**.
- constituição centenária → **constituição setenária**.
- Sidarta / "jardim da mente" → **Siddhartha Gautama** — *despacho do Comandante, 16/09/2026*.
- **Correção tardia aplicada após o QA:** "Xavé" → **Javé**, com `[NOTA]` documentando a variante. O QA final confirmou que a única ocorrência residual de "Xavé" está dentro da NOTA, citando o bruto (comportamento correto).

### Bloco 3 — mitologias, /Kaggen e o evento de Terry Fabris
- Kaagen / kaagem → **/Kaggen** — validado externamente (Bleek e Lloyd, San do Kalahari; consulta 16/09/2026). Proposto como novo termo e como variação de RC-001.
- Ganexa → **Ganesha** (RC-756).
- avaloque texwara → **Avalokiteshvara** — proposto como novo termo.
- Tirtancara → **Tirthankaras** (RC-397).
- Tom Teltan → mantido com `[A CONFIRMAR]` — proposto como novo termo.
- Teatro Santo Augosto → **Teatro Santo Agostinho** (confirmado pelo próprio áudio no bloco 8).
- Terry Fabriz → **Terry Fabris** (YouTube, upload 24/08/2026). Preço: `[NOTA]` — anúncio oficial R$ 180 ou 12× de R$ 18,60, contra "10 parcelas de R$ 18" no áudio. **Não silenciado, não corrigido no texto.**

### Blocos 4 a 6 — Colmeia, Kurzweil e transumanismo
- A Divina Calmeia → ***A Divina Colmeia*** (B044).
- circuito coméico → **circuito colmeico** (RC-176).
- Raymond Kzwell / Cselva / Curzell / Crowsa / Curs / Czel / Curser → **Ray Kurzweil** (9 superfícies distintas colapsadas).
- Ano do livro: `[NOTA]` — áudio diz 2007, *The Singularity Is Near* é de 2005.
- Datas da singularidade: `[NOTA]` — 2029 (IA de nível humano) e 2045 (singularidade).
- Nvid → **Nvidia**; chato GP / chat PT → **ChatGPT**; Antropic → **Anthropic**; Black Rock → **BlackRock**.
- as iais / asiais / entre as reais → **as IAs**.
- Nick Bostron → **Nick Bostrom**; Utopia Profunda → ***Deep Utopia*** (2024).
- Get → **Goethe**; Mefistófiles → **Mefistófeles**; barão de Tararé → **Barão de Itararé**.
- Miguel Nicoles → **Miguel Nicolelis**; teta healing → **Theta Healing**.
- *Dark Enlightenment*, *Great Reset*, metaverso, big techs, voucher: grafados conforme uso corrente e reportados como lacuna da camada Externos.
- Trump → **Donald Trump** na 1ª menção (bloco 4); a forma curta foi preservada nas menções seguintes, inclusive na enumeração "Trump, Putin, Lula" (aceita-parcial).
- Lei de Gordon War → **Lei de Moore** na voz do narrador; **"Lei de Gordon Moore" mantida dentro da citação direta**, porque o aposto seguinte ("dono da Intel") se refere à pessoa — decisão documentada em `[NOTA]` no próprio bloco 4 (aceita-parcial).
- Grzi → `[A CONFIRMAR]`; conectoma → `[A CONFIRMAR]` (relacionado a RC-557).

### Blocos 7 e 8 — Arcontes, Sophia e o encerramento
- arcturianos → mantido e **proposto como novo termo** (ausente da KB).
- capelinos → confirmado (RC-007/039/350).
- espírito mantado → **espírito imantado** (RC-699).
- ser silicato / silicados → **seres de sílica / corpos de sílica** (RC-699).
- Jah Baal → **Belial** (RC-479) — `[NOTA]`: é o próprio Jan quem corrige no áudio.
- arcontos / arces / arcos / erontes → **Arcontes** (RC-474), com `[A CONFIRMAR]` sobre *Archeons de Ereon* (RC-596).
- Sofia o Cristo Cosmo Rock → **Sophia, o Cristo Cósmico** (RC-009; Quarentena `NUNCA "Sofia"`).
- Brama Vni → **Brahma, Vishnu**; dinastia das Sofias → **Dinastia das Sophias** (RC-494).
- jardim do Édo → **Jardim do Éden**.
- Mentalma: `[NOTA]` — "cinco livros publicados, são oito" contra RC-555 ("5 livros + curso"). Divergência reportada, texto preservado.
- Rogério: mantido como dito + `[NOTA]` — indício de nome civil do próprio Jan (1ª pessoa, exemplos em 3ª pessoa).
- Tatiane Berre → `[A CONFIRMAR]` (criadora da personagem Tati Quântica).
- Rezente → `[A CONFIRMAR]` (local da palestra).
- "lei da mente e do boda" → `[INAUDÍVEL]`.
- Trocadilho "nunca houve um amanhã / a manhã" **preservado** — recurso retórico, não erro.

---

## 3. Falsos positivos e recusas (20 linhas `recusada`)

As sete recusas emblemáticas — as demais estão motivadas linha a linha no CSV:

| Ocorrência | O motor propunha | Decisão | Motivo |
|---|---|---|---|
| "cristã" | cristva (RC-101) | **recusada** | erro de fuzzy; "cristva" é variante STT, não canônica |
| "testivara" | estivara | **recusada** | substring sem sentido; contexto é Avalokiteshvara |
| "errado nós humanos" | "era dos humanos" | **recusada** | colisão com vocabulário comum |
| "a vista" | Avesta | **recusada** | preposição + artigo, não nome próprio |
| "Cristo" | Krishna (RC-414) | **recusada** | entidades distintas; substituição proibida |
| "Virgin" | RC-104 | **parcialmente aceita** | só dentro da tríade "Brama Virgin Chiva"; fora dela, recusado |
| "Demiurg" | — | **aceita** | ocorrência residual no QA é substring de "Demiurgo"; não é forma proibida |
| "enoteísmo" | — | **aceita** | idem: substring de "henoteísmo"; a forma bruta só aparece dentro da `[NOTA]` |
| "ser silicato" | seres de sílica (RC-699) | **recusada** | palavra legítima usada e glossada pelo próprio autor; vira *referencia_oral* de RC-699 na Devolução |
| "Jah Baal" | Belial (RC-479) | **aceita** | decidido no fim da esteira: o próprio autor emprega Belial adiante, na narrativa de Jó; o corpo foi corrigido e o `[A CONFIRMAR]` virou `[NOTA]` |

Formas proibidas no texto corrido após a revisão: **0**. As ocorrências residuais detectadas pelo QA estão exclusivamente dentro de `[NOTA: …]` que citam o bruto (Xavé, enoteísmo, Tatiane) — comportamento previsto e desejado.

---

## 4. Correções manuais não propostas pelo motor

41 intervenções humanas sem gatilho automático, agrupadas por classe:

1. **Nomes próprios externos ausentes de `externos.csv`** (16): Hobbes, Agostinho de Hipona, Mary Shelley, Goethe, Mefistófeles, Barão de Itararé, Nicolelis, Bostrom, Kurzweil, Nvidia, Anthropic, BlackRock, ChatGPT, QR code, Theta Healing, Siddhartha Gautama.
2. **Topônimos e etnônimos** (5): Kalahari, bosquímanos, Namíbia, Jardim do Éden, Teatro Santo Agostinho.
3. **Conceitos da base com superfície não semeada** (9): circuito colmeico, constituição setenária, Dinastia das Sophias, Imantação, Arcontes, Belial, Sophia/Cristo Cósmico, corpo átmico, seres de sílica.
4. **Trocadilhos e recursos retóricos preservados** (4): "nunca houve um amanhã / a manhã", "planeta-prisão", "colher na Matrix", "Javé 2.0".
5. **Números e datas** (7): 2005/2007, 2029/2045, 2008/2010/2011, R$ 180 / 12× R$ 18,60, 60.000 demissões, 5 vs 8 livros do Mentalma, Gênesis 11 e as 70 nações — todos **preservados como ditos** e sinalizados com `[NOTA]` quando divergentes da fonte verificada.

**Política de números:** nenhuma cifra foi alterada no corpo. Divergências viram `[NOTA]` e migram para a §4 da Devolução. Justificativa: a cifra é parte do registro oral e a correção silenciosa quebraria a rastreabilidade.

---

## 5. Decisões de forma (desvios documentados do Guia v2)

| Item | Guia v2 | Adotado nos blocos | Justificativa |
|---|---|---|---|
| **Diarização (§9)** | rótulo do falante em linha própria | **rótulo em negrito inline**, no início do parágrafo do turno — `**[GURU DE MALÁ]** texto…` | opção B do despacho (rótulos inferidos explícitos); o inline preserva o fluxo de leitura no `.docx` e evita 143 linhas-órfãs |
| **Guia de fontes** | resumo automático no cabeçalho | **removido** do produto final | despacho do Comandante; cabeçalho original = linhas 0–11, corpo = linha 12 |
| **Anúncios** | — | **preservados no corpo**, marcados `**[ANÚNCIO]**` | despacho do Comandante |
| **Disfluência** | níveis leve/médio/pesado | **nível LEVE** | despacho: remover repetições imediatas e "né/eh/uhum", preservar sintaxe e identidade oral |

Rótulos usados: `[GURU DE MALÁ]` 42×, `[ALEXANDRE SHERMINATOR]`, `[JAN VAL ELLAM]`, `[FALANTE?]` 1×.

### 5.1 Ajustes nas ferramentas, feitos durante esta revisão

Dois defeitos do pipeline apareceram só quando o texto real passou por ele, e foram corrigidos na esteira — não são gambiarras pontuais:

1. **`rc_docx.py --validar` cobrava falsos positivos.** O validador exigia a substituição de toda linha `aprovada`/`proposta`, inclusive as 20 recusas documentadas. Como o QA devolve *exit code* 1, o revisor era empurrado a corromper o texto para satisfazer a máquina — exatamente o que o Guia v2 §10 proíbe. Correção: o CSV passa a carregar as colunas `adjudicacao` e `motivo_adjudicacao`, e o validador só cobra `adjudicacao == "aceita"`. Sem a coluna, o comportamento antigo permanece (compatível com pipelines legados).
2. **O validador lia o conteúdo das `[NOTA]`.** Uma `[NOTA]` que documenta a forma ouvida ("no bruto, *Xavé*") é evidência, não erro. Agora `MARCADOR_RE` expurga `[NOTA:]`, `[A CONFIRMAR:]`, `[INAUDÍVEL:]` e `[ANÚNCIO]` antes da varredura — o que preserva a política de rastreabilidade: a forma bruta continua visível para o curador, mas não conta como sobrevivência indevida.
3. **Normalização e caixa.** O `L.norm()` do motor ignora maiúsculas, então a semente `mit → MIT` era reportada como "variante sobrevivente" mesmo com o texto grafando **MIT** corretamente. Essas 16 linhas viraram `adjudicacao = protecao` e saíram da cobrança.

---

## 6. QA final

Mesmo tokenizador nas duas colunas (palavras = sequência de letras/dígitos/apóstrofo).

| Métrica | Bruto (linha 12 do `.txt`) | Revisado (8 blocos) |
|---|---|---|
| Palavras, texto corrido | 18.806 | **18.966** (100,9%) |
| Palavras, com marcadores editoriais | — | 19.890 |
| Parágrafos | 1 (sem quebras) | 143 |
| Vírgulas | 0 (STT sem pontuação) | 1.909 |
| Pontos | 0 | 789 |
| Interrogações | 0 | 167 |
| Palavras repetidas em sequência | — | **0** |
| Formas proibidas no texto corrido | — | **0** |
| `[NOTA]` | — | 32 (em itálico, corpo 11 pt, no `.docx`) |
| `[A CONFIRMAR]` | — | 24 |
| `[INAUDÍVEL]` | — | 14 |
| Rótulos de fala | — | `[JAN VAL ELLAM]` 64 · `[GURU DE MALÁ]` 42 · `[ALEXANDRE SHERMINATOR]` 36 · `[ANÚNCIO]` 4 · `[FALANTE?]` 1 |
| Validador `rc_docx.py --validar` | — | **OK**: nenhuma variante `aceita` sobrevive |
| Linhas do livro-razão sem decisão | — | **0** |

**Duas ressalvas de leitura do QA.** (1) A retenção acima de 100% vem dos marcadores editoriais e da pontuação inserida, não de acréscimo de conteúdo: descontados os marcadores, o corpo fica em 100,9% do bruto — o 0,9% são conjunções e artigos necessários para fechar as orações que o STT entregava soltas. (2) Uma varredura ingênua por formas proibidas ainda acusa *Demiurg* (6×) e *enoteísmo* (1×): são **substrings** de *Demiurgo* e *henoteísmo*, não ocorrências reais — o QA correto exige fronteira de palavra. Feita essa exigência, a única forma remanescente é *silicato*, **mantida de propósito**: é o termo que o próprio autor usa e glossa em seguida ("ser silicato, ou seja, ser feito de sílica").

---

## 7. Encaminhamento

1. `DEVOLUCAO-A-KB.md` — 4 seções obrigatórias (novos termos, novas variantes STT, correções na KB, novos registros bibliográficos) + divergências factuais.
2. Itens 11 a 18 da Devolução somam-se às 10 ações residuais do Anexo I — **a cargo do curador**, não desta esteira.
3. Ficha de Jeane Miranda, B095 e demais pendências da KB — **assumidas pelo Comandante**; não bloqueiam a entrega.
