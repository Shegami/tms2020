"""
Рассчитать значение х определив
и использовав необходимую функции.
(x ** (1 / 2) + x) / 2
"""

from funcs.funcs_10 import divide


def test_devide():
    result = divide(0)
    assert result == 0
