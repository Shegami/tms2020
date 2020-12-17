"""
Написать программу для работы с матрицами:
1) Создание
2) Вывод
3) Сумма всех элементов
4) Нахождение максимального элемента
5) Нахождение минимального элемента.
"""

from random import randint


def create_matrix(x, y):
    matrix = []
    for i in range(x):
        row = []
        for q in range(y):
            row.append(randint(0, 9))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def summ_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    return summ


def max_elem_matrix(matrix):
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem


def min_elem_matrix(matrix):
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem


def main():
    M = create_matrix(2, 2)
    print_matrix(M)
    suma = summ_matrix(M)
    max_elem = max_elem_matrix(M)
    min_elem = min_elem_matrix(M)
    print(suma, max_elem, min_elem, sep='\n')


if __name__ == '__main__':
    main()
