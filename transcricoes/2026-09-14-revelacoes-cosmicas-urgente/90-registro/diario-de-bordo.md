# Diário de bordo — Revelações Cósmicas Urgente

Registro cronológico do que foi feito, do que falhou e do que foi decidido ao longo do caminho.
*Append-only*: entrada nova embaixo, nunca reescrita em cima. É o que permite a outra pessoa —
ou a outro agente, noutra sessão — retomar sem refazer descobertas.

---

## 2026-09-15 — auditoria e protótipo

- Auditado o repositório: 4 arquivos na raiz (README, Guia v1 em `.docx`, planilha
  `base-terminologica.xlsx` com 946 termos/104 obras/1.887 relações, e o `.txt` da transcrição).
- Lido o bruto: **101.468 caracteres numa única linha, sem nenhuma pontuação**, corpo na linha 13
  (índice 12); linhas 1 a 12 são cabeçalho com o "Guia de fontes".
- Protótipo de varredura: a intuição ("ler e ir corrigindo") não fecha — 18.806 palavras contra
  946 termos exige motor. Decidido construir pipeline em três passos: léxico → diagnóstico →
  montagem.
- Escrito `docs/pareceres/parecer-de-viabilidade.md`: viável, com a condição de que a
  substituição seja sempre adjudicada por humano.

## 2026-09-15 — ferramentas

- `rc_kb.py` (camada 1: leitura da KB-RC), `rc_lexicon.py` (normalização pt-BR + chave fonética),
  `rc_variantes.py` (extrai da **prosa** das 820 fichas a camada variante → canônico: 1.590 pares,
  299 regras de substituição), `rc_diagnostico.py`, `rc_docx.py`, `md_para_docx.py`.
- **Beco sem saída:** o campo "Variações" das fichas NÃO é regra de substituição — é conceitual.
  Tratá-lo como regra gerava propostas absurdas. Alvos com mais de 4 palavras foram reclassificados
  como `referencia_oral`.
- **Beco sem saída:** sementes curtas colidem com palavra comum (`Nick` → Nyx). Criado
  `vocabular-guarda-pt.txt` (1.878 formas) e a proteção da camada Externos.
- **Erro grave encontrado e corrigido:** o motor casava superfícies *variante_stt* que estão no
  índice canônico e propunha "Javé → jabe" — inversão de direção. Correção: pular se a forma
  normalizada já é canônica, e exibir `canonico_display` / `superficie_casada`.
- **Erro:** a regra de homografia em sementes disparava em excesso (Terra Atlântis, Alamaior,
  Tempérium). Resolvido com `remissivo()` e comparação do código dono da ficha.

## 2026-09-15 — KB-RC vira fonte de verdade

- Despacho do Comandante: **`KB-RC/` + JSONs são a fonte de verdade; a planilha é legado.**
- Importados `canonico.json` (946 termos), `biblio.json` (97 códigos B — **falta B095**) e
  `KB-RC/termos/` (820 fichas, 7,1 MB). 126 termos não têm ficha.
- Escrito `docs/normas/resolucao-de-conflitos.md` (Anexo I): os oito conflitos da base resolvidos
  um a um, com 10 ações residuais para o curador.

## 2026-09-16 — Guia v2 e despacho do Comandante

- Entregue `docs/normas/guia-revisao-v2.md` (18 seções) + `.docx`.
- Despacho do Comandante: **autorização total para processar e revisar os 8 blocos**, com contrato
  editorial fechado (ver `despachos/2026-09-15-contrato-editorial.md`).
- `externos.csv` montado com 37 entidades — em formato *pipe*, que **não carregava**: `csv.DictReader`
  espera vírgula. Convertido com `csv.writer`; comentários `#` quebravam a leitura até o patch em
  `rc_lexicon.carregar_sementes()`.
- **"Sherminetro" não é Terminator.** Quase virou semente externa apontando para a franquia; é o
  apelido do apresentador. Lição: nunca criar semente sem ler o contexto.
- Diagnóstico final: 100 superfícies da base presentes no texto · 61 adjudicáveis · 145 ausentes ·
  90 termos no dossiê de trabalho (≈1.153 tokens).

## 2026-09-16 — revisão dos blocos 1 a 8

