# Diário de bordo — Alienígenas e humanos: Eles já estão entre nós?

Registro cronológico do que foi feito, do que falhou e do que foi decidido.
*Append-only*: entrada nova embaixo, nunca reescrita em cima. É o que permite retomar o trabalho
sem refazer descobertas.

Pasta `transcricoes/2026-09-12-alienigenas-e-humanos-entre-nos` · fonte `Y2026-09-12` ·
vídeo https://www.youtube.com/watch?v=v0gJWn50gg8 (canal Jan Val Ellam, 19:24, publicado 2026-09-12).

---

## 2026-09-16 — o vídeo chegou por duas vias, e nenhuma delas era o bruto

- O Comandante commitou na branch, pelo GitHub web, `upload/alienigenas-ou-seres-de-outro-universo.docx`
  (`0ea4388`): texto **revisado** por aplicativo especialista + revisão dele. 58 parágrafos, 1.817
  palavras de corpo, sha256 `d188b7ee…`.
- Não havia bruto. O sandbox não tem egresso para o YouTube (`yt-dlp` e `curl` morrem em SSL EOF); a
  única rota é `fetch_page`, que alcança a página do vídeo.
- Por `fetch_page`: identidade confirmada (título oficial "Alienígenas e humanos: Eles já estão entre
  nós?", canal Jan Val Ellam / @JanValEllam, *uploaded* 2026-09-12, 19:24, 76.950 visualizações,
  categoria People & Blogs) **e** o transcript do painel, gravado como
  `docs/pareceres/captura-referencia-v0gJWn50gg8.txt`.
- Escrito o parecer de recepção da revisão externa (`dc2dbce`), auditando o `.docx` contra aquela
  captura. Veredito: nada censurado, 2 regressões a corrigir, divergência de 9,23%.

## 2026-09-16 — o bruto oficial chegou e desmentiu a captura

- `upload/video-2-transcri-youtube.txt` (commit `87a3525` do Comandante): 11.638 bytes, 12 linhas,
  corpo na linha 12, **1.810 palavras**, sha256 `16c9276a…`.
- Conferência bruto × captura: divergência de 1,22%, mas três defeitos da captura —
  **(a)** pontuou (144 vírgulas contra **zero** no bruto), **(b)** corrompeu "ovo cósmico" em
  "novo cósmico", **(c)** inventou anotações de áudio (`[roncando]`, `[limpando a garganta]`) que o
  bruto não tem.
- Conclusão: os 13,66 sinais de pontuação por 100 palavras que o parecer atribuía ao ASR eram da
  **rota de captura**, não do YouTube. O ASR do YouTube **não pontua**: 0,11 sinais por 100 palavras
  no corpo do bruto (só os decimais de "3.000" e "5.000"). Guia §8 continua valendo.
- **Norma nova da casa:** transcrição obtida por *fetch* de página não é fonte. Serve para descobrir
  que um vídeo existe; não serve para instalar bruto, atestar variante nem medir.
- Parecer §3 **retratado**; §0, §2, §4, §7, §9 e §11 reescritos com os números oficiais; a variante
  "novo cósmico" → RC-034 saiu da fila (era corrupção minha, não do ASR).

## 2026-09-16 — terceira régua de corpo achada e morta

- Ao rerodar a medição no par oficial, o `rc_perfil_stt.py` devolveu **14,37%** de divergência onde o
  corpo tem **8,12%**: ele media o **arquivo inteiro**, e o cabeçalho do bruto traz o "guia de fontes"
  resumido (167 palavras, pontuado por ser resumo automático) — o suficiente para inventar 6,6 sinais
  de pontuação por 1.000 palavras e 3 pontos de divergência.
- Corrigido: o instrumento agora localiza o corpo pelo critério único do `rc_leitura.py` e mantém
  `texto_integral`/`linhas_integrais` para o eixo 4 (que pergunta justamente "onde começa o corpo?").
- **154 verificações, 0 falhas.** Medições regeneradas em `docs/pareceres/video-2-medicao-oficial.md`
  e `video-2-perfil-oficial.json`.
- Segundo achado do mesmo turno: o Guia §13.1 ensinava `rc_diagnostico.py --saida "transcricoes/<slug>"`,
  que joga os arquivos na raiz da pasta e deixa `diagnostico.json` (135 KB regeneráveis) **fora** do
  padrão do `.gitignore`. Rodar sem `--saida`: a ferramenta descobre `10-diagnostico/` sozinha.
  Guia corrigido.

## 2026-09-16 — esteira normal: pasta, diagnóstico, blocos

- `rc_novo.py --slug 2026-09-12-alienigenas-e-humanos-entre-nos --bruto upload/video-2-transcri-youtube.txt`
  → pasta criada, bruto instalado e medido (critério linha-mais-longa, cobertura 88,3%, sem aviso).
