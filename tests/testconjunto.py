# archivo: conjunto_test.py

import unittest

class Conjunto:

    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto) == 0:
            return None
        return sum(self.__conjunto) / len(self.__conjunto)


class MyTestCase(unittest.TestCase):

    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7])
        self.assertEqual(6, conjunto.promedio())

    def test_conjunto_nElementos_retornaPromedioNElementos(self):
        conjunto = Conjunto([2, 4, 8, 9, 10, 15])
        self.assertEqual((2 + 4 + 8 + 9 + 10 + 15) / 6, conjunto.promedio())


if __name__ == '__main__':
    unittest.main()
