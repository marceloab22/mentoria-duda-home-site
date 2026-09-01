# Glossário

Vocabulário usado nesta skill. Quem for usar ou adaptar precisa entender estas palavras,
porque elas aparecem nas instruções e nos pedidos do usuário.

---

**Base64.** Jeito de escrever uma imagem como texto, dentro do próprio HTML, sem arquivo
separado. Útil para a prévia (um arquivo só, funciona em qualquer lugar). Ruim para o site
final: infla o tamanho em cerca de 33% e o navegador não consegue cachear a imagem.

**Breakpoint.** A largura de tela em que o layout muda. Ex: `@media (min-width: 900px)`
significa "daqui pra cima, faça assim". Os desta skill: 700px (celular para tablet), 900px
(uma coluna para duas), 1200px (trilho cheio).

**Chip / pílula.** Item curto num retângulo de cantos bem arredondados, usado em lista de
condições, sintomas ou especialidades. Lê melhor que bullet quando são muitos itens curtos.

**Comparador.** Página com abas que mostra várias versões da mesma coisa lado a lado, pro
usuário escolher. Usado na Fase 1 (3 versões) e na regra do "não gostei" (6 versões).

**Copy.** O texto do site. "Copy aprovada" é o texto que o cliente já leu e autorizou. Nesta
skill, copy aprovada é intocável.

**CTA (call to action).** O botão ou frase que pede uma ação. Nesta skill, quase sempre
"falar no WhatsApp".

**Dobra.** A parte da página visível sem rolar. "Abaixo da dobra" = só aparece rolando.

**Especificidade.** A regra que decide qual CSS ganha quando duas regras brigam. Seletor com
ID (`#site-home button`) vence seletor de classe (`.btn`). Causa do bug número 1 desta skill
(botão sem cor).

**Fase 1 / Fase 2.** Fase 1: três direções visuais só do topo, pro usuário escolher o estilo.
Fase 2: a página completa no estilo escolhido.

**Full-bleed.** Elemento cujo fundo vai de borda a borda da tela, ignorando o trilho. O
conteúdo dentro dele ainda precisa alinhar com o trilho, e é aí que nasce o bug de "está
torto".

**Handoff.** A entrega: arquivo final, lista de pendências, tarefas de `<head>` e instruções
pra subir no ar.

**Hero.** O bloco de abertura da página, logo abaixo do cabeçalho: nome, especialidade, foto,
botão. É onde aparecem quase todos os bugs visuais desta skill.

**IIFE.** `(function(){ ... })();` Jeito de rodar JavaScript sem criar variável global, pra
não conflitar com o tema do WordPress.

**JSON-LD / schema.org.** Bloco de dados estruturados que explica pro Google que aquela
página é de um médico, com endereço e horário. Ajuda no resultado de busca local.

**NAP.** Nome, Address (endereço), Phone (telefone). Precisam estar escritos exatamente
iguais no site e no Google Business Profile, senão atrapalha SEO local.

**Pendência (`.pending`).** Marca visual discreta para informação que o cliente ainda não
mandou. Fica no site em itálico com opacidade reduzida ("a confirmar com a clínica") e é
listada na entrega. Melhor que inventar e melhor que deixar buraco.

**Respiro.** Espaçamento vertical entre os blocos de uma seção. Ver
[respiro-e-distribuicao.md](respiro-e-distribuicao.md).

**RQE.** Registro de Qualificação de Especialista. Número que autoriza o médico a anunciar
uma especialidade. Sem RQE, não se anuncia a especialidade.

**Token.** Variável de cor ou fonte no CSS (`--cor-destaque: #2AAE5F`). Toda seção usa o
token, nunca o hex direto, pra mudar tudo num lugar só.

**Trilho (container).** A faixa central onde o conteúdo vive, com largura máxima e padding
iguais em toda a página (ex: `max-width: 1200px; margin: 0 auto; padding: 0 64px`). Header,
hero e todas as seções precisam usar o **mesmo** trilho, senão nada alinha.

**Wrapper.** A `<div>` que embrulha a página inteira (`<div id="site-home">`), e cujo id
prefixa todo o CSS. Serve pra não vazar estilo pro tema do site e não sofrer interferência
dele.
