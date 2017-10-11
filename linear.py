"""Calculates linear equations"""
from fractions import Fraction


def calc_equation(coordinates):
    """coordinates = [{x, y}, {x, y}]"""
    slope = calc_slope(coordinates)
    return {'x': slope, 'b': coordinates[0].get('y') - slope * coordinates[0].get('x')}


def calc_slope(coordinates):
    """coordinates = [{x, y}, {x, y}]"""
    y_coordinates = coordinates[0].get('y') - coordinates[1].get('y')
    x_coordinates = coordinates[0].get('x') - coordinates[1].get('x')
    return Fraction(y_coordinates, x_coordinates)
