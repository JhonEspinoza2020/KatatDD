import unittest
from src.logica.conjunto import conjunto

class MyTestCase(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])

    self.assertIsNone(conjunto.promedio())