- Blocos 1 a 3: Jan Vaillan/Jean Valan → Jan Val Ellam; Emanuel Kant → Immanuel Kant; Yahé/Jahé →
  Javé; Thomas Robs → Thomas Hobbes; Agostinho de Pona → Agostinho de Hipona; Mary Chiley → Mary
  Shelley; Kaagen → **/Kaggen** (verificado externamente: divindade San do Kalahari, forma de
  louva-a-deus, registrada por Bleek e Lloyd nos anos 1870); Ganexa → Ganesha; avaloque texwara →
  Avalokiteshvara; constituição centenária → **setenária**; enoteísmo → henoteísmo.
- Blocos 4 a 6: A Divina Calmeia → *A Divina Colmeia* (B044); circuito coméico → circuito colmeico
  (RC-176); Raymond Kzwell/Cselva/Curzell/Crowsa/Curs/Czel/Curser → **Ray Kurzweil** (nove
  superfícies colapsadas); Nick Bostron → Nick Bostrom; Utopia Profunda → *Deep Utopia*; Get →
  Goethe; barão de Tararé → Barão de Itararé; Miguel Nicoles → Miguel Nicolelis.
- Blocos 7 e 8: arcturianos (**ausente da KB** — lacuna grave, já que Capela está registrada);
  arcontos/arces/arcos/erontes → Arcontes (RC-474); Sofia o Cristo Cosmo Rock → Sophia, o Cristo
  Cósmico (RC-009); espírito mantado → imantado (RC-699); dinastia das Sofias → Dinastia das
  Sophias (RC-494).
- **Corrigida troca de falantes** no diálogo da levitação (bloco 8): a atribuição invertida mudava
  o sentido da passagem.
- **Achado "Rogério":** nome civil provável do próprio Jan Val Ellam (1ª pessoa + exemplos em 3ª).
  Mantido como dito, com `[NOTA]`.

## 2026-09-16 — QA e correções tardias

- QA dos 8 blocos: 0 palavras repetidas em sequência, 0 formas proibidas no texto corrido.
- **"Xavé" escapou no bloco 2** e foi pego pelo QA: corrigido para Javé com `[NOTA]` documentando a
  variante. A única ocorrência residual é dentro da nota, citando o bruto — comportamento esperado.
- **"Jah Baal" era `[A CONFIRMAR]` indevido:** o próprio autor emprega Belial adiante, na narrativa
  de Jó. Corrigido para Belial (RC-479) e o marcador convertido em `[NOTA]`.
- **"ser silicato" quase foi corrigido** para "ser de sílica": o autor usa o termo e o glossa em
  seguida. Mantido; vai para a KB como *referencia_oral* de RC-699.

## 2026-09-16 — adjudicação, devolução e produto

- Livro-razão gravado em `../10-diagnostico/variantes-propostas.csv` com as colunas `adjudicacao` e
  `motivo_adjudicacao`: **98 linhas, 0 sem decisão** (24 aceitas · 7 parciais · 20 recusadas ·
  30 informativas · 16 de proteção · 1 superada).
- **Defeito do validador descoberto aqui:** `rc_docx.py --validar` cobrava a substituição das 20
  linhas recusadas e devolvia *exit code* 1 — ou seja, o QA empurrava o revisor a corromper o texto
  para satisfazer a máquina. Corrigido: só se cobra `adjudicacao == "aceita"`, e o conteúdo dos
  marcadores editoriais é expurgado antes da varredura.
- Escritos `../40-devolucao/devolucao-a-kb.md` (10 novos termos, ~50 variantes STT, 8 correções na
  KB, 7 divergências factuais) e `adjudicacao.md`.
- Montado `../30-produto/transcricao-revisada.docx`: 143 parágrafos, 32 notas em itálico, títulos
  em Heading 2.

## 2026-09-16 — migração do repositório

- Aprovado o `docs/planos/plano-de-organizacao.md` (quatro decisões do Comandante: por transcrição,
  ASCII-safe, mídia só por link externo, migrar agora).
- Esta pasta nasceu da migração: o bruto saiu da raiz, os blocos saíram de `analise/…-kb/blocos/` e
  foram renomeados para `bloco-0N.md`, os produtos saíram da raiz e de `analise/`.
- Tag `v1-antes-reorganizacao` marca o estado anterior; a migração foi em cinco fases, um commit por
  fase, tudo com `git mv`.
- **Verificação pós-mudança:** o `.docx` foi regenerado no caminho novo e comparado parágrafo a
  parágrafo com o anterior — 154 = 154, nenhuma diferença. O diagnóstico foi refeito com o código
  novo e reproduziu exatamente as mesmas métricas (100 superfícies · 61 adjudicáveis · 145 ausentes
  · 90 termos no dossiê · 98 linhas).
