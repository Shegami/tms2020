"""
Создать файл matrix.py. Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности: n, m
и диапазона случайных чисел: a, b),
по-умолчанию (матрица 5 на 5 где все элементы равны нулю),
копирования) , переопределить магический метод __str__ для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix.
Функции позволяют искать максимальный элемент матрицы,
минимальный, сумму всех элементов.
Создать в файле main.py матрицу.
Воспользоваться всеми описанными функциями и методами
"""

from random import randint


class Matrix:
    def __init__(self,
                 n=5, m=5,
                 a=0, b=0):
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self.data = [[randint(a, b) for n in range(n)] for m in range(m)]

    def __str__(self):
        return '\n'.join(str(i) for i in self.data)


def max_elem(matrix):
    max_e = matrix.data[0][0]
    for row in matrix.data:
        for elem in row:
            if elem > max_e:
                max_e = elem
    return max_e


def min_elem(matrix):
    min_e = matrix.data[0][0]
    for row in matrix.data:
        for elem in row:
            if elem < min_e:
                min_e = elem
    return min_e


def sum_elem(matrix):
    summa = 0
    for row in matrix.data:
        for elem in row:
            summa += elem
    return summa


def main():
    pass


if __name__ == '__main__':
    main()
