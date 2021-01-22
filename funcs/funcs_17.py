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


def sin1(x, eps):
    n = 0
    value = x
    summ = 0
    while abs(value) >= eps:
        value = (-1) ** n * x ** (2 * n + 1) / fact(n)
        n += 1
        summ += value
    return summ


def fact(number):
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
    return result


def main():
    eps = 0.01
    number = math.pi/6
    for i in range(0, 4):
        f = sin1(number, eps)
        eps /= 10
        print(f'eps= {eps}, sin({number})= {f}')


if __name__ == '__main__':
    main()
