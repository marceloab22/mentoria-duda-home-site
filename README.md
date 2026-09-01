# mentoria-duda-home-site

Skill para criar a **home** (página única) de um site de profissional de saúde, em duas
fases: primeiro 3 direções visuais para escolher o estilo, depois a página completa.

Portátil: não depende de nenhum sistema, CRM, planilha ou base de dados. Tudo vem do que o
usuário escrever no chat.

---

## Para quem é

Quem monta site de médico, dentista, psicólogo, fisioterapeuta, nutricionista ou clínica e
precisa de um processo repetível, com testes de verdade, em vez de "gerar HTML bonito e
torcer".

Serve também para outros nichos de serviço profissional. O que muda é o arquivo de
compliance e a lista de seções. Ver SKILL.md seção 11.

## O que ela entrega

1. Um comparador com 3 direções visuais do topo da página, para o cliente escolher.
2. A home completa no estilo escolhido, testada em desktop e celular.
3. Lista de pendências, tarefas de SEO e instruções para subir no ar.

## Como instalar

Clonar direto no diretório de skills do seu Claude Code:

```bash
git clone https://github.com/SEU-USUARIO/mentoria-duda-home-site.git ~/.claude/skills/mentoria-duda-home-site
```

Ou, se você recebeu a pasta em vez do link:

```bash
cp -R mentoria-duda-home-site ~/.claude/skills/
```

Para atualizar depois, dentro da pasta:

```bash
git pull
```

A skill aparece na lista automaticamente. Invocar com `/mentoria-duda-home-site` ou apenas
descrevendo a tarefa ("preciso montar a home do site da Dra. Fulana").

### Renomear a skill

Se quiser outro nome, mude **duas** coisas, que precisam bater:

1. O nome da pasta.
2. O campo `name:` no topo do `SKILL.md`.

## Dependências

**Obrigatória:** uma forma de exibir HTML para o usuário (no Claude Code, a ferramenta
Artifact). Sem ela, entregue o HTML como arquivo.

**Opcionais, mas recomendadas:**

- Plugin `frontend-design` (marketplace `anthropics/claude-plugins-official`)
- Ferramenta de navegador com inspeção (Browser / Chrome MCP / DevTools). **Sem isso você
  não consegue rodar os testes numéricos e vai entregar bug.**
- Ferramenta `Workflow` (só acelera a Fase 1)
- Python 3 (para os scripts de `references/`)

## Estrutura da pasta

```
mentoria-duda-home-site/
  README.md                     este arquivo
  SKILL.md                      as instruções principais
  references/
    checklist-briefing.md       o que juntar antes de desenhar
    estrutura-home.md           quais seções a home tem e em que ordem
    compliance-cfm-lgpd.md      publicidade em saúde e LGPD
    hero-armadilhas.md          os bugs do hero, com número medido
    fase2-componentes.md        CSS testado de cada bloco
    respiro-e-distribuicao.md   espaçamento vertical e layout de colunas
    whatsapp-botao.md           botão flutuante e de texto
    seo-acessibilidade.md       SEO, acessibilidade, performance
    testes-medicao.md           snippets de medição prontos
    troubleshooting.md          catálogo de bugs por sintoma
    entrega-handoff.md          checklist de fechamento e como subir no ar
    glossario.md                vocabulário
    comparador-template.html    template da prévia comparativa
    comparador.py               monta o comparador de N versões
    base64-embed.py             embute as fotos no final
    recorte-secoes.py           recorta cada seção para testar isolada
```

## Uso dos scripts

```bash
# 1. Montar a prévia comparativa (Fase 1, 3 versões)
python3 references/comparador.py \
  --titulo "Home . Dra. Marina Xavier" \
  --subtitulo "Fase 1: cabecalho, hero e amostra da proxima secao" \
  --nota "A: escura e centralizada. B: clara com foto ao lado. C: bloco de cor da marca." \
  --saida comparador-fase1.html \
  "Versao A=vA.html" "Versao B=vB.html" "Versao C=vC.html"

# 2. Testar cada seção isolada, sem rolar a página
python3 references/recorte-secoes.py home-final.html --wrapper site-home --saida testes/
python3 -m http.server 8899 --directory testes

# 3. Embutir as fotos, só no final
python3 references/base64-embed.py home-trabalho.html home-final.html \
  FOTO_1=imagens/hero.jpg FOTO_2=imagens/recepcao.jpg
```

Os três scripts falham com mensagem clara em vez de gerar arquivo quebrado em silêncio
(placeholder sem imagem, seção inexistente, template com placeholder sobrando).

## Como ela começa

Três rodadas, **uma coisa de cada vez**, sempre nesta ordem:

1. **Copy da página**, sozinha, na primeira mensagem
2. **Identidade visual** (cores em hex, fontes, logo), depois que a copy chegar
3. **Fotos, uma por uma**: com a copy na mão ela monta a lista de fotos que a página
   precisa e pede cada uma pelo nome e pela finalidade

Ela não gera HTML, não propõe layout e não sugere cor antes disso.

## As 8 regras que sustentam a skill

1. Pedir copy, identidade visual e fotos antes de qualquer coisa, uma de cada vez
2. Nada de dado inventado
3. Copy exata, palavra por palavra
4. Só foto real, nunca banco de imagens
5. Cor e fonte nunca vêm de outro projeto
6. Zero travessão (em-dash)
7. Medir antes de afirmar que corrigiu
8. Publicidade em saúde tem lei

Detalhe de cada uma no `SKILL.md`.

## Limites conhecidos

- É só home, página única
- Não faz formulário com backend
- Não gera imagem
- Compliance é orientação prática, não parecer jurídico

## Histórico

**v2.2 (agosto/2026).** A abertura virou sequencial: copy, depois identidade visual, depois
cada foto individualmente, uma pergunta por mensagem. A lista de fotos passou a ser derivada
da copy, então cada foto é pedida pelo nome e pela finalidade.

**v2.1 (agosto/2026).** Abertura obrigatória: a skill agora começa toda conversa pedindo
copy, identidade visual e fotos, com a mensagem pronta no `SKILL.md`. Virou a regra 1 (as
regras passaram de 7 para 8).

**v2 (agosto/2026).** Revisão completa para exportação. Removida toda referência a projeto
e cliente específico; exemplos genericizados para `#site-home`. Adicionados:
`estrutura-home.md`, `compliance-cfm-lgpd.md`, `seo-acessibilidade.md`,
`respiro-e-distribuicao.md`, `testes-medicao.md`, `troubleshooting.md`,
`entrega-handoff.md`, `glossario.md`, `comparador.py`, `recorte-secoes.py`. Comparador
passou a aceitar N versões (3 da Fase 1 e 6 da regra do "não gostei") com abas geradas
automaticamente. Scripts ganharam validação e mensagens de erro. `SKILL.md` reorganizado em
fluxo de 7 passos com tabela de navegação.

**v1.** Fluxo de 2 fases, armadilhas do hero, componentes da Fase 2, botão de WhatsApp,
regra das 6 versões.
