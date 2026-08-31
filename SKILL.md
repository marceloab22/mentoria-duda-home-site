---
name: mentoria-duda-home-site
description: "Use quando o usuário pedir para criar ou revisar a home (página única) de um site de profissional de saúde (médico, dentista, psicólogo, fisioterapeuta, clínica), em duas fases. Fase 1 gera 3 direções visuais diferentes (cabeçalho + hero + amostra da seção seguinte) para o usuário escolher o estilo; Fase 2 monta a página completa no estilo escolhido, testada e pronta para ir pro site. Não usa nenhuma base de dados interna: trabalha só com o que o usuário fornecer no chat. Começa sempre pedindo, uma coisa de cada vez e nesta ordem, antes de desenhar qualquer pixel: primeiro a copy da página, depois a identidade visual (cores e fontes), depois cada foto necessária individualmente."
---

# Home de site de profissional de saúde: visual em 2 fases

Skill portátil. Não depende de nenhum sistema, CRM, planilha ou memória interna.
Tudo que ela precisa vem do que o usuário escrever nesta conversa.

Ela existe porque montar uma home bonita é fácil e montar uma home **certa** é difícil:
o que trava são bugs de alinhamento invisíveis em screenshot, respiro inconsistente entre
seções, copy inventada sem querer, e regra de publicidade médica ignorada. Cada seção
abaixo é a resposta a um erro que já aconteceu de verdade.

---

## Mapa: o que ler e quando

Não leia tudo de uma vez. Abra a referência quando chegar naquele passo.

| Quando você estiver... | Abra |
| --- | --- |
| **Abrindo a conversa** | **"Abertura obrigatória" logo abaixo, antes de tudo** |
| Completando o briefing depois das 3 rodadas | [checklist-briefing.md](references/checklist-briefing.md) |
| Decidindo quais seções a home vai ter | [estrutura-home.md](references/estrutura-home.md) |
| **Escolhendo o esqueleto (antes da Fase 1)** | [variacoes-estruturais.md](references/variacoes-estruturais.md) |
| Escrevendo/revisando qualquer texto do site | [compliance-cfm-lgpd.md](references/compliance-cfm-lgpd.md) |
| Montando o hero (Fase 1) | [hero-armadilhas.md](references/hero-armadilhas.md) |
| Montando a prévia comparativa (3 ou 6 versões) | [comparador-template.html](references/comparador-template.html) + [comparador.py](references/comparador.py) |
| Montando as seções da Fase 2 | [fase2-componentes.md](references/fase2-componentes.md) |
| Ajustando espaçamento vertical ou duas colunas | [respiro-e-distribuicao.md](references/respiro-e-distribuicao.md) |
| Colocando botão de WhatsApp | [whatsapp-botao.md](references/whatsapp-botao.md) |
| Testando antes de publicar | [testes-medicao.md](references/testes-medicao.md) |
| Com um bug estranho na mão | [troubleshooting.md](references/troubleshooting.md) |
| Fechando SEO, acessibilidade e performance | [seo-acessibilidade.md](references/seo-acessibilidade.md) |
| Entregando pro cliente / subindo no WordPress | [entrega-handoff.md](references/entrega-handoff.md) |
| Sem entender uma palavra usada aqui | [glossario.md](references/glossario.md) |

Scripts prontos: [base64-embed.py](references/base64-embed.py) (embutir fotos no final),
[recorte-secoes.py](references/recorte-secoes.py) (testar seção por seção isolada),
[comparador.py](references/comparador.py) (montar a prévia de N versões).

---

## Abertura obrigatória: pedir uma coisa de cada vez

**Assim que esta skill for acionada, a PRIMEIRA resposta ao usuário é a rodada 1 abaixo.**
Não gerar HTML, não propor layout, não sugerir cores, não fazer pergunta solta sobre estilo
antes disso.

**Uma rodada por mensagem. Nunca as três juntas.** Pedir tudo de uma vez produz resposta
pela metade, e aí falta justamente o que ninguém percebeu que faltou. Peça, espere a
resposta, confirme o que chegou em uma linha, e só então peça a próxima.

Antes de mandar a rodada 1, cheque as dependências (seção 0). Se faltar alguma, o aviso vai
em **uma linha** no topo da mesma mensagem da rodada 1, não numa mensagem separada.

