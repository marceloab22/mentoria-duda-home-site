#!/usr/bin/env python3
"""Troca placeholders de imagem ({{FOTO_1}}) por base64 embutido.

Por que só no final: base64 gigante no arquivo entope o contexto da conversa e deixa cada
iteração de design lenta. Trabalhe com {{FOTO_1}} no arquivo mestre e gere o arquivo final
com este script.

Lembre: base64 infla o arquivo em cerca de 33%. Use base64 na prévia; no site final,
prefira arquivo de imagem de verdade. Redimensione antes (lado maior de no máximo 1600px
para foto de seção, 2000px para hero) e use JPEG qualidade 80.

Uso:
    python3 base64-embed.py home-trabalho.html home-final.html \\
        FOTO_1=imagens/hero.jpg \\
        FOTO_2=imagens/recepcao.jpg \\
        LOGO=imagens/logo.png

Cada par vira a troca de "{{NOME}}" pelo data URI do arquivo.
"""

import base64
import mimetypes
import os
import sys

LIMITE_AVISO_MB = 2.0


def data_uri(path):
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        sys.exit('nao consegui descobrir o tipo de %s (use .jpg, .png, .svg, .webp)' % path)
    with open(path, 'rb') as f:
        dados = base64.b64encode(f.read()).decode()
    return 'data:%s;base64,%s' % (mime, dados)


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)

    entrada, saida = sys.argv[1], sys.argv[2]
    pares = sys.argv[3:]

    with open(entrada, encoding='utf-8') as f:
        html = f.read()

    for par in pares:
        if '=' not in par:
            sys.exit('formato invalido: %r (esperado "NOME=caminho.jpg")' % par)
        nome, caminho = par.split('=', 1)
        placeholder = '{{%s}}' % nome.strip()
        if placeholder not in html:
            sys.exit('placeholder %s nao existe em %s' % (placeholder, entrada))
        if not os.path.isfile(caminho):
            sys.exit('arquivo nao encontrado: %s' % caminho)
        html = html.replace(placeholder, data_uri(caminho))

    # Nenhum placeholder pode sobrar: imagem quebrada no site publicado.
    if '{{' in html:
        restantes = set()
        for pedaco in html.split('{{')[1:]:
            restantes.add('{{' + pedaco.split('}}')[0] + '}}')
        sys.exit('sobrou placeholder sem imagem: %s' % ', '.join(sorted(restantes)))

    with open(saida, 'w', encoding='utf-8') as f:
        f.write(html)

    tamanho_mb = len(html.encode('utf-8')) / 1024 / 1024
    print('ok: %s (%.2f MB)' % (saida, tamanho_mb))
    if tamanho_mb > LIMITE_AVISO_MB:
        print('AVISO: acima de %.1f MB. Redimensione as fotos antes de embutir.'
              % LIMITE_AVISO_MB)
    if '—' in html:
        print('AVISO: o arquivo contem travessao (em-dash). Corrigir antes de publicar.')


if __name__ == '__main__':
    main()
