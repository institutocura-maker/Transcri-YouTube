# Mídia desta transcrição — nada aqui é arquivado

**Política:** `docs/planos/plano-de-organizacao.md` §7 (Princípio P9 — peso pesado fora do Git).

| Item | Situação |
|---|---|
| Vídeo original | **não arquivado** — o YouTube já é o arquivo; um `.mp4` longo inutiliza o clone |
| Áudio | **não arquivado** — a cota gratuita do LFS (1 GB) comportaria poucos vídeos |
| Legenda automática | **arquivada** — é o bruto em `../transcricao-bruta.txt` |

## Link para a fonte

O endereço do vídeo fica em `url` no `../metadados.yaml`. Se ele não foi registrado na captura,
preencher no primeiro commit de revisão — sem proveniência o bruto é um `.txt` órfão.

## Se for preciso reouvir um trecho

Os marcadores `[INAUDÍVEL: "…"]` são o único motivo plausível. Nesse caso: baixe o áudio para fora
do repositório, registre o minuto aproximado em `../../90-registro/diario-de-bordo.md` e **não**
faça commit do arquivo.
