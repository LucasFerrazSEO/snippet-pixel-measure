#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
snippet-pixel-measure — estima a largura em pixels de um título e de uma
meta description, porque o Google corta o snippet por pixel renderizado, e
não por número de caracteres (um título cheio de "W" maiúsculo estoura bem
antes de chegar em 60 caracteres; um título só de "iiiiii" cabe bem além
disso).

O QUE FAZ
    Usa uma tabela de largura relativa por caractere (heurística de fonte
    sans-serif proporcional, não a métrica exata e oficial de nenhuma fonte
    específica) para estimar quantos pixels um texto ocuparia, e compara
    contra limites de referência comuns de título e meta description em
    desktop e mobile.

USO
    python snippet_pixel_measure.py --titulo "Consultoria de SEO em Belo Horizonte | Lucas Ferraz"
    python snippet_pixel_measure.py --meta "Descrição de até 145 caracteres..."
    python snippet_pixel_measure.py --titulo "..." --meta "..." --mobile

LIMITAÇÕES
    A tabela de largura é uma APROXIMAÇÃO heurística de fonte sans-serif
    proporcional — não é a métrica exata do Arial nem de qualquer fonte que
    o Google use hoje, que muda sem aviso e varia por idioma e dispositivo.
    Use o resultado como sinal de ordem de grandeza ("este título está bem
    longo, provavelmente corta"), nunca como previsão exata de onde o corte
    cai. Os limites de referência (~600px desktop, ~920px meta) também são
    aproximações amplamente citadas, não valores garantidos pelo Google.

Autor: Lucas Ferraz (lucasferraz.com) — dependência zero, só biblioteca padrão.
Licença: MIT.
"""
from __future__ import annotations

import argparse

# Largura relativa por caractere, em unidades arbitrárias (heurística de fonte
# sans-serif proporcional comum, não métrica oficial de nenhuma fonte).
ESTREITOS = set("iIlj.,:;'!|")
MEDIOS_ESTREITOS = set("ftr()[]{}\"")
LARGOS = set("mMWw@%")
MAIUSCULAS_MEDIAS = set("ABCDEFGHJKLNOPQRSTUVXYZ")

LIMITES = {
    "titulo_desktop": 600,
    "titulo_mobile": 500,
    "meta_desktop": 920,
    "meta_mobile": 680,
}


def largura_caractere(c: str) -> float:
    if c == " ":
        return 4.0
    if c in ESTREITOS:
        return 4.5
    if c in MEDIOS_ESTREITOS:
        return 6.0
    if c in LARGOS:
        return 12.5
    if c in MAIUSCULAS_MEDIAS:
        return 9.5
    if c.isdigit():
        return 8.0
    if c.islower():
        return 7.5
    return 7.5


def largura_texto(texto: str) -> float:
    return sum(largura_caractere(c) for c in texto)


def avalia(rotulo: str, texto: str, limite: float) -> None:
    largura = largura_texto(texto)
    n_chars = len(texto)
    pct = largura / limite * 100
    status = "dentro do limite" if largura <= limite else "PROVAVELMENTE CORTA"
    print(f"{rotulo}: {n_chars} caracteres | ~{largura:.0f}px estimado de ~{limite:.0f}px ({pct:.0f}%) | {status}")


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
        avalia("Título", args.titulo, LIMITES[f"titulo_{sufixo}"])
    if args.meta:
        avalia("Meta description", args.meta, LIMITES[f"meta_{sufixo}"])
    print("\n(Estimativa heurística — ver Limitações no README antes de tratar como valor exato.)")


if __name__ == "__main__":
    main()