- **Incidente:** o commit de normalização de fins de linha reescreveu o *blob* deste bruto no
  repositório (CRLF → LF), sem tocar no arquivo de trabalho. O sha256 gravado em `metadados.yaml`
  é o que permitiu perceber: `34f9bcf4…` contra `db3fa8ae…`. Corrigido no commit seguinte com
  `-text` no `.gitattributes` para `00-fonte/*.txt|.vtt|.srt`, blob restaurado e conferido por
  clone fresco + portão G1 verde. **Lição:** convenção de estilo não se aplica a evidência — o
  bruto é o único arquivo deste repositório que não pode ser "melhorado".

---

## Becos sem saída — não repetir

| Tentativa | Por que falhou |
|---|---|
| Tratar o campo "Variações" das fichas como regra de substituição | é campo conceitual; gerava propostas absurdas |
| Sementes externas sem ler o contexto | "Sherminetro" quase virou *Terminator* |
| `externos.csv` em formato *pipe* | `csv.DictReader` usa vírgula; o arquivo carregava vazio |
| Comentários `#` dentro de CSV lido por `DictReader` | viravam linha de dados; exigiu patch no carregador |
| QA por substring, sem fronteira de palavra | acusa *Demiurg* dentro de *Demiurgo* e *enoteísmo* dentro de *henoteísmo* |
| Regex única para negrito/itálico/código no conversor | o itálico casava através de `código` com asterisco e emendava trechos distantes |
| Corrigir cifra divergente no corpo | quebra a rastreabilidade; o certo é `[NOTA]` + devolução ao produtor |
| Fuzzy sem vocabulário-guarda | `Nick` → Nyx, `a vista` → Avesta, `Cristo` → Krishna |

## 16/09/2026 — a fonte deixou de ser órfã: URL registrada, padrão Y, lote 02

O Comandante forneceu o URL que faltava desde a captura de 15/09 e aprovou o padrão Y para fontes
audiovisuais. O que isso fechou, nesta pasta:

- **URL gravada nos três lugares** que precisam concordar: `00-fonte/metadados.yaml`,
  `00-fonte/midia/README.md` e `KB-RC/biblio.json` (registro `Y2026-09-14`). O CI confere os três
  desde então (`rc_indice.py --checar`).
- **Duração corrigida: 125 → 146 min.** O vídeo tem 2:25:50 conferidos na plataforma; os 125 eram
  estimativa da captura. Registrado também em `duracao_real` e no registro Y.
- **Título oficial confirmado:** *ASSISTA ANTES QUE SAIA DO AR - Jan Val Ellam*, canal PARANORMAL
  EXPERIENCE (@PARANORMALBR), publicado em 14/09, upload em 15/09/2026 — bate com a `chamada` e com
  o `titulo` que a captura registrou.
- **A descrição oficial corroborou dois pontos da revisão:** o anúncio da Insider com cupom PARANORMAL
  (bloco 1) e as Mandalas Arcturianas (bloco 6, que sustentou o termo novo RC-951).
- **E acrescentou um alerta:** a descrição anuncia *outro* evento — Conexão com os Guardiões
  Espirituais, Robson Pinheiro, R$ 160 ou 10× R$ 16 — que **não** é o evento de 03/10 no Teatro Santo
  Agostinho citado no bloco 3 (Terry Fabris + Robson Pinheiro, R$ 180 ou 12× R$ 18,60). As duas
  `[NOTA]` de preço do bloco 3 continuam corretas: o áudio diz "10 parcelas de R$ 18", que fecha com
  R$ 180. O risco de conflate ficou registrado no item 0041 da fila, para não virar erro numa
  revisão futura. **Nenhuma linha do produto foi alterada** — a revisão continua aprovada como está.
- **Os 10 termos propostos por esta transcrição foram criados** (RC-947 a RC-956) no lote 02 de
  curadoria, citando `Y2026-09-14`. Nenhum nasceu `verificado`: fonte audiovisual única, STT sem
  pontuação, entram `provisório` (9) ou `candidato` (1 — Tom Teltan, grafia `[A CONFIRMAR]`).
- **Uma variante mudou de ficha por causa disso:** "circuito coméico" estava em RC-176 (Modelo
  Colmeia) porque não havia canônico próprio; com RC-953 (Circuito Colmeico) criado, a variante foi
  movida e RC-176 recebeu remissiva. É o único caso de variante que trocou de ficha.
