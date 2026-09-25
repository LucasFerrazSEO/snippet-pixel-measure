**English** · [Português (Brasil)](README.pt-BR.md)

# snippet-pixel-measure

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`snippet-pixel-measure` is a free, open source command-line tool that
estimates the pixel width of a title and a meta description, because
Google truncates snippets by rendered pixels, not by character count. A
title full of capital "W" overflows well before 60 characters; a title of
narrow letters only fits well beyond that. It runs locally with the Python
standard library only.

## Contents

- [Background](#background)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [FAQ](#faq)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Background

The "title up to 55 to 60 characters" rule is a rough approximation. Two
phrases with the same number of characters can take up very different
widths on screen, depending on which letters they use.
`snippet-pixel-measure` estimates the actual space the text would take, so
you know whether a title that is "technically within the character limit"
is in practice already being cut.

## Requirements

Python 3.9 or newer. Standard library only, no external dependencies.

## Installation

```bash
git clone https://github.com/LucasFerrazSEO/snippet-pixel-measure.git
cd snippet-pixel-measure
```

## Usage

The tool prints its report in Brazilian Portuguese.

**1. Measure a title.**

```bash
python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte com Especialista em GEO e IA"
```

**2. Measure a meta description.**

```bash
python snippet_pixel_measure.py --meta "Agência de SEO em BH com mais de 19 anos de experiência ajudando empresas a aparecerem no Google e nas IAs."
```

**3. Measure both at once.**

```bash
python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte com Especialista em GEO e IA" --meta "Agência de SEO em BH com mais de 19 anos de experiência ajudando empresas a aparecerem no Google e nas IAs."
```

Real sample output:

```
=== snippet-pixel-measure (desktop) ===

Título: 65 caracteres | ~454px estimado de ~600px (76%) | dentro do limite
Meta description: 107 caracteres | ~744px estimado de ~920px (81%) | dentro do limite

(Estimativa heurística — ver Limitações no README antes de tratar como valor exato.)
```

**4. Use the mobile limits**, which are usually narrower than desktop:

```bash
python snippet_pixel_measure.py --titulo "..." --meta "..." --mobile
```

## FAQ

**Is snippet-pixel-measure really free?**
Yes. It is open source under the MIT license.

**Is this the exact measurement Google uses?**
No, and no public tool has access to that (see Limitations below). It is
an approximation, useful for comparing two titles with each other, not for
predicting the exact cut pixel by pixel.

**Where can I visually confirm the real cut?**
In the actual rendered search result. The tool is a quick checkpoint
before publishing and does not replace looking at the real SERP.

## Limitations

Read this before using the tool. The width table is a **heuristic
approximation** of a proportional sans-serif font, not the exact metrics
of Arial or of any font Google uses today. That changes without notice and
varies by language and device. The reference limits (~600px for desktop
titles, ~920px for meta descriptions) are also approximations widely cited
by SERP simulation tools, not values guaranteed or officially documented
by Google.

Treat the result as an order-of-magnitude signal ("this title is quite
long, it will probably be cut"), never as an exact prediction of where the
cut falls.

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/LucasFerrazSEO/snippet-pixel-measure/issues).

## Author

[Lucas Ferraz](https://lucasferraz.com) is an SEO, website development and Generative Engine Optimization specialist and the founder of [Lucas Ferraz SEO](https://lucasferrazseo.com).

## License

MIT. See [LICENSE](LICENSE).
