# snippet-pixel-measure — ferramenta grátis e de código aberto para medir título e meta em pixels

`snippet-pixel-measure` é uma ferramenta gratuita e de código aberto que
estima a largura em pixels de um título e de uma meta description, porque
o Google corta o snippet por pixel renderizado, não por número de
caracteres. Um título cheio de "W" maiúsculo estoura bem antes de chegar
em 60 caracteres; um título só de letras estreitas cabe bem além disso.

## Por que medir em pixels, não em caracteres

A regra "título até 55-60 caracteres" é uma aproximação grosseira. Duas
frases com o mesmo número de caracteres podem ocupar larguras bem
diferentes na tela, dependendo de quais letras usam. `snippet-pixel-measure`
estima o espaço real que o texto ocuparia, para você saber se um título
"tecnicamente dentro do limite de caracteres" já está, na prática, sendo
cortado.

## Como usar, passo a passo

**1. Instale.** Só biblioteca padrão do Python (3.9 ou mais recente), sem
dependência externa:

```bash
git clone https://github.com/lucasferrazseo/snippet-pixel-measure.git
cd snippet-pixel-measure
```

**2. Meça um título.**

```bash
python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte com Especialista em GEO e IA"
```

**3. Meça uma meta description.**

```bash
python snippet_pixel_measure.py --meta "Agência de SEO em BH com mais de 19 anos de experiência ajudando empresas a aparecerem no Google e nas IAs."
```

**4. Meça os dois de uma vez.** Exemplo real de saída:

```
=== snippet-pixel-measure (desktop) ===

Título: 65 caracteres | ~454px estimado de ~600px (76%) | dentro do limite
Meta description: 107 caracteres | ~744px estimado de ~920px (81%) | dentro do limite

(Estimativa heurística — ver Limitações no README antes de tratar como valor exato.)
```

**5. Use os limites de mobile**, que costumam ser mais estreitos que
desktop:

```bash
python snippet_pixel_measure.py --titulo "..." --meta "..." --mobile
```

## Perguntas frequentes

**snippet-pixel-measure é realmente grátis?**
Sim, código aberto sob licença MIT.

**Isso é a medida exata que o Google usa?**
Não, e nenhuma ferramenta pública tem acesso a isso — ver Limitações
abaixo. É uma aproximação, útil para comparar dois títulos entre si, não
para prever o corte exato pixel a pixel.

**Onde consigo confirmar visualmente o corte de verdade?**
No resultado renderizado de fato na busca. A ferramenta é um checkpoint
rápido antes de publicar, não substitui olhar a SERP real.

## Limitações — leia antes de usar

A tabela de largura é uma **aproximação heurística** de fonte sans-serif
proporcional, não a métrica exata do Arial nem de qualquer fonte que o
Google use hoje — isso muda sem aviso e varia por idioma e dispositivo. Os
limites de referência (~600px de título em desktop, ~920px de meta)
também são aproximações amplamente citadas por ferramentas de simulação
de SERP, não valores garantidos ou documentados oficialmente pelo Google.

Trate o resultado como sinal de ordem de grandeza ("este título está bem
longo, provavelmente corta"), nunca como previsão exata de onde o corte
cai.

## Autor

[Lucas Ferraz](https://lucasferraz.com) — especialista em SEO, criação de
sites e SEO para IA, fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT — ver [LICENSE](LICENSE).
