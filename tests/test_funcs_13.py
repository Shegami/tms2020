"""
Дан массив целых чисел A. Найти суммы положительных
и отрицательных элементов массива, используя
функцию определения суммы.
"""

from funcs.funcs_13 import summa


def test_summa():
    positive, negative = summa([1, 2, 3])
    assert positive == 6
    assert negative == 0
