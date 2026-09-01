# Arquitetura da home: quais seções e em que ordem

Passo 2 do fluxo. Fazer **antes** de desenhar. Mostrar a lista pro usuário e pedir o "ok"
explícito. Descobrir na Fase 2 que faltava uma seção significa refazer respiro, navegação e
âncoras.

---

## A ordem que funciona

A home de profissional de saúde tem uma lógica de leitura previsível: quem chega quer saber,
nessa ordem, **onde estou → isso é pra mim? → posso confiar? → como falo com você?**

| # | Seção | Responde a pergunta | Obrigatória? |
| --- | --- | --- | --- |
| 1 | Header fixo | Onde estou, como falo agora | Sim |
| 2 | Hero | Quem é, o que faz, onde atende | Sim |
| 3 | Condições / o que trata | Isso é pra mim? | Sim |
| 4 | Sintomas / quando procurar | Eu me encaixo? | Recomendada |
| 5 | Sobre o profissional | Posso confiar? | Sim |
| 6 | A clínica / estrutura | Como é o lugar? | Recomendada |
| 7 | Como funciona o atendimento | O que vai acontecer comigo? | Recomendada |
| 8 | Exames e procedimentos | O que é oferecido? | Depende |
| 9 | Convênios / formas de pagamento | Consigo pagar? | Depende |
| 10 | Localização e horários | Como chego? | Sim |
| 11 | FAQ | Dúvida que trava a decisão | Recomendada |
| 12 | CTA final | Fecha a decisão | Sim |
| 13 | Rodapé | Dados legais e contato | Sim |

Menos de 7 seções costuma ficar raso. Mais de 13 costuma cansar. A faixa saudável é 9 a 12.

---

## O que entra em cada seção

**1. Header fixo.** Logo, menu de âncoras (3 a 6 itens, não mais), botão de contato. Vira
hamburguer só em tela pequena de verdade. Ver [hero-armadilhas.md](hero-armadilhas.md)
seção 2.

**2. Hero.** Nome, especialidade, uma frase de posicionamento, cidade/região, foto real do
profissional, botão de WhatsApp. **CRM aparece aqui ou logo abaixo**, não só no rodapé.

**3. Condições / o que trata.** A seção mais importante de SEO e de qualificação. Lista as
condições em chips ou bullets. Se forem muitas, agrupar por tema em vez de listar 40 itens
soltos.

**4. Sintomas / quando procurar.** Escrita do ponto de vista do paciente ("cansaço ao subir
escada"), não do médico ("dispneia aos esforços"). Nunca em tom alarmista. Ver
[compliance-cfm-lgpd.md](compliance-cfm-lgpd.md).

**5. Sobre o profissional.** Formação, tempo de atuação, títulos, onde atende. Foto
diferente da do hero, se houver. Sem superlativo ("o melhor", "referência nacional").

**6. A clínica / estrutura.** Fotos reais da recepção e da sala. Se não houver fotos, essa
seção vira moldura vazia ou sai da lista, nunca banco de imagens.

**7. Como funciona o atendimento.** Passos numerados do agendamento até o retorno. Reduz
ansiedade e reduz pergunta no WhatsApp. Números ímpares de passos deixam o último item
sozinho na linha do grid: isso é normal, não force um número par.

**8. Exames e procedimentos.** Descrição informativa. Nunca prometer resultado, nunca
antes/depois.

**9. Convênios / pagamento.** Listar convênios só se o usuário confirmar a lista atualizada
(convênio muda). **Nunca publicar preço de consulta ou procedimento** sem checar a regra do
conselho.

**10. Localização e horários.** Endereço completo linkado pro Google Maps, mapa embutido,
horário dia a dia, referências de acesso, estacionamento. O endereço e o horário precisam
bater exatamente com o Google Business Profile.

**11. FAQ.** 5 a 8 perguntas reais, as que mais chegam no WhatsApp. Acordeão nativo com
`<details>`, sem JS. Pergunta que ninguém faz ocupa espaço à toa.

**12. CTA final.** Uma frase e um botão. Sem formulário, sem novidade nesse ponto.

**13. Rodapé.** Nome, CRM + UF, RQE, CNPJ, endereço, telefone, WhatsApp, Instagram, horário,
diretor técnico (quando clínica), link da política de privacidade, ano.

---

## Seções que quase sempre são má ideia

- **Depoimento de paciente**: proibido para autopromoção em publicidade médica no Brasil.
  Ver [compliance-cfm-lgpd.md](compliance-cfm-lgpd.md).
- **Antes e depois**: proibido em publicidade médica.
- **Contador de "pacientes atendidos"**: número não verificável, tom de propaganda.
- **Blog na home**: se o cliente tem blog, um link basta; feed de posts na home envelhece
  mal e some quando o cliente para de postar.
- **Newsletter**: dado pessoal sem finalidade clara, e ninguém assina newsletter de médico.
- **Carrossel de logos de convênio sem confirmação**: convênio descredenciado no site gera
  paciente irritado na recepção.

---

## Antes de fechar a arquitetura, confirmar

- [ ] O usuário aprovou a lista de seções e a ordem
- [ ] Cada seção tem copy aprovada (ou pendência marcada)
- [ ] Cada seção que usa foto tem foto (ou vai ficar com moldura vazia, avisado)
- [ ] Os itens do menu do header foram escolhidos entre essas seções (3 a 6)
- [ ] Ficou claro onde o CRM e o RQE aparecem
