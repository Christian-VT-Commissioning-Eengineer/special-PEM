import unittest

from calculator import calcular_total


class CalcularTotalTests(unittest.TestCase):
    def test_suma_sin_impuesto(self):
        self.assertEqual(calcular_total([10, 20, 30]), 60)

    def test_suma_con_impuesto(self):
        self.assertEqual(calcular_total([100, 50], 0.19), 178.5)

    def test_impuesto_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total([100], -0.1)


if __name__ == "__main__":
    unittest.main()

