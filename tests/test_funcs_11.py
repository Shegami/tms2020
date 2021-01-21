"""
Написать функцию по решению квадратных уравнений.
"""

from funcs.funcs_11 import discriminant


def test_discriminant():
    result = discriminant(1, 12, 36)
    assert result == -6
