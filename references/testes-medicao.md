# Testes de medição: snippets prontos

Regra que vale pra tudo: **screenshot não prova alinhamento nem altura.** Ele mostra que
"tem texto na tela". Não mostra que o texto está 283px fora do eixo.

Rodar estes snippets no console da ferramenta de navegador. Todos devolvem JSON curto, sem
poluir o contexto da conversa.

Trocar `#site-home` e os nomes de classe pelos reais do projeto.

---

## 1. Alinhamento horizontal (o teste mais importante)

Os três valores têm que dar **o mesmo número**.

```javascript
const L = s => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().left) : null; };
JSON.stringify({
  logo:  L('#site-home .logo'),
  hero:  L('#site-home .hero-title'),
  secao: L('#site-home section h2'),
  larguraJanela: window.innerWidth
})
```

Rodar em 1024, 1280, 1440, 1512, 1844, 1920 e 2560 de largura.

## 2. Menu do cabeçalho cortando

`corta` tem que ser `false`. `precisa` maior que `tem` significa que o menu não cabe no
trilho.

```javascript
const W = s => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().width) : 0; };
const i = document.querySelector('#site-home .header-inner');
JSON.stringify({
  precisa: W('#site-home .logo') + W('#site-home .nav') + W('#site-home .header-actions'),
  tem: i.clientWidth,
  corta: i.scrollWidth > i.clientWidth,
  navVisivel: getComputedStyle(document.querySelector('#site-home .nav')).display !== 'none',
  larguraJanela: window.innerWidth
})
```

Em 1280 e 1440, `navVisivel` tem que ser `true` (menu completo, não hamburguer) e `corta`
tem que ser `false`.

## 3. Overflow horizontal da página inteira

Nada pode passar da largura da janela. Este snippet lista os culpados.

```javascript
JSON.stringify({
  paginaEstoura: document.documentElement.scrollWidth > window.innerWidth,
  culpados: [...document.querySelectorAll('#site-home *')]
    .filter(e => e.getBoundingClientRect().right > window.innerWidth + 1)
    .slice(0, 8)
    .map(e => e.className || e.tagName)
})
```

## 4. Altura do hero contra a janela

O hero não pode ser mais alto que a janela, senão o texto centralizado cai abaixo da dobra e
o usuário jura que "sumiu".

```javascript
const h = document.querySelector('#site-home .hero').getBoundingClientRect();
JSON.stringify({
  alturaHero: Math.round(h.height),
  alturaJanela: window.innerHeight,
  cabe: h.height <= window.innerHeight
})
```

Testar numa janela **baixa** (ex: 1844x720), não só alta. O bug só aparece em janela baixa e
larga.

## 5. Duas colunas: texto invadindo a coluna vizinha

`invade` tem que ser `false`.

```javascript
const a = document.querySelector('#site-home #secao-x .section-head').getBoundingClientRect();
const b = document.querySelector('#site-home #secao-x .coluna-direita').getBoundingClientRect();
JSON.stringify({
  textoTerminaEm: Math.round(a.right),
  colunaComecaEm: Math.round(b.left),
  invade: a.right > b.left
})
```

## 6. Folga entre dois blocos (antes de aumentar margem negativa)

Antes de aplicar mais um "sobe mais", medir. `folga` perto de zero significa teto físico.

```javascript
const cima  = document.querySelector('#site-home .bloco-de-cima').getBoundingClientRect();
const baixo = document.querySelector('#site-home .bloco-que-sobe').getBoundingClientRect();
JSON.stringify({ folga: Math.round(baixo.top - cima.bottom) })
```

## 7. Centro vertical de texto e foto no hero

Os dois centros têm que bater. Rodar também com o texto artificialmente maior.

```javascript
const c = s => { const r = document.querySelector(s).getBoundingClientRect(); return Math.round(r.top + r.height/2); };
JSON.stringify({ texto: c('#site-home .hero-text'), foto: c('#site-home .hero-media') })
```

## 8. Moldura de foto refém da altura do texto

Forçar o texto a ficar bem mais alto e conferir que a proporção da foto **não muda**.

```javascript
const foto = () => { const r = document.querySelector('#site-home .hero-media-frame').getBoundingClientRect(); return (r.width/r.height).toFixed(3); };
const antes = foto();
const t = document.querySelector('#site-home .hero-text');
const orig = t.style.minHeight;
t.style.minHeight = '900px';
const depois = foto();
t.style.minHeight = orig;
JSON.stringify({ antes, depois, ok: antes === depois })
```

`ok: false` significa que a moldura ainda depende da altura do irmão. Ver
[hero-armadilhas.md](hero-armadilhas.md) seção 5.

## 9. Contraste de cor

Retorna a razão de contraste de cada bloco de texto contra o fundo dele. Mínimo 4,5 para
texto normal, 3 para texto grande.

```javascript
function lum(c){const[r,g,b]=c.match(/\d+/g).map(Number).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*r+.7152*g+.0722*b}
function bg(el){let e=el;while(e){const c=getComputedStyle(e).backgroundColor;if(c&&c!=='rgba(0, 0, 0, 0)')return c;e=e.parentElement}return 'rgb(255,255,255)'}
JSON.stringify([...document.querySelectorAll('#site-home p, #site-home h1, #site-home h2, #site-home h3, #site-home a, #site-home li')]
  .slice(0,40)
  .map(e=>{const s=getComputedStyle(e);const l1=lum(s.color),l2=lum(bg(e));
    const r=((Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05));
    return {el:(e.className||e.tagName)+'', px:parseFloat(s.fontSize), ratio:+r.toFixed(2)}})
  .filter(x=>x.ratio < (x.px>=24?3:4.5)))
```

Lista vazia significa que passou. Qualquer item na lista é reprovação de contraste.

## 10. Alvo de toque no celular

Rodar com a janela em 375px. Lista vazia significa que passou.

```javascript
JSON.stringify([...document.querySelectorAll('#site-home a, #site-home button, #site-home summary')]
  .map(e=>{const r=e.getBoundingClientRect();return {el:(e.className||e.tagName)+'', w:Math.round(r.width), h:Math.round(r.height)}})
  .filter(x=>x.w && (x.w<44 || x.h<44)))
```

## 11. Fonte carregou de verdade

Se a fonte não carregar, o navegador cai no fallback **em silêncio**, sem erro nenhum.

```javascript
const f = getComputedStyle(document.querySelector('#site-home h1')).fontFamily;
JSON.stringify({
  fontFamilyCSS: f,
  carregou: document.fonts.check('16px "Fraunces"')
})
```

Trocar `Fraunces` pelo nome da fonte real. No terminal, conferir também:
`grep -c "fonts.googleapis" arquivo.html` (tem que ser maior que 0).

## 12. Checagens de terminal

```bash
grep -c "—" arquivo.html                  # travessão: tem que dar 0
grep -c "fonts.googleapis" arquivo.html   # fonte do Google: maior que 0
grep -c "<h1" arquivo.html                # tem que dar exatamente 1
grep -o 'alt=""' arquivo.html | wc -l     # alt vazio: só em imagem decorativa
grep -c "wa.me" arquivo.html              # links de WhatsApp presentes
```

---

## Protocolo mínimo antes de publicar

Rodar, na ordem: 1, 2, 3, 4, 11, 12. Depois, com a janela em 375px: 3, 10.
Depois de qualquer mexida em duas colunas: 5, 6. Depois de mexer no hero: 7, 8.
Antes do handoff: 9, mais o checklist de
[seo-acessibilidade.md](seo-acessibilidade.md).
