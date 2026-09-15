# Transcri-YouTube

Repositório de transcrições de vídeos do YouTube geradas automaticamente e revisadas
(ortografia e terminologia) contra uma base de conhecimento — o acervo das
**Revelações Cósmicas de Jan Val Ellam**.

## Arquivos-fonte

| arquivo | papel |
|---|---|
| `Guia - SISTEMA DE REVISÃO E GOVERNANÇA TERMINOLÓGICA.docx` | norma editorial do processo (skill importada de outra plataforma) |
| `base-terminologica.xlsx` | fonte de verdade terminológica: 946 termos, 104 obras, 1.887 relações, 7 abas |
| `Revelações Cósmicas Urgente – Jan Val Ellam.txt` | primeira transcrição em processamento (live Paranormal Experience, 14/09/2026, ~125 min) |

## Estrutura

```
ferramentas/            código do pipeline
  rc_lexicon.py         acesso à base + normalização pt-BR + chave fonética
  rc_diagnostico.py     varredura transcrição × base (métricas, candidatos, ausentes, dossê)
  rc_docx.py            montagem do DOCX final + QA de variantes sobreviventes
  sementes-variantes-stt.csv   variantes -> canônico curadas a partir do Guia (39 pares)
  vocabular-guarda-pt.txt      vocabulário comum pt-BR que nunca é termo (1.844 formas)
  requirements.txt
analise/                estudos, diagnósticos e pareceres
  PARECER-DE-VIABILIDADE.md/.docx
  <slug-da-transcricao>/       diagnóstico + dossê + amostras
termos/                 (a importar) fichas-fonte em Markdown referidas pela aba "Como usar"
transcricoes/           (a criar) um diretório por vídeo, com bruto, blocos e final
```

## Início rápido

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ferramentas/requirements.txt

# diagnóstico de uma transcrição contra a base
python ferramentas/rc_diagnostico.py "Revelações Cósmicas Urgente – Jan Val Ellam.txt"

# montagem do DOCX revisado a partir dos blocos + QA
python ferramentas/rc_docx.py analise/<slug>/20-blocos/*.md \
    --lexico analise/<slug>/dossie-bloco.txt \
    --saida "analise/<slug>/40-final.docx" \
    --titulo "Título da palestra" \
    --subtitulo "Transcrição revisada — Padronização terminológica conforme a Revelação Cósmica de Jan Val Ellam" \
    --validar analise/<slug>/variantes-propostas.csv
```

## Princípios

1. **A base é a única fonte de canônicos.** Nenhuma grafia é padronizada por intuição.
2. **Variante não é canônico:** o mapeamento variante → canônico vive em CSV versionado
   (`ferramentas/sementes-variantes-stt.csv`) e cresce a cada transcrição revisada.
3. **Script levanta evidência, revisor decide.** A varredura reduz 18 mil palavras a algumas
   dezenas de candidatos com contexto; a substituição exige julgamento contextual.
4. **Saída determinística.** Tipografia, negrito de primeira menção e QA são feitos por código.
5. **O ciclo devolve à base:** variantes novas, termos ausentes e conflitos encontrados
   retornam como proposta de atualização.
