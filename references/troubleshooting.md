# Troubleshooting: catálogo de bugs reais

Todos os itens abaixo aconteceram de verdade em projetos com esta skill. Cada um tem
sintoma (como o usuário descreve), causa, diagnóstico e correção.

Procure pelo **sintoma**, que é o que você recebe do usuário.

---

## Índice por sintoma

| O usuário diz | Vá para |
| --- | --- |
| "Está torto" | [B1](#b1) |
| "O texto sumiu" / "só aparece a foto" | [B2](#b2), [B3](#b3) |
| "O menu está cortado" / "virou hamburguer no computador" | [B4](#b4) |
| "O botão está sem cor" | [B5](#b5) |
| "Esse texto passa da linha" | [B6](#b6) |
| "No celular está sobrepondo" | [B7](#b7) |
| "Está mal distribuído" / "sobrou vazio" | [B8](#b8) |
| "Pedi pra subir mais e ficou pior" | [B9](#b9) |
| "Não mudou nada" (depois de você publicar) | [B10](#b10) |
| "A fonte está diferente" | [B11](#b11) |
| "O mapa está em branco" | [B12](#b12) |
| A foto corta mal, proporção estranha | [B3](#b3) |
| O preview trava ou dá screenshot preto | [B13](#b13) |
| A seção nova ficou "apertada" perto das outras | [B14](#b14) |
| O botão de WhatsApp está na cor da marca, ou com texto | [B15](#b15) |

---

<a id="b1"></a>
## B1. "Está torto": desalinhamento horizontal do hero

**Causa:** hero full-bleed (fundo de borda a borda) com `padding-left` fixo, enquanto o
resto da página usa um trilho `max-width: 1200px; margin: 0 auto`. Em tela larga o hero fica
dezenas ou centenas de pixels à esquerda de tudo. Medido num caso real: 283px de diferença
em monitor de 1844px.

**Erro de diagnóstico que custou 4 rodadas:** ficar verificando "o texto está visível?"
quando a pergunta era "o título do hero começa na mesma coordenada X que os títulos das
seções?".

**Diagnóstico:** snippet 1 de [testes-medicao.md](testes-medicao.md).

**Correção:** manter o fundo full-bleed e alinhar o conteúdo ao trilho:

```css
#site-home .hero {
  padding-left:  max(64px, calc((100% - 1200px) / 2 + 64px));
  padding-right: max(64px, calc((100% - 1200px) / 2 + 64px));
}
```

Trocar 1200px e 64px pelos valores reais do projeto, por breakpoint.

---

<a id="b2"></a>
## B2. "O texto sumiu": hero mais alto que a janela

**Causa:** hero com `align-items: center` e altura maior que a viewport. O texto
centralizado cai abaixo da dobra.

**Diagnóstico:** snippet 4 de [testes-medicao.md](testes-medicao.md), numa janela **baixa**
(ex: 1844x720). Em janela alta o bug não aparece.

**Correção:** limitar a altura da foto com `calc(100vh - altura_do_header - folga)`.

---

<a id="b3"></a>
## B3. Foto gigante ou cortando mal

**Duas causas diferentes:**

**(a) `padding-top: X%` para dar proporção.** Porcentagem em padding é calculada sobre a
largura do **pai**, não do elemento. Caso real: foto com `max-width: 512px; height: 0;
padding-top: 125%` dentro de uma coluna de 866px virou 512x1075 em vez de 512x640. O hero
foi pra 1155px de altura e empurrou o texto pra fora da tela.

**(b) `height: 100%` na moldura.** A foto vira refém da altura do texto ao lado (via
`align-items: stretch`). Em telas onde o texto tem mais linhas, a moldura fica estreita e
alta, e a foto corta mal, mesmo com `max-height`.

**Diagnóstico:** snippet 8 de [testes-medicao.md](testes-medicao.md).

**Correção:** `aspect-ratio` fixo com `height: auto` e `max-height` só como teto, ou moldura
de altura limitada:

```css
#site-home .hero-media { display: flex; align-items: center; justify-content: flex-end; }
#site-home .hero-media-frame {
  height: min(560px, calc(100vh - var(--header-h) - 120px));
  width: min(100%, 448px);
  margin: 40px 0;
}
```

A imagem dentro fica `position: absolute; width: 100%; height: 100%; object-fit: cover`.

---

<a id="b4"></a>
## B4. Menu cortado, ou hamburguer aparecendo no desktop

**Causa:** o menu precisa de mais largura do que o trilho oferece. Ou o breakpoint do
hamburguer está calibrado alto demais.

Menu virando hamburguer em tela grande é **sempre bug**, nunca comportamento esperado.

**Diagnóstico:** snippet 2 de [testes-medicao.md](testes-medicao.md), em 1280 e 1440.
Não confiar em screenshot de navegador headless: alguns ambientes têm largura mínima de
janela (cerca de 500px no Chrome headless em Mac) e renderizam a página larga mesmo quando
você pede uma janela menor, escondendo overflow real de mobile.

**Correção:** compactar tudo de uma vez (altura do logo, fonte do menu, gap dos itens, gap
do container, padding do botão). Caso real: header precisava de 1304px e o trilho oferecia
1072px; foi preciso ir de logo 32px para 24px, fonte 11px para 9,5px, gap 14px para 9px,
gap do container 16px para 10px, botão 12px para 11px.

**Armadilha:** essas regras de compactação **não podem ficar fora de media query**, senão o
logo do celular encolhe junto. Elas valem só a partir da largura em que o menu horizontal
completo aparece (achar onde o `nav` deixa de ser `display: none`).

---

<a id="b5"></a>
## B5. Botão sem cor (o bug número 1 desta skill)

**Sintoma:** o botão virou texto puro, sem fundo. Nenhum teste por código detecta: o
elemento existe, o texto está certo, o `href` está certo.

**Causa:** especificidade. Um reset por ID vence uma regra de classe simples:

```css
#site-home button { background: none; }   /* ID + elemento: vence */
.btn-verde { background: green; }          /* classe: perde, em silêncio */
```

Também acontece com `#site-home img { display: block }` sobrescrevendo `.algo { display: none }`.

Variante comum: a classe base de botão (`.btn`) só tem estrutura (ícone, gap, fonte), e a
cor vem de uma variante (`.btn-hero`). Copiar só a classe base pras seções novas produz
exatamente esse bug.

**Correção:** toda variante aplicada a `button`, `img` ou `a` escrita com o prefixo do ID:

```css
#site-home .btn-section { background: var(--cor-destaque); color: #fff; }
```

E **conferir visualmente**. Este bug não é pego por JS/DOM.

---

<a id="b6"></a>
## B6. Texto vazando pra dentro da coluna vizinha

Ver [respiro-e-distribuicao.md](respiro-e-distribuicao.md) seção 4.1.

Resumo: `.section-head` com `max-width` fixo maior que a coluna do grid abaixo.
Correção: `max-width: calc(50% - gap/2)` dentro do breakpoint do grid.

---

<a id="b7"></a>
## B7. Sobreposição no celular

Ver [respiro-e-distribuicao.md](respiro-e-distribuicao.md) seção 4.2.

Resumo: `margin-top` negativo sem media query. No celular o grid empilha e a margem negativa
puxa a foto pra cima do bloco anterior. Correção: embrulhar no mesmo
`@media (min-width: ...)` do grid, e sempre testar em 375px.

---

<a id="b8"></a>
## B8. "Mal distribuído", vazio embaixo de uma coluna

Ver [respiro-e-distribuicao.md](respiro-e-distribuicao.md) seção 4.3.

Resumo: `align-items` do grid. Não é escolha fixa por seção, muda toda vez que o conteúdo de
alguma coluna muda.

---

<a id="b9"></a>
## B9. "Pedi pra subir mais e ficou pior"

Ver [respiro-e-distribuicao.md](respiro-e-distribuicao.md) seção 4.4.

Resumo: aumentar margem negativa no escuro, sem medir a folga real. Correção: medir a cada
aumento (snippet 6), e quando a folga chegar a zero, abrir espaço reduzindo o respiro do
vizinho em vez de forçar sobreposição.

---

<a id="b10"></a>
## B10. "Não mudou nada" depois de você publicar

**Causa provável 1: versão fixada (pinned).** O artifact pode servir uma versão antiga a
quem abre o link, mesmo você publicando versões novas.

**Detectar:** rodar `action: "read"` no artifact e ler o cabeçalho da resposta; se citar
versão fixada, é isso.
**Confirmar:** comparar um texto específico (o H1) entre o que o usuário descreve e o que
está no arquivo publicado.
**Corrigir:** publicar num artifact novo (arquivo com caminho novo, sem passar `url`).

**Causa provável 2: cache do navegador do usuário.** Pedir hard refresh
(Ctrl+Shift+R / Cmd+Shift+R) antes de investigar.

**Causa provável 3: você publicou o arquivo errado.** Quando há arquivo de trabalho e
arquivo de publicação separados, é fácil regenerar um e publicar o outro. Conferir a data de
modificação dos dois.

---

<a id="b11"></a>
## B11. Fonte diferente do combinado

**Causa:** o `<link>` do Google Fonts sumiu na conversão pro formato do Artifact. O CSS
continua pedindo a fonte e o navegador cai no fallback **sem nenhum erro**.

Variante: `@import` de fonte que não é a **primeira** regra do bloco `<style>`. O navegador
ignora silenciosamente.

**Diagnóstico:** `grep -c "fonts.googleapis" arquivo.html` e snippet 11 de
[testes-medicao.md](testes-medicao.md).

---

<a id="b12"></a>
## B12. Mapa do Google em branco

**Não é bug.** A prévia do Artifact bloqueia iframe de outros sites por política de
segurança. No WordPress/site final funciona normal. Avisar o usuário.

**Bug de verdade relacionado:** montar a URL do embed com `.replace(" ", "+")` manual.
Endereço com acento ("Vila Olímpia") vira URL inválida. Usar encode de verdade:

```python
from urllib.parse import quote
url = f'https://www.google.com/maps?q={quote(endereco)}&output=embed'
```

---

<a id="b13"></a>
## B13. Preview trava ou dá screenshot preto ao rolar

**Causa:** peso da página. Várias fotos em base64 mais 10+ seções. A ferramenta de scroll,
`scroll_to` e `window.scrollTo` travam igual: o problema não é a ferramenta.

**Correção:** parar de tentar rolar a página inteira. Usar
[recorte-secoes.py](recorte-secoes.py) pra gerar um arquivo por seção
(`#wrapper + <style> + só aquela seção`). Cada um cabe na tela sem scroll. Testar um por um.

---

<a id="b14"></a>
## B14. Seção nova "apertada" perto das outras

**Causa:** padrão de layout reaproveitado sem a escala de respiro que vem junto com ele.

Ver [respiro-e-distribuicao.md](respiro-e-distribuicao.md) seção 3. Layout e respiro são um
pacote só.

---

<a id="b15"></a>
## B15. Botão de WhatsApp fora do padrão

**Sintoma:** o botão flutuante saiu pintado com a cor da marca (bege, marrom, azul), ou
virou uma pílula com frase do tipo "Informações e agendamento" em vez de círculo com ícone.

**Causa:** as regras do botão ficaram só no arquivo de referência, que é aberto sob demanda.
Quando a sessão não abre, ela improvisa e "harmoniza" o botão com a paleta da página, o que
parece bonito e está errado.

**Por que é erro:** o verde do WhatsApp é o que faz a pessoa reconhecer o botão sem ler
nada. Pintado da cor da marca, ele vira mais um botão redondo na página. E a pílula com
texto compete com o CTA da seção, além de ocupar espaço no celular.

**Correção:** aplicar as 4 regras fixas do SKILL.md seção 5 (verde `#25D366` ou `#2AAE5F`,
círculo sem texto, ícone oficial em SVG, 58px no desktop e 54px no celular). Código pronto
em [whatsapp-botao.md](whatsapp-botao.md).

**Diagnóstico:** snippet 12 de [testes-medicao.md](testes-medicao.md), que devolve
`verde` e `semTexto`.

---

## Regra geral de diagnóstico

1. Traduzir a frase do usuário em uma **grandeza mensurável** ("está torto" → coordenada X).
2. Medir (snippets de [testes-medicao.md](testes-medicao.md)).
3. Só então mexer no CSS.
4. Medir de novo, com o número anterior e o novo lado a lado.
5. Só então dizer que corrigiu.

Pular o passo 1 é o que gera as rodadas de correção errada.
