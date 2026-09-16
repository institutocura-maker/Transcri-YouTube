# Plano de Organização do Repositório — Transcri-YouTube

**Autor:** Agente 86 · **Data:** 16 de setembro de 2026 · **Status:** **APROVADO E EXECUTADO** em 16/09/2026
**Decisões do Comandante (16/09/2026):** organização **por transcrição** · nomenclatura **ASCII-safe** · mídia **só por link externo** · migração **imediata**.
Relato da execução, com o que mudou em relação à proposta: §14.
**Escopo:** estrutura de pastas, convenções de nomenclatura, ciclo de vida das transcrições, política de arquivos grandes, automação de QA e plano de migração.
**Gatilho:** o repositório vai deixar de ter 1 transcrição e passar a ter várias, além de outros tipos de arquivo do Projeto.

---

## 1. Diagnóstico do estado atual

O repositório cresceu de forma orgânica durante a primeira transcrição. O que serviu para um vídeo não serve para dez.

| # | Problema | Evidência | Consequência se nada for feito |
|---|---|---|---|
| 1 | **A raiz virou depósito** | `.txt` bruto, `.docx` final, Guia v1, Guia v2 (`.md`+`.docx`), planilha legada e README convivem no mesmo nível | A cada nova transcrição somam-se 2 arquivos na raiz; em 20 vídeos são 40 arquivos soltos |
| 2 | **Duas pastas para a mesma transcrição** | `analise/revelacoes-cosmicas-urgente-jan-val-ellam/` (protótipo) e `…-jan-val-ellam-kb/` (definitiva) | Ninguém sabe qual é a boa sem abrir as duas |
| 3 | **Documento de projeto misturado com trabalho de transcrição** | `analise/` guarda PARECER e RESOLUCAO-DE-CONFLITOS (normativos, valem para sempre) ao lado das pastas por vídeo (descartáveis quando o vídeo fecha) | Documentos normativos ficam enterrados e somem do radar |
| 4 | **Código misturado com dados** | `ferramentas/` tem 6 scripts `.py` + 4 arquivos de dados (`.csv`/`.txt`) que os scripts consomem | Dados curados (sementes, externos, vocabulário-guarda) não têm dono nem histórico claro |
| 5 | **O produto final fica longe da transcrição** | `Revelações Cósmicas Urgente – Jan Val Ellam (revisado).docx` está na raiz; os blocos que o geraram estão em `analise/…-kb/blocos/` | Impossível saber, olhando o arquivo, de qual vídeo ele veio |
| 6 | **Não há lugar para mídia** | nenhum diretório para áudio/vídeo; nenhum `.gitattributes` | Alguém vai subir um `.mp4` de 300 MB no Git e o clone fica inutilizável |
| 7 | **Não há catálogo nem status** | nada diz quantas transcrições existem, em que estágio estão, qual a URL de origem | Controle por memória; trabalho duplicado ou esquecido |
| 8 | **Nomes longos, com espaço e acento** | `Revelações Cósmicas Urgente – Jan Val Ellam.txt` (travessão U+2013) | Quebra `for` em shell, exige aspas em todo script, dificulta URL e CI |
| 9 | **Ordenação de blocos frágil** | `bloco-1.md` … `bloco-8.md`; com 12 blocos o glob ordena `bloco-1, bloco-10, bloco-11, bloco-2…` | O DOCX final sairia com blocos fora de ordem — defeito silencioso e grave |
| 10 | **Sem portão de qualidade automático** | o QA existe (`rc_docx.py --validar`) mas só roda se alguém lembrar | Regressão entra sem barreira; o `.docx` pode divergir dos `.md` |

**O que está bom e deve ser preservado:** `KB-RC/` como fonte de verdade isolada e autocontida; `ferramentas/` com scripts de propósito único e docstring explicando o *porquê*; o contrato de dupla saída `.md` + `.docx`; o `.gitignore` já distinguindo regenerável de precioso; a numeração embrionária de estágios que o README ensaia (`20-blocos/`, `40-final.docx`).

---

## 2. Princípios

Dez princípios. Toda decisão concreta deste plano deriva deles — e é por eles que uma proposta futura deve ser julgada.

| # | Princípio | Tradução prática |
|---|---|---|
| **P1** | **Uma transcrição = um diretório autossuficiente** | Tudo o que diz respeito a um vídeo vive dentro da pasta dele. Arquivar, reativar ou auditar um vídeo é operar uma pasta, não caçar arquivos em quatro árvores |
| **P2** | **O bruto é sagrado e isolado** | `00-fonte/transcricao-bruta.txt` nunca é editado. Sua integridade é verificada por hash no CI |
| **P3** | **Estágio no nome, ordem no número** | `00 → 10 → 20 → 30 → 40 → 90`. O vão de 10 permite inserir etapas sem renumerar nada |
| **P4** | **O slug vive na pasta; os arquivos têm nome fixo** | Dentro de `transcricoes/<slug>/` o produto é sempre `transcricao-revisada.docx`. Caminhos previsíveis = automação sem parâmetro |
| **P5** | **ASCII em caminho de máquina, legibilidade em documento de gente** | Pastas e arquivos operacionais sem acento nem espaço. Títulos com acento só *dentro* dos documentos |
| **P6** | **Código separado de dados** | `ferramentas/*.py` versus `ferramentas/dados/*`. Dado curado tem histórico próprio e é o que mais cresce |
| **P7** | **A KB-RC não se move** | Fonte de verdade referenciada por 6 scripts e 82 documentos. Renomeá-la é risco sem ganho |
| **P8** | **Regenerável é versionado, lixo não** | `diagnostico.json` fora do Git; os CSV de decisão dentro (são o livro-razão) |
| **P9** | **Peso pesado fora do Git** | Áudio e vídeo por link externo ou LFS, nunca no repositório comum |
| **P10** | **Nada se apaga: legado é arquivado com data** | Guia v1, planilha e protótipo vão para `docs/legado/`, não para a lixeira |

