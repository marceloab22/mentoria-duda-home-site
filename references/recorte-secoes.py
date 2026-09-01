#!/usr/bin/env python3
"""Recorta cada <section id="..."> num arquivo HTML isolado, para testar sem rolar a página.

Por que existe: página pesada (fotos em base64 + 10 seções) trava o preview ao rolar em
alguns ambientes (a ferramenta de scroll, scroll_to e window.scrollTo travam igual: o
problema é o peso da página). Cada seção isolada cabe na tela sem scroll nenhum.

Cada arquivo gerado tem: o mesmo <style> do original + o wrapper + só aquela seção.
Assim o CSS prefixado por #wrapper continua valendo e o visual é fiel.

Uso:
    python3 recorte-secoes.py home-final.html --wrapper site-home --saida testes/

    # só algumas seções:
    python3 recorte-secoes.py home-final.html --wrapper site-home --saida testes/ \\
        --apenas local faq

Depois, para ver no navegador:
    python3 -m http.server 8899 --directory testes
"""

import argparse
import os
import re
import sys


def extrair_estilos(html):
    """Devolve todos os blocos <style>...</style> concatenados."""
    blocos = re.findall(r'<style\b[^>]*>.*?</style>', html, re.S | re.I)
    if not blocos:
        sys.exit('nenhum bloco <style> encontrado no arquivo')
    return '\n'.join(blocos)


def extrair_scripts(html):
    """Devolve os blocos <script> inline (sem src), para seções com interatividade."""
    return '\n'.join(
        b for b in re.findall(r'<script\b(?![^>]*\bsrc=)[^>]*>.*?</script>', html, re.S | re.I)
    )


def extrair_secoes(html):
    """Devolve [(id, html_da_secao)] para cada <section id="..."> de primeiro nível."""
    achados = []
    for m in re.finditer(r'<section\b[^>]*\bid="([^"]+)"', html, re.I):
        sec_id = m.group(1)
        inicio = m.start()
        # Casamento de <section> aninhada, contando abertura e fechamento.
        profundidade = 0
        pos = inicio
        for t in re.finditer(r'</?section\b', html[inicio:], re.I):
            pos = inicio + t.end()
            profundidade += 1 if not t.group(0).startswith('</') else -1
            if profundidade == 0:
                fim = html.find('>', pos) + 1
                achados.append((sec_id, html[inicio:fim]))
                break
    return achados


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('arquivo')
    p.add_argument('--wrapper', required=True,
                   help='id do wrapper da pagina, sem #. Ex: site-home')
    p.add_argument('--saida', default='testes')
    p.add_argument('--apenas', nargs='*', default=None,
                   help='ids de secao a recortar (padrao: todas)')
    p.add_argument('--com-script', action='store_true',
                   help='inclui os <script> inline (para secoes com FAQ, carrossel etc)')
    a = p.parse_args()

    with open(a.arquivo, encoding='utf-8') as f:
        html = f.read()

    estilos = extrair_estilos(html)
    scripts = extrair_scripts(html) if a.com_script else ''
    secoes = extrair_secoes(html)

    if not secoes:
        sys.exit('nenhuma <section id="..."> encontrada')

    if a.apenas:
        pedidos = set(a.apenas)
        faltando = pedidos - {s for s, _ in secoes}
        if faltando:
            sys.exit('secao nao encontrada: %s' % ', '.join(sorted(faltando)))
        secoes = [(i, h) for i, h in secoes if i in pedidos]

    os.makedirs(a.saida, exist_ok=True)

    for sec_id, sec_html in secoes:
        destino = os.path.join(a.saida, 'secao-%s.html' % sec_id)
        with open(destino, 'w', encoding='utf-8') as f:
            f.write('<!doctype html><meta charset="utf-8">\n')
            f.write('<title>%s</title>\n' % sec_id)
            f.write(estilos)
            f.write('\n<div id="%s">\n' % a.wrapper)
            f.write(sec_html)
            f.write('\n</div>\n')
            if scripts:
                f.write(scripts)
        print('ok: %s' % destino)

    print('\n%d secoes. Para ver:\n  python3 -m http.server 8899 --directory %s'
          % (len(secoes), a.saida))


if __name__ == '__main__':
    main()
