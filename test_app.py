import unittest
from app import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("1 + 1"), 2)
        self.assertEqual(calculate("10 + 5"), 15)

    def test_subtraction(self):
        self.assertEqual(calculate("10 - 5"), 5)
        self.assertEqual(calculate("5 - 10"), -5)

    def test_multiplication(self):
        self.assertEqual(calculate("3 * 4"), 12)
        self.assertEqual(calculate("2 * 0"), 0)

    def test_division(self):
        self.assertEqual(calculate("20 / 4"), 5)
        self.assertEqual(calculate("5 / 2"), 2.5)

    def test_division_by_zero(self):
        self.assertEqual(calculate("5 / 0"), "Помилка: ділення на нуль")

    def test_parentheses(self):
        self.assertEqual(calculate("(2 + 3) * 4"), 20)
        self.assertEqual(calculate("2 + (3 * 4)"), 14)

    def test_invalid_expression(self):
        self.assertIn("Помилка", calculate("2 + abc"))
        self.assertIn("Помилка", calculate("2 + "))

    def test_floats(self):
        self.assertEqual(calculate("1.5 + 2.5"), 4.0)

if __name__ == "__main__":
    unittest.main()