- **Item 0023 desbloqueado:** "constituição centenária" esperava o termo *Constituição Setenária*
  (RC-952) existir; já nasceu na ficha dele.
\n
---

## 16/09/2026 — experimento de motor STT: régua pronta, lado B ausente

- **Despacho do Comandante:** lote 02 ratificado (com elogio ao tratamento do bug `/Kaggen`) e nova
  missão, urgente e substitutiva — comparar o STT do YouTube com o do **NotebookLM** sobre o mesmo
  áudio e emitir parecer de engenharia em quatro eixos (pontuação/segmentação, disfluência,
  fidelidade terminológica contra a KB, veredito de integração). Critério de aceite fixado por ele:
  diagnóstico de viabilidade **antes** de definir o novo padrão de entrada da esteira. Os 14 itens
  pendentes da fila e a segunda transcrição tradicional foram para a **geladeira** por ordem expressa.
- **O arquivo `Opcao-B.txt` não chegou.** Varredura completa (`/home/user`, `/tmp`, `git status`
  limpo em `3d45365`, workspace do Arena): não existe cópia em lugar nenhum. Nenhuma comparação foi
  simulada e nenhum número de B foi inventado — o parecer saiu com status **PARCIAL** e "aguardando"
  onde falta medição.
- **Instrumento construído: `ferramentas/rc_perfil_stt.py`.** Mede os quatro eixos sobre qualquer
  arquivo de STT; com dois argumentos imprime o comparativo A × B com coluna "melhor"; com
  `--com-diagnostico` roda o motor da casa inteiro sobre cada arquivo, que é a medida mais direta de
  carga das `rc_*`. Sai em terminal, `--json` e `--md`. 3 s sem diagnóstico, 8 s com.
- **A régua tinha três defeitos que teriam falsificado o resultado — corrigidos antes de medir:**
  1. marcador oral contado no texto normalizado: `norm("ó") == "o"` contava o artigo e inflava a
     disfluência do lado A de 768 para 1.308 marcas (+71%);
  2. `Variações` da ficha (equivalência **conceitual**, Guia §5) contado como corrupção: apontava
     "humano"×58 e "espirito"×12 como erro do motor e derrubava a taxa de confiança de 0,8262 para
     0,6040;
  3. `externos.csv` lido sem pular os comentários `#` que antecedem o cabeçalho: zero entidades
     Externos medidas, exatamente a camada que protege "Ray Kurzweil".
  Os três estão travados por teste. Teste de fumaça: **105 → 124 verificações, 0 falhas**. QA G1–G8
  verde, sha256 do bruto intacto.
- **Linha de base A medida** (`00-fonte/transcricao-bruta.txt`, 106.243 bytes, estágio bruto):
  18.966 palavras · 0,22 sinais por 100 palavras · 35 sentenças · mediana de 331 palavras/sentença
  (maior: 2.604) · **4 parágrafos reais, todos do cabeçalho — o corpo é uma linha só** · 768 marcas
  de disfluência (40,49/1.000; 115 repetições de palavra) · 271 ocorrências canônicas × 57 corrupções
  mapeadas · taxa de confiança 0,8262 · 56 ocorrências de Externos corrompidos · e **263 itens de
  curadoria** gerados pelo diagnóstico (132 linhas de livro-razão, das quais 44 propostas a decidir,
  + 131 formas ausentes da base).
- **Viés da régua registrado:** a KB foi construída *sobre* as corrupções deste STT (90 variantes dos
  lotes 01 e 02), então as corrupções de A já estão mapeadas e as de B apareceriam como "ausentes da
  base". Métrica simétrica adotada: **carga terminológica total = linhas do livro-razão + ausentes**.
  Limiar de vitória de B pré-registrado em ≤ 197 itens (redução de 25%).
- **Defeito latente da esteira, descoberto pelo experimento e independente do resultado:**
  `rc_novo.py:71` e `rc_indice.py:62` tomam o corpo como `max(linhas, key=len)`, enquanto
  `rc_diagnostico.carregar_transcricao` o separa pelo marcador "Transcrição Automática". Sobre A os
  dois critérios coincidem (a linha 12 tem 101.468 chars) e ninguém notou. Sobre um STT paragraphado,
  `max(linhas, key=len)` devolve **um parágrafo** e grava `corpo_palavras` fracionário no
  `metadados.yaml` — sem exceção, sem aviso, com o QA G1 verde (ele confere sha256, não coerência).
  Recomendação escrita no parecer §5: unificar o critério num só lugar, com cascata
  marcador → linha mais longa → arquivo inteiro, e guarda que avise quando a cobertura da maior linha
  ficar abaixo de 80%.