---

## 3. Estrutura proposta

```
Transcri-YouTube/
│
├── README.md                       porta de entrada: o que é, como rodar, onde está cada coisa
├── .gitignore                      lixo e regeneráveis
├── .gitattributes                  LFS, binários, fim de linha
│
├── docs/                           documentos DO PROJETO (valem para todas as transcrições)
│   ├── normas/
│   │   ├── guia-revisao-v2.md          norma editorial vigente
│   │   ├── guia-revisao-v2.docx
│   │   └── resolucao-de-conflitos.md   Anexo I — os 8 conflitos resolvidos
│   ├── pareceres/
│   │   └── parecer-de-viabilidade.md
│   ├── planos/
│   │   └── plano-de-organizacao.md     este documento
│   └── legado/                     congelado, datado, somente leitura
│       ├── 2026-09-guia-v1/
│       ├── 2026-09-base-terminologica.xlsx
│       └── 2026-09-prototipo-analise/
│
├── KB-RC/                          FONTE DE VERDADE (não muda de lugar — P7)
│   ├── canonico.json               946 termos + 1.887 relações
│   ├── biblio.json                 104 obras
│   ├── termos/                     820 fichas RC-*.md
│   ├── CHANGELOG.md                NOVO: quem aplicou o quê, quando, a pedido de qual transcrição
│   └── _fila-de-curadoria.csv      NOVO: propostas pendentes, consolidadas de todas as transcrições
│
├── ferramentas/                    SOMENTE código (P6)
│   ├── rc_kb.py  rc_lexicon.py  rc_variantes.py
│   ├── rc_diagnostico.py  rc_docx.py  md_para_docx.py
│   ├── rc_novo.py                  NOVO: cria a pasta de uma transcrição a partir do modelo
│   ├── rc_indice.py                NOVO: regenera o catálogo e confere consistência
│   ├── rc_qa.py                    NOVO: os 8 portões de qualidade
│   ├── requirements.txt
│   └── dados/                      dados curados que os scripts consomem
│       ├── sementes-variantes-stt.csv
│       ├── externos.csv
│       ├── variantes-kb-extraidas.csv   (gerado por rc_variantes.py)
│       └── vocabular-guarda-pt.txt
│
├── transcricoes/                   UM DIRETÓRIO POR VÍDEO (P1)
│   ├── _indice.csv                 catálogo: uma linha por transcrição
│   ├── _indice.md                  mesma informação, legível no GitHub
│   ├── _modelo/                    esqueleto copiado por rc_novo.py
│   ├── 2026-09-14-revelacoes-cosmicas-urgente/
│   ├── 2026-10-02-lemuria-terry-fabris/
│   └── …
│
├── publicacoes/                    produtos prontos para distribuição (opcional, fase 2)
│   └── 2026-09-14-revelacoes-cosmicas-urgente.docx
│
├── testes/                         fixtures e testes do pipeline
│   ├── fixtures/mini-transcricao.txt
│   └── test_pipeline.py
│
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CONTRIBUTING.md             papéis: revisor, curador, Comandante
│
└── ferramentas/ci/
    ├── qa.yml                      CI pronto: roda os portões em todo PR
    └── README.md                   como ativar (ver §14.4)
```

### 3.1 O que entra e o que não entra em cada pasta

| Pasta | Entra | **Não** entra |
|---|---|---|
| `docs/` | norma, parecer, plano, anexo — texto que rege o processo | trabalho de uma transcrição específica |
| `KB-RC/` | termos, obras, fichas, histórico de curadoria | transcrições, blocos, produtos |
| `ferramentas/` | código executável | dados curados (vão para `dados/`), saídas de processamento |
| `transcricoes/<slug>/` | tudo o que pertence àquele vídeo, do bruto ao produto | norma geral, código, mídia pesada |
| `publicacoes/` | versão final congelada para distribuir | rascunho, bloco, diagnóstico |
| `testes/` | fixtures pequenas e sintéticas | a transcrição real (grande e com direitos) |

---

## 4. Anatomia da pasta de uma transcrição

```
transcricoes/2026-09-14-revelacoes-cosmicas-urgente/
│
├── 00-fonte/                       ENTRADA — imutável
│   ├── transcricao-bruta.txt           o STT como saiu, sem nenhum retoque
│   ├── metadados.yaml                  URL, canal, data, duração, falantes, licença, hash
│   └── midia/README.md                 link externo do áudio/vídeo + por que não está aqui
│
├── 10-diagnostico/                 SAÍDA DO MOTOR — regenerável
│   ├── diagnostico.md                  radiografia legível
│   ├── variantes-propostas.csv         FILA DE DECISÃO + livro-razão (coluna adjudicacao)
│   ├── ausentes-da-base.csv            candidatos a novo termo
│   └── dossie-bloco.txt                léxico de trabalho do revisor
│
├── 20-blocos/                      TRABALHO HUMANO — o coração da revisão
│   ├── bloco-01.md … bloco-NN.md       zero-padded: ordena certo com qualquer quantidade
│   └── notas-de-revisao.md             desvios de forma do Guia, decisões editoriais
│
├── 30-produto/                     RESULTADO — o que se lê
│   ├── transcricao-revisada.docx
│   └── transcricao-revisada.pdf        opcional
│
├── 40-devolucao/                   O QUE VOLTA PARA A KB
│   ├── devolucao-a-kb.md / .docx       4 seções obrigatórias do Guia §15
│   ├── adjudicacao.md / .docx          livro-razão das decisões
│   └── externos-novos.csv              linhas a acrescentar em ferramentas/dados/externos.csv
│
└── 90-registro/                    MEMÓRIA DO PROCESSO
    ├── diario-de-bordo.md              o que foi feito, em que ordem, o que falhou
    └── despachos/                      decisões do Comandante, uma por arquivo, datadas
        └── 2026-09-16-apresentadores-e-sidarta.md
```

