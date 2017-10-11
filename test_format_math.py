"""Tests for format_equation.py"""
import unittest
from fractions import Fraction
import format_math

MDASH = u'\u2014'


class TestFormatting(unittest.TestCase):
    def test_equation(self):
        equation = {'x': Fraction(1, 2), 'b': Fraction(1, 2)}
        expected = '    1    1\ny = ' + MDASH + 'x + ' + MDASH + '\n    2    2'
        self.assertEqual(format_math.equation(equation), expected)

        equation = {'x': Fraction(-3, 2), 'b': Fraction(-1, 2)}
        line1 = '      3    1\n'
        line2 = 'y = ' + '- ' + MDASH + 'x - ' + MDASH + '\n'
        line3 = '      2    2'
        expected = line1 + line2 + line3
        self.assertEqual(format_math.equation(equation), expected)

        equation = {'x': Fraction(10, 2), 'b': Fraction(13, 6)}
        line1 = '         13\n'
        line2 = 'y = 5x + ' + MDASH * 2 + '\n'
        line3 = '         6 '
        expected = line1 + line2 + line3
        self.assertEqual(format_math.equation(equation), expected)


if __name__ == '__main__':
    unittest.main()
