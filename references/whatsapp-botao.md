# Botão de WhatsApp (padrão testado)

## O ícone (SVG oficial, viewBox 24x24)

```html
<svg viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" aria-hidden="true">
<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/>
</svg>
```

## Montar a URL

```python
from urllib.parse import quote
numero = "5511999999999"      # DDI + DDD + numero, só digitos
nome   = "Fulano"              # nome que a logo/site usa, sem CRM/especialidade
trato  = "o Dr."                # ou "a Dra." conforme o caso
msg = f"Olá, tudo bem? Vim pelo site e gostaria de mais informações sobre a consulta com {trato} {nome}"
url = f"https://wa.me/{numero}?text={quote(msg)}"
```

## Botão flutuante (padrão testado nesta skill)

Círculo verde no canto da tela, sem balão de convite por padrão (só adicionar balão se o
usuário pedir explicitamente). Cor: verde oficial do WhatsApp `#25D366` (ou uma variante
próxima, ex: `#2AAE5F` com hover `#249752`, se o usuário indicar outra referência).

```html
<a class="float-wa" href="https://wa.me/NUMERO?text=MENSAGEM_CODIFICADA"
   target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
  <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/>
  </svg>
</a>
```

Prefixar com o id do wrapper: sem isso, um reset do tipo `#site-home a { color: inherit }`
vence e o botão sai errado, em silêncio (ver [troubleshooting.md](troubleshooting.md) B5).

```css
#site-home .float-wa {
  position: fixed; right: 26px; bottom: 26px; z-index: 60;
  width: 58px; height: 58px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  background: #2AAE5F; color: #fff;
  box-shadow: rgba(42,174,95,.6) 0 12px 30px -8px;
  transition: transform .18s, background .18s;
}
#site-home .float-wa:hover { background: #249752; transform: scale(1.06); }
#site-home .float-wa:focus-visible { outline: 3px solid #fff; outline-offset: 3px; }
@media (max-width: 640px) {
  #site-home .float-wa { width: 54px; height: 54px; right: 16px; bottom: 16px; }
}
@media (prefers-reduced-motion: reduce) {
  #site-home .float-wa { transition: none; }
}
```

Tamanho: 54px é o mínimo confortável no celular (acima dos 44px de alvo de toque). Se o
usuário pedir "aumenta o botão", 72px a 76px é o teto antes de virar estorvo na tela.

## Botão de texto (dentro da página, ex: no header ou numa seção de CTA)

```html
<a class="btn-wa" href="https://wa.me/NUMERO?text=MENSAGEM_CODIFICADA"
   target="_blank" rel="noopener">
  <svg viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" aria-hidden="true">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/>
  </svg>
  Agendar pelo WhatsApp
</a>
```

```css
#site-home .btn-wa { display: inline-flex; align-items: center; gap: .5em; }
#site-home .btn-wa svg { flex-shrink: 0; }
```

A classe base costuma ter só estrutura, sem cor de fundo. A cor vem de uma variante
(`.btn-section`, ver [fase2-componentes.md](fase2-componentes.md)). Copiar só a base pros
CTAs das seções novas produz botão sem cor, e nenhum teste por código pega isso.

## Se o usuário pedir pra copiar o botão de outro site

Medir o valor real no site indicado (cor exata, formato, sombra) em vez de estimar de olho.
Se tiver acesso a ferramenta de navegador com inspeção, ler `getComputedStyle()` do elemento
real. Nunca aplicar a referência em nenhum site além do que o próprio usuário está pedindo
pra editar nesta conversa.

## Conferir antes de entregar

- [ ] número com DDI + DDD, só dígitos
- [ ] `text=` presente e codificado (`quote()`) em todos os links
- [ ] a mesma mensagem em todos os pontos do site
- [ ] "Dr." ou "Dra." resolvido, nunca "Dr(a)"
- [ ] todo botão com o ícone
- [ ] botão flutuante presente e não cobre o menu fixo nem outro elemento importante
