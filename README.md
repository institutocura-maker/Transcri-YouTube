# Transcri-YouTube

Transcrições automáticas de vídeos do YouTube **revisadas** — ortografia e terminologia —
contra uma base de conhecimento: o acervo das **Revelações Cósmicas de Jan Val Ellam**.

O problema é concreto: a legenda automática entrega 18 mil palavras sem nenhuma pontuação,
com `Raymond Kzwell` no lugar de Ray Kurzweil, `Brama` no lugar de Brahma e `Xavé` no lugar
de Javé. Corrigir na intuição produz inconsistência; corrigir com motor produz falso positivo.
Este repositório faz as duas coisas na ordem certa — **o script levanta evidência, o revisor
decide, e a decisão fica registrada**.

## Estrutura

```
docs/            documentos DO PROJETO — valem para todas as transcrições
  normas/        guia-revisao-v2.md/.docx · resolucao-de-conflitos.md/.docx (Anexo I)
  pareceres/     parecer-de-viabilidade.md/.docx
  planos/        plano-de-organizacao.md/.docx — a estrutura deste repositório e o porquê dela
  legado/        Guia v1, planilha e protótipo: congelados, datados, somente leitura

KB-RC/           FONTE DE VERDADE
  canonico.json  946 termos + 1.887 relações · biblio.json 104 obras · termos/ 820 fichas
  CHANGELOG.md   histórico de curadoria: o que mudou, quando, a pedido de quem
  _fila-de-curadoria.csv   propostas pendentes, consolidadas de todas as transcrições

ferramentas/     somente código
  rc_kb.py rc_lexicon.py rc_variantes.py rc_diagnostico.py rc_docx.py md_para_docx.py
  rc_novo.py     cria a pasta de uma transcrição a partir do modelo
  rc_ledger.py   mantém o livro-razão da adjudicação (decisões + contagem de sobrevivências)
  rc_indice.py   gera e confere o catálogo
  rc_qa.py       os oito portões de qualidade
  dados/         sementes de variantes, externos.csv, vocabulário-guarda

transcricoes/    UM DIRETÓRIO POR VÍDEO, autossuficiente
  _indice.csv    catálogo derivado do disco (não editar à mão)
  _modelo/       esqueleto que o rc_novo.py copia
  <AAAA-MM-DD-slug>/
    00-fonte/       bruto imutável + metadados.yaml (com sha256) + política de mídia
    10-diagnostico/ saída do motor + livro-razão da adjudicação
    20-blocos/      bloco-01.md … bloco-NN.md + notas-de-revisao.md
    30-produto/     transcricao-revisada.docx
    40-devolucao/   devolucao-a-kb.md · adjudicacao.md · externos-novos.csv
    90-registro/    diario-de-bordo.md + despachos/ do Comandante

testes/          fixture + teste de fumaça (63 verificações, sem pytest)
.github/         template de PR e papéis (CONTRIBUTING)
ferramentas/ci/  configuração pronta do GitHub Actions — veja o README de lá para ativar
```

## Início rápido

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ferramentas/requirements.txt
python testes/test_pipeline.py            # 63 verificações de fumaça

# 1. abrir uma transcrição nova (valida o slug, grava o hash do bruto, atualiza o catálogo)
python ferramentas/rc_novo.py --slug 2026-10-02-lemuria-terry-fabris \
    --titulo "LEMÚRIA ESTÁ em busca URGENTE DE CONTATO" --canal "Paranormal Experience" \
    --url https://youtu.be/9DvQf6DikA8 --data 2026-10-02 --bruto ~/Downloads/legenda.txt

# 2. diagnóstico contra a fonte de verdade (a saída é descoberta sozinha)
python ferramentas/rc_diagnostico.py \
    transcricoes/2026-10-02-lemuria-terry-fabris/00-fonte/transcricao-bruta.txt --kb KB-RC

# 3. revisar em 20-blocos/bloco-01.md … (zero à esquerda: com 10 blocos o glob
#    ordenaria 1, 10, 11, 2 e embaralharia o produto)

# 4. montar o produto + escrever a devolução à KB

# 5. portões e catálogo
python ferramentas/rc_qa.py transcricoes/2026-10-02-lemuria-terry-fabris
python ferramentas/rc_indice.py
```

Fluxo completo, papéis e convenções: **`.github/CONTRIBUTING.md`**.

## Os oito portões

O CI roda tudo isto em cada PR que toque `transcricoes/`, `KB-RC/`, `ferramentas/` ou `docs/`.
O workflow está versionado em **`ferramentas/ci/qa.yml`**, ainda não instalado em
`.github/workflows/`: o GitHub App por onde o Agente empurra este repositório não tem a permissão
`workflows`. Enquanto não for ativado, rode os três comandos acima — de preferência num clone
fresco, que é o único teste capaz de pegar divergência entre repositório e cópia de trabalho.

| | Portão | Pega o quê |
|---|---|---|
| G1 | bruto intacto | alguém "só corrigiu um errinho" no arquivo sagrado (sha256 × metadados) |
| G2 | blocos íntegros | bloco sem título, sem falante, com comentário HTML ou nome fora do padrão |
| G3 | formas proibidas | canônico violado — a lista vem da Quarentena da KB e do livro-razão, não de memória |
| G4 | ledger fechado | linha de adjudicação sem decisão: o revisor não terminou |
| G5 | validador | variante adjudicada como *aceita* sobreviveu no texto |
| G6 | produto reproduzível | o `.docx` publicado não corresponde aos `.md` |
| G7 | índice consistente | o catálogo diz uma coisa, a pasta diz outra |
| G8 | higiene | arquivo >5 MB fora do LFS, `~$trava` do Office, espaço ou acento em caminho de máquina |

Três estados por portão: `OK`, `FALHA` e `N/A` — não se cobra `.docx` de quem ainda não revisou nada.

## Princípios

1. **A KB-RC é a única fonte de canônicos.** Nenhuma grafia é padronizada por intuição; a planilha
   `base-terminologica.xlsx` é legado e só serve a conferência.
2. **Variante não é canônico.** O mapeamento vive em CSV versionado (`ferramentas/dados/`) e cresce
   a cada transcrição revisada.
3. **Script levanta evidência, revisor decide.** A varredura reduz 18 mil palavras a algumas dezenas
   de candidatos com contexto; a substituição exige julgamento — e fica registrada com motivo.
4. **O revisor propõe; o curador aplica.** Trabalho de revisão não altera `KB-RC/`: vai para
   `40-devolucao/` e para `_fila-de-curadoria.csv`.
5. **Saída determinística e dupla.** `.md` para versionar (inegociável), `.docx` para ler — sempre
   gerado, nunca editado à mão. Tipografia, negrito de primeira menção e QA são feitos por código.
6. **O bruto é sagrado.** Nunca editado, hash registrado, protegido de normalização de fim de linha.
7. **Nada se apaga:** legado é arquivado com data em `docs/legado/`.
8. **O ciclo devolve à base:** variantes novas, termos ausentes, conflitos e divergências factuais
   voltam como proposta de atualização.

## Estado

| | |
|---|---|
| Transcrições | 1 devolvida — [`transcricoes/_indice.md`](transcricoes/_indice.md) |
| Referência | `2026-09-14-revelacoes-cosmicas-urgente` · 8 blocos · 18.966 palavras revisadas · 98 linhas adjudicadas |
| Propostas na fila de curadoria | 38 (10 novos termos, 14 variantes, 8 correções de ficha, 1 obra, 5 divergências factuais) |
| Base | 946 termos · 820 fichas · 104 obras · 299 regras de substituição · 37 entidades externas |
