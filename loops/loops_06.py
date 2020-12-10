"""
Написать программу, которая будет выводить на экран
случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""

from random import randint

while True:
    number = randint(1, 10)
    if number == 7:
        break
    print(number)