### Rodada 1: copy

Primeira mensagem da conversa. Só isso, mais nada:

> Vamos começar pela copy. Me manda o texto aprovado da página, seção por seção,
> exatamente como vai entrar no site.
>
> Se alguma parte ainda não estiver pronta, me diz qual: eu marco como pendente no lugar
> certo, em vez de inventar.

Quando a copy chegar: confirmar em uma linha quantas seções vieram e o que ficou pendente.
Aí sim, rodada 2.

### Rodada 2: identidade visual

> Agora a identidade visual. Preciso de:
>
> - as cores em hex (do manual de marca, do logo ou de um print, não de olho)
> - o nome exato da fonte de título e da fonte de corpo
> - o logo em duas versões: para fundo claro e para fundo escuro
>
> Se ainda não existe identidade definida, me avisa: nesse caso as 3 direções da Fase 1
> propõem paletas diferentes e você escolhe uma.

Quando chegar: confirmar as cores e fontes em uma linha. Aí sim, rodada 3.

### Rodada 3: fotos, uma por uma

Aqui a ordem importa: com a copy na mão, você **já sabe** quais blocos usam foto. Então
não peça "as fotos" no genérico.

1. Monte a lista de fotos que a página vai precisar, a partir da copy e da
   [estrutura-home.md](references/estrutura-home.md). Ex: retrato para o hero, fachada,
   recepção, sala de atendimento, foto do profissional para a seção "sobre".
2. Mostre a lista numerada pro usuário, com a finalidade de cada uma.
3. **Peça uma por vez**, na ordem da lista, esperando cada resposta:

> São 4 fotos pra essa página:
>
> 1. Retrato do profissional (hero)
> 2. Fachada do prédio
> 3. Recepção
> 4. Sala de atendimento
>
> Vamos pela primeira: me manda o retrato do profissional, o que for usar no topo da
> página. Boa resolução, foto real.

Depois de cada foto recebida: confirmar em uma linha e pedir a próxima pelo nome
("recebi o retrato. Agora a foto 2, a fachada").

Regras desta rodada:

- **Só foto real.** Banco de imagens e imagem gerada por IA de pessoa estão fora.
- **"Não tenho essa"**: registre como moldura vazia, siga para a próxima sem insistir, e
  inclua na lista de pendências da entrega.
- **Se o usuário mandar várias de uma vez**: aceite, confirme quais chegaram e peça só a
  próxima que faltou. Não repita o que já veio.
- Não avance para a Fase 1 antes de fechar a lista inteira (recebida ou marcada como
  pendente).
- **A lista de fotos pode mudar no passo 2.** Ela sai da copy, mas quem fecha a lista de
  seções é a arquitetura aprovada. Se o passo 2 criar um bloco novo com foto, volte e peça
  só as fotos novas, uma por uma, do mesmo jeito. Se o passo 2 cortar uma seção, avise que
  aquela foto não vai mais ser usada.

### Depois das 3 rodadas

Complete o que faltar com [checklist-briefing.md](references/checklist-briefing.md) (dados
de registro, contato, endereço, horário) e siga para o passo 2 do fluxo.

**Se o usuário disser "faz do seu jeito" ou "inventa aí"**, explique em uma linha que copy,
foto e cor inventadas quebram as regras 3, 4 e 5 abaixo, e ofereça a alternativa: montar a
Fase 1 com texto marcado como provisório e molduras vazias, para ele ver a estrutura antes
de mandar o conteúdo real.

**Se o usuário mandar tudo junto de uma vez, sem esperar as rodadas**: aproveite o que veio,
não peça de novo o que já chegou, e use as rodadas só para o que ficou faltando.

---

## 0. Dependências (checar antes de começar)

**Obrigatória:** uma forma de exibir HTML pro usuário ver. No Claude Code isso é a
ferramenta **Artifact**. Sem ela, entregue o HTML como arquivo e peça pro usuário abrir no
navegador.

**Opcionais, melhoram o resultado:**

- **Skill `frontend-design`** (plugin oficial `frontend-design` do marketplace
  `anthropics/claude-plugins-official`): dá o olhar de design (hierarquia, tipografia,
  espaçamento) ao gerar o HTML. Checar com `/plugin`, procurar "frontend-design" nos
  instalados. Instalar:
  ```
  /plugin marketplace add anthropics/claude-plugins-official
  /plugin install frontend-design@claude-plugins-official
  ```
