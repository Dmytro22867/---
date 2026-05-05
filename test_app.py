import unittest
from app import add, subtract, multiply, divide

class TestMathApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)
        self.assertEqual(divide(5, 0), "Помилка: ділення на нуль!")

if __name__ == "__main__":
    unittest.main()
