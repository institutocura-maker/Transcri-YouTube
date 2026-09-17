# Despacho de 17/09/2026 — adjudicação da fila de curadoria do vídeo 2

| campo | valor |
|---|---|
| data | 17 de setembro de 2026 |
| de | Comandante |
| para | Agente 86 |
| assunto | "Adjudicação da Fila (Vídeo 2)" — os 10 itens pendentes e a proposta de Externos |
| rege | `KB-RC/_fila-de-curadoria.csv` (ids 0042–0051), fichas RC-034, RC-077, RC-548, RC-577, RC-636, RC-894, `ferramentas/dados/externos.csv` |
| execução | `KB-RC/_relatorio-curadoria-lote-03.md` · `40-devolucao/devolucao-a-kb.md` §8 |

## 1. O que o Comandante decidiu

Abertura do despacho: *"Excelente trabalho de auditoria. A captura da regressão causada pelo corretor
ortográfico (glues/pósetron) prova o valor absoluto de cruzar a revisão humana com o STT bruto. A
retratação do §3 está lida e validada; a norma de nunca atestar variante via fetch de página está
aprovada."*

1. **Variantes STT (0043–0047): APROVADAS.** "Pode incorporar às fichas as variantes atestadas no
   bruto: `locas` e `louoca` (RC-077), `glu` (RC-034), e `acásicos/acáxicos` (RC-548)." E, sobre o
   item 0046: "Confirmo a decisão de `chamanismo` como `aceita-parcial` para RC-577, mantendo a
   integridade doutrinária sem forçar um conceito onde ele não foi aplicado."
2. **Quarentena de quase-canônicas (0049, 0050): APROVADAS.** "Esta é uma defesa crítica. Insira
   imediatamente as regras `NUNCA \"glues\"` na RC-034 e `NUNCA \"pósetron\"` na RC-636 para que o
   portão G3 barre essas intervenções de editores de texto no futuro. O encargo derivado de varredura
   de formas quase-canônicas entra para o nosso radar de melhorias."
3. **Falso amigo (0048): APROVADA.** "A palavra `qualia` neste contexto foi claramente uma corruptela
   do STT para \"colmeia\" (RC-174). Insira a ressalva na ficha RC-894 para exigir validação de
   contexto e evitar falsos positivos automatizados."
4. **Divergências factuais (0051 e título): APROVADAS.** Data: "Mantenha 12/09/2026 (data da
   plataforma) como a oficial nos metadados." Título/slug: "De acordo com o tratamento: título oficial
   e slug mantidos, com a minha sugestão alocada no campo `chamada`."
5. **Camada 3: APROVADO.** "Pode incluir o termo `Jesus` no arquivo `externos.csv` conforme proposto
   na devolução."
6. **Fecho:** "Pode aplicar todas as decisões, atualizar o `CHANGELOG.md` e fechar o pacote do
   Vídeo 2!"

## 2. Como a casa executou

* As cinco variantes foram gravadas **pelo `rc_curadoria.py --aplicar`**, que exige atestação no bruto
  antes de escrever — não à mão. RC-077 e RC-034 ganharam seção *Etimologia e Grafias* nova; RC-577 e
  RC-548 receberam a linha de variações. Fila e CHANGELOG atualizados pela própria ferramenta.
* As duas **Quarentenas** e as duas **cautelas editoriais** (RC-894 e RC-577) foram gravadas à mão, no
  formato da anatomia de ficha do Guia §2.2, porque a ferramenta só aplica `nova-variante`
  mecanicamente. Cada seção traz a origem, o trecho atestado e o número do item da fila.
* `Jesus` entrou em `ferramentas/dados/externos.csv` como **semente de proteção** (38 entidades).
* **Efeito medido:** o portão G3 desta pasta passou de 6 para **8 formas proibidas varridas** (e o do
  vídeo 1, de 25 para 27), com **0 ocorrências** nos textos revisados — `glues` e `pósetron` só
  aparecem dentro das `[NOTA]` que documentam a regressão, e o QA expurga marcadores antes de varrer.
* Fila do vídeo 2: **10 de 10 itens `aplicada`**, zero pendência. Relatório:
  `KB-RC/_relatorio-curadoria-lote-03.md`.

## 3. O que o despacho pôs no radar (não é encargo fechado)

**Varredura de formas quase-canônicas** — palavras que diferem do canônico por uma letra ou um acento
e que o corretor do editor produz (`glues`/`gluons`, `pósetron`/`pósitron`, a família
`positelétron`). Enquanto não existir, a defesa é a Quarentena ficha a ficha, reativa: só barra o que
já foi visto. Proposta em `docs/pareceres/parecer-video-2-revisao-externa.md` §9, agora com duas
Quarentenas de exemplo gravadas na KB.

## 4. Um defeito de instrumento achado durante a aplicação

A `[NOTA]` do *pósitron* cita a notação da ficha RC-636, que tem colchete dentro
(«pósitrons [STT 'positelétron']»). `MARCADOR_RE` e `NOTA_RE` fechavam no primeiro `]`: o rabo da nota
voltava a ser corpo — saía sem itálico no `.docx`, contava como palavra (1.874 em vez de 1.865) e, se
uma forma proibida fosse citada depois do colchete interno, o G3 daria **falso positivo punindo o
revisor por documentar**. Corrigido em `ferramentas/rc_docx.py` (um nível de aninhamento tolerado),
com quatro verificações novas em `testes/test_pipeline.py`: **158 verificações, 0 falhas**.
