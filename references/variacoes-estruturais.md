# Variações estruturais: não entregar a mesma página com outra roupa

O risco número 1 de usar uma skill para vários clientes: trocar cor e fonte, manter tudo o
resto, e entregar a mesma página duas vezes. O cliente percebe. Quem vê os dois sites
percebe mais ainda.

Trocar a paleta **não** conta como página diferente. O que precisa mudar é o **esqueleto**.

---

## 1. O teste da frase

Antes de montar a Fase 2, descreva a página em uma frase, só com estrutura, sem cor:

> "Hero com foto à direita, depois faixas empilhadas de largura cheia, cada uma com título,
> parágrafo, lista e botão."

Agora leia essa frase pensando no último site que você (ou a skill) entregou. **Se a frase
serve para os dois, o esqueleto é o mesmo e precisa mudar.**

Foi exatamente isso que aconteceu num caso real: dois sites, paletas totalmente diferentes,
e a mesma frase descrevia os dois.

## 2. Esqueleto: as 5 decisões que definem a página

Escolha uma opção de cada linha **antes** de desenhar. Combinações diferentes dão páginas
que não se parecem, mesmo com os mesmos blocos internos.

| Decisão | Opções |
| --- | --- |
| **Ritmo das seções** | faixas empilhadas de largura cheia / cards flutuantes sobre um fundo contínuo / seções com fundo alternado / blocos que se sobrepõem nas bordas |
| **Eixo de leitura** | tudo centralizado / tudo à esquerda com margem larga à direita / zig-zag (texto e foto trocam de lado a cada seção) / assimétrico fixo (texto sempre 40%, mídia 60%) |
| **Navegação** | header fixo com menu / header que some ao rolar / índice lateral fixo (sticky) com as seções / sem menu, só o botão de contato |
| **Papel da foto** | foto emoldurada dentro da seção / foto sangrando até a borda da tela / foto de fundo com texto por cima / poucas fotos, muito espaço em branco |
| **Marcação de seção** | título grande / eyebrow curto acima do título / numeração lateral (01, 02, 03) / linha divisória com rótulo |

Anote as 5 escolhas no início do projeto e siga elas. Duas páginas com 5 escolhas diferentes
não se parecem, mesmo usando os mesmos componentes.

## 3. Banco de variações por seção

Cada seção tem mais de um jeito de existir. Escolha por seção, não por hábito.

### Hero

1. Foto grande à direita, texto à esquerda (o mais comum, e por isso o mais gasto)
2. Foto sangrando em tela cheia, texto sobreposto num canto
3. Sem foto: só tipografia grande, nome e especialidade ocupando a tela
4. Foto pequena e circular ao lado do nome, hero curto e direto ao CTA
5. Duas colunas invertidas: foto à esquerda, texto à direita
6. Hero dividido na diagonal, cor de um lado e foto do outro

### Condições tratadas / o que trata

1. Chips em pílula, todos no mesmo bloco
2. Grade de cards, um por grupo de condições, com uma linha de descrição
3. Duas ou três colunas de lista simples com marcador
4. Acordeão por grupo (endócrino, metabólico, hormonal), aberto o primeiro
5. Lista numerada em coluna única, com bastante respiro entre itens
6. Nuvem de tamanhos: as condições mais buscadas em corpo maior

### Sobre o profissional

1. Foto à esquerda, texto à direita
2. Texto em coluna única centralizada, foto acima
3. Linha do tempo da formação (ano + instituição)
4. Texto corrido com uma citação em destaque no meio
5. Cartão de credenciais (formação, títulos, tempo de atuação) ao lado do texto

### A clínica

1. Carrossel de fotos
2. Mosaico de 3 fotos em tamanhos diferentes
3. Foto única grande sangrando na borda
4. Duas fotos lado a lado com legenda curta em cada

### Como funciona o atendimento

1. Timeline vertical com linha ligando os passos
2. Grade de cards numerados
3. Passos horizontais com seta entre eles (vira coluna no celular)
4. Lista simples numerada, sem card e sem círculo
5. Acordeão: cada passo abre com o detalhe

### FAQ

1. Acordeão simples, uma coluna
2. Acordeão em cards com sombra
3. Duas colunas de perguntas curtas
4. Perguntas sempre abertas, sem acordeão, em blocos separados

### Localização

1. Mapa à direita, endereço e horário à esquerda
2. Mapa de largura cheia, dados abaixo em três colunas
3. Mapa acima, dados abaixo em coluna única centralizada
4. Sem mapa: só endereço, referências de acesso e botão "como chegar"

### CTA final

1. Faixa de cor cheia com uma frase e um botão
2. Card centralizado sobre fundo claro
3. Bloco com foto de fundo e texto por cima
4. Só uma linha de texto e o botão, sem caixa nenhuma

## 4. Regras de diversidade

**Entre projetos:**
- Nunca repetir a mesma combinação de 5 escolhas do esqueleto (seção 2) do projeto anterior.
- Se o usuário já fez outro site com esta skill, peça um print ou o link **antes da Fase 1**
  e escolha um esqueleto diferente daquele. Uma pergunta, resolve o problema inteiro.
- A ordem das seções também conta: mudar quais seções existem e em que sequência já muda
  muito a sensação da página.

**Dentro do mesmo projeto:**
- Não usar o mesmo tratamento de bloco em mais de **duas** seções da página. Se três seções
  seguidas são "título centralizado, texto, chips, botão", a página fica monótona.
- Seções vizinhas nunca com o mesmo tratamento. Alternar: uma centralizada, a próxima em
  duas colunas, a seguinte em cards.

**Na Fase 1:**
- As 3 direções precisam divergir em **esqueleto**, não só em cor e tipografia. Se as três
  são "hero com foto à direita" mudando só a paleta, não são 3 direções, são 1 direção
  pintada de três jeitos.

## 5. O que continua igual entre projetos (e tudo bem)

Não é para reinventar tudo. Continuam padronizados:

- O trilho único e o CSS prefixado pelo wrapper
- A escala de respiro (o espaçamento é técnica, não identidade)
- **A formatação da seção de texto puro**: cabeçalho, corpo, lista e botão centralizados,
  nunca alinhados à esquerda com a metade direita vazia. Ver
  [respiro-e-distribuicao.md](respiro-e-distribuicao.md) seção 2b
- As correções de bug (alinhamento do hero, grid de duas colunas, especificidade)
- O botão de WhatsApp (verde, círculo, sem texto)
- O protocolo de teste

**Erro dos dois lados, no mesmo projeto:** copiar o esqueleto do cliente anterior (errado) e
não copiar a formatação de seção (também errado). É exatamente o contrário do que deve
acontecer.

A diferença: isso é **como o CSS funciona**. Esqueleto é **como a página parece**. O
primeiro se repete de propósito, o segundo nunca deve.
