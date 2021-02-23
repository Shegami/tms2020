"""
Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
from time import sleep
"""

from time import sleep
from random import randint


def create_generator():
    while True:
        yield randint(0, 9)
        sleep(1)


my_generator = create_generator()
for number in my_generator:
    print(number)
