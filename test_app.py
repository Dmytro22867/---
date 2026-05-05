import unittest
from app import multiply

class TestMath(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 5), -5)

if __name__ == '__main__':
    unittest.main()
