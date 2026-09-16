# Mídia desta transcrição — nada aqui é arquivado

**Política:** Plano de Organização §7 (Princípio P9 — peso pesado fora do Git).

| Item | Situação |
|---|---|
| Vídeo original | **não arquivado.** O YouTube já é o arquivo; um `.mp4` de 125 min tem 300 MB a 2 GB e inutiliza o clone para todos |
| Áudio | **não arquivado.** Ficaria em ~60 MB; a cota gratuita do Git LFS (1 GB) comportaria cerca de 16 vídeos e acabaria |
| Legenda automática (`.txt`/`.vtt`) | **arquivada** — é o bruto em `../transcricao-bruta.txt`, texto pequeno e diffável |

## Link para a fonte

`url` em `../metadados.yaml` está **A PREENCHER**: a captura de 15/09/2026 não registrou o
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