- **`upload/` implantada** (resposta à pergunta do Comandante, com implementação em vez de opinião):
  zona de trânsito ignorada pelo git (`/upload/*` + `!/upload/README.md`, verificado com
  `git check-ignore`), porque fonte de verdade não pode morar fora do alcance do QA G1. O ciclo é
  `upload/` → perfil → parecer → `00-fonte/` versionado com sha256. O README lista as quatro vias de
  entrega para quando o anexo do chat falhar: reanexar, colar, link público (Drive aberto) ou commit
  do Comandante com `git add -f`.
- **Parecer publicado:** `docs/pareceres/parecer-motor-stt.md` + `.docx`. Traz a linha de base, os
  três defeitos de régua, os **critérios de decisão pré-registrados** (limiares numéricos fixados
  antes de existir qualquer número de B, para que a trave não possa ser movida depois) e a guarda de
  comparabilidade: se B tiver menos de 90% ou mais de 110% das palavras de A, o parecer não compara
  motores — compara recortes, porque ferramenta que resume pode devolver síntese em vez de transcrição.
- **Fixture sintético** `testes/fixtures/stt-com-paragrafos-sintetico.txt`: escrito à mão para provar
  que o eixo 4 detecta arquivo paragraphado. Está rotulado como sintético no próprio cabeçalho e
  **nenhum número dele entra no parecer**.
- **Becos sem saída deste turno:** caminhos relativos em ferramenta de escrita criaram um diretório
  `Transcri-YouTube/` aninhado dentro do repositório (movido e removido); e assertiva de teste com
  corte fixo de 0,8 de cobertura falhou sobre o fixture pequeno, onde o cabeçalho pesa — o corte é
  comportamento correto em arquivo grande, e o teste passou a medir a discriminação (3× entre os dois
  formatos) em vez de um limiar absoluto.
- **Pendente, e só isso fecha o parecer:** o arquivo B. Comando pronto no §7 do parecer.
\n
---

## 16/09/2026 — o arquivo B chegou: medição completa e a descoberta de que não são dois motores

- **`Opcao-B.txt` chegou pela quarta via do `upload/README.md`** — commit direto do Comandante pela
  interface web do GitHub (`6eddae0`, "Add files via upload"), que grava na **raiz** do repositório.
  109.452 bytes, 300 linhas, sha256 `5aa247f3487752…`. Meu trabalho local foi rebasado sobre ele.
- **O cabeçalho de B é cópia do de A** (linhas 0–11 idênticas, mais um separador `====` na linha 10).
  Logo a prosa do "Guia de fontes" não é saída do NotebookLM, e o marcador "Transcrição Automática"
  presente em B é mérito de quem preparou o arquivo, não do motor. Um export futuro sem cabeçalho
  quebraria essa suposição também.
- **Guarda de comparabilidade aprovada:** 18.966 palavras em A contra 18.975 em B (+9, +0,05%), mesmo
  áudio de 2h25min50s, os dois acentuados, os dois em estado bruto.
- **A descoberta que requalifica a pergunta do despacho: não há dois motores.** Divergência lexical
  3,00% (280 palavras de A ausentes em B, 289 de B ausentes em A), Jaccard de vocabulário 0,929,
  93% dos hapax em comum, e **nove marcadores orais com contagem idêntica ao dígito** (então 132,
  uhum 31, cara 26, tipo 25, ó 21, tô 20, sabe 17, quer dizer 5, sei lá 2). A repetição "blá"×22
  aparece igual nos dois. Dois ASR diferentes erram diferente; estes erram igual. É o reconhecimento
  de fala do YouTube com uma **camada de reescrita** por cima.
- **A camada CENSURA.** Cinco tokens mascarados com asterisco, todos inexistentes em A: três `m****`
  (onde A diz "merda") e dois `b******` (onde A diz "bandido") — estes num trecho teologicamente
  central: "os europeus viam Jesus como um b******" e "não mais um b****** judeu". Asterisco não é
  palavra; se B entrasse em `00-fonte` como bruto, essas cinco palavras estariam perdidas e o QA G1
  continuaria verde, porque ele confere sha256, não conteúdo.