- **Skill `artifact-design`**: nativa da ferramenta Artifact, carrega sozinha ao publicar.
- **Ferramenta `Workflow`** (múltiplos agentes em paralelo): só acelera a Fase 1 (3 versões
  ao mesmo tempo). Sem ela, gere em sequência com o mesmo prompt-base.
- **Ferramenta de navegador com inspeção** (Browser / Chrome MCP / DevTools): necessária
  pros testes numéricos da seção 7. Sem ela, você **não consegue** validar alinhamento e
  vai entregar bug. Avise o usuário se faltar.
- **Python 3** para os scripts de `references/`.

Se faltar algo, avise o que vai funcionar diferente **em uma linha, no topo da mensagem da
rodada 1** (nunca numa mensagem separada, que atrasaria o pedido da copy). Exemplo:
"não tenho Workflow aqui, vou gerar as 3 versões uma depois da outra, demora mais".

---

## 1. As 8 regras invioláveis

Se alguma dessas quebrar, o trabalho está errado mesmo que pareça bonito.

1. **Pedir copy, identidade visual e fotos antes de qualquer coisa, uma coisa de cada vez.**
   Primeiro a copy, depois a identidade visual, depois cada foto individualmente. Nunca os
   três no mesmo pedido. Ver a seção "Abertura obrigatória" acima.
2. **Nada de dado inventado.** Nome, especialidade, endereço, horário, telefone, preço,
   convênio: tudo vem do que o usuário escreveu nesta conversa. Faltou? Pergunte ou marque
   como pendente (seção 4). Nunca preencha com algo plausível.
3. **Copy exata.** Usar o texto aprovado palavra por palavra. Nunca reescrever, resumir ou
   "melhorar" por conta própria. Se precisar quebrar um parágrafo longo em blocos com
   subtítulo, use só palavras que já existem no texto aprovado.
4. **Só foto real.** Nunca banco de imagens, nunca imagem gerada por IA de pessoa. Faltou
   foto? Moldura vazia com legenda ("foto real da recepção, a confirmar").
5. **Cor e fonte nunca vêm de outro projeto, e o esqueleto também não.** Identidade visual
   (paleta, tipografia) sai sempre do briefing daquele cliente. E o **esqueleto** da página
   (ritmo das seções, eixo de leitura, papel da foto, navegação) precisa ser diferente do
   projeto anterior: trocar só a cor entrega a mesma página duas vezes, e o cliente percebe.
   O que se reaproveita entre projetos é só **como o CSS funciona**: trilho único, escala de
   respiro, correções de bug conhecidas, protocolo de teste. Ver
   [variacoes-estruturais.md](references/variacoes-estruturais.md).
6. **Zero travessão** (em-dash, `—`, U+2014) em qualquer texto gerado, no site e no chat.
   Use vírgula, ponto, dois-pontos, parênteses ou reescreva. Hífen normal (`-`) pode.
   Conferir antes de entregar: `grep -c "—" arquivo.html` tem que dar 0.
7. **Medir antes de afirmar que corrigiu.** Screenshot mostra que "tem texto na tela", não
   mostra que o texto está 283px fora do eixo. Toda correção de alinhamento, altura ou
   espaçamento se prova com número (`getBoundingClientRect()`), não com olho. Ver seção 7.
8. **Publicidade médica tem lei.** Antes de escrever ou aprovar qualquer texto, passar pelo
   filtro de [compliance-cfm-lgpd.md](references/compliance-cfm-lgpd.md). Promessa de
   resultado, antes/depois e preço de procedimento podem gerar processo ético pro cliente.

---

## 2. Fluxo de ponta a ponta

Sete passos. Não pular, não inverter. Marcar cada um como concluído antes do próximo.

| # | Passo | Entregável | Referência |
| --- | --- | --- | --- |
| 1 | Briefing | Copy, identidade visual e fotos na mão, pendências listadas | Abertura obrigatória + [checklist-briefing.md](references/checklist-briefing.md) |
| 2 | Arquitetura | Lista de seções aprovada pelo usuário | [estrutura-home.md](references/estrutura-home.md) |
| 3 | Fase 1 | 3 direções visuais num comparador | Seção 3 |
| 4 | Escolha | Usuário escolhe uma (ou mistura duas) | Seção 3 |
| 5 | Fase 2 | Página completa testada | Seção 4 |
| 6 | Refino | Rodadas de ajuste, regra das 6 versões | Seção 6 |
| 7 | Handoff | Arquivo final + lista de pendências + instruções | [entrega-handoff.md](references/entrega-handoff.md) |

