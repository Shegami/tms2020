"""
Создать функцию, которая принимает на вход
неопределенное количество именованных аргументов
и выводит на экран те из них, длина ключа которых четна
"""

from funcs.funcs_07 import len_even


def test_len():
    result = len_even(a=23, abc=17, c=9, ddsa=20)
    assert result == {'ddsa': 20}