- `git mv` do `.docx` do Comandante para `00-fonte/revisao-comandante.docx`; `git rm` da cópia de
  trânsito do bruto em `upload/` (o `upload/` é caixa de entrada, não arquivo: nada que seja fonte de
  verdade pode morar só ali — Plano §7).
- `rc_diagnostico.py` sobre o bruto: 25 superfícies da base presentes, 189 candidatos, **27
  adjudicáveis**, 2 ausentes. Livro-razão com 29 linhas.
- Blocos montados **por script**, sem redigitação: cada substituição assertada contra o texto do
  `.docx` (contador de ocorrências exato). 3 blocos por fronteira de assunto — 484 / 933 / 586
  palavras, 25 parágrafos, 1.874 palavras de corpo, 5 `[NOTA]`, 3 rótulos `**[JAN VAL ELLAM]**`.
- As três regressões do editor corrigidas aqui: `glues` → **gluons**, `pósetron` → **pósitron**,
  "hoje a parte" → "hoje **à tarde**". Mais ortografia/hífen: *dia a dia*, *abelha-rainha*,
  *preestabelecidas*. Disfluência LEVE: 1 falso início removido, 1 anáfora enfática preservada.

## 2026-09-16 — adjudicação, devolução e produto

- Livro-razão fechado: **29 linhas decididas** (19 informativa, 6 recusada, 2 proteção, 1 aceita,
  1 aceita-parcial). A aceita é `locas` → Lokas (RC-077), atestada 2× no corpo do bruto; a parcial é
  `chamanismo` → *xamanismo*, com o termo RC-577 (Xamanismo Cósmico) **não** aplicado: o autor fala do
  xamanismo genérico.
- Falso amigo registrado: `qualia` no bruto é corruptela de **colmeia** (RC-174), não RC-894.
- `rc_docx.py` → `30-produto/transcricao-revisada.docx` (28 parágrafos de corpo, 17 negritos de
  primeira menção, 5 notas). QA do montador: nenhuma variante aceita sobrevive.
- Fonte `Y2026-09-12` registrada em `KB-RC/biblio.json` (106 obras) — sem ela o `rc_indice.py`
  reclama (Guia §2.5). 10 propostas na fila de curadoria (ids **0042–0051**), 1 proposta de Externos
  (`Jesus`).
- **Portões: G1–G8 `ok`, G9 `n/a`** (sem camada derivada — a revisão externa é humana, não derivado de
  máquina). Catálogo: `30-revisada`.

---

## Becos sem saída — não repetir

| Tentativa | Por que falhou |
|---|---|
| Usar transcript obtido por `fetch_page` como bruto ou como evidência | Devolve texto **reescrito**: pontuado (144 vírgulas contra 0 do bruto), capitalizado, com anotações de áudio inventadas e ao menos uma palavra corrompida ("ovo cósmico" → "novo cósmico"). Fidelidade desconhecida e não verificável. Serve para identificar o vídeo, nada mais |
| Concluir "o ASR do YouTube agora pontua" a partir dessa captura | Falso. O bruto oficial tem 0,11 sinais por 100 palavras. O que pontuou foi a rota de captura. Atalho que produziu um parecer inteiro a ser retratado |
| Medir arquivo com cabeçalho longo pelo arquivo inteiro | O "guia de fontes" resumido do bruto (167 palavras pontuadas) contaminou a medição: 14,37% no lugar de 8,12%, e pontuação "nativa" inventada. Usar sempre `rc_leitura.localizar_corpo` — vale para `rc_perfil_stt.py`, `rc_novo.py`, `rc_indice.py` |
| `rc_diagnostico.py --saida "transcricoes/<slug>"` (como o Guia ensinava) | Grava na raiz da pasta em vez de `10-diagnostico/` e deixa `diagnostico.json` fora do `.gitignore`. Rodar sem `--saida` |
| Confiar no corretor ortográfico do editor sobre termo técnico | Produz `glues` (por *gluons*) e `pósetron` (por *pósitron*): formas que **existem** na língua ou quase, e por isso passam por G3, G5 e G6. Só a conferência contra o bruto pegou |
| Deixar o revisor decidir "a parte" por "à tarde" sem conferir | Troca de uma palavra mudou o sentido da frase de abertura. O bruto atesta "à tarde". Divergência de palavra comum também se confere, não só termo da KB |
| Propor variante de `qualia` → RC-894 automaticamente | Nesta transcrição `qualia` é corruptela de **colmeia** (RC-174). Falso amigo: a varredura casa a forma, o sentido não |
| `ask_user` com quatro perguntas quando o Comandante já respondeu por mensagem | O despacho veio por extenso no chat (esteira normal, bruto entregue, nomeação justificada). Perguntar de novo seria pedir o que já foi dito |
