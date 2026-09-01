# SEO, acessibilidade e performance

Três coisas que não aparecem no screenshot e que o cliente só descobre depois, quando o site
não ranqueia, o paciente idoso não consegue ler, ou a página demora 8 segundos no celular.

Rodar este arquivo inteiro antes do handoff.

---

## 1. SEO: o que entra no HTML e o que vira tarefa de handoff

Esta skill gera HTML **sem** `<head>` (ver SKILL.md seção 5). Então os itens de `<head>`
não são feitos aqui, eles viram lista de tarefas na entrega.

### Fica no HTML gerado (responsabilidade desta skill)

- **Um único `<h1>`** na página, no hero, com nome + especialidade + cidade.
  Ex: `Dra. Marina Xavier, cardiologista em Vitória`.
- **Hierarquia de heading sem pular nível**: `h1` no hero, `h2` em cada seção, `h3` dentro
  das seções. Nunca escolher heading por tamanho de fonte; tamanho é CSS.
- **`alt` em toda imagem**, descritivo e específico. `alt="Dra. Marina Xavier em consultório"`
  e não `alt="foto"` nem `alt="imagem1"`. Imagem puramente decorativa: `alt=""`.
- **Texto de link com sentido próprio**: "ver como chegar" e não "clique aqui".
- **Endereço em HTML de verdade** (texto selecionável), não dentro de imagem.
- **NAP consistente**: nome, endereço e telefone escritos **exatamente** iguais ao Google
  Business Profile. Diferença de "Av." vs "Avenida" atrapalha SEO local.
- **Nome da cidade e do bairro no texto**, de forma natural, em pelo menos hero, seção de
  localização e rodapé.
- **Schema.org** (JSON-LD) pode entrar no corpo do HTML, funciona fora do `<head>`. Ver
  modelo abaixo.

### Vira tarefa de handoff (fazer no WordPress/CMS)

- `<title>`: 50 a 60 caracteres. Padrão que funciona:
  `Nome, especialidade em Cidade | Clínica`
- `meta description`: 140 a 155 caracteres, com o que o profissional faz e onde.
- `canonical` apontando pra URL final.
- Open Graph (`og:title`, `og:description`, `og:image`) pro link ficar bonito no WhatsApp.
  A imagem OG é a que aparece quando alguém compartilha: 1200x630px.
- Favicon.
- Sitemap e robots.txt.
- Google Search Console e Google Analytics.

### Schema.org: modelo para profissional de saúde

