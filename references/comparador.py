#!/usr/bin/env python3
"""Monta a prévia comparativa (abas + Computador/Celular) a partir de N arquivos HTML.

Serve para a Fase 1 (3 direções) e para a regra do "não gostei" (6 versões de um bloco).
Cada versão vira um <iframe srcdoc="..."> com escape de HTML feito corretamente.

Uso:
    python3 comparador.py \\
        --titulo "Home . Dra. Marina Xavier" \\
        --subtitulo "Fase 1: cabecalho, hero e amostra da proxima secao" \\
        --nota "A: escura e centralizada. B: clara com foto ao lado. C: bloco de cor." \\
        --saida comparador-fase1.html \\
        "Versao A=vA.html" "Versao B=vB.html" "Versao C=vC.html"

Depois: publicar o arquivo de saída com a ferramenta Artifact.
"""

import argparse
import html
import os
import sys

TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'comparador-template.html')


def montar(titulo, subtitulo, nota, versoes, template_path=TEMPLATE):
    """versoes: lista de (rotulo, caminho_html). Devolve o HTML do comparador."""
    with open(template_path, encoding='utf-8') as f:
        tpl = f.read()

    # Tira o comentario de instrucao do template: nao deve ir pro arquivo publicado.
    if tpl.lstrip().startswith('<!--'):
        tpl = tpl[tpl.index('-->') + 3:].lstrip()

    tpl = (tpl
           .replace('{{TITULO}}', html.escape(titulo))
           .replace('{{SUBTITULO}}', html.escape(subtitulo))
           .replace('{{NOTA}}', html.escape(nota)))

    sobrando = [m for m in ('{{TITULO}}', '{{SUBTITULO}}', '{{NOTA}}') if m in tpl]
    if sobrando:
        raise ValueError('placeholder nao substituido: %s' % ', '.join(sobrando))
    if '{{IFRAMES}}' not in tpl:
        raise ValueError('template sem {{IFRAMES}}')

    iframes = []
    for rotulo, caminho in versoes:
        with open(caminho, encoding='utf-8') as f:
            conteudo = f.read()
        iframes.append(
            '    <iframe data-label="{rot}" title="{rot}" srcdoc="{doc}"></iframe>'.format(
                rot=html.escape(rotulo, quote=True),
                doc=html.escape(conteudo, quote=True),
            )
        )

    return tpl.replace('{{IFRAMES}}', '\n'.join(iframes))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--titulo', required=True)
    p.add_argument('--subtitulo', default='')
    p.add_argument('--nota', default='')
    p.add_argument('--saida', required=True)
    p.add_argument('versoes', nargs='+',
                   help='cada item no formato "Rotulo=caminho.html"')
    a = p.parse_args()

    versoes = []
    for item in a.versoes:
        if '=' not in item:
            sys.exit('formato invalido: %r (esperado "Rotulo=caminho.html")' % item)
        rotulo, caminho = item.split('=', 1)
        if not os.path.isfile(caminho):
            sys.exit('arquivo nao encontrado: %s' % caminho)
        versoes.append((rotulo.strip(), caminho.strip()))

    saida = montar(a.titulo, a.subtitulo, a.nota, versoes)

    with open(a.saida, 'w', encoding='utf-8') as f:
        f.write(saida)

    # Checagem que evita publicar comparador quebrado.
    assert saida.count('<iframe data-label=') == len(versoes), 'numero de iframes nao bate'
    if '—' in saida:
        print('AVISO: o comparador contem travessao (em-dash). Corrigir antes de publicar.')

    print('ok: %s (%d versoes, %d KB)'
          % (a.saida, len(versoes), len(saida.encode('utf-8')) // 1024))


if __name__ == '__main__':
    main()
