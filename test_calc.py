import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.evaluate("2 + 3"), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.evaluate("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.evaluate("3 * 4"), 12)

    def test_division(self):
        self.assertEqual(self.calc.evaluate("10 / 2"), 5)

    def test_precedence(self):
        self.assertEqual(self.calc.evaluate("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(self.calc.evaluate("(2 + 3) * 4"), 20)

    def test_invalid_char_raises(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("2 + import os")


if __name__ == "__main__":
    unittest.main()