Cole no corpo do HTML, dentro do wrapper. Trocar todos os valores pelos reais. **Não
inventar campo nenhum**: se o dado não veio no briefing, remova a linha.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Physician",
  "name": "Dra. Marina Xavier",
  "medicalSpecialty": "Cardiovascular",
  "url": "https://exemplo.com.br",
  "image": "https://exemplo.com.br/foto.jpg",
  "telephone": "+5511999999999",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Exemplo, 123, sala 4",
    "addressLocality": "Vitória",
    "addressRegion": "ES",
    "postalCode": "29000-000",
    "addressCountry": "BR"
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }]
}
</script>
```

Tipos úteis conforme o caso: `Physician` (médico), `Dentist` (dentista), `Psychologist`,
`MedicalClinic` (clínica), `MedicalBusiness` (genérico). Para FAQ, `FAQPage` com
`mainEntity` costuma render trecho destacado na busca.

Validar em `search.google.com/test/rich-results` antes de entregar.

---

## 2. Acessibilidade

Público de site médico tem muita gente com 60+ anos e visão cansada. Acessibilidade aqui
não é conformidade burocrática, é conversão.

### Contraste

- Texto normal: mínimo **4,5:1** contra o fundo.
- Texto grande (acima de 24px, ou 19px em negrito): mínimo **3:1**.
- Elemento de interface (borda de botão, ícone): mínimo **3:1**.

Conferir cada par cor-de-texto / cor-de-fundo do projeto. Os que mais falham:
texto claro sobre foto, texto cinza claro em fundo bege, e botão de cor da marca com texto
branco quando a cor da marca é clara.

Medir, não olhar. Snippet em [testes-medicao.md](testes-medicao.md).

### Foco de teclado

Muita gente navega por Tab. O reset de CSS costuma apagar o contorno de foco e ninguém nota.

```css
#site-home a:focus-visible,
#site-home button:focus-visible,
#site-home summary:focus-visible {
  outline: 2px solid var(--cor-destaque);
  outline-offset: 3px;
  border-radius: 4px;
}
```

### Alvo de toque

Botão, link de menu e item de FAQ precisam de pelo menos **44x44px** de área clicável no
celular. Link de texto pequeno em rodapé é o campeão de reprovação.

### Semântica

- `<header>`, `<main>`, `<section>`, `<footer>` em vez de `<div>` para tudo.
- `aria-label` em qualquer botão que seja só ícone (`aria-label="Falar no WhatsApp"`).
- `aria-hidden="true"` em ícone decorativo dentro de botão que já tem texto.
- FAQ com `<details>`/`<summary>` nativo já é acessível de graça. Acordeão feito à mão com
  `div` + JS quase sempre não é.
- Se houver carrossel, ele precisa de botões reais (`<button>`) com `aria-label`, e não pode
  girar sozinho sem pausa.

### Movimento

```css
@media (prefers-reduced-motion: reduce) {
  #site-home * { animation: none !important; transition: none !important; }
}
```

### Zoom

A página tem que funcionar com zoom de 200% no navegador. Testar: nada pode sumir, cortar
ou sobrepor.

---

## 3. Performance

### Imagens

O maior peso de qualquer home de médico são as fotos.

- Redimensionar **antes** de embutir: lado maior de no máximo 1600px para foto de seção,
  2000px para foto de hero em tela cheia.
- JPEG qualidade 80 é indistinguível de 100 e pesa metade. Para logo e ícone, PNG ou SVG.
- Considerar WebP no site final (o construtor do WordPress costuma converter sozinho).
- **Base64 infla o arquivo em cerca de 33%.** Use base64 só para a prévia; no site final,
  arquivo de imagem de verdade.
- `loading="lazy"` em toda imagem abaixo da dobra. **Nunca** na foto do hero.
- `width` e `height` (ou `aspect-ratio` no CSS) em toda imagem, para o texto não pular
  enquanto a foto carrega.

```html
<img src="{{FOTO_2}}" alt="Recepção da clínica" width="800" height="600" loading="lazy">
```

### Fontes

- No máximo 2 famílias, no máximo 4 pesos no total. Cada peso é um download.
- `&display=swap` na URL do Google Fonts, senão o texto fica invisível enquanto carrega.
- Sempre declarar fallback real: `font-family: 'Fraunces', Georgia, serif`.

### Alvo

Numa conexão 4G comum, a página inteira deve carregar em menos de 3 segundos. Se a soma dos
arquivos passar de 2 MB, tem foto grande demais.

---

## 4. Checklist final

**SEO**
- [ ] Um único `<h1>`, com especialidade e cidade
- [ ] Hierarquia de heading sem pular nível
- [ ] `alt` descritivo em toda imagem
- [ ] Endereço e telefone em texto, batendo com o Google Business Profile
- [ ] Cidade e bairro citados no texto
- [ ] JSON-LD presente e validado
- [ ] Itens de `<head>` listados no handoff

**Acessibilidade**
- [ ] Contraste medido, todos os pares acima do mínimo
- [ ] `:focus-visible` visível em link, botão e summary
- [ ] Alvos de toque com 44px no celular
- [ ] `aria-label` em botão só de ícone
- [ ] Tags semânticas em vez de `div` para tudo
- [ ] `prefers-reduced-motion` respeitado
- [ ] Página funciona com zoom 200%

**Performance**
- [ ] Nenhuma imagem com lado maior acima de 2000px
- [ ] `loading="lazy"` abaixo da dobra, e não no hero
- [ ] `width`/`height` ou `aspect-ratio` em toda imagem
- [ ] No máximo 2 famílias de fonte, com `display=swap` e fallback
- [ ] Página inteira abaixo de 2 MB
