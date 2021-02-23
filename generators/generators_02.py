"""
Создать бесконечный генератор случайных чисел.
Генератор должен принимать диапазон случайных чисел и смещение
Пример: a = 1, b = 10, diff = 10
"""

from time import sleep
from random import randint


def create_generator(first, last, diff):
    while True:
        yield randint(first, last)
        first += diff
        last += diff
        sleep(1)


my_generator = create_generator(1, 10, 10)
for number in my_generator:
    print(number)
