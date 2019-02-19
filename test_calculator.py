import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        print("Setup")

    def test_add_two_numbers(self):
        print("Test add two numbers")
        result = self.calculator.add(3, 6)
        self.assertEqual(9, result)

    def test_subtract_two_numbers(self):
        print("Test subtract two numbers")
        result = self.calculator.subtract(9, 6)
        self.assertEqual(3, result)

    def test_multiply_two_numbers(self):
        print("Test multiply two numbers")
        result = self.calculator.multiply(2, 4)
        self.assertEqual(8, result)

    def test_divide_two_numbers(self):
        print("Test divide two numbers")
        result = self.calculator.divide(10, 2)
        self.assertEqual(5, result)


unittest.main()