| Estágio | Quem escreve | Editável depois? | Regenerável? | Versionado? |
|---|---|---|---|---|
| `00-fonte/` | quem captura o vídeo | **nunca** (hash travado no CI) | não | sim |
| `10-diagnostico/` | `rc_diagnostico.py` | só pelo motor | **sim** | CSV sim; `.json` não |
| `20-blocos/` | revisor (Agente 86) | sim, até fechar | não | sim — **é o ativo** |
| `30-produto/` | `rc_docx.py` | só pelo montador | **sim** | sim (o CI confere se bate com os `.md`) |
| `40-devolucao/` | revisor | sim, até o curador aplicar | não | sim |
| `90-registro/` | revisor + Comandante | append-only | não | sim |

**Por que `bloco-01.md` e não `bloco-1.md`:** com 10 blocos ou mais, o glob `bloco-*.md` ordena `1, 10, 11, 2, 3…` e o DOCX sai com a palestra embaralhada. Zero à esquerda resolve para sempre. Isso é um defeito latente hoje, não uma preferência estética.

---

## 5. Convenções de nomenclatura

### 5.1 Slug da transcrição

```
AAAA-MM-DD-titulo-curto-em-kebab-case
└── data da gravação   └── até 5 palavras, sem acento, sem pontuação, minúsculas
```

| ✅ Certo | ❌ Errado | Por quê |
|---|---|---|
| `2026-09-14-revelacoes-cosmicas-urgente` | `Revelações Cósmicas Urgente – Jan Val Ellam` | acento, espaço e travessão quebram shell, URL e CI |
| `2026-10-02-lemuria-terry-fabris` | `transcricao-nova-2` | sem data, sem assunto: nada diz |
| `2026-11-20-jan-val-ellam-entrevista-x` | `2026-11-20-entrevista-com-jan-val-ellam-sobre-o-futuro-da-humanidade-e-as-ias` | longo demais para caminho e terminal |

Data **da gravação**, não da revisão: é ela que ordena o acervo cronologicamente. Se a gravação não tem data conhecida, usa-se a de publicação e registra-se o fato em `metadados.yaml`.

### 5.2 Arquivos dentro da pasta

Nomes **fixos e minúsculos**, sem o slug (P4). O slug já está no caminho; repeti-lo só alonga.

| Arquivo | Nome canônico |
|---|---|
| bruto | `00-fonte/transcricao-bruta.txt` |
| metadados | `00-fonte/metadados.yaml` |
| blocos | `20-blocos/bloco-NN.md` |
| produto | `30-produto/transcricao-revisada.docx` |
| devolução | `40-devolucao/devolucao-a-kb.md` |
| adjudicação | `40-devolucao/adjudicacao.md` |

Exceção: documentos **institucionais** em `docs/` mantêm nomes legíveis (`guia-revisao-v2.md`), porque são lidos por gente fora do pipeline. Ainda assim, sem espaço e sem acento.

### 5.3 Versões e sufixos

- Nunca `arquivo-final.docx`, `arquivo-final-2.docx`, `arquivo-final-AGORA.docx`. **Versão é o Git.**
- Rascunho em andamento: sufixo `-rascunho` **só** dentro de `20-blocos/`, removido ao fechar.
- Documento substituído: vai para `docs/legado/AAAA-MM-nome/`, nunca fica ao lado do vigente.

---

## 6. Catálogo e ciclo de vida

### 6.1 `transcricoes/_indice.csv`

Uma linha por transcrição. Gerado e conferido por `rc_indice.py`; nenhum campo é preenchido à mão onde der para derivar.

```csv
slug,data,titulo,canal,url,duracao_min,falantes,estatus,palavras_brutas,palavras_revisadas,blocos,notas,a_confirmar,inaudivel,devolucao,curadoria_aplicada,revisor,responsavel
2026-09-14-revelacoes-cosmicas-urgente,2026-09-14,Revelações Cósmicas Urgente,Paranormal Experience,https://youtu.be/…,125,"Guru de Malá; Alexandre Sherminator; Jan Val Ellam",40-devolvida,18806,18966,8,32,24,14,2026-09-16,pendente,Agente 86,Comandante
```

### 6.2 Status — vocabulário fechado

| Status | Critério de entrada | Artefato obrigatório |
|---|---|---|
| `00-nova` | pasta criada, bruto capturado | `00-fonte/` completo + hash |
| `10-em-diagnostico` | motor rodou | `10-diagnostico/variantes-propostas.csv` |
| `20-em-revisao` | revisão começou | ≥1 bloco em `20-blocos/` |
| `30-revisada` | todos os blocos prontos + QA verde | `30-produto/transcricao-revisada.docx` |
| `40-devolvida` | extrato final escrito | `40-devolucao/devolucao-a-kb.md` |
| `50-publicada` | curador aplicou na KB e o produto foi distribuído | `KB-RC/CHANGELOG.md` atualizado |
| `90-suspensa` | parada por decisão ou falta de insumo | registro do motivo em `90-registro/` |

