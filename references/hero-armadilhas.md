# Hero: armadilhas de alinhamento e altura

O hero é onde quase todo bug visual desta skill aparece. Tudo abaixo saiu de bug real, com
número medido. Ler antes de montar o hero da Fase 1 e antes de responder qualquer
"está torto" / "o texto sumiu" do cliente.

Os snippets de medição citados aqui estão prontos em
[testes-medicao.md](testes-medicao.md). Bugs de outras partes da página estão em
[troubleshooting.md](troubleshooting.md).

## 1. "Está torto" quase sempre é desalinhamento horizontal, não texto sumido

O erro de diagnóstico que custou 4 rodadas de correção errada: ficar verificando "o texto
está visível na tela?" quando a pergunta certa era "o texto do hero começa na MESMA
coordenada X que os títulos das outras seções?".

Toda página tem um trilho (container) do tipo
`max-width: 1200px; margin: 0 auto; padding: 0 64px`. Se o hero for full-bleed (fundo
sangrando de borda a borda) e receber padding fixo do tipo `padding-left: 64px`, em telas
largas ele fica dezenas ou centenas de pixels à esquerda de todo o resto. Num monitor de
1844px a diferença medida foi de 283px.

Correção sem precisar de wrapper novo no HTML, mantendo o fundo full-bleed:

```css
#site-home .hero {
  padding-left:  max(64px, calc((100% - 1200px) / 2 + 64px));
  padding-right: max(64px, calc((100% - 1200px) / 2 + 64px));
}
```

Trocar 1200px e 64px pelos valores reais do container do projeto. Usar o mesmo valor de
padding que as seções usam em cada breakpoint (ex: 56px entre 960 e 1199, 64px de 1200
pra cima).

Conferir com o teste de aceite numérico da seção 7 abaixo.

## 2. O header também conta

Se o header usar um container mais largo que o corpo (ex: header com max-width 1360 e
seções com 1200), o logo fica mais à esquerda que o título do hero e o botão fica mais à
direita que a foto. Medido: 116px de diferença de cada lado em 1440px.

Header, hero e seções devem usar o mesmo trilho.

### Quando o menu não cabe no trilho do corpo

Antes de encolher qualquer coisa, MEDIR o que o header precisa e o que ele tem:

```javascript
const i = document.querySelector('.header-inner');
const W = s => Math.round(document.querySelector(s).getBoundingClientRect().width);
JSON.stringify({
  precisa: W('.logo') + W('.nav') + W('.header-actions'),
  tem: 1200 - 2*64,   // trilho do corpo menos o padding
  corta: i.scrollWidth > i.clientWidth
})
```

Caso real: o header precisava de 1304px e o trilho de 1200 só oferece 1072px. Pra caber,
foi preciso compactar de uma vez: logo de 32px para 24px de altura, fonte do menu de 11px
para 9,5px, gap dos itens de 14px para 9px, gap do container de 16px para 10px, botão de
12px para 11px com padding menor.

A armadilha: essas regras de compactação NÃO podem ficar fora de media query, senão o logo
do celular encolhe junto. Elas valem só a partir da largura em que o menu horizontal
completo aparece. Descobrir essa largura procurando onde o nav deixa de ser `display: none`
(no caso real era `@media (min-width: 1240px)`) e usar exatamente esse breakpoint. O
alinhamento do container em si (`max-width` e `padding` do `.header-inner`) pode começar
antes, na largura em que o hero vira duas colunas.

Teste de aceite: o mesmo snippet de coordenada X da seção 7, com `logo`, `hero` e `secao`
dando o mesmo número, mais `corta` igual a `false`, medido em 1200, 1240, 1280, 1440, 1512,
1844, 1920 e 2560 (1200 e 1240 entram na lista porque é onde o menu completo aparece e o
aperto acontece).

## 3. Nunca usar `padding-top: X%` pra dar proporção a um bloco com `max-width`

Porcentagem em padding é calculada sobre a largura do CONTAINING BLOCK (o pai), não sobre a
largura final do elemento. Caso real: foto com `max-width: 512px; height: 0;
padding-top: 125%` dentro de uma coluna de grid de 866px virou uma foto de 512 de largura
por 1075 de altura (o esperado era 512x640). O hero ficou com 1155px de altura, empurrando
todo o texto pra fora da tela. O cliente via só a foto e um vazio ao lado, e reportava "o
texto sumiu".

