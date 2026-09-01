# Componentes da Fase 2 (CSS testado)

Blocos que toda home de profissional de saúde acaba precisando, além do header e do hero
que vieram da Fase 1.

**Como usar:** trocar `#site-home` pelo wrapper real do projeto e `--cor-*` / `--fonte-*`
pelos tokens definidos na Fase 1. Nunca hex solto. Todo bloco assume o wrapper único e o CSS
prefixado (SKILL.md seção 5).

Padrões de distribuição (chips, duas colunas, bloco centralizado, frase de destaque) estão
em [respiro-e-distribuicao.md](respiro-e-distribuicao.md). Aqui ficam os blocos estruturais.

---

## Tokens: o mínimo que todo projeto precisa

Definidos na Fase 1, usados em toda a Fase 2.

```css
#site-home {
  --cor-fundo:      #FFFFFF;
  --cor-superficie: #F7F5F2;   /* fundo alternado de seção, card */
  --cor-borda:      #E4DFD8;
  --cor-texto:      #2A2F3A;
  --cor-texto-fraco:#6B7280;
  --cor-destaque:   #9B4C2D;   /* cor da marca, usada em CTA e detalhe */
  --cor-escura:     #2A2F3A;   /* rodapé, seção escura */
  --fonte-display: 'NomeDaFonte', Georgia, serif;
  --fonte-corpo:   'NomeDaFonte', -apple-system, sans-serif;
  --header-h: 72px;
}
```

Alternar `--cor-fundo` e `--cor-superficie` entre seções vizinhas dá ritmo à página sem
precisar de linha divisória.

## Trilho e seção

O mesmo trilho no header, no hero e em toda seção. Isso é o que faz a página alinhar.

```css
#site-home .section-inner { max-width: 1200px; margin: 0 auto; padding: 64px 24px; }
@media (min-width: 700px)  { #site-home .section-inner { padding: 80px 56px; } }
@media (min-width: 1200px) { #site-home .section-inner { padding: 96px 64px; } }
```

## Cabeçalho de seção (título + subtítulo)

```css
#site-home .section-head { max-width: 640px; margin-bottom: 36px; }
#site-home .section-head h2 {
  font-family: var(--fonte-display);
  font-size: clamp(26px, 4vw, 36px);
  line-height: 1.2;
  text-wrap: balance;
}
#site-home .section-head p {
  margin-top: 14px; font-size: 15.5px; line-height: 1.6;
  color: var(--cor-texto-fraco);
}
```

Atenção: se este cabeçalho ficar acima de um grid de duas colunas, o `max-width: 640px` pode
vazar pra coluna vizinha. Ver [respiro-e-distribuicao.md](respiro-e-distribuicao.md) 4.1.

## Botão de seção (CTA no corpo da página)

A classe base de botão geralmente só tem estrutura, sem cor. Criar uma variante com fundo e
**escrevê-la com o prefixo do ID**, senão o reset `#site-home button { background: none }`
vence e o botão fica sem cor, em silêncio. É o bug número 1 desta skill.

```css
#site-home .btn-section {
  display: inline-flex; align-items: center; gap: .5em;
  margin-top: 32px;
  font-family: var(--fonte-corpo);
  font-size: 14.5px; font-weight: 600;
  padding: 14px 24px;
  background: var(--cor-destaque);
  color: #fff;
  border: none; border-radius: 100px;
  cursor: pointer; text-decoration: none;
  transition: background .18s, transform .18s;
}
#site-home .btn-section:hover { filter: brightness(.92); transform: translateY(-1px); }
#site-home .btn-section:focus-visible { outline: 2px solid var(--cor-destaque); outline-offset: 3px; }
```

## Lista de bullets (fatores, serviços, sintomas)

```css
#site-home .check-list { display: grid; gap: 14px; margin-top: 28px; }
@media (min-width: 700px) {
  #site-home .check-list { grid-template-columns: 1fr 1fr; gap: 16px 32px; }
}
#site-home .check-item {
  display: flex; gap: 12px; align-items: flex-start;
  font-size: 15px; line-height: 1.5;
}
#site-home .check-item::before {
  content: ""; flex-shrink: 0;
  width: 9px; height: 9px; margin-top: 7px;
  border-radius: 50%; background: var(--cor-destaque);
}
```