Regra: **status só avança com o artefato correspondente presente.** O `rc_indice.py` verifica isso e reclama — status aspiracional é a forma mais comum de autoengano em acervo.

### 6.3 `_fila-de-curadoria.csv` na KB-RC

Com várias transcrições, propostas de novo termo se perdem. Um único arquivo consolida todas:

```csv
id,origem_slug,tipo,termo,categoria,codigo_afetado,evidencia,status,data_proposta,data_aplicada,curador
0001,2026-09-14-revelacoes-cosmicas-urgente,novo-termo,Eu Parasitário,2.x Conceitos,—,"bloco 4: 'o eu de Javé sempre foi parasitário'",pendente,2026-09-16,,
```

`tipo` ∈ {novo-termo, nova-variante, correcao-ficha, novo-registro-biblio, divergencia-factual}. Assim o curador trabalha por fila, não por pasta de vídeo.

---

## 7. Arquivos pesados e mídia

| Tipo | Destino | Justificativa |
|---|---|---|
| `.txt` `.md` `.csv` `.json` `.yaml` | Git normal | texto pequeno, diffável, é o ativo do projeto |
| `.docx` `.pdf` | Git normal | produto de leitura; 40–90 KB cada; diff binário não importa |
| `.xlsx` legado | Git normal, em `docs/legado/` | 311 KB, congelado, não cresce |
| `KB-RC/` (7,8 MB, 822 arquivos) | Git normal | fonte de verdade; texto puro; cabe com folga |
| áudio `.mp3`/`.m4a` | **link externo** em `00-fonte/midia/README.md`; LFS só se indispensável | 125 min ≈ 60 MB; o plano gratuito do LFS é 1 GB — caberiam ~16 vídeos e acabou |
| vídeo `.mp4` | **nunca** no repositório | 300 MB a 2 GB; inutiliza o clone; o YouTube já é o arquivo |
| `diagnostico.json` | `.gitignore` | regenerável pelo motor em segundos |

`.gitattributes` proposto:

```
* text=auto eol=lf
*.docx binary
*.xlsx binary
*.pdf  binary
*.png  binary
# LFS — só se a decisão for manter áudio no repositório
transcricoes/**/00-fonte/midia/*.mp3 filter=lfs diff=lfs merge=lfs -text
transcricoes/**/00-fonte/midia/*.m4a filter=lfs diff=lfs merge=lfs -text
```

**Trava de segurança no CI:** qualquer arquivo acima de 5 MB fora do LFS reprova o PR. Isso impede o acidente clássico de arrastar um vídeo para dentro do repositório.

---

## 8. Automação

### 8.1 Três scripts novos

| Script | O que faz | Por que existe |
|---|---|---|
| `rc_novo.py` | cria `transcricoes/<slug>/` a partir de `_modelo/`, grava `metadados.yaml` com o hash do bruto e acrescenta a linha no `_indice.csv` | Sem ele, cada transcrição nova nasce com estrutura ligeiramente diferente — e a diferença vira exceção permanente |
| `rc_indice.py` | regenera `_indice.csv`/`_indice.md` varrendo as pastas e confere: status × artefatos, hash do bruto, slug bem formado, blocos ordenáveis | Catálogo desatualizado é pior que catálogo nenhum |
| `rc_qa.py` | roda os 8 portões abaixo sobre uma pasta de transcrição (ou todas) e devolve *exit code* | Hoje o QA só roda se alguém lembrar de chamar o `rc_docx.py --validar` |

Esqueleto do `rc_novo.py` (Apêndice D) e dos portões (§8.2).

### 8.2 Os oito portões de qualidade

| Portão | Verifica | Falha quando |
|---|---|---|
| **G1 — bruto intacto** | SHA-256 de `00-fonte/transcricao-bruta.txt` × `metadados.yaml` | alguém editou o bruto (P2) |
| **G2 — blocos íntegros** | todo `bloco-NN.md` tem `## Bloco N`, ≥1 rótulo de fala, zero comentário HTML, zero marcador de rascunho | bloco incompleto ou com andaimes esquecidos |
| **G3 — formas proibidas** | varredura **com fronteira de palavra**, ignorando o conteúdo de `[NOTA]`/`[A CONFIRMAR]`/`[INAUDÍVEL]` | canônico violado no texto corrido |
| **G4 — ledger fechado** | nenhuma linha de `variantes-propostas.csv` com `adjudicacao` vazia ou `REVISAR` | decisão pendente — o revisor não terminou |
| **G5 — validador** | `rc_docx.py --validar` devolve 0 | variante adjudicada como *aceita* sobreviveu |
| **G6 — produto reproduzível** | regenera o `.docx` a partir dos `.md` e compara com o que está versionado | o `.docx` publicado não corresponde aos blocos |
| **G7 — índice consistente** | slug existe no `_indice.csv`, status bate com os artefatos presentes, contagens conferem | catálogo mente |
| **G8 — higiene de repositório** | nenhum arquivo >5 MB fora do LFS; nenhum `~$*`; nenhum espaço ou acento em `transcricoes/**` e `ferramentas/**` | convenção violada |

G3 e G6 são os que valem ouro: **G3** pega a regressão terminológica que o olho não vê em 19 mil palavras; **G6** garante que o contrato de dupla saída (`.md` + `.docx`) não se degrade em "o `.docx` é de terça, os `.md` são de hoje".

### 8.3 CI

