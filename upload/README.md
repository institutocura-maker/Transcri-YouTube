# `upload/` — zona de trânsito do Comandante

Pasta para **entregar arquivo ao Agente 86 sem passar pelo chat**. É a resposta prática a uma
falha que já aconteceu: no despacho de 16/09/2026 o anexo `Opcao-B.txt` (STT do NotebookLM) não
chegou ao workspace, e o experimento de motor ficou parado sem que nenhum dos dois lados soubesse
dizer onde o arquivo estava.

## Regras

1. **O conteúdo desta pasta NÃO é versionado** (`.gitignore`: `/upload/*`, com exceção deste
   README). Ela é caixa de entrada, não arquivo permanente.
2. **O que for aprovado migra e passa a ser versionado.** STT que entra na esteira vai para
   `transcricoes/<slug>/00-fonte/`, onde ganha `metadados.yaml` com sha256 e passa a ser
   fiscalizado pelo QA (portão G1). Nada que seja fonte de verdade pode morar só aqui.
3. **Nome ASCII-safe**, sem acento, espaço ou travessão (mesma norma dos slugs — Princípio P8).
   Sugestão: `<video>--<motor>.txt`, ex.: `revelacoes-cosmicas-urgente--notebooklm.txt`.
4. **Formatos aceitos:** `.txt`, `.md`, `.csv`, `.json`, `.docx`, `.zip` (eu descompacto).
   **Não** mandar áudio ou vídeo: `*.mp4`, `*.wav`, `*.mkv` etc. já são bloqueados pelo
   `.gitignore` da raiz, e mídia entra só por link externo em `00-fonte/midia/README.md` (P9).
5. Arquivo grande não é problema — o bruto de referência tem 106 KB e é lido inteiro.

## Como entregar quando o anexo do chat falha

| via | como | observação |
|---|---|---|
| **A. reanexar no chat** | arrastar o arquivo de novo na conversa | a via normal; quando funciona, eu mesmo gravo em `upload/` |
| **B. colar o texto no chat** | colar o conteúdo na mensagem | bom até ~50 KB; acima disso fica truncado |
| **C. link público** | mandar a URL | eu busco com `fetch_page`. Link de Drive precisa estar como "qualquer pessoa com o link"; Drive privado não abre |

**A via C serve para documento, não para transcrição.** O `fetch_page` lê a página do YouTube e
devolve também o transcript do painel — mas esse texto vem **reescrito**: pontuado, capitalizado,
com anotações de áudio que o ASR não produziu e palavras trocadas. Conferido contra o bruto oficial
do vídeo 2 em 16/09/2026, corrompeu "ovo cósmico" em "novo cósmico" e inventou 144 vírgulas onde o
bruto tem zero (Guia v2 §2.6, regra 8). **Bruto de transcrição só entra por A, B ou D** — de
preferência D (`git add -f upload/<video>--<motor>.txt`), que preserva o arquivo byte a byte e me
deixa registrar sha256 no `metadados.yaml`. Sem bruto, a fila de curadoria fica bloqueada e a pasta
espera: eu não instalo texto de *fetch* como fonte, nem o uso para atestar variante.
| **D. commit do Comandante** | `git add -f upload/x.txt && git commit && git push` | o `-f` vence o ignore; eu puxo no turno seguinte |

## O que acontece quando um arquivo chega aqui

1. `python ferramentas/rc_perfil_stt.py upload/<arquivo>` — perfil nos quatro eixos
   (pontuação/segmentação, disfluência, fidelidade terminológica contra a KB-RC, integração).
2. Se houver contraparte, o comparativo A × B sai na mesma execução — basta passar os dois
   arquivos como argumentos — e o relatório vai para `docs/pareceres/` com `--md`.
3. Parecer de engenharia com veredito: o motor entra em `00-fonte/` ou não entra, e o que custa
   em código nas ferramentas `rc_*` se entrar.

Nenhuma decisão de padrão de entrada é tomada sem esse diagnóstico — foi o critério de aceite que
o Comandante fixou.
