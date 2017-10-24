"""Tests for format_equation.py"""
import unittest
from fractions import Fraction
import format_math

MDASH = u'\u2014'


class TestFormatting(unittest.TestCase):

    def test_equation_with_two_positive_fractions(self):
        """
        equation() displays fractions in 3 lines with a MDASH in between
        """
        equation = {'x': Fraction(1, 2), 'b': Fraction(1, 3)}
        expected = '    1    1\ny = ' + MDASH + 'x + ' + MDASH + '\n    2    3'
        self.assertEqual(format_math.equation(equation), expected)

    def test_equation_with_two_negative_fractions(self):
        """
        equation() shows negative sign on x and b
        """
        equation = {'x': Fraction(-3, 2), 'b': Fraction(-1, 2)}
        line1 = '      3    1\n'
        line2 = 'y = ' + '- ' + MDASH + 'x - ' + MDASH + '\n'
        line3 = '      2    2'
        expected = line1 + line2 + line3
        self.assertEqual(format_math.equation(equation), expected)

    def test_equation_with_two_positive_double_digits_fractions(self):
        """
        equation() shows x and b in one line whenever it's possible
        """
        equation = {'x': Fraction(10, 2), 'b': Fraction(12, 6)}
        line1 = '          \n'
        line2 = 'y = 5x + 2\n'
        line3 = '          '
        expected = line1 + line2 + line3
        self.assertEqual(format_math.equation(equation), expected)


if __name__ == '__main__':
    unittest.main()
