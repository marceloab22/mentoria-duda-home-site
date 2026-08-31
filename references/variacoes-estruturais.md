# Variações estruturais: não entregar a mesma página com outra roupa

O risco número 1 de usar uma skill para vários clientes: trocar cor e fonte, manter tudo o
resto, e entregar a mesma página duas vezes. O cliente percebe. Quem vê os dois sites
percebe mais ainda.

Trocar a paleta **não** conta como página diferente. O que precisa mudar é o **esqueleto**.

---

## 1. Por que isto existe

Uma skill não tem memória entre conversas. Cada projeto começa do zero, sem saber como
ficou o anterior. Sem regra nenhuma, todo Claude cai no mesmo desenho previsível (hero com
foto à direita, faixas empilhadas, tudo à esquerda) e dois clientes recebem a mesma página
com paletas diferentes. Aconteceu de verdade.

Não dá para resolver isso perguntando ao usuário "como ficou o site anterior": quem usa a
skill pode nunca ter feito nenhum, e não tem obrigação de saber disso.

A solução é o **sorteio da seção 2**: um número tirado do próprio nome do profissional
decide o esqueleto. É determinístico (o mesmo cliente sempre dá o mesmo resultado, então dá
para retomar o projeto depois) e diferente entre clientes, sem memória nenhuma.

## 2. O sorteio do esqueleto (fazer antes de desenhar)

**Passo 1: calcular S.** Escreva o nome do profissional sem "Dr."/"Dra.", sem espaço e sem
acento, em maiúsculas. Some a posição de cada letra no alfabeto (A=1, B=2, ... Z=26).

Exemplo: "Dra. Marina Xavier" → `MARINAXAVIER` →
13+1+18+9+14+1+24+1+22+9+5+18 = **S = 135**

**Passo 2: tirar as 5 decisões de S.** Cada linha usa um divisor diferente, então elas não
andam juntas. `÷` é divisão inteira (descarta o resto).

| # | Decisão | Conta | Opção 0 | Opção 1 | Opção 2 | Opção 3 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ritmo das seções | `S % 4` | faixas empilhadas de largura cheia | cards flutuantes sobre fundo contínuo | fundo alternado entre seções | blocos que se sobrepõem nas bordas |
| 2 | Eixo de leitura | `(S ÷ 2) % 4` | tudo centralizado | à esquerda com margem larga à direita | zig-zag (texto e mídia trocam de lado) | assimétrico fixo (texto 40%, mídia 60%) |
| 3 | Navegação | `(S ÷ 5) % 4` | header fixo com menu | header que some ao rolar | índice lateral fixo com as seções | sem menu, só o botão de contato |
| 4 | Papel da foto | `(S ÷ 7) % 4` | foto emoldurada dentro da seção | foto sangrando até a borda | foto de fundo com texto por cima | poucas fotos, muito espaço em branco |
| 5 | Marcação de seção | `(S ÷ 11) % 4` | título grande, sem enfeite | eyebrow curto acima do título | numeração lateral (01, 02, 03) | linha divisória com rótulo |

**Exemplo completo, S = 135:**
`135%4=3` blocos sobrepostos · `(135÷2=67)%4=3` assimétrico 40/60 ·
`(135÷5=27)%4=3` sem menu, só botão · `(135÷7=19)%4=3` poucas fotos ·
`(135÷11=12)%4=0` título grande.

**Por que divisores diferentes:** uma versão anterior desta regra usava só a contagem de
letras com deslocamentos fixos. Testada em 24 nomes reais, ela produziu **4 combinações
diferentes só**, com 67 pares de clientes recebendo a mesma página. Com os divisores acima,
os mesmos 40 nomes geraram 36 combinações distintas, com as 4 opções bem distribuídas em
todas as 5 linhas.

**Passo 3.** Escreva as 5 escolhas no chat, em uma linha, e siga elas na Fase 1 e na Fase 2.

**Quando ignorar o sorteio:** se uma escolha briga com o material do cliente (sorteou
"poucas fotos" e ele mandou 6 fotos ótimas; sorteou "foto de fundo com texto por cima" e a
única foto é escura), troque **aquela linha** por outra opção da mesma linha e diga em uma
linha por quê. Trocar uma linha por motivo real é ajuste; trocar as cinco de volta para o
padrão de sempre é o erro que este sorteio existe para evitar.

## 3. Banco de variações por seção

Cada seção tem mais de um jeito de existir. Escolha por seção, não por hábito.

### Hero

Os três heros da Fase 1 saem daqui, também por sorteio: com o mesmo **S**, use as opções
`S%6`, `(S+2)%6` e `(S+4)%6`. Somar 2 e 4 garante que os três sejam sempre distintos, e o S
faz mudarem de cliente para cliente. Com S = 135: heros 3, 5 e 1.

0. Foto grande à direita, texto à esquerda (o mais comum, e por isso o mais gasto)
1. Foto sangrando em tela cheia, texto sobreposto num canto
2. Sem foto: só tipografia grande, nome e especialidade ocupando a tela
3. Foto pequena e circular ao lado do nome, hero curto e direto ao CTA
4. Duas colunas invertidas: foto à esquerda, texto à direita
5. Hero dividido na diagonal, cor de um lado e foto do outro

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
- Rodar o sorteio da seção 2 e seguir o resultado. É isso que garante variedade sem memória.
- Nunca "corrigir" o sorteio de volta para o padrão de sempre (hero com foto à direita,
  faixas empilhadas, tudo à esquerda) só porque parece mais seguro.
- Para o hero, usar as três opções da seção 3 que o sorteio indica, não as três primeiras
  da lista.
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
