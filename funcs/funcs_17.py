"""
Описать функцию Sin1( x , ε ) вещественного типа
(параметры x ,ε — вещественные, ε > 0), находящую
приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ...
+ (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε.
С помощью Sin1 найти приближенное значение синуса для
данного x при шести данных ε
"""

import math


def sin1(x, n):
    sin_x = (((-1) ** n) * (x ** (2 * n + 1))) / fact(n)
    return sin_x


def fact(n):
    factorial = 2 * n + 1
    result = 1
    for numb in range(1, factorial+1):
        result *= numb
    return result


def main():
    sin = sin1(math.pi/6, 0)
    print(sin)


if __name__ == '__main__':
    main()