**Passo 2 é o mais pulado e o que mais custa caro.** Antes de desenhar qualquer pixel,
mostre ao usuário a lista de seções na ordem e peça o "ok". Descobrir na Fase 2 que faltava
uma seção inteira significa refazer respiro e navegação.

---

## 3. Fase 1: 3 direções visuais

Objetivo: mostrar 3 estilos bem diferentes de **só** cabeçalho + hero + uma tira de amostra
(cerca de 220px) da seção seguinte. **Nunca a página inteira nesta fase.** É rápido de gerar
e rápido de decidir; a página completa só vem depois da escolha.

**Antes de gerar: escolher o esqueleto.** Cinco decisões (ritmo das seções, eixo de leitura,
navegação, papel da foto, marcação de seção) que definem como a página **parece**, separadas
da paleta. Escolher em [variacoes-estruturais.md](references/variacoes-estruturais.md) e
anotar as 5 escolhas.

Se o usuário já tem outro site feito com esta skill, **peça um print ou o link agora** e
escolha um esqueleto diferente daquele. É uma pergunta só, e é o que impede o segundo
cliente de receber a mesma página com outra cor.

**Teste da frase:** descreva a página em uma frase, só estrutura, sem cor ("hero com foto à
direita, depois faixas empilhadas com título, texto, lista e botão"). Se essa frase também
descreve o site anterior, o esqueleto não mudou. Refaça.

As 3 versões precisam divergir de verdade nestes 5 eixos (travar isso no prompt de cada
uma, ou nos 3 agentes do Workflow):

1. **Composição do hero**: foto em tela cheia / foto dividida ao meio / foto pequena
   emoldurada.
2. **Luminosidade**: fundo escuro / claro / bloco de cor da marca.
3. **Tipografia**: peso e estilo do título (serifada elegante / sem serifa firme / mista).
4. **Respiro**: mais espaçado vs. mais compacto.
5. **Alinhamento**: centralizado / à esquerda / assimétrico.

Se duas versões pudessem ser confundidas numa olhada rápida, elas não divergiram o
suficiente. Refaça. O mesmo vale se as três forem "hero com foto à direita" pintado de três
jeitos: isso é uma direção só, não três.

Cada versão é um HTML independente seguindo a estrutura técnica da seção 5.

**Montar a prévia comparativa**: use [comparador.py](references/comparador.py) com o
template [comparador-template.html](references/comparador-template.html). Ele gera abas
(Versão A/B/C) mais alternância Computador/Celular. Publicar com a ferramenta Artifact.

**Ao apresentar**, diga em uma linha o que diferencia cada versão. O usuário decide melhor
com "A é escura e centralizada, B é clara com foto ao lado, C é bloco de cor da marca" do
que com "escolhe uma".

---

## 4. Fase 2: página completa

Só começa depois da escolha. Monta todas as seções da copy aprovada, na estrutura técnica
da seção 5, com o estilo visual escolhido na Fase 1.

**Reaproveitar os tokens e componentes da Fase 1, não recriar do zero.** A Fase 1 já
definiu as variáveis de cor e fonte e componentes como `.btn`, `.card`, `.float-wa`. Toda
seção nova usa essas variáveis, nunca hex solto.

CSS pronto e testado dos blocos que toda home médica acaba precisando (cabeçalho de seção,
bullets, chips, passos numerados, FAQ, moldura vazia, rodapé, mapa) em
[fase2-componentes.md](references/fase2-componentes.md).

**Lacuna na copy: marcar, nunca inventar, nunca travar.** Quando o texto aprovado tiver
`[FALTA:]`, `[INFORMAÇÃO NÃO FORNECIDA]` ou simplesmente não cobrir um bloco, coloque no
lugar exato um texto curto tipo "a confirmar com a clínica" com uma classe discreta
(`.pending`, itálico + opacidade reduzida). Não pule a seção, não invente a resposta.
Depois de publicar, liste pro usuário, de forma curta, tudo que ficou pendente.

**O que NÃO vira pendência (ignorar em silêncio, mesmo se a copy pedir):**

- **Política de privacidade.** Não colocar bloco no rodapé, não marcar como pendente, não
  listar na entrega. Se a copy trouxer `[FALTA: link da política de privacidade]`, apague o
  trecho em vez de virar `.pending`.
- **Palavra-chave, SEO por seção, meta tag.** Se a copy vier com campos de palavra-chave
  principal/secundária por seção, use o texto e ignore os campos. Palavra-chave que não veio
  não é pendência: não perguntar, não listar.

Pendência é informação **do consultório** que falta (duração da consulta, estacionamento,
lista de convênios, foto). Item de configuração e de SEO não entra nessa lista.

**Ordem de trabalho dentro da Fase 2**: montar todas as seções com placeholders de imagem
(`{{FOTO_1}}`), testar seção por seção isolada, e só no fim trocar por base64 com
[base64-embed.py](references/base64-embed.py). Embutir base64 cedo entope o contexto da
conversa e deixa cada iteração lenta.

---

## 5. Estrutura técnica obrigatória do HTML

- Tudo dentro de um único wrapper, ex: `<div id="site-home">`.
- **Todo** CSS prefixado por esse wrapper (`#site-home .algo { ... }`), pra não vazar estilo
  pro resto do site nem sofrer interferência do tema do WordPress.
- **Escolha um prefixo de classe por projeto** e use sempre (ex: `mx-` para Dra. Marina
  Xavier: `.mx-btn`, `.mx-card`). Nesta documentação as classes aparecem sem prefixo por
  legibilidade.
- Um **trilho único** pro projeto inteiro: mesmo `max-width` e mesmo padding por breakpoint
  no header, no hero e em todas as seções. Ver
  [hero-armadilhas.md](references/hero-armadilhas.md) seções 1 e 2.
- **Sem** `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`: quem exibe já cuida disso. Consequência
  importante: `<title>`, `meta description` e schema.org **não** entram no HTML gerado, viram
  tarefa de handoff (ver [seo-acessibilidade.md](references/seo-acessibilidade.md)).
- JavaScript sempre dentro de uma IIFE: `(function(){ ... })();`. Nunca variável global.
- Nenhum recurso externo além de: Google Fonts, links `wa.me`, embed do Google Maps, embed
  do Instagram.
- Imagem grande fica como placeholder (`{{FOTO_1}}`) durante o desenvolvimento e só vira
  base64 no final.
- **Cuidado com especificidade.** Um reset por ID (`#site-home button { background: none }`)
  vence qualquer regra de classe simples (`.btn-verde { background: green }`) e o botão fica
  sem cor **sem nenhum erro aparecer**. Toda variante de componente aplicada a `button`,
  `img` ou `a` deve ser escrita com o mesmo prefixo de ID: `#site-home .btn-verde { ... }`.
  Esse é o bug número 1 desta skill, já apareceu 4 vezes.

### Botão flutuante de WhatsApp: 4 regras fixas

Não são preferência de estilo, são padrão do projeto. Valem já na Fase 1, porque o botão
aparece no primeiro print que o cliente vê. Código pronto em
[whatsapp-botao.md](references/whatsapp-botao.md).

1. **Verde do WhatsApp, sempre.** `#25D366` (ou `#2AAE5F` com hover `#249752`). **Nunca a
   cor da marca do cliente.** O verde é o que faz a pessoa reconhecer o botão sem ler nada;
   pintado de bege, marrom ou azul ele vira "mais um botão redondo" e perde clique. Se o
   cliente pedir a cor da marca, diga isso em uma linha e só troque se ele insistir.
2. **Círculo com o ícone, sem texto.** Nada de balão de convite, pílula com frase, ou
   "Informações e agendamento" escrito ao lado. Só o círculo com o ícone oficial. Balão só
   se o usuário pedir com essas palavras.
3. **Ícone oficial do WhatsApp**, em SVG, branco, dentro do círculo. Sem ícone genérico de
   telefone ou de balão de fala.
4. **Tamanho**: 58px no desktop, 54px no celular. Se o usuário pedir maior, 76px é o teto.

**O botão de texto é outra coisa, não confunda.** O CTA que fica dentro da página (header,
fim de seção, "Informações e agendamento") usa a **cor da marca**, não o verde: verde ali
brigaria com a paleta em cada seção. Mas ele **sempre leva o ícone do WhatsApp** ao lado do
texto, senão ninguém sabe pra onde o botão vai. Resumindo:

| Botão | Cor | Ícone | Texto |
| --- | --- | --- | --- |
| Flutuante (canto da tela) | verde do WhatsApp | sim | não |
| De seção / header | cor da marca | sim | sim |

Erro real: uma sessão entregou o flutuante marrom (devia ser verde) e os botões de texto
sem ícone nenhum (devia ter). Os dois casos passam despercebidos porque a página fica
bonita mesmo assim.

Erro real, aconteceu com esta skill: uma sessão entregou o botão pintado de marrom (a cor
da marca) numa versão e, na outra, uma pílula verde com a frase "Informações e agendamento"
dentro. As duas quebram as regras 1 e 2. Antes de publicar, olhe o botão e confirme: é um
círculo verde com o ícone e nada mais?

---

## 6. Regra das 6 versões: quando o usuário disser "não gostei"

Sempre que o usuário disser "não gostei disso", "ficou ruim", "está estranho" sobre um
elemento ou seção **já publicada**, sem detalhar exatamente qual mudança quer, a resposta é
gerar **6 versões diferentes só daquele elemento** (nunca a página inteira) num comparador
com abas, pro usuário escolher.

- **Não perguntar antes** se pode gerar as versões. Essa pergunta já está respondida aqui.
- **Não escolher uma sozinho** e publicar direto.
- **Mesma copy nas 6.** Só muda distribuição e layout, nunca o texto.
- **As 6 precisam divergir de verdade** entre si, não é a mesma coisa 6 vezes com detalhe
  cosmético diferente.
- Depois da escolha: aplicar no arquivo real, testar (seção 7), republicar e **reenviar o
  link**, mesmo que já tenha mandado antes.

**Respiro e alinhamento também entram nessa regra.** O usuário pode pedir 6 opções de
espaçamento vertical, ou reclamar de forma vaga do alinhamento. Como gerar essas variações,
os 6 eixos de respiro que funcionam, e a escala de referência já testada estão em
[respiro-e-distribuicao.md](references/respiro-e-distribuicao.md).

**Padrão aprovado vira padrão do projeto.** Depois que o usuário escolher um layout ou uma
escala de respiro, aplique direto nas outras seções com o mesmo problema, sem nova rodada
de 6. E aplique o **pacote completo**: layout e respiro andam juntos. Copiar só as classes
de layout e esquecer a escala de espaçamento entrega a seção com a "cara" errada e o usuário
percebe na hora. Isso já aconteceu e gerou reclamação direta.

---

## 7. Testar de verdade antes de publicar (obrigatório)

**Screenshot não serve pra julgar alinhamento nem altura.** Medir com
`getBoundingClientRect()` / `scrollWidth` e comparar números antes de dizer que corrigiu.
Snippets prontos de medição em [testes-medicao.md](references/testes-medicao.md).

Protocolo mínimo antes de qualquer publicação:

1. **Alinhamento horizontal**: coordenada X do título do hero, dos títulos de seção e do
   logo do header têm que dar o mesmo número. Testar em 1280, 1440, 1512, 1920.
2. **Menu do cabeçalho**: `scrollWidth > clientWidth` do menu tem que ser `false` em 1280 e
   1440. Menu virando hamburguer em desktop normal é sempre bug.
3. **Altura do hero**: não pode passar da altura da janela. Testar numa janela **baixa**
   (ex: 1844x720), não só alta.
4. **Mobile em 375px**: obrigatório em toda correção de posição de foto/mapa. Margem
   negativa que funciona em duas colunas vira sobreposição quando o grid empilha.
5. **Visual de cada seção**: teste isolado, não rolando a página inteira (ver abaixo).
6. **Fonte carregando**: `grep -c "fonts.googleapis" arquivo.html` maior que 0 se o CSS
   pedir fonte do Google.
7. **Zero travessão**: `grep -c "—" arquivo.html` igual a 0.

**Página pesada trava o preview ao rolar.** Com várias fotos em base64 e 10+ seções, alguns
ambientes travam ou tiram screenshot preto ao rolar (a ferramenta de scroll, `scroll_to` e
`window.scrollTo` travam igual: o problema é o peso da página, não a ferramenta). Solução:
pare de tentar rolar. Use [recorte-secoes.py](references/recorte-secoes.py) pra gerar um
arquivinho por seção (`#wrapper + <style> + só aquela seção`), cada um cabe na tela sem
scroll, e teste um por um.

Armadilhas específicas do hero (o campeão de bugs) em
[hero-armadilhas.md](references/hero-armadilhas.md). Catálogo completo de bugs já vistos,
com sintoma, diagnóstico e correção, em [troubleshooting.md](references/troubleshooting.md).

---

## 8. Armadilhas na hora de publicar

**Versão fixada (pinned): o usuário continua vendo uma versão antiga.** Um artifact pode
ficar com uma versão fixada para quem abre o link, então você publica versões novas e o link
serve a antiga.
- Sintoma: o usuário diz "não mudou nada" mesmo após hard refresh, e descreve conteúdo que
  não bate com o que você publicou.
- Detectar: rodar `action: "read"` no artifact e ler o cabeçalho. Se aparecer aviso de
  versão fixada, é isso.
- Confirmar: comparar um texto específico (o H1, por exemplo) entre o que o usuário descreve
  e o que está no arquivo publicado.
- Resolver: publicar num artifact novo (arquivo com caminho novo, sem passar `url`).

**O `<link>` do Google Fonts some na conversão pro formato do Artifact.** O CSS continua
pedindo a fonte e o navegador cai no fallback em silêncio, sem erro nenhum. Conferir sempre
com `grep -c "fonts.googleapis"`. Se o CSS usar `@import` de fonte, ele precisa ser a
**primeira** regra do bloco `<style>`, senão o navegador ignora.

**Mapa do Google não renderiza dentro da prévia do Artifact** (política de segurança bloqueia
iframe de outros sites). No site final funciona normal. Avisar o usuário: não é bug.

**Salvar em lugar que não some.** Arquivos de trabalho (versões HTML, fotos preparadas)
ficam numa pasta persistente do projeto, nunca só no scratchpad temporário, que pode ser
limpo entre sessões. Já se perdeu trabalho assim.

**Republicar sempre no mesmo link durante o refino.** O usuário não deve colecionar 12 links.
Um link por entrega, atualizado a cada rodada, reenviado a cada mudança.

---

## 9. Entrega e handoff

A página não está pronta quando está bonita. Está pronta quando o usuário consegue colocá-la
no ar. Checklist de fechamento, itens de `<head>` que ficaram de fora do HTML, como subir no
WordPress/Elementor, e o que passar pro cliente em
[entrega-handoff.md](references/entrega-handoff.md).

Sempre entregar junto: a **lista de pendências** (tudo marcado como `.pending`, toda moldura
de foto vazia, toda informação que ficou "a confirmar").

---

## 10. Honestidade sobre o que foi usado

Se o usuário perguntar quais skills ou ferramentas foram realmente usadas, responda com a
lista exata do que rodou **de fato** nesta conversa, não a lista do que estava planejado.
É fácil confundir as duas. Confira antes de responder.

Mesma regra para "está pronto?": só dizer que está pronto quando o protocolo de teste da
seção 7 passou. Se um item ficou de fora, dizer qual.

---

## 11. Limites conhecidos desta skill

Documentado para quem for usar ou adaptar:

- **É só home, página única.** Páginas internas (blog, cada especialidade, sobre) não estão
  cobertas. A técnica de componentes serve, o fluxo de 2 fases não.
- **Não faz formulário com backend.** O contato é WhatsApp e telefone. Formulário de lead
  precisa de decisão de LGPD e de destino do dado, fora do escopo.
- **Não gera imagem.** Toda foto vem do usuário.
- **Compliance é orientação, não parecer jurídico.** As regras de publicidade médica mudam;
  o texto final é responsabilidade do profissional e da assessoria dele.
- **Adaptar para outro nicho** (advogado, arquiteto, pet shop): o fluxo de 2 fases, o
  protocolo de teste, a regra das 6 versões e todos os componentes servem. O que troca é
  [compliance-cfm-lgpd.md](references/compliance-cfm-lgpd.md) (cada conselho tem regra
  própria: OAB, CAU, CRO, CRP) e [estrutura-home.md](references/estrutura-home.md).