## Passos numerados (como funciona o atendimento)

Duas formas. Grid quando os passos são curtos e independentes; timeline quando a ordem
importa e o usuário precisa sentir a sequência.

### Grid

```css
#site-home .steps { display: grid; gap: 28px; margin-top: 8px; }
@media (min-width: 700px) {
  #site-home .steps { grid-template-columns: repeat(2, 1fr); gap: 32px 40px; }
}
#site-home .step { display: flex; gap: 16px; }
#site-home .step-num {
  flex-shrink: 0; width: 36px; height: 36px; border-radius: 50%;
  background: var(--cor-destaque); color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--fonte-display); font-size: 15px;
}
```

Número ímpar de passos deixa o último sozinho na linha. Isso é normal, não force um número
par só pra preencher.

### Timeline (linha vertical ligando os passos)

```css
#site-home .timeline {
  position: relative; padding-left: 56px;
  display: flex; flex-direction: column; gap: 36px; margin-top: 8px;
}
#site-home .timeline::before {
  content: ""; position: absolute; left: 19px; top: 20px; bottom: 20px;
  width: 2px; background: var(--cor-borda);
}
#site-home .timeline-item { position: relative; }
#site-home .timeline-num {
  position: absolute; left: -56px; top: 0;
  width: 40px; height: 40px; border-radius: 50%;
  background: var(--cor-destaque); color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--fonte-display); font-size: 15px;
}
```

## FAQ em acordeão (`<details>` nativo, sem JS)

Acessível de graça, diferente de acordeão feito à mão com `div` + JS.

```html
<details class="faq-item">
  <summary>Pergunta aqui?</summary>
  <p>Resposta aqui.</p>
</details>
```

```css
#site-home .faq-list { display: flex; flex-direction: column; gap: 12px; margin-top: 8px; }
#site-home .faq-item {
  background: var(--cor-superficie);
  border-radius: 6px;
  box-shadow: 0 4px 16px rgba(0,0,0,.06);
}
#site-home .faq-item summary {
  cursor: pointer; list-style: none;
  padding: 20px; font-weight: 700;
  display: flex; justify-content: space-between; align-items: center; gap: 16px;
}
#site-home .faq-item summary::-webkit-details-marker { display: none; }
#site-home .faq-item summary::after { content: "+"; font-size: 20px; flex-shrink: 0; }
#site-home .faq-item[open] summary::after { content: "\2013"; }
#site-home .faq-item p { padding: 0 20px 20px; line-height: 1.6; }
```

## Moldura de foto vazia (quando falta foto real)

Nunca preencher com banco de imagens. Moldura vazia com legenda é honesto e vira item da
lista de pendências.

```css
#site-home .photo-placeholder {
  aspect-ratio: 4/3;
  border: 1.5px dashed var(--cor-borda);
  display: flex; align-items: center; justify-content: center;
  text-align: center; padding: 20px;
  font-size: 12.5px; font-style: italic; opacity: .8;
  color: var(--cor-texto-fraco);
}
```
```html
<div class="photo-placeholder">Foto real da recepção<br>(a confirmar com a clínica)</div>
```

## Texto pendente (lacuna da copy)

```css
#site-home .pending { font-style: italic; opacity: .8; }
```
```html
<p class="pending">Duração da consulta a confirmar.</p>
```

## Carrossel de fotos

Para quando há 2 ou mais fotos do mesmo ambiente e empilhar esticaria a seção.

```html
<div class="carousel" data-index="0">
  <div class="carousel-track">
    <img src="{{FOTO_2}}" alt="Recepção da clínica" width="800" height="600">
    <img src="{{FOTO_3}}" alt="Sala de atendimento" width="800" height="600">
  </div>
  <button class="carousel-prev" aria-label="Foto anterior">&#8249;</button>
  <button class="carousel-next" aria-label="Próxima foto">&#8250;</button>
</div>
```