- **Outras microedições localizadas, todas conferidas nos dois textos:** "planeta de expiação **e**
  provas" → "**em** provas" (uma preposição derrubou o casamento com RC-954, que zerou em B);
  "as calmeias começaram a colapsar" → "as colmeias" (corrigiu uma das duas ocorrências, produzindo
  inconsistência interna); "num circuito" → "num num circuito" (acrescentou palavra).
- **Placar dos quatro eixos contra os limiares pré-registrados:** eixo 1 **B ganha 4 de 4** (sinais
  por 100 palavras 0,22 → 15,93; mediana de palavras por sentença 331 → 11; maior sentença 2.604 →
  75; segmentos nativos 8 → 295). Eixo 2 **B perde** (40,49 → 40,79 marcas por 1.000 palavras: a
  camada não limpa disfluência, e as 12 repetições a mais são ruído de palavra funcional — "que"
  17→14, "não" 10→13, "blá" 22→22). Eixo 3 **B perde pelo limiar composto** (carga terminológica
  total 263 → 342 contra teto de 197) mas **ganha nos três acessórios** (taxa de confiança 0,8262 →
  0,8476; formas proibidas 37 → 10 ocorrências; Externos corrompidos 56 → 51). Eixo 4 **B é 3/4**:
  uma quebra custa código (linha mais longa: cobertura de 98,9% → 3,9%) e uma premissa foi superada
  (Guia §8, pontuação nativa).
- **A pergunta literal do despacho — B alucinou menos ou mais nas entidades dos lotes 01 e 02? —
  resposta: praticamente igual.** Canônicos 113 (A) × 109 (B); corrupções 51 × 43. `/Kaggen` é
  corrompido de forma **idêntica** nos dois (3× `kaagen`/`kaagem`), o que é mais uma prova do mesmo
  ouvido. B eliminou os dois truncamentos `demiurg` de RC-048 e piorou RC-756 (Ganesha: 4 grafias
  contra 3). Dispersão: 75 grafias/58 entidades (1,29) em A contra 77/63 (1,22) em B.
- **Quarto defeito de régua, este do motor da casa:** `rc_diagnostico.py:372` procura **sequências
  capitalizadas** sem registro. Num STT pontuado toda inicial de frase é maiúscula, e a lista de
  ausentes de B encheu de verbo comum. Separando os baldes: dos 211 ausentes de B, 83 são janelas,
  26 vocabulário comum e 26 inicial de frase — sobram **76 candidatas reais**, contra 41 em A (que
  tem 131 brutos). Ainda é resíduo contaminado ("Desintegrou", "Oremos", "Acreditem"). Conclusão
  honesta: não há evidência de que B alucine mais entidades; há evidência de que a régua conta mais
  candidatos quando o texto é pontuado. O limiar de 197 reprovou B por um efeito da virtude de B —
  registrado no parecer como derrota pré-registrada **e** como métrica que precisa de versão 2.
- **Veredito do parecer:** adotar a saída do NotebookLM como **texto de trabalho**, nunca como fonte.
  `00-fonte` continua sendo o STT cru do YouTube (imutável, sha256, G1); o derivado pontuado entra
  ao lado, versionado, com proveniência e divergência registradas em `metadados.yaml`; e a esteira
  ganha o portão **G9 (divergência produto × bruto)**, que sobre este experimento teria apontado
  sozinho as cinco palavras censuradas. Custo de código: 5 itens, cerca de um dia.
- **Instrumento ampliado no caminho:** eixo de **proveniência** (divergência lexical, Jaccard, hapax,
  marcadores idênticos, tokens mascarados) — é o que impede o parecer de atribuir ao motor errado o
  que é mérito ou dano da camada de reescrita; separação de ruído nos ausentes; dispersão de grafias
  por entidade; e o veredito de integração em **três estados** (compatível / custa código / premissa
  superada), porque "incompatível" estava rotulando como defeito justamente o ponto em que B mais
  ajuda. Tabela comparativa virou fonte única entre terminal e markdown — duas listas separadas já
  tinham produzido um relatório mais curto que a medição.
- **Testes: 124 → 136 verificações, 0 falhas.** QA G1–G8 verde, bruto de A intacto.
- **Pendência de decisão do Comandante:** (1) a arquitetura de três camadas do parecer §6; (2) o
  destino do `Opcao-B.txt`, que está na raiz — lugar que o Plano de Organização não prevê. Não movi o
  arquivo por conta própria: é entrega dele e o destino depende da arquitetura aprovada.
