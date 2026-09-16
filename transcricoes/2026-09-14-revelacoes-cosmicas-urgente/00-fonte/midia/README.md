# Mídia desta transcrição — nada aqui é arquivado

**Política:** Plano de Organização §7 (Princípio P9 — peso pesado fora do Git).

| Item | Situação |
|---|---|
| Vídeo original | **não arquivado.** O YouTube já é o arquivo; um `.mp4` de 125 min tem 300 MB a 2 GB e inutiliza o clone para todos |
| Áudio | **não arquivado.** Ficaria em ~60 MB; a cota gratuita do Git LFS (1 GB) comportaria cerca de 16 vídeos e acabaria |
| Legenda automática (`.txt`/`.vtt`) | **arquivada** — é o bruto em `../transcricao-bruta.txt`, texto pequeno e diffável |

## Link para a fonte

`url` em `../metadados.yaml` está **https://www.youtube.com/watch?v=enBUKAWXQRw**: a captura de 15/09/2026 não registrou o
endereço do vídeo. Identificação conhecida até aqui:

- canal **Paranormal Experience**, transmissão ao vivo de **14/09/2026**
- chamada *"ASSISTA ANTES QUE SAIA DO AR"*
- entrevistado **Jan Val Ellam**, apresentação **Guru de Malá**, com **Alexandre Sherminator**

Quem localizar o vídeo deve preencher `url` em `metadados.yaml` e `link` no bloco `midia`,
no mesmo commit — sem isso a proveniência do bruto fica incompleta.

## Se um dia for preciso reouvir um trecho

Os 14 marcadores `[INAUDÍVEL: "…"]` desta transcrição são o único motivo plausível para
reouvir o áudio. Nesse caso:

1. baixe o áudio para fora do repositório (por exemplo `~/audio/`);
2. registre o trecho em `../90-registro/diario-de-bordo.md` com o minuto aproximado;
3. **não** faça commit do arquivo. Se a decisão do Projeto mudar para LFS, o
   `.gitattributes` já tem as regras prontas e o Plano §7 documenta o custo.


---

## Registro de 16/09/2026 — URL fornecida pelo Comandante e conferida

| campo | valor |
|---|---|
| URL | https://www.youtube.com/watch?v=enBUKAWXQRw |
| Título oficial | ASSISTA ANTES QUE SAIA DO AR - Jan Val Ellam |
| Canal | PARANORMAL EXPERIENCE (@PARANORMALBR) |
| Publicado | 2026-09-14 (upload em 2026-09-15) |
| Duração | 2:25:50 (≈146 min — o `metadados.yaml` trazia 125, corrigido) |
| Categoria | Education · 162.368 visualizações · 9.935 likes (em 16/09/2026) |
| Código na base | **Y2026-09-14** (`KB-RC/biblio.json`, padrão Y do Guia §2.5) |

A descrição oficial confirma dois pontos da revisão: o anúncio da Insider com cupom PARANORMAL (bloco 1) e as Mandalas Arcturianas (bloco 6). E acrescenta um alerta: ela anuncia **outro** evento — Conexão com os Guardiões Espirituais, Robson Pinheiro, R$ 160 ou 10× R$ 16 —, que não é o evento de 03/10 no Teatro Santo Agostinho citado no bloco 3 (Terry Fabris + Robson Pinheiro, R$ 180 ou 12× R$ 18,60). As duas `[NOTA]` de preço do bloco 3 continuam corretas; a diferença entre os dois eventos ficou registrada no item 0041 da fila de curadoria.
