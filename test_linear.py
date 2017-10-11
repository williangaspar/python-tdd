"""Tests for linear.py"""
import unittest
from fractions import Fraction
import linear


class TestLienar(unittest.TestCase):

    def test_calc_slope(self):
        coordinates = [{'x': 0, 'y': 1}, {'x': -6, 'y': -2}]
        self.assertEqual(linear.calc_slope(coordinates), Fraction(1, 2))

        coordinates = [{'x': -5, 'y': -2}, {'x': 6, 'y': 4}]
        self.assertEqual(linear.calc_slope(coordinates), Fraction(6, 11))

        coordinates = [{'x': 2, 'y': -3}, {'x': -4, 'y': 5}]
        self.assertEqual(linear.calc_slope(coordinates), Fraction(-4, 3))

    def test_calc_equation(self):
        coordinates = [{'x': 0, 'y': 1}, {'x': -6, 'y': -2}]
        equation = linear.calc_equation(coordinates)
        expected = {'x': Fraction(1, 2), 'b': Fraction(1, 1)}
        self.assertEqual(equation, expected)

        coordinates = [{'x': -5, 'y': -2}, {'x': 6, 'y': 4}]
        equation = linear.calc_equation(coordinates)
        expected = {'x': Fraction(6, 11), 'b': Fraction(8, 11)}
        self.assertEqual(equation, expected)

        coordinates = [{'x': 2, 'y': -3}, {'x': -4, 'y': 5}]
        equation = linear.calc_equation(coordinates)
        expected = {'x': Fraction(-4, 3), 'b': Fraction(-1, 3)}
        self.assertEqual(equation, expected)


if __name__ == '__main__':
    unittest.main()