`ferramentas/ci/qa.yml` (a instalar em `.github/workflows/`): em todo PR que toque `transcricoes/**`, `KB-RC/**`, `ferramentas/**` ou `docs/**`, roda `rc_qa.py --tudo` + `rc_indice.py --checar`. Falhou, não mergeia. Tempo estimado: < 2 min (o corpus inteiro são 100 mil caracteres).

---

## 9. Migração

Cinco fases, **um commit por fase**, tag antes de começar. `git mv` preserva o histórico (`git log --follow` continua funcionando). Nada é apagado (P10).

```bash
git tag v1-antes-reorganizacao && git push origin v1-antes-reorganizacao
```

| Fase | Ação | Risco | Verificação |
|---|---|---|---|
| **1** | criar `docs/{normas,pareceres,planos,legado}` e mover Guia v2, Anexo I, parecer, Guia v1, planilha | baixo | `grep -rn "docs/normas" README.md` |
| **2** | criar `transcricoes/2026-09-14-revelacoes-cosmicas-urgente/{00-fonte,…}` e mover bruto (da raiz), blocos, diagnóstico, devolução e produto (da `analise/…-kb/`); renomear `bloco-N.md` → `bloco-0N.md` | médio | regenerar o `.docx` e comparar palavra a palavra com o anterior |
| **3** | criar `ferramentas/dados/` e mover os 4 arquivos de dados; atualizar os *defaults* de `argparse` em 5 scripts | médio | rodar o pipeline inteiro de ponta a ponta |
| **4** | arquivar o protótipo `analise/revelacoes-cosmicas-urgente-jan-val-ellam/` em `docs/legado/2026-09-prototipo-analise/`; remover `analise/`; criar `_modelo/`, `_indice.csv`, `.gitattributes`, `rc_novo.py`, `rc_indice.py`, `rc_qa.py`, `.github/` | baixo | `rc_qa.py --tudo` verde |
| **5** | reescrever README, atualizar os caminhos no Guia v2 (§1 a §18) e nos documentos que citam paths; criar `KB-RC/CHANGELOG.md` e `_fila-de-curadoria.csv` a partir da devolução já escrita | baixo | leitura humana + CI verde |

### 9.1 Mapeamento antigo → novo

| Hoje | Passa a ser |
|---|---|
| `Revelações Cósmicas Urgente – Jan Val Ellam.txt` | `transcricoes/2026-09-14-revelacoes-cosmicas-urgente/00-fonte/transcricao-bruta.txt` |
| `Revelações Cósmicas Urgente – Jan Val Ellam (revisado).docx` | `…/30-produto/transcricao-revisada.docx` |
| `analise/revelacoes-cosmicas-urgente-jan-val-ellam-kb/blocos/bloco-N.md` | `…/20-blocos/bloco-0N.md` |
| `analise/…-kb/{diagnostico.md,variantes-propostas.csv,ausentes-da-base.csv,dossie-bloco.txt}` | `…/10-diagnostico/` |
| `analise/…-kb/{DEVOLUCAO-A-KB,ADJUDICACAO}.md/.docx` | `…/40-devolucao/{devolucao-a-kb,adjudicacao}.md/.docx` |
| `analise/revelacoes-cosmicas-urgente-jan-val-ellam/` (protótipo) | `docs/legado/2026-09-prototipo-analise/` |
| `analise/{PARECER-DE-VIABILIDADE,RESOLUCAO-DE-CONFLITOS}.md/.docx` | `docs/pareceres/` e `docs/normas/` |
| `Guia de Revisão e Governança Terminológica v2.md/.docx` | `docs/normas/guia-revisao-v2.md/.docx` |
| `Guia - SISTEMA DE REVISÃO E GOVERNANÇA TERMINOLÓGICA.docx` | `docs/legado/2026-09-guia-v1/` |
| `base-terminologica.xlsx` | `docs/legado/2026-09-base-terminologica.xlsx` |
| `ferramentas/{sementes-variantes-stt.csv,externos.csv,variantes-kb-extraidas.csv,vocabular-guarda-pt.txt}` | `ferramentas/dados/` |
| `KB-RC/` | **não muda** (P7) |

### 9.2 O que muda no código

| Arquivo | Mudança |
|---|---|
| `rc_kb.py` | nenhuma (`KB-RC` continua na raiz) |
| `rc_lexicon.py` | default de `carregar_sementes()` → `ferramentas/dados/sementes-variantes-stt.csv` |
| `rc_variantes.py` | `--saida` default → `ferramentas/dados/variantes-kb-extraidas.csv` |
| `rc_diagnostico.py` | `--base` → `docs/legado/…xlsx`; `--saida` → `transcricoes/<slug>/10-diagnostico`; defaults de `--sementes/--externos/--guarda/--variantes-kb` → `ferramentas/dados/` |
| `rc_docx.py` | só docstring/exemplos (caminhos já vêm por argumento) |
| `md_para_docx.py` | só docstring/exemplos |
| `.gitignore` | `analise/**/diagnostico.json` → `transcricoes/**/10-diagnostico/diagnostico.json`; acrescentar travas de mídia |

### 9.3 Varredura de referências

82 menções a caminhos em 6 documentos precisam ser atualizadas: Guia v2 (32), PARECER (21), RESOLUCAO-DE-CONFLITOS (15), README (10), DEVOLUCAO-A-KB (2), `diagnostico.md` (2). As 68 fichas da KB-RC que mencionam `termos/` **não** são afetadas — referem-se a caminhos internos da própria KB.

---

## 10. Fluxo de trabalho e governança

### 10.1 Papéis

