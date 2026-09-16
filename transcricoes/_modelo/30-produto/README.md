# 30-produto — o que se lê

`transcricao-revisada.docx` é **gerado** a partir de `../20-blocos/*.md` e nunca editado à mão:

```bash
python ferramentas/rc_docx.py ../20-blocos/bloco-*.md \
    --lexico ../10-diagnostico/dossie-bloco.txt \
    --saida transcricao-revisada.docx \
    --titulo "Título da palestra" \
    --subtitulo "Transcrição revisada · padronização terminológica conforme a KB-RC" \
    --validar ../10-diagnostico/variantes-propostas.csv
```

O portão **G6** do QA regenera este arquivo e compara com o versionado: se divergir, o `.docx`
publicado não corresponde aos blocos e o PR não passa.
