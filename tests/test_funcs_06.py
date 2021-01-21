"""
Создать функцию, которая принимает на вход неопределенное
количество аргументов и возвращает их сумму и максимальное из них.
"""

from funcs.funcs_06 import sum_max_args


def test_max_min():
    args = [1, 2, 33, 4]
    summ, maxx = sum_max_args(*args)
    assert summ == 40
    assert maxx == 33