| Papel | Escreve em | Não escreve em |
|---|---|---|
| **Capturador** | `00-fonte/` | qualquer outra |
| **Revisor (Agente 86)** | `20-blocos/`, `40-devolucao/`, `90-registro/` | `KB-RC/`, `00-fonte/` |
| **Curador** | `KB-RC/`, `ferramentas/dados/` | blocos revisados |
| **Comandante** | `90-registro/despachos/`, aprovação de PR | — |

Regra de ouro que a primeira transcrição ensinou: **o revisor propõe, o curador aplica.** O revisor não toca na KB-RC nem para "corrigir um errinho óbvio" — tudo passa pela fila (§6.3).

### 10.2 Branches e PRs

- `main` — só o que está fechado. Nunca trabalho em andamento.
- `arena/<sessao>` ou `rev/<slug>` — uma branch por transcrição.
- `kb/<lote>` — uma branch por lote de curadoria (agrega as devoluções de várias transcrições).
- **Um PR por transcrição revisada**, contendo obrigatoriamente: blocos, produto, devolução, linha do índice atualizada.
- Template de PR pergunta: quantos blocos? QA verde? quantas propostas de novo termo? quantas divergências factuais reportadas ao produtor? algum despacho do Comandante embutido?

### 10.3 Commits

Verbo no imperativo + o quê + por quê quando não for óbvio. Exemplos do que já funciona neste repositório: `Revisão completa dos 8 blocos + devolução à KB-RC`, `Guia v2 + resolução dos 8 conflitos`. Manter o padrão; acrescentar o slug quando o commit tocar uma transcrição específica: `[revelacoes-cosmicas-urgente] bloco 4: Lei de Moore na voz do narrador`.

---

## 11. Alternativas consideradas e recusadas

| Alternativa | Por que foi recusada |
|---|---|
| **A. Organização por tipo no topo** — `brutos/`, `blocos/`, `produtos/`, `devolucoes/`, cada uma com um arquivo por vídeo | É a intuição mais comum e a mais frágil aqui: para auditar, reabrir ou arquivar **um** vídeo é preciso operar em 5 árvores e casar nomes de arquivo em todas. Viola P1. O tipo já está expresso pelo estágio dentro da pasta do vídeo (`00-fonte` = brutos, `30-produto` = resultados), então o benefício existe sem o custo |
| **B. Agrupar por ano** — `transcricoes/2026/2026-09-14-…` | Profundidade extra sem ganho: o prefixo `AAAA-MM-DD` já ordena cronologicamente em uma listagem plana. Vale reconsiderar acima de ~60 transcrições |
| **C. Renomear `KB-RC/` para `kb/`** | Estética. Custa a atualização de 6 scripts e dezenas de referências, e a KB-RC é citada pelo nome em despachos e fichas. P7 |
| **D. Manter tudo em `analise/<slug>`** | Status quo. Mistura norma permanente com trabalho descartável e não separa estágio nenhum (problemas 3, 4 e 5 do diagnóstico) |
| **E. Um repositório por transcrição** | Destroi a base compartilhada: sementes, externos, vocabulário-guarda e KB crescem justamente **entre** transcrições |
| **F. Submódulos para a KB-RC** | Complexidade de submódulo para 7,8 MB de texto. Só se a KB passar a ter vida e permissões independentes |

---

## 12. Decisões que preciso do Comandante

Quatro escolhas mudam a implementação. Minha recomendação está marcada.

1. **Organização primária.** *(recomendado: por transcrição, com estágios numerados dentro — §3/§4)* ou por tipo de arquivo no topo (alternativa A)?
2. **Nomenclatura.** *(recomendado: ASCII sem acento nem espaço em tudo que é caminho operacional — §5)* ou preservar os nomes atuais, com acento e travessão?
3. **Mídia.** *(recomendado: só link externo em `00-fonte/midia/README.md`)*, Git LFS para áudio, ou pasta local ignorada pelo Git?
4. **Quando migrar.** *(recomendado: agora, antes da segunda transcrição — migrar 1 vídeo custa 5 commits; migrar 10 custa uma tarde de arqueologia)* ou depois de acumular algumas?

Decisões menores que assumi por padrão e podem ser revertidas: pasta `publicacoes/` criada só na fase 2; `testes/` criado com fixture mínima; `_fila-de-curadoria.csv` alimentado a partir da devolução já escrita; nomes de arquivo em minúsculas dentro de `transcricoes/`.

---

## 13. Checklist de implantação (executado)

- [x] Comandante respondeu as 4 decisões do §12 — todas pela recomendação
- [ ] `git tag v1-antes-reorganizacao` e push da tag
- [x] Branch `arena/01a0a743-transcri-youtube` (ou dedicada) para a migração
- [x] Fase 1 — `docs/` · commit · README aponta para as normas
- [x] Fase 2 — `transcricoes/<slug>/` · commit · **DOCX regenerado confere com o anterior**
- [x] Fase 3 — `ferramentas/dados/` + defaults · commit · pipeline roda de ponta a ponta
- [x] Fase 4 — `_modelo/`, `_indice.csv`, `.gitattributes`, `rc_novo.py`, `rc_indice.py`, `rc_qa.py`, CI · commit
- [x] Fase 5 — README, Guia v2, CHANGELOG da KB, fila de curadoria · commit
- [x] Um commit por fase, todos na branch `arena/01a0a743-transcri-youtube`
- [x] Teste de fogo em cópia no `/tmp`: G1 pegou bruto adulterado, G6 pegou `.docx` com parágrafo intruso, G4 pegou linha sem decisão

---

## Apêndice A — `metadados.yaml`

