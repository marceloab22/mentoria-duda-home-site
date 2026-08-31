# Respiro e distribuição: espaçamento vertical e layout de colunas

"Respiro" é o espaçamento vertical entre os blocos de uma seção. É a diferença entre uma
página que parece cara e uma que parece template. É também o assunto que mais gera pedido
vago do tipo "dá um respiro maior aqui".

Este arquivo é técnica de distribuição, **reaproveitável entre projetos** (não é identidade
visual, funciona com qualquer paleta).

---

## 1. A cadeia de gaps de uma seção

Toda seção tem os mesmos cinco pontos de espaçamento. Mexer em um só desequilibra o resto.
Quando o usuário pedir respiro, ajustar a **cadeia inteira**, não um gap isolado.

| # | Gap | Onde |
| --- | --- | --- |
| 1 | Título → subtítulo | dentro do cabeçalho da seção |
| 2 | Cabeçalho → corpo | do bloco de título ao primeiro parágrafo |
| 3 | Parágrafo → parágrafo | dentro do corpo de texto |
| 4 | Texto → lista/chips | do último parágrafo ao primeiro item |
| 5 | Lista/chips → botão | do último item ao CTA |

## 2. Escala de referência "arejada" (ponto de partida testado)

Escala aprovada em projeto real. Serve como **default** quando não há motivo pra outra
coisa. Sempre escopada por seção, nunca alterando a regra base compartilhada.

```css
#site-home #secao-x .section-head p      { margin-top: 32px; }  /* 1 */
#site-home #secao-x .section-head-center { margin-bottom: 24px; } /* 2 */
#site-home #secao-x .body-text p + p     { margin-top: 20px; }  /* 3 */
#site-home #secao-x .chip-row            { margin-top: 36px; }  /* 4 */
#site-home #secao-x .btn-wrap-center     { margin-top: 36px; }  /* 5 */
```

Escalas alternativas, mesma cadeia, outros números:

| Escala | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Compacta | 12 | 16 | 12 | 20 | 20 |
| Equilibrada | 20 | 20 | 16 | 28 | 28 |
| **Arejada** | **32** | **24** | **20** | **36** | **36** |
| Muito arejada | 44 | 40 | 24 | 52 | 52 |
| Progressiva | 16 | 24 | 20 | 40 | 56 |
| Agrupada | 10 | 48 | 12 | 48 | 48 |

"Progressiva" cresce de cima pra baixo. "Agrupada" cola o que é do mesmo assunto e abre
espaço grande só entre blocos diferentes. Esses seis são exatamente os eixos a usar quando o
usuário pedir 6 opções de respiro.

## 2b. Formatação padrão de seção de texto (esta parte SE copia entre projetos)

Cuidado para não confundir com a regra de esqueleto: **o esqueleto muda entre clientes, a
formatação de uma seção de texto não.** Toda seção do tipo "título, subtítulo, parágrafos,
lista, botão", **sem foto ou mapa ao lado**, usa o mesmo tratamento:

- Cabeçalho **centralizado** (`.section-head-center`)
- Corpo **centralizado**, ocupando o trilho (não deixar o texto colado à esquerda com a
  metade direita vazia)
- Lista ou chips centralizados
- Botão centralizado (`.btn-wrap-center`)
- Escala arejada da seção 2 (32 / 24 / 20 / 36 / 36)

**Sintoma de que a regra não foi aplicada:** o usuário diz "ficou muito para o lado". É o
cabeçalho com `max-width` fixo alinhado à esquerda, num bloco que não tem nada na coluna da
direita. O texto fica com linha longa demais **e** com um vazio enorme ao lado.

Seção que **tem** foto, mapa ou carrossel ao lado continua alinhada à esquerda, em duas
colunas. A regra vale só para bloco de texto puro.

