# -*- coding: utf-8 -*-
"""Testes do snippet-pixel-measure contra larguras medidas em navegador.

As referências foram medidas em 2026-10-05 com canvas measureText, fonte
Arial real. Tolerância: ±3%.

    python -m unittest test_snippet_pixel_measure
"""
import unittest

from snippet_pixel_measure import (
    TAMANHO_META_PX,
    TAMANHO_TITULO_PX,
    largura_caractere,
    largura_texto,
)

TOLERANCIA = 0.03

REFERENCIAS = [
    ("título com prefixo",
     "➜Google e Bing citam conteúdos diferentes de pequenas empresas, mostra estudo brasileiro",
     TAMANHO_TITULO_PX, 830),
    ("título curto",
     "Google e Bing citam páginas diferentes de PMEs, diz estudo",
     TAMANHO_TITULO_PX, 538),
    ("meta longa",
     "Estudo com quatro PMEs brasileiras mostra que a IA do Google prioriza conteúdo informacional e o Copilot cita mais páginas de comparação.",
     TAMANHO_META_PX, 883),
    ("meta curta",
     "Estudo com quatro PMEs: o Google priorizou conteúdo informacional e o Copilot, páginas de comparação.",
     TAMANHO_META_PX, 661),
]


class TestReferencias(unittest.TestCase):
    def test_larguras_medidas_no_navegador(self):
        for rotulo, texto, tamanho, esperado in REFERENCIAS:
            with self.subTest(rotulo):
                obtido = largura_texto(texto, tamanho)
                self.assertLessEqual(
                    abs(obtido - esperado) / esperado, TOLERANCIA,
                    f"{rotulo}: {obtido:.1f}px, esperado {esperado}px",
                )


class TestCaracteres(unittest.TestCase):
    def test_acento_mede_como_a_base(self):
        for acentuada, base in [("á", "a"), ("ã", "a"), ("ç", "c"), ("é", "e"),
                                ("õ", "o"), ("ú", "u"), ("É", "E"), ("Ç", "C")]:
            with self.subTest(acentuada):
                self.assertEqual(largura_caractere(acentuada), largura_caractere(base))

    def test_i_acentuado_mais_largo(self):
        self.assertGreater(largura_caractere("í"), largura_caractere("i"))

    def test_acento_combinante_sem_avanco(self):
        self.assertEqual(largura_texto("á", 20), largura_texto("a", 20))

    def test_titulo_escala_pelo_tamanho(self):
        texto = "Consultoria de SEO"
        self.assertAlmostEqual(
            largura_texto(texto, 20) / largura_texto(texto, 14), 20 / 14)


if __name__ == "__main__":
    unittest.main()
