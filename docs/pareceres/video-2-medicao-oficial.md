# Perfil de motores de STT — medição de 2026-09-16

Gerado por `ferramentas/rc_perfil_stt.py` (régua: KB-RC com 956 termos, 1085 superfícies canônicas, 124 corrupções mapeadas).

## video-2-transcri-youtube.txt

```text

==============================================================================
video-2-transcri-youtube.txt  (11.638 bytes · 1 linhas · 1 parágrafos reais · CRLF 11/LF 0)
==============================================================================
    estágio na esteira: solto — arquivo fora de transcricoes/ (ex.: upload/) — leitura de BRUTO, é o caso do experimento de motor

[1] PONTUAÇÃO E SEGMENTAÇÃO — 1.810 palavras
    sinais por 100 palavras: 0.11
    sentenças: 3 · palavras/sentença: 603.3 (mediana 61, maior 1.737)
    parágrafos: 1 · palavras/parágrafo: 1810.0
      ponto                        2  (1.1/1.000 palavras)

[2] DISFLUÊNCIA — 27 marcas (14.92 por 1.000 palavras)
    repetições: palavra 3 · bigrama 0 · trigrama 0 · prolongamentos 3
    marcadores orais: então 8 · sabe 8 · tipo 4 · aí 2 · eh 1 · ó 1

[3] FIDELIDADE TERMINOLÓGICA (contra a KB-RC)
    canônicos presentes: 12 formas distintas, 26 ocorrências
    variantes STT mapeadas presentes: 0 formas, 0 ocorrências (0.0/1.000 palavras)
    formas proibidas (Quarentena + livro-razão): 0 formas, 0 ocorrências
    Externos — forma canônica: 0 formas, 0 ocorrências · forma corrompida: 0 formas, 0 ocorrências
    taxa de confiança (canônico ÷ canônico+variante): 1.0000

[4] INTEGRAÇÃO À ESTEIRA
    maior linha: 10.008 chars = 88.3% do arquivo
    marcador 'Transcrição Automática': não
    rótulos de fala nativos: nenhum → diarização nativa: não
      [compatível        ] rc_novo.py / rc_indice.py medem o corpo pelo critério único de rc_leitura.py (marcador → linha mais longa → arquivo inteiro, com aviso)
                         a maior linha cobre 88.3% do arquivo
      [CUSTA CÓDIGO      ] rc_diagnostico.carregar_transcricao separa cabeçalho pelo marcador 'Transcrição Automática' (pendência: parecer-motor-stt §8 item 2)
                         sem marcador: o arquivo inteiro vira corpo e o cabeçalho sai vazio
      [compatível        ] diarização opção B (rótulos inferidos pelo revisor)
                         sem rótulos nativos: o revisor continua inferindo
      [compatível        ] Guia §8 (pontuação é corretiva, o STT não traz)
                         1.1 sinais por 1.000 palavras — pontuação praticamente ausente
```

## video-2-revisao-corpo.txt

```text

==============================================================================
video-2-revisao-corpo.txt  (10.664 bytes · 25 linhas · 1 parágrafos reais · CRLF 0/LF 25)
==============================================================================
    estágio na esteira: solto — arquivo fora de transcricoes/ (ex.: upload/) — leitura de BRUTO, é o caso do experimento de motor

[1] PONTUAÇÃO E SEGMENTAÇÃO — 1.817 palavras
    sinais por 100 palavras: 16.13
    sentenças: 85 · palavras/sentença: 21.4 (mediana 15, maior 282)
    parágrafos: 1 · palavras/parágrafo: 1817.0
      vírgula                    206  (113.37/1.000 palavras)
      ponto                       81  (44.58/1.000 palavras)
      interrogação                 6  (3.3/1.000 palavras)
      reticências (3 pontos)       1  (0.55/1.000 palavras)

[2] DISFLUÊNCIA — 24 marcas (13.21 por 1.000 palavras)
    repetições: palavra 2 · bigrama 0 · trigrama 0 · prolongamentos 1
    marcadores orais: então 8 · sabe 8 · tipo 4 · aí 2

[3] FIDELIDADE TERMINOLÓGICA (contra a KB-RC)
    canônicos presentes: 16 formas distintas, 31 ocorrências
    variantes STT mapeadas presentes: 0 formas, 0 ocorrências (0.0/1.000 palavras)
    formas proibidas (Quarentena + livro-razão): 0 formas, 0 ocorrências
    Externos — forma canônica: 0 formas, 0 ocorrências · forma corrompida: 0 formas, 0 ocorrências
    taxa de confiança (canônico ÷ canônico+variante): 1.0000

[4] INTEGRAÇÃO À ESTEIRA
    maior linha: 2.070 chars = 19.9% do arquivo
    marcador 'Transcrição Automática': não
    rótulos de fala nativos: nenhum → diarização nativa: não
      [CUSTA CÓDIGO      ] rc_novo.py / rc_indice.py medem o corpo pelo critério único de rc_leitura.py (marcador → linha mais longa → arquivo inteiro, com aviso)
                         a maior linha cobre 19.9% do arquivo — cai no critério 3 (arquivo inteiro): o corpo inclui o cabeçalho, medição contaminada; rc_leitura AVISA em metadados.yaml, mas ainda não separa
      [CUSTA CÓDIGO      ] rc_diagnostico.carregar_transcricao separa cabeçalho pelo marcador 'Transcrição Automática' (pendência: parecer-motor-stt §8 item 2)
                         sem marcador: o arquivo inteiro vira corpo e o cabeçalho sai vazio
      [compatível        ] diarização opção B (rótulos inferidos pelo revisor)
                         sem rótulos nativos: o revisor continua inferindo
      [PREMISSA SUPERADA ] Guia §8 (pontuação é corretiva, o STT não traz)
                         161.3 sinais por 1.000 palavras — pontuação nativa: a norma passa a ser de conferência, não de reconstrução
```

