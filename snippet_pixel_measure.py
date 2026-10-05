#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
snippet-pixel-measure — estima a largura em pixels de um título e de uma
meta description, porque o Google corta o snippet por pixel renderizado, e
não por número de caracteres (um título cheio de "W" maiúsculo estoura bem
antes de chegar em 60 caracteres; um título só de "iiiiii" cabe bem além
disso).

O QUE FAZ
    Soma a largura de avanço de cada caractere em Arial, a partir das
    métricas públicas do Helvetica (arquivo AFM do Adobe Core 14, em
    unidades de 1/1000 do em), que o Arial reproduz por desenho. A soma é
    escalada pelo tamanho de fonte de cada elemento do snippet: título em
    20px e meta description em 14px. O resultado é comparado com limites de
    referência de desktop e mobile.

USO
    python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte | Lucas Ferraz"
    python snippet_pixel_measure.py --meta "Descrição de até 145 caracteres..."
    python snippet_pixel_measure.py --titulo "..." --meta "..." --mobile

LIMITAÇÕES
    A tabela cobre o ASCII imprimível, as letras acentuadas do português
    (medidas como a letra base, com exceção do "i" acentuado, que no Arial é
    mais largo que o "i") e a pontuação tipográfica comum. Não considera
    kerning nem arredondamento de renderização. Caractere fora da tabela
    entra com largura de reserva (1 em para símbolo, 0,556 em para o resto),
    porque o navegador o desenha com outra fonte. O Google pode trocar fonte
    e tamanho sem aviso, e os limites (~600px título desktop, ~920px meta
    desktop) são aproximações amplamente citadas, não valores documentados
    pelo Google. Use o número como estimativa, não como o pixel exato do
    corte.

Autor: Lucas Ferraz (lucasferraz.com) — dependência zero, só biblioteca padrão.
Licença: MIT.
"""
from __future__ import annotations

import argparse
import unicodedata

# Tamanho de fonte com que o Google renderiza cada elemento do snippet (Arial).
TAMANHO_TITULO_PX = 20
TAMANHO_META_PX = 14

LIMITES = {
    "titulo_desktop": 600,
    "titulo_mobile": 500,
    "meta_desktop": 920,
    "meta_mobile": 680,
}

# Largura de avanço por caractere, em unidades de 1/1000 do em.
# Fonte: Adobe Core 14 AFM, Helvetica.afm (métricas públicas do Helvetica,
# que o Arial reproduz caractere a caractere).
LARGURAS = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "<": 584, "=": 584, ">": 584,
    "?": 556, "@": 1015, "[": 278, "\\": 278, "]": 278, "^": 469, "_": 556,
    "`": 333, "{": 334, "|": 260, "}": 334, "~": 584,
    # pontuação tipográfica e sinais comuns em português
    "\u00a0": 278,  # espaço não separável
    "–": 556,  # meia-risca
    "—": 1000,  # travessão
    "‘": 222, "’": 222, "“": 333, "”": 333,
    "•": 350,  # marcador
    "…": 1000,  # reticências
    "«": 556, "»": 556, "·": 278, "°": 400,
    "ª": 370, "º": 365, "©": 737, "®": 737,
    "€": 556, "£": 556, "¿": 611, "¡": 333,
    "×": 584, "÷": 584,
}
LARGURAS.update({d: 556 for d in "0123456789"})
LARGURAS.update(zip(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    (667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833,
     722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611),
))
LARGURAS.update(zip(
    "abcdefghijklmnopqrstuvwxyz",
    (556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833,
     556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500),
))
# No Arial o "i" acentuado é mais largo que o "i" (278 contra 222).
LARGURAS.update({c: 278 for c in "ìíîï"})

# Caractere fora da tabela: o navegador cai em outra fonte.
RESERVA_SIMBOLO = 1000  # setas, emoji e demais símbolos (categoria S*)
RESERVA_OUTROS = 556


def largura_caractere(c: str) -> int:
    """Largura de avanço de um caractere em 1/1000 do em."""
    if c in LARGURAS:
        return LARGURAS[c]
    base = unicodedata.normalize("NFD", c)[0]
    if base in LARGURAS:
        return LARGURAS[base]
    categoria = unicodedata.category(c)
    if categoria in ("Mn", "Me", "Cf"):
        return 0  # acento combinante ou caractere de formato, sem avanço
    if categoria.startswith("S"):
        return RESERVA_SIMBOLO
    return RESERVA_OUTROS


def largura_texto(texto: str, tamanho_px: float) -> float:
    """Largura estimada do texto, em pixels, no tamanho de fonte informado."""
    return sum(largura_caractere(c) for c in texto) * tamanho_px / 1000


def avalia(rotulo: str, texto: str, tamanho_px: float, limite: float) -> None:
    largura = largura_texto(texto, tamanho_px)
    n_chars = len(texto)
    pct = largura / limite * 100
    status = "dentro do limite" if largura <= limite else "PROVAVELMENTE CORTA"
    print(f"{rotulo}: {n_chars} caracteres | ~{largura:.0f}px em Arial {tamanho_px:g}px de ~{limite:.0f}px ({pct:.0f}%) | {status}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Estima a largura em pixels de título e meta description para SERP."
    )
    ap.add_argument("--titulo", default="", help="texto do título")
    ap.add_argument("--meta", default="", help="texto da meta description")
    ap.add_argument("--mobile", action="store_true", help="usa os limites de referência de mobile em vez de desktop")
    args = ap.parse_args()

    if not args.titulo and not args.meta:
        ap.error("informe --titulo, --meta, ou os dois")

    sufixo = "mobile" if args.mobile else "desktop"
    print(f"\n=== snippet-pixel-measure ({sufixo}) ===\n")
    if args.titulo:
        avalia("Título", args.titulo, TAMANHO_TITULO_PX, LIMITES[f"titulo_{sufixo}"])
    if args.meta:
        avalia("Meta description", args.meta, TAMANHO_META_PX, LIMITES[f"meta_{sufixo}"])
    print("\n(Estimativa por métricas do Arial; ver Limitações no README antes de tratar como valor exato.)")


if __name__ == "__main__":
    main()
