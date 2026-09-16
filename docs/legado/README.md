# Legado — congelado, datado, somente leitura

Nada aqui é fonte de verdade. Estes arquivos ficam no repositório porque o histórico
do Projeto passa por eles (Princípio P10 do Plano de Organização: nada se apaga,
legado é arquivado com data).

| Arquivo | O que foi | Substituído por | Data do congelamento |
|---|---|---|---|
| `2026-09-base-terminologica.xlsx` | fonte de verdade terminológica até 15/09/2026: 946 termos, 104 obras, 1.887 relações, 7 abas | `KB-RC/canonico.json` + `KB-RC/biblio.json` + `KB-RC/termos/*.md` | 2026-09-15 |
| `2026-09-guia-v1/guia-sistema-de-revisao-e-governanca-terminologica-v1.docx` | norma editorial v1, importada de outra plataforma como skill | `docs/normas/guia-revisao-v2.md` (18 seções) | 2026-09-15 |

## Regras

1. **Não editar.** Correção em arquivo congelado se faz no substituto, nunca aqui.
2. **A planilha ainda serve para conferência** — é um retrato anterior, sem prosa
   curatorial. Onde ela e a KB-RC divergem, **a KB-RC vence** (despacho do Comandante,
   15/09/2026; ver `docs/normas/resolucao-de-conflitos.md`).
3. **Novo legado entra com data no nome** — `AAAA-MM-assunto` — e com uma linha na
   tabela acima dizendo o que foi e quem o substituiu.
4. O protótipo de diagnóstico da primeira transcrição está em
   `2026-09-prototipo-analise/` (fase 4 da migração).
