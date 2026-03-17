import unittest

from utils import (
    meu_buscar_chave,
    meu_dividir,
    meu_normalizar_nome,
    meu_somar_itens,
)


class UtilsTests(unittest.TestCase):
    def test_meu_somar_itens_com_lista_vazia(self):
        self.assertEqual(meu_somar_itens([]), 0.0)

    def test_meu_somar_itens_ignora_booleano(self):
        self.assertEqual(meu_somar_itens([1, True, 2]), 3.0)

    def test_meu_somar_itens_falha_para_texto(self):
        with self.assertRaises(TypeError):
            meu_somar_itens([1, "2"])

    def test_meu_dividir(self):
        self.assertEqual(meu_dividir(10, 2), 5.0)

    def test_meu_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            meu_dividir(10, 0)

    def test_meu_normalizar_nome(self):
        self.assertEqual(meu_normalizar_nome("  mAtHeUs   silva  "), "Matheus Silva")

    def test_meu_buscar_chave(self):
        self.assertEqual(meu_buscar_chave({"nome": "Matheus"}, "nome"), "Matheus")
        self.assertIsNone(meu_buscar_chave({}, "nao_existe"))
        self.assertEqual(meu_buscar_chave({}, "nao_existe", "padrão"), "padrão")


if __name__ == "__main__":
    unittest.main()