```yaml
slug: 2026-09-14-revelacoes-cosmicas-urgente
titulo: "Revelações Cósmicas Urgente"
titulo_completo: "ASSISTA ANTES QUE SAIA DO AR — Revelações Cósmicas Urgente"
canal: Paranormal Experience
url: https://www.youtube.com/watch?v=XXXXXXXXXXX
data_gravacao: 2026-09-14
data_publicacao: 2026-09-14
data_captura: 2026-09-15
duracao_min: 125
idioma: pt-BR
ferramenta_stt: youtube-autosub          # qual STT gerou o bruto
falantes:
  - rotulo: "[GURU DE MALÁ]"
    papel: apresentador
    turnos: 42
  - rotulo: "[ALEXANDRE SHERMINATOR]"
    papel: coapresentador
    turnos: 36
  - rotulo: "[JAN VAL ELLAM]"
    papel: entrevistado
    turnos: 64
licenca: uso interno do Projeto
bruto:
  arquivo: transcricao-bruta.txt
  caracteres: 101468
  palavras: 18806
  linhas_cabecalho: 12                   # corpo começa na linha 12 (0-indexed)
  sha256: <hash>
midia:
  audio: nao-arquivado                   # ou: lfs | externo
  link: https://www.youtube.com/watch?v=XXXXXXXXXXX
revisao:
  guia: docs/normas/guia-revisao-v2.md
  disfluencia: leve
  diarizacao: opcao-b-rotulos-inferidos
  despachos:
    - 90-registro/despachos/2026-09-16-apresentadores-e-sidarta.md
```

## Apêndice B — `.gitignore` consolidado

```
# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Editores / SO
.DS_Store
Thumbs.db
~$*.docx
~$*.xlsx

# Regeneráveis
*.log
transcricoes/**/10-diagnostico/diagnostico.json

# Mídia pesada: nunca no repositório comum
*.mp4
*.mkv
*.wav
*.avi
# Áudio só via LFS (ver .gitattributes); se a decisão for "link externo", descomente:
# transcricoes/**/00-fonte/midia/*.mp3
# transcricoes/**/00-fonte/midia/*.m4a
```

## Apêndice C — `rc_qa.py`, contrato de saída

```
$ python ferramentas/rc_qa.py transcricoes/2026-09-14-revelacoes-cosmicas-urgente
[G1] bruto intacto                    OK   sha256 confere com metadados.yaml
[G2] blocos íntegros                  OK   8 blocos, 143 parágrafos, 147 rótulos
[G3] formas proibidas                 OK   0 ocorrências (fronteira de palavra, marcadores ignorados)
[G4] ledger fechado                   OK   98 linhas, 0 sem decisão
[G5] validador rc_docx                OK   24 aceitas, nenhuma sobrevive
[G6] produto reproduzível             OK   transcricao-revisada.docx == regenerado
[G7] índice consistente               OK   status 40-devolvida, artefatos presentes
[G8] higiene                          OK   maior arquivo 636 KB, 0 com espaço/acento
exit 0
```

`--tudo` varre `transcricoes/*/`; `--portao G3` roda um só; `--json` emite máquina-legível para o CI.

## Apêndice D — `rc_novo.py`, esqueleto

```python
"""rc_novo — cria o diretório de uma transcrição a partir de _modelo/.

    python ferramentas/rc_novo.py \
        --slug 2026-10-02-lemuria-terry-fabris \
        --titulo "LEMÚRIA ESTÁ em busca URGENTE DE CONTATO" \
        --canal "Paranormal Experience" \
        --url https://youtu.be/9DvQf6DikA8 \
        --data 2026-10-02 \
        --bruto ~/Downloads/legenda.txt

Passos: valida o slug (§5.1), copia _modelo/, grava metadados.yaml com o
SHA-256 do bruto, cria a linha no _indice.csv com status 00-nova e devolve
o caminho criado. Recusa slug malformado, bruto ausente e slug duplicado.
"""
```

## Apêndice E — template de PR

```markdown
## Transcrição
slug: `2026-09-14-revelacoes-cosmicas-urgente` · status: 30-revisada → 40-devolvida

## Números
blocos: 8 · palavras brutas: 18.806 · revisadas: 18.966 · [NOTA]: 32 · [A CONFIRMAR]: 24 · [INAUDÍVEL]: 14

## QA
- [ ] G1–G8 verdes (`python ferramentas/rc_qa.py <pasta>`)
- [ ] `.docx` regenerado a partir dos `.md` (G6)
- [ ] nenhuma linha do ledger sem decisão (G4)

## Devolução à KB
novos termos: N · novas variantes STT: N · correções de ficha: N · divergências factuais: N

## Despachos embutidos
- [ ] `90-registro/despachos/AAAA-MM-DD-*.md` citado e aplicado

## Para o curador
itens acrescentados a `KB-RC/_fila-de-curadoria.csv`: IDs …
```


---

## 14. Execução — o que foi feito e o que mudou em relação à proposta

Cinco fases, um commit por fase, tag `v1-antes-reorganizacao` antes de começar, tudo com `git mv`
(histórico preservado — `git log --follow` continua funcionando).

| Fase | Commit | Verificação |
|---|---|---|
| 1 · `docs/` | `3e120c4` | 10 arquivos movidos, todos detectados como renomeação |
| 2 · `transcricoes/<slug>/` | `40cb9e6` | `.docx` regenerado no novo caminho e comparado parágrafo a parágrafo com o anterior: **154 = 154, 0 diferenças** |
| 3 · `ferramentas/dados/` | `5896ecc` | pipeline de ponta a ponta reproduz **exatamente** as métricas do diagnóstico versionado |
| 4 · automação, catálogo, CI | `36309c9` | G1–G8 verdes na transcrição de referência; 63 verificações de fumaça |
| 5 · README e varredura de caminhos | este commit | 50 referências atualizadas em 3 documentos; `rc_indice.py --checar` em dia |

