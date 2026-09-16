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
