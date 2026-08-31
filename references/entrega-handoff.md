# Entrega e handoff

A página não está pronta quando está bonita. Está pronta quando o usuário consegue colocar
no ar sem voltar pra perguntar nada.

---

## 1. Checklist de fechamento

Rodar inteiro antes de dizer "está pronto". Se algum item não passar, dizer **qual**.

### Originalidade
- [ ] O sorteio do esqueleto foi feito e seguido, e as 5 escolhas foram escritas no chat
      (ver [variacoes-estruturais.md](variacoes-estruturais.md) seção 2)
- [ ] Nenhuma das 5 linhas foi trocada de volta para o padrão de sempre sem motivo real
- [ ] Nenhum tratamento de bloco se repete em mais de duas seções
- [ ] Seções vizinhas não usam o mesmo tratamento

### Conteúdo
- [ ] Toda a copy aprovada está na página, palavra por palavra
- [ ] Nenhum dado inventado (nome, endereço, horário, convênio, preço)
- [ ] Toda lacuna marcada com `.pending` e listada na entrega
- [ ] Toda moldura de foto vazia listada na entrega
- [ ] Zero travessão: `grep -c "—" arquivo.html` igual a 0

### Compliance
- [ ] Checklist de [compliance-cfm-lgpd.md](compliance-cfm-lgpd.md) inteiro

### Técnico
- [ ] Protocolo de teste de [testes-medicao.md](testes-medicao.md) passou
- [ ] Testado em 1280, 1440 e 1920 de largura
- [ ] Testado em 375px (celular)
- [ ] Testado em janela baixa (ex: 1844x720)
- [ ] Todos os links de WhatsApp com número, `text=` codificado e mesma mensagem
- [ ] Botão flutuante de WhatsApp: círculo **verde**, com ícone, **sem texto e sem balão**
      (ver [whatsapp-botao.md](whatsapp-botao.md); cor da marca no botão é erro)
- [ ] Todos os links externos com `target="_blank" rel="noopener"`
- [ ] Todas as âncoras do menu apontando para `id` que existe
- [ ] Endereço linkado para o Google Maps
- [ ] Nenhum `console.log` ou comentário de desenvolvimento sobrando

### SEO, acessibilidade, performance
- [ ] Checklist de [seo-acessibilidade.md](seo-acessibilidade.md) inteiro

---

## 2. O que entregar junto com o arquivo

Sempre estes quatro itens, mesmo que o usuário não peça:

**1. O link da prévia**, atualizado, o mesmo desde o início do refino.

**2. A lista de pendências**, curta e específica:
```
Pendências (informação que faltou):
- Duração da consulta
- Se tem estacionamento no prédio
- Lista atualizada de convênios
- Foto real da recepção (está com moldura vazia)
```

**3. A lista de tarefas de `<head>`** (que não cabem no HTML gerado):
```
Fazer no WordPress:
- title: "Dra. Marina Xavier, cardiologista em Vitória | Clínica X"
- meta description: (texto de 150 caracteres)
- imagem de compartilhamento (og:image) 1200x630
- favicon
```

**4. O que precisa de decisão do cliente**: banner de cookies (se houver rastreamento),
confirmação da lista de convênios.

---

## 3. Subir num WordPress

### Opção A: bloco de HTML puro (mais fiel, recomendada)

1. Criar a página no WordPress.
2. Escolher um template **em branco / full width**, sem título, sem sidebar. No Elementor:
   "Elementor Canvas". Em temas de bloco: um template sem cabeçalho e rodapé do tema, se a
   ideia é usar o header e o rodapé da página gerada.
3. Colar o HTML num bloco "HTML personalizado" (Gutenberg) ou num widget "HTML" (Elementor).
4. As fotos **não** vão como base64: subir na biblioteca de mídia e trocar cada `src` pela
   URL do WordPress.
5. Conferir se o tema não está injetando CSS por cima. O wrapper `#site-home` já protege a
   maior parte; se algo escapar, aumentar a especificidade em vez de usar `!important`.

### Opção B: reconstruir no construtor

Mais trabalhoso e quase sempre perde fidelidade de espaçamento. Só vale se o cliente
precisar editar o conteúdo sozinho com frequência.

### Cuidados comuns

- Editor visual do WordPress reescreve HTML colado. Usar sempre o bloco de **HTML
  personalizado**, nunca o editor de texto rico.
- Alguns temas definem `box-sizing` diferente. Adicionar no início do CSS:
  `#site-home, #site-home * { box-sizing: border-box; }`
- Plugin de cache e de otimização (minificação de CSS/JS, lazy load agressivo) pode quebrar
  a página. Se algo estranho aparecer só no site e não na prévia, limpar cache e testar com
  o plugin de otimização desligado.
- Se o header da página gerada for fixo, conferir se não briga com a barra de admin do
  WordPress (que aparece só pra quem está logado).

---

## 4. Depois da publicação

Entregar como lista curta pro cliente:

- [ ] Testar a página no celular do próprio cliente
- [ ] Clicar em todos os botões de WhatsApp e conferir se a mensagem abre certa
- [ ] Conferir se o endereço e o horário batem com o Google Business Profile
- [ ] Validar o JSON-LD em `search.google.com/test/rich-results`
- [ ] Enviar a URL para o Google Search Console
- [ ] Confirmar que o Analytics está registrando visita

---

## 5. Arquivos de trabalho

Manter numa pasta persistente do projeto, nunca só no scratchpad temporário (que pode ser
limpo entre sessões: já se perdeu trabalho assim).

Organização que funciona:

```
projeto-cliente/
  home-trabalho.html          arquivo mestre, com placeholders {{FOTO_1}}
  home-final.html             gerado, com fotos embutidas, pronto pra publicar
  imagens/
    hero-profissional.jpg
    clinica-recepcao.jpg
  comparadores/
    fase1-3versoes.html
    faq-6versoes.html
  briefing.md                 copy aprovada e dados, como vieram do usuário
  pendencias.md               o que falta
```

Regra: **toda edição acontece no arquivo mestre.** O arquivo final é sempre regenerado a
partir dele, nunca editado à mão. Editar os dois é o caminho mais rápido pra publicar a
versão errada.