### 14.1 O que a execução acrescentou à proposta

- **`transcricoes/_indice.md`**, além do `.csv`: o catálogo precisa ser legível no GitHub sem
  baixar nada.
- **`10-diagnostico/README.md`** na transcrição de referência, avisando que
  `variantes-propostas.csv` **não pode ser regenerado por cima**: o motor escreve 12 colunas, o
  revisor acrescentou `adjudicacao`, `motivo_adjudicacao` e `ocorrencias_no_revisado`. Sem esse
  aviso, rodar o motor de novo destruiria o livro-razão.
- **`docs/legado/README.md`** e README próprio do protótipo arquivado, dizendo o que cada um foi e
  quem o substituiu — arquivo congelado sem explicação vira mistério.
- **`rc_indice.py --checar`** como passo próprio no CI, separado dos portões.
- **Portão G3 derivado da base**, não de lista escrita à mão: as formas proibidas vêm da
  Quarentena das fichas (`NUNCA "Sofia"`) somada às variantes que o livro-razão marcou como
  *aceitas*. Lista manual apodrece; a KB não.
- **Terceiro estado nos portões (`N/A`)**: sem ele, o QA reprovaria uma transcrição recém-criada
  por não ter `.docx` — e o revisor aprenderia a ignorar o QA.

### 14.2 Incidente real durante a execução — e a regra que ele produziu

O commit de normalização de fins de linha (`git add --renormalize .`, para aplicar o
`* text=auto eol=lf` do novo `.gitattributes`) **reescreveu o blob do bruto capturado**, que tem
CRLF: `34f9bcf4…` virou `db3fa8ae…`. O arquivo de trabalho não mudou — o repositório mudou. Um
clone fresco receberia bytes diferentes dos capturados e o portão G1 reprovaria.

Correção no commit seguinte: `.gitattributes` marca
`transcricoes/**/00-fonte/*.txt|.vtt|.srt` como `-text` (nunca normalizar), o blob foi restaurado
e a restauração foi verificada por **clone fresco + G1 verde**.

**Regra que fica (acrescentada ao Princípio P2):** convenção de estilo não se aplica a evidência.
Normalização global de fim de linha, formatador automático e "limpeza" de whitespace precisam ter
exceção explícita para `00-fonte/`. O bruto é a única coisa neste repositório que não pode ser
melhorada.

### 14.3 O que ficou para depois

| Item | Por que não agora |
|---|---|
| `publicacoes/` | só faz sentido quando houver produto distribuído; a pasta nasce vazia e o CI passaria a cobrar coerência de um lugar sem conteúdo |
| LFS para áudio | a decisão foi link externo; as regras ficaram prontas no `.gitattributes` |
| ~~`url` do vídeo de referência~~ | **RESOLVIDO em 16/09/2026**: URL fornecida pelo Comandante, conferida na plataforma (2:25:50, canal PARANORMAL EXPERIENCE) e gravada nos três lugares; a duração estimada de 125 min foi corrigida para 146 |
| Reescrever o Guia v2 inteiro para a nova estrutura | os caminhos foram atualizados (26 referências); uma revisão de texto do Guia é trabalho de curadoria, não de migração |

### 14.4 O CI ficou pronto, mas não pôde ser ativado

O workflow `qa.yml` foi escrito e testado quanto à lógica (os três comandos que ele roda passam
localmente), mas o push que o criaria em `.github/workflows/` foi **recusado pelo GitHub**:

```
! [remote rejected] (refusing to allow a GitHub App to create or update workflow
  `.github/workflows/qa.yml` without `workflows` permission)
```

O Agente 86 empurra este repositório por um GitHub App sem a permissão `workflows`. Duas saídas,
ambas do lado do Comandante: **(a)** quem tem acesso direto ao repositório copia
`ferramentas/ci/qa.yml` para `.github/workflows/qa.yml` e faz o commit — instruções em
`ferramentas/ci/README.md`; **(b)** concede-se *Read and write* em *Workflows* ao app, e o Agente
mesmo instala e mantém o workflow daí em diante.

Enquanto nenhuma das duas acontecer, os portões rodam **localmente e em clone fresco** —
`rc_qa.py --tudo`, `rc_indice.py --checar`, `testes/test_pipeline.py`. A diferença não é o que se
verifica, é quem verifica e quando: sem CI, a verificação depende de disciplina humana, e o
incidente do §14.2 mostrou exatamente o que a disciplina sozinha não pega.

Nota de transparência: para publicar as demais fases sem o arquivo bloqueante, o histórico local
(nunca publicado) foi reescrito retirando `.github/workflows/` dos commits; o conteúdo do workflow
está intacto em `ferramentas/ci/qa.yml`. Nenhum commit já publicado foi alterado.

**RESOLVIDO em 16/09/2026 (opção a):** o Comandante instalou o workflow por conta própria — commit
`5744f1f`, *Ativando CI: workflow de QA do Agente 86*, byte-idêntico a `ferramentas/ci/qa.yml`. Os
quatro passos foram simulados localmente antes do primeiro PR: 105 verificações de fumaça, G1–G8
verdes, catálogo em dia, `qa.json` válido. Fica um encargo permanente: o Agente não pode editar o
arquivo instalado (a permissão `workflows` continua ausente), então as duas cópias têm de ser
mantidas iguais à mão — divergência entre elas é o único modo de o CI passar a verificar outra coisa
do que o repositório documenta.