Bug real: um projeto reaproveitou o esqueleto de outro (errado) mas **não** reaproveitou
essa formatação (também errado). Saiu com 5 seções de texto alinhadas à esquerda, linha de
mais de 100 caracteres e metade da tela vazia.

## 3. Regra do pacote: layout e respiro andam juntos

Quando um padrão de layout já aprovado é reaproveitado em outra seção (ex: "centralizado
com chips"), **copiar junto a escala de respiro daquele padrão, na mesma tacada**.

Bug real: em um projeto, o layout foi reaproveitado e a escala não. A seção nova saiu com o
espaçamento base (bem mais apertado) e o usuário reparou na hora, com razão. Layout e
respiro são **um pacote só**, não dois passos.

Checklist ao reaproveitar um padrão:
- [ ] Classes de estrutura copiadas
- [ ] As 5 regras de respiro copiadas, com o `#id` da seção nova
- [ ] Testado visualmente ao lado da seção original (as duas devem parecer da mesma família)

---

## 4. Layout de duas colunas: os quatro bugs clássicos

### 4.1 `max-width` do cabeçalho vazando pra coluna vizinha

**Sintoma:** o usuário diz "esse texto passa da linha" ou manda screenshot com uma linha
vermelha marcando onde deveria parar.

**Causa:** `.section-head` tem `max-width` fixo (ex: 640px) e fica **acima** de um grid de
duas colunas cuja coluna é mais estreita que isso. O subtítulo estoura a largura real da
coluna e invade visualmente a coluna vizinha.

**Diagnóstico:** comparar `getBoundingClientRect().right` do bloco de texto com o `.left` da
coluna vizinha. Não confiar no olho.

**Correção:** travar o `max-width` do cabeçalho na largura real da coluna, só a partir do
breakpoint em que o grid vira duas colunas.

```css
@media (min-width: 900px) {
  #site-home #secao-x .section-head { max-width: calc(50% - 24px); }
}
```

O `24px` é metade do `gap` do grid (`gap: 48px` → `48/2`).

### 4.2 `margin-top` negativo virando sobreposição no celular

**Sintoma:** no desktop está perfeito; no celular a foto sobe por cima do botão ou do texto
anterior.

**Causa:** `margin-top: -50px` usado pra "subir" uma foto/mapa dentro de um grid de duas
colunas, escrito **sem media query**. No celular o grid vira uma coluna empilhada e a margem
negativa puxa a foto pra cima do bloco anterior.

**Correção:** todo `margin-top` negativo de ajuste de posição em grid vai **dentro** do
mesmo breakpoint em que o grid é de duas colunas.

```css
@media (min-width: 900px) {
  #site-home #secao-x .foto { margin-top: -50px; }
}
```

E testar em 375px antes de dizer que a correção está pronta. Esse bug passou uma seção
inteira despercebido porque ninguém abriu no celular.

### 4.3 `align-items` errado deixando uma coluna "solta"

**Sintoma:** o usuário diz "mal distribuído", "sobrou um vazio embaixo".

**Regra:** `align-items` de grid de duas colunas **não é escolha fixa por seção**, é uma
conta que muda toda vez que o conteúdo de alguma coluna muda.

- Colunas de alturas bem diferentes, e a curta ficando "grudada no topo" com vazio embaixo:
  `align-items: center` resolve.
- Depois de mover um bloco pra dentro da coluna que era curta (ex: endereço passando a ficar
  embaixo do mapa), ela pode virar a mais alta: aí o certo é voltar pra `align-items: start`
  e as duas começarem juntas no topo.

Reavaliar sempre que mexer no conteúdo de uma coluna.

### 4.4 "Sobe mais" repetido: medir o teto, não adivinhar

Quando o usuário pede pra empurrar um bloco com margem e depois pede "mais um pouco",
**não dobrar o valor no escuro.**

A cada aumento, medir a distância real até o vizinho na direção do movimento:

```javascript
const a = document.querySelector('.bloco-de-cima').getBoundingClientRect();
const b = document.querySelector('.bloco-que-sobe').getBoundingClientRect();
JSON.stringify({ folga: Math.round(b.top - a.bottom) });
```

Se `folga` chegar perto de zero ou ficar negativa, **parou**: é o teto físico, continuar só
faz sobrepor.

Bug real: um valor negativo grande demais foi aplicado sem medir, invadiu o texto de cima; a
tentativa de corrigir recuando acabou publicando **menos** movimento que a versão anterior.
O usuário pediu mais e recebeu menos.

Se ele insistir em "mais" depois que a medição mostrar folga zero, o espaço não vem de
aumentar essa margem: vem de **reduzir o respiro de um vizinho** (ex: o `margin-bottom` do
título logo acima), abrindo espaço de verdade.

---

## 5. Padrões de distribuição reaproveitáveis

Soluções estruturais que resolvem os problemas de distribuição mais comuns. Servem em
qualquer projeto, com as cores daquele cliente.

### 5.1 Texto denso deixando vazio do lado: grid dividido

Parágrafo longo ocupando 100% da largura fica com linha de 140 caracteres, cansativo de ler.

```css
#site-home .split-grid { display: grid; gap: 48px; align-items: start; }
@media (min-width: 900px) {
  #site-home .split-grid { grid-template-columns: 1fr 1fr; }
}
#site-home .split-text p + p { margin-top: 20px; }
```

### 5.2 Lista solta sem lugar: chips em pílula

Boa para condições tratadas, sintomas, especialidades. Lê melhor que bullet quando são
muitos itens curtos.

```css
#site-home .chip-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 36px; }
#site-home .chip-row-center { justify-content: center; }
#site-home .chip {
  font-size: 13.5px; line-height: 1.3; padding: 10px 16px;
  border-radius: 100px;
  background: var(--cor-superficie);
  border: 1px solid var(--cor-borda);
  color: var(--cor-texto);
}
```

### 5.3 Bloco centralizado (título, texto, chips, botão)

Utilitários que sempre andam juntos. Quando reaproveitar este padrão, copiar também a escala
de respiro da seção 2.

```css
#site-home .section-head-center { text-align: center; margin: 0 auto; max-width: 720px; }
#site-home .body-text-center    { text-align: center; margin: 0 auto; max-width: 720px; }
#site-home .btn-wrap-center     { display: flex; justify-content: center; margin-top: 36px; }
```

### 5.4 Frase de destaque no meio do texto

Uma frase na fonte de título, maior, para quebrar um bloco longo sem inventar texto novo.

```css
#site-home .lead-center {
  font-family: var(--fonte-display);
  font-size: 22px; line-height: 1.35; font-weight: 500;
  text-align: center; margin-top: 28px;
  color: var(--cor-texto);
}
#site-home .lead-center em { color: var(--cor-destaque); font-style: normal; }
```

### 5.5 Carrossel de fotos (quando há 2+ fotos do mesmo ambiente)

Evita empilhar três fotos e esticar a seção. Botões precisam ser `<button>` reais com
`aria-label`, e o `#site-home button { background: none }` do reset vence a cor deles:
escrever a cor com o prefixo de ID (ver SKILL.md seção 5).

---

## 6. Como gerar 6 opções de respiro

Quando o usuário pedir (ou reclamar de forma vaga do espaçamento):

1. Isolar **só aquela seção** num arquivo (usar [recorte-secoes.py](recorte-secoes.py)).
2. Gerar 6 cópias, cada uma com uma das escalas da tabela da seção 2.
3. Montar o comparador com [comparador.py](comparador.py), abas V1 a V6.
4. Publicar, deixar o usuário escolher.
5. Aplicar a escolhida no arquivo real, testar, republicar, reenviar o link.
6. A escala escolhida vira o padrão do projeto: nas próximas seções parecidas, aplicar
   direto, sem nova rodada de 6.
