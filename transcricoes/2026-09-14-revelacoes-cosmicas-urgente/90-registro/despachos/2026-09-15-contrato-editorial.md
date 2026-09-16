# Despacho — contrato editorial e autorização de processamento

**Emissor:** Comandante · **Data:** 15 de setembro de 2026 (complementado em 16/09/2026)
**Destinatário:** Agente 86 · **Escopo:** esta transcrição e as seguintes, até revisão do Guia
**Status:** EM VIGOR

---

## 1. Fonte de verdade

`KB-RC/` + `canonico.json` + `biblio.json` + `termos/*.md` **são a fonte de verdade**.
A planilha `base-terminologica.xlsx` é **legado** — serve a conferência, não a decisão.
Onde planilha e KB-RC divergem, a KB-RC vence.

*(A planilha está hoje em `docs/legado/2026-09-base-terminologica.xlsx`.)*

## 2. Saída — dois formatos, ambos obrigatórios

| Formato | Papel |
|---|---|
| `.md` | versionamento. **Inegociável**: é o que o Git diffa e o que o motor remonta |
| `.docx` | produto de leitura, com tipografia fixa (justificado, entrelinha 1,5, corpo 12 pt) |

O `.docx` é sempre **gerado** a partir dos `.md`, nunca editado à mão. O portão G6 do QA verifica
isso regenerando o arquivo e comparando.

## 3. "Guia de fontes" — REMOVER do produto final

O resumo automático que abre a transcrição (linhas 7 a 11 do cabeçalho) **não vai para o produto**.
O cabeçalho inteiro permanece íntegro em `00-fonte/transcricao-bruta.txt`; o corpo começa na linha 13.

## 4. Anúncios e trechos promocionais — PRESERVAR no corpo

Ficam no texto, marcados com `**[ANÚNCIO]**`. Nesta transcrição: Insider (40% de desconto, cupom
PARANORMAL), evento com Terry Fabris no Teatro Santo Agostinho e Mandalas Arcturianas. Têm valor
documental — inclusive quando o preço anunciado diverge do oficial, caso que virou `[NOTA]`.

## 5. Diarização — opção B: rótulos inferidos explícitos

Rótulos usados: `[GURU DE MALÁ]` (apresentador principal), `[ALEXANDRE SHERMINATOR]`
(coapresentador), `[JAN VAL ELLAM]`, e `[FALANTE?]` quando a atribuição não é segura.
A forma de aplicação (negrito inline no início do parágrafo, em vez de linha própria como pede o
Guia §9) é um **desvio documentado** em `20-blocos/notas-de-revisao.md` §3.

## 6. Disfluência — nível LEVE

Remover repetições imediatas e marcadores de hesitação ("né", "eh", "uhum").
**Preservar** sintaxe oral, repetições retóricas e a identidade de fala do autor.

## 7. Busca externa — somente camada Externos

Autorizada **apenas** para a camada 3 (autores, obras, empresas, pessoas e lugares do mundo real),
sempre **com fonte e data** registradas. Termos da Revelação Cósmica não se resolvem por busca
externa: resolvem-se pela KB-RC ou ficam como `[A CONFIRMAR]`.

## 8. Autorização de processamento

> "Autorização total para iniciar o processamento e a revisão dos 8 blocos."

Entregáveis esperados, cumpridos em 16/09/2026:

1. os `.md` revisados, um por bloco → `20-blocos/bloco-01.md` … `bloco-08.md`
2. o `.docx` montado → `30-produto/transcricao-revisada.docx`
3. o extrato final com a devolução à KB-RC → `40-devolucao/devolucao-a-kb.md`

## 9. Pendências assumidas pelo Comandante

Ficha de Jeane Miranda, código B095 e demais pendências residuais da KB **não bloqueiam** esta
esteira; foram assumidas pelo Comandante.

## 10. Regra que este despacho não precisou enunciar, mas que vale

**O revisor propõe; o curador aplica.** Nenhuma alteração entra em `KB-RC/` a partir do trabalho de
revisão — tudo vai para `40-devolucao/` e para a fila de curadoria.
