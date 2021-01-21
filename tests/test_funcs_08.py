"""
Написать функцию принимающая на вход неопределенным
количеством аргументов и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое
либо среднегеометрическое.
Написать программу в виде трех функций.
"""

from funcs.funcs_08 import arithmetic_mean, \
                           geometric_mean


def test_choose():
    result = arithmetic_mean(1, 2, 3, 4)
    assert result == 2.5
    result = geometric_mean(1, 2, 3, 4)
    assert result == 2.2133638394006434