Alternativa segura, sem `aspect-ratio` e sem porcentagem:

```css
#site-home .hero-media { display: flex; align-items: center; justify-content: flex-end; }
#site-home .hero-media-frame {
  height: min(560px, calc(100vh - var(--header-h) - 120px));
  width: min(100%, 448px);
  margin: 40px 0;
}
```

A imagem dentro fica `position: absolute; width: 100%; height: 100%; object-fit: cover`,
então não distorce mesmo quando a proporção varia um pouco entre telas.

## 4. A altura do hero nunca pode ultrapassar a altura da janela

Se o hero tiver `align-items: center` e ficar mais alto que a viewport, o texto
centralizado cai abaixo da dobra e o cliente jura que ele sumiu.

Sempre limitar a altura da foto com `calc(100vh - altura_do_header - folga)`. Testar numa
janela BAIXA (ex: 1844x720), não só numa alta: o bug só aparece em janela baixa e larga.

## 5. Foto refém da altura do texto (`height: 100%`)

Se a moldura da foto usa `height: 100%` (herdando a altura do bloco de texto ao lado, via
`align-items: stretch` no container flex), ela fica refém de quanto texto tem do outro
lado. Em telas onde o texto ocupa mais altura (mais linhas, ou o operador testou só 1-2
larguras), a moldura vira quase quadrada e a foto corta muito mal (sobra fundo vazio em
cima, corta braço embaixo), mesmo com `max-height` definido, porque o problema é a moldura
ficar **estreita e alta**, não só alta.

Correção: nunca depender de `height: 100%` do irmão pra moldura de foto. Usar
`aspect-ratio` fixo (ex: `4/5` pra retrato) com `height: auto` e um `max-height` só como
teto de segurança, ou a moldura de altura limitada da seção 3. O texto ao lado ganha seu
próprio `min-height` + `justify-content: center` pra ficar simétrico sem "puxar" a foto.

Teste: forçar o bloco de texto a ficar bem mais alto que o normal (via JS,
`minHeight = '900px'` por exemplo) e conferir que a proporção da moldura
(`getBoundingClientRect()`) não muda. Se mudar, ainda tem essa dependência escondida.

## 6. Texto e foto desalinhados verticalmente

Irmão do problema acima. Se o texto usa `justify-content: center` dentro de um bloco com
altura própria fixa (`min-height`) e a foto fica só com `align-items: flex-start` no
container pai, o texto centraliza dentro do *seu* espaço enquanto a foto fica colada no
topo do *dela*. Os dois ficam alinhados por lógicas diferentes, e o título acaba começando
bem mais abaixo que o topo da foto (visualmente "torto", mesmo cada bloco isolado parecendo
certo).

Correção: usar `align-items: center` no container pai do hero e deixar tanto o texto quanto
a foto na altura natural deles (sem `min-height` extra no texto), assim os dois ficam
centralizados **um em relação ao outro**, não cada um sozinho dentro do próprio espaço.

Teste: medir o centro vertical dos dois blocos via JS (`el.getBoundingClientRect()`,
conferir `top + height/2` igual nos dois) com o texto no tamanho normal e também
artificialmente maior (múltiplas linhas). Os dois centros devem bater sempre.

## 7. Teste de aceite: numérico, não visual

Confiar em screenshot pra julgar alinhamento é o erro. Screenshot mostra que "tem texto na
tela", ele não mostra que o texto está 283px fora do eixo. Sempre medir e comparar números
antes de dizer que está corrigido.

```javascript
const L = s => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().left) : null; };
JSON.stringify({
  hero:  L('#site-home .hero-title'),
  secao: L('#site-home section h2'),
  logo:  L('#site-home .logo')
})
```

Os três têm que dar o mesmo número. Rodar em 1024, 1280, 1440, 1512, 1844, 1920 e 2560 de
largura, e num tamanho de janela parecido com o do cliente, incluindo janela baixa (ver
seção 4).

Antes de dar o hero por pronto, rodar também os snippets 2, 3, 4, 7 e 8 de
[testes-medicao.md](testes-medicao.md).
