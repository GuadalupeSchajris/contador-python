import unittest
from main import contar_letras

class TestContarLetras(unittest.TestCase):

    def test_cadena_vacia(self):
        self.assertEqual(contar_letras(""), 0)

    def test_solo_letras(self):
        self.assertEqual(contar_letras("abc"), 3)
        self.assertEqual(contar_letras("Hola"), 4)

    def test_letras_con_espacios(self):
        self.assertEqual(contar_letras("a b c"), 3)
        self.assertEqual(contar_letras("Hola Mundo"), 9)

    def test_solo_numeros(self):
        self.assertEqual(contar_letras("123"), 0)

    def test_letras_con_numeros(self):
        self.assertEqual(contar_letras("a1b2c"), 3)

    def test_letras_con_puntuacion(self):
        self.assertEqual(contar_letras("a.b,c!"), 3)
        self.assertEqual(contar_letras("¿Qué?"), 3)

    def test_mezcla(self):
        self.assertEqual(contar_letras("Hola123!"), 4)
        self.assertEqual(contar_letras("a b c 1 2 3 . , !"), 3)

if __name__ == "__main__":
    unittest.main()