```css
#site-home .carousel { position: relative; overflow: hidden; border-radius: 8px; }
#site-home .carousel-track { display: flex; transition: transform .35s ease; }
#site-home .carousel-track img { width: 100%; flex-shrink: 0; object-fit: cover; display: block; }
#site-home .carousel-prev,
#site-home .carousel-next {
  position: absolute; top: 50%; transform: translateY(-50%);
  width: 40px; height: 40px; border-radius: 50%;
  background: rgba(255,255,255,.9);   /* precisa do prefixo #site-home, ver bug B5 */
  border: none; cursor: pointer; font-size: 22px; line-height: 1;
  color: var(--cor-texto);
}
#site-home .carousel-prev { left: 12px; }
#site-home .carousel-next { right: 12px; }
@media (prefers-reduced-motion: reduce) { #site-home .carousel-track { transition: none; } }
```

```html
<script>
(function () {
  document.querySelectorAll('#site-home .carousel').forEach(function (c) {
    var track = c.querySelector('.carousel-track');
    var total = track.children.length;
    function go(delta) {
      var i = (parseInt(c.dataset.index, 10) + delta + total) % total;
      c.dataset.index = i;
      track.style.transform = 'translateX(' + (-i * 100) + '%)';
    }
    c.querySelector('.carousel-prev').addEventListener('click', function () { go(-1); });
    c.querySelector('.carousel-next').addEventListener('click', function () { go(1); });
  });
})();
</script>
```

Não girar sozinho. Carrossel automático é problema de acessibilidade e de leitura.

## Rodapé

```css
#site-home .footer { background: var(--cor-escura); color: var(--cor-superficie); }
#site-home .footer-inner { max-width: 1200px; margin: 0 auto; padding: 56px 24px 32px; }
#site-home .footer-top { display: flex; flex-direction: column; gap: 32px; }
@media (min-width: 700px) {
  #site-home .footer-top { flex-direction: row; justify-content: space-between; flex-wrap: wrap; }
}
#site-home .footer-col { font-size: 13.5px; line-height: 1.7; }
#site-home .footer a { color: inherit; }
#site-home .footer-bottom {
  margin-top: 40px; padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,.16);
  font-size: 12.5px; opacity: .7; text-align: center;
}
```

O rodapé precisa conter: nome, registro profissional com UF, RQE, CNPJ, endereço, telefone,
WhatsApp, Instagram, horário, diretor técnico (quando clínica) e link da política de
privacidade. Ver [compliance-cfm-lgpd.md](compliance-cfm-lgpd.md).

## Mapa do Google (embed por endereço, sem chave de API)

Só renderiza fora da prévia do Artifact (SKILL.md seção 8). Montar a URL com encode de
verdade, nunca substituição manual de caractere: endereço com acento vira URL inválida.

```python
from urllib.parse import quote
endereco = "Rua Exemplo, 123, Bairro, Cidade, CEP 00000-000"
url = f'https://www.google.com/maps?q={quote(endereco)}&output=embed'
```

```html
<div class="map-frame">
  <iframe src="URL_AQUI" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          title="Mapa da localização da clínica"></iframe>
</div>
```
```css
#site-home .map-frame { width: 100%; aspect-ratio: 4/3; border: 1px solid var(--cor-borda); }
#site-home .map-frame iframe { width: 100%; height: 100%; border: 0; display: block; }
```

Linkar também o endereço em texto para o Google Maps (link curto `maps.app.goo.gl`, que o
usuário pode gerar), em **todas** as ocorrências do endereço na página.

## Botão de voltar ao topo (opcional)

Só vale em página longa (10+ seções). Não pode brigar com o botão flutuante de WhatsApp:
colocar do lado oposto ou acima dele.

```css
#site-home .to-top {
  position: fixed; left: 26px; bottom: 26px; z-index: 59;
  width: 44px; height: 44px; border-radius: 50%;
  background: var(--cor-superficie); border: 1px solid var(--cor-borda);
  display: none; align-items: center; justify-content: center;
}
#site-home .to-top.is-visible { display: flex; }
```
