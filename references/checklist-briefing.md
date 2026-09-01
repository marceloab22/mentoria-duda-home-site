# Checklist de briefing

**Três itens são a porta de entrada, pedidos um de cada vez, nesta ordem** (SKILL.md, seção
"Abertura obrigatória"):

1. **Copy da página** (seção 4 abaixo), sozinha, na primeira mensagem
2. **Identidade visual** (seção 3 abaixo), depois que a copy chegar
3. **Fotos** (seção 5 abaixo), uma por uma, com a lista derivada da copy

Nunca pedir os três no mesmo pedido: vem resposta pela metade e falta justamente o que
ninguém percebeu que faltou. Sem os três, não se desenha nada. As outras seções deste
checklist são o complemento, perguntado depois.

Juntar tudo isso com o usuário **antes** de desenhar qualquer coisa. Se algo faltar,
perguntar. Nunca inventar, nunca preencher com algo plausível.

Forma prática de usar: colar essa lista no chat, marcar `[x]` no que já veio, e devolver ao
usuário só o que ainda falta. Costuma render uma resposta única com tudo, em vez de cinco
idas e voltas.

---

## 1. Dados do profissional / clínica

- [ ] Nome completo, como deve aparecer no site
- [ ] Tratamento: Dr. / Dra. / sem tratamento (nunca escrever "Dr(a)")
- [ ] Especialidade principal, escrita exatamente como deve sair
- [ ] Subespecialidades ou áreas de atuação, se for exibir
- [ ] Nome da clínica, se diferente do nome do profissional
- [ ] Registro profissional: CRM/CRO/CRP + UF, número completo
- [ ] RQE (Registro de Qualificação de Especialista), se anunciar especialidade médica
- [ ] CNPJ, se for exibir no rodapé
- [ ] Nome do diretor técnico e registro dele, quando for clínica

> Registro profissional e RQE não são opcionais em site de médico. Ver
> [compliance-cfm-lgpd.md](compliance-cfm-lgpd.md).

## 2. Contato

- [ ] WhatsApp completo: DDI + DDD + número, só dígitos (ex: 5511999999999)
- [ ] Mensagem padrão que abre ao clicar no WhatsApp
- [ ] Telefone fixo, se houver, no formato que deve aparecer
- [ ] E-mail, se for exibir
- [ ] Endereço completo, com CEP, se for exibir mapa
- [ ] Complemento (sala, andar, edifício)
- [ ] Ponto de referência / instruções de acesso, se o usuário quiser
- [ ] Estacionamento: tem, não tem, é conveniado?
- [ ] Horário de atendimento, dia a dia
- [ ] Instagram (URL completa), se for linkar
- [ ] Outras redes, se for linkar

## 3. Identidade visual

- [ ] Paleta de cores exata, em hex, vinda de manual de marca, logo ou print. **Nunca
      aproximar de olho.** Se só houver o logo, extrair as cores dele e confirmar com o
      usuário antes de usar
- [ ] Fonte de título (nome exato)
- [ ] Fonte de corpo (nome exato)
- [ ] Logo em pelo menos duas versões: fundo claro e fundo escuro
- [ ] Logo em formato de boa qualidade (SVG ou PNG grande, não print de tela)
- [ ] Existe manual de marca? Se sim, pedir o arquivo

Se o cliente **não tem** identidade definida, isso vira uma decisão da Fase 1: as 3
direções propõem paletas diferentes e o usuário escolhe. Deixar isso explícito, não assumir.

## 4. Copy

- [ ] Texto aprovado, seção por seção, exatamente como vai entrar no site
- [ ] Quem aprovou? (o profissional já leu ou é rascunho da agência?)
- [ ] Trechos ainda não prontos, marcados como pendentes

Regra: texto provisório que **parece** final é pior que lacuna marcada. Se o usuário mandar
"depois eu ajusto essa parte", marque com `.pending` no site e liste na entrega.

## 5. Fotos

- [ ] Foto do profissional (retrato), boa resolução
- [ ] Fotos da clínica: fachada, recepção, sala de atendimento, equipamento
- [ ] Uma foto por bloco que vai usar foto
- [ ] Direito de uso confirmado (foto de fotógrafo contratado costuma ter contrato)
- [ ] Blocos sem foto disponível: avisar que ficará moldura vazia

Nunca usar banco de imagens nem imagem de pessoa gerada por IA em site de saúde. Além de
ficar falso, cria problema de confiança e pode esbarrar em regra do conselho.

Pedir **uma foto por vez**, pelo nome e pela finalidade ("o retrato do profissional, o que
vai no topo da página"), na ordem da lista derivada da copy. Pedir "me manda as fotos" no
genérico é o jeito mais rápido de receber três fotos soltas e descobrir só na Fase 2 que
faltavam duas.

## 6. Escopo e destino

- [ ] Onde a página vai rodar: WordPress (qual construtor?), HTML puro, outro?
- [ ] Domínio final
- [ ] Já existe site no ar? A home nova substitui ou é uma landing page separada?
- [ ] Tem Google Business Profile? (o endereço e o horário do site precisam bater com ele)
- [ ] Vai ter tráfego pago apontando pra essa página?

## 7. Referências (opcional, mas ajuda muito)

- [ ] Sites que o usuário gosta, com o que exatamente gosta em cada um ("o formato do
      botão", "o jeito que a foto entra no hero")
- [ ] Sites que o usuário **não** gosta, e por quê
- [ ] Concorrentes que ele não quer parecer

Referência solta ("gosto desse site") não ajuda. Sempre puxar o "o quê exatamente".

---

## Saída deste passo

Antes de ir pra Fase 1, você deve conseguir responder, sem consultar ninguém:

1. Como o profissional se chama e o que ele faz, no texto exato do site.
2. Quais são as 4 a 6 cores da página, em hex.
3. Quais são as 2 fontes.
4. Quantas seções a home vai ter e em que ordem (ver [estrutura-home.md](estrutura-home.md)).
5. Quais fotos existem e quais blocos vão ficar com moldura vazia.
6. O que ainda está pendente.

Se não conseguir responder alguma, o briefing não terminou.
