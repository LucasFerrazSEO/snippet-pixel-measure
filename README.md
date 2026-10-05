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

The estimate sums the advance width of each character in Arial and scales
it by the font size of each snippet element: 20px for the title and 14px
for the meta description. The widths come from the public Helvetica
metrics (Adobe Core 14 AFM, in 1/1000 em units), which Arial matches
character by character.

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

Título: 65 caracteres | ~627px em Arial 20px de ~600px (104%) | PROVAVELMENTE CORTA
Meta description: 107 caracteres | ~734px em Arial 14px de ~920px (80%) | dentro do limite

(Estimativa por métricas do Arial; ver Limitações no README antes de tratar como valor exato.)
```

**4. Use the mobile limits**, which are usually narrower than desktop:

```bash
python snippet_pixel_measure.py --titulo "..." --meta "..." --mobile
```

## FAQ

**Is snippet-pixel-measure really free?**
Yes. It is open source under the MIT license.

**Is this the exact measurement Google uses?**
No, and no public tool has access to that (see Limitations below). It
uses Arial metrics at the font sizes Google commonly renders, so it lands
close to the browser width, but it does not predict the exact cut pixel by
pixel.

**Where can I visually confirm the real cut?**
In the actual rendered search result. The tool is a quick checkpoint
before publishing and does not replace looking at the real SERP.

## Limitations

Read this before using the tool.

- **Font and size are an assumption.** The tool assumes Google renders the
  title in Arial 20px and the meta description in Arial 14px. Google can
  change font, size and layout without notice, and the rendering varies by
  device, language and browser.
- **Metrics, not rendering.** Widths come from the public Helvetica AFM
  table, which Arial matches. The tool ignores kerning and the browser's
  subpixel rounding. Brazilian Portuguese accented letters are measured as
  their base letter, except accented "i", which is wider in Arial.
- **Characters outside the table** (arrows, emoji, non-Latin scripts) get a
  fallback width (1 em for symbols, 0.556 em for the rest), because the
  browser draws them with another font. Results for those are rougher.
- **Checked against real measurements.** On 2026-10-05, four titles and
  meta descriptions in Brazilian Portuguese were measured with canvas
  `measureText` in Arial. The tool stayed within 3% of all four (the test
  file uses that tolerance). That is a small sample, not a guarantee for
  every text.
- **The limits are approximations.** ~600px for desktop titles and ~920px
  for desktop meta descriptions (680px on mobile) are widely cited by SERP
  simulation tools, not values documented by Google.

Treat the result as an estimate close to the browser width, useful for
deciding whether a title or description is at risk of being cut, not as
the exact pixel where the cut falls. Run the tests with
`python -m unittest test_snippet_pixel_measure`.

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/LucasFerrazSEO/snippet-pixel-measure/issues).

## Author

[Lucas Ferraz](https://lucasferraz.com) is an SEO, website development and Generative Engine Optimization specialist and the founder of [Lucas Ferraz SEO](https://lucasferrazseo.com).

## License

MIT. See [LICENSE](LICENSE).
