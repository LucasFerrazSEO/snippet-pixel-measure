[English](README.md) · **Português (Brasil)**

# snippet-pixel-measure

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`snippet-pixel-measure` é uma ferramenta de linha de comando gratuita e de
código aberto que estima a largura em pixels de um título e de uma meta
description, porque o Google corta o snippet por pixel renderizado, não
por número de caracteres. Um título cheio de "W" maiúsculo estoura bem
antes de chegar em 60 caracteres; um título só de letras estreitas cabe
bem além disso. Roda localmente, só com a biblioteca padrão do Python.

## Sumário

- [Contexto](#contexto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Perguntas frequentes](#perguntas-frequentes)
- [Limitações](#limitações)
- [Como contribuir](#como-contribuir)
- [Autor](#autor)
- [Licença](#licença)

## Contexto

A regra "título até 55 a 60 caracteres" é uma aproximação grosseira. Duas
frases com o mesmo número de caracteres podem ocupar larguras bem
diferentes na tela, dependendo de quais letras usam.
`snippet-pixel-measure` estima o espaço real que o texto ocuparia, para
você saber se um título "tecnicamente dentro do limite de caracteres" já
está, na prática, sendo cortado.

A estimativa soma a largura de avanço de cada caractere em Arial e escala
pelo tamanho de fonte de cada elemento do snippet: 20px no título e 14px
na meta description. As larguras vêm das métricas públicas do Helvetica
(AFM do Adobe Core 14, em unidades de 1/1000 do em), que o Arial reproduz
caractere a caractere.

## Requisitos

Python 3.9 ou mais recente. Só biblioteca padrão, sem dependência externa.

## Instalação

```bash
git clone https://github.com/LucasFerrazSEO/snippet-pixel-measure.git
cd snippet-pixel-measure
```

## Uso

**1. Meça um título.**

```bash
python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte com Especialista em GEO e IA"
```

**2. Meça uma meta description.**

```bash
python snippet_pixel_measure.py --meta "Agência de SEO em BH com mais de 19 anos de experiência ajudando empresas a aparecerem no Google e nas IAs."
```

**3. Meça os dois de uma vez.**

```bash
python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte com Especialista em GEO e IA" --meta "Agência de SEO em BH com mais de 19 anos de experiência ajudando empresas a aparecerem no Google e nas IAs."
```

Exemplo real de saída:

```
=== snippet-pixel-measure (desktop) ===

Título: 65 caracteres | ~627px em Arial 20px de ~600px (104%) | PROVAVELMENTE CORTA
Meta description: 107 caracteres | ~734px em Arial 14px de ~920px (80%) | dentro do limite

(Estimativa por métricas do Arial; ver Limitações no README antes de tratar como valor exato.)
```

**4. Use os limites de mobile**, que costumam ser mais estreitos que
desktop:

```bash
python snippet_pixel_measure.py --titulo "..." --meta "..." --mobile
```

## Perguntas frequentes

**snippet-pixel-measure é realmente grátis?**
Sim, código aberto sob licença MIT.

**Isso é a medida exata que o Google usa?**
Não, e nenhuma ferramenta pública tem acesso a isso (veja Limitações
abaixo). Ela usa as métricas do Arial nos tamanhos de fonte que o Google
costuma renderizar, então chega perto da largura no navegador, mas não
prevê o corte exato pixel a pixel.

**Onde consigo confirmar visualmente o corte de verdade?**
No resultado renderizado de fato na busca. A ferramenta é um checkpoint
rápido antes de publicar, não substitui olhar a SERP real.

## Limitações

Leia antes de usar.

- **Fonte e tamanho são uma premissa.** A ferramenta supõe que o Google
  renderiza o título em Arial 20px e a meta description em Arial 14px. O
  Google pode trocar fonte, tamanho e layout sem aviso, e a renderização
  varia por dispositivo, idioma e navegador.
- **Métrica, não renderização.** As larguras vêm da tabela AFM pública do
  Helvetica, que o Arial reproduz. A ferramenta ignora kerning e o
  arredondamento de subpixel do navegador. Letra acentuada do português é
  medida como a letra base, com exceção do "i" acentuado, que no Arial é
  mais largo.
- **Caractere fora da tabela** (seta, emoji, alfabeto não latino) entra com
  largura de reserva (1 em para símbolo, 0,556 em para o resto), porque o
  navegador o desenha com outra fonte. Nesses casos a estimativa é mais
  grosseira.
- **Conferida contra medição real.** Em 2026-10-05, quatro títulos e meta
  descriptions em português foram medidos com `measureText` de canvas em
  Arial. A ferramenta ficou a menos de 3% dos quatro (o arquivo de testes
  usa essa tolerância). É uma amostra pequena, não garantia para todo
  texto.
- **Os limites são aproximações.** ~600px de título em desktop e ~920px de
  meta em desktop (680px no celular) são valores amplamente citados por
  ferramentas de simulação de SERP, não documentados pelo Google.

Trate o resultado como estimativa próxima da largura no navegador, útil
para decidir se um título ou uma descrição corre risco de corte, não como
o pixel exato onde o corte cai. Os testes rodam com
`python -m unittest test_snippet_pixel_measure`.

## Como contribuir

Relatos de erro e sugestões são bem-vindos pelas [Issues do GitHub](https://github.com/LucasFerrazSEO/snippet-pixel-measure/issues).

## Autor

[Lucas Ferraz](https://lucasferraz.com) é especialista em SEO, criação de sites e Generative Engine Optimization e fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE).