## Comparativo — video-2-transcri-youtube.txt (A) × video-2-revisao-corpo.txt (B)

| métrica | A | B | Δ B−A | melhor |
|---|---:|---:|---:|:---:|
| bytes | 11.638 | 10.664 | -974 | — |
| linhas | 1 | 25 | 24 | — |
| parágrafos (separados por linha em branco) | 1 | 1 | 0 | — |
| segmentos por quebra de linha | 1 | 25 | 24 | B |
| palavras | 1.810 | 1.817 | 7 | — |
| sinais por 100 palavras | 0.11 | 16.13 | 16.02 | B |
| sentenças | 3 | 85 | 82 | B |
| palavras/sentença | 603.3 | 21.4 | -581.9 | B |
| maior sentença (palavras) | 1.737 | 282 | -1455 | B |
| disfluências totais | 27 | 24 | -3 | B |
| disfluências/1.000 palavras | 14.92 | 13.21 | -1.71 | B |
| repetições de palavra | 3 | 2 | -1 | B |
| marcadores orais | 24 | 22 | -2 | B |
| canônicos KB presentes | 26 | 31 | 5 | B |
| corrupções STT presentes | 0 | 0 | 0 | — |
| corrupções/1.000 palavras | 0.0 | 0.0 | 0 | — |
| formas proibidas | 0 | 0 | 0 | — |
| taxa de confiança | 1.0 | 1.0 | 0 | — |

### Proveniência — os dois lados vêm do mesmo reconhecimento de fala?

| medida | valor |
|---|---:|
| divergência lexical | 8.12% (70 de A ausentes em B · 77 de B ausentes em A) |
| Jaccard de vocabulário | 0.916 |
| hapax em comum | 0.922 |
| marcadores orais com contagem idêntica | 4 (67%) |
| tokens mascarados com asterisco | A 0 · B 0 |

**Veredito:** mesma base de áudio com edição substancial em um dos lados.


Compatibilidade com a esteira: **A 3/4** · **B 2/4** (premissas superadas: A 0, B 1).

- **B CUSTA CÓDIGO** `rc_novo.py / rc_indice.py medem o corpo pelo critério único de rc_leitura.py (marcador → linha mais longa → arquivo inteiro, com aviso)` — a maior linha cobre 19.9% do arquivo — cai no critério 3 (arquivo inteiro): o corpo inclui o cabeçalho, medição contaminada; rc_leitura AVISA em metadados.yaml, mas ainda não separa
- **B CUSTA CÓDIGO** `rc_diagnostico.carregar_transcricao separa cabeçalho pelo marcador 'Transcrição Automática' (pendência: parecer-motor-stt §8 item 2)` — sem marcador: o arquivo inteiro vira corpo e o cabeçalho sai vazio
- **B SUPERA A PREMISSA** `Guia §8 (pontuação é corretiva, o STT não traz)` — 161.3 sinais por 1.000 palavras — pontuação nativa: a norma passa a ser de conferência, não de reconstrução (trabalho manual que deixa de existir; não é defeito)

