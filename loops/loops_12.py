"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы, превосходящих
среднее арифметическое значение элементов матрицы
и сумма индексов которых четна.
"""

from random import randint


def create_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for elem in range(m):
            row.append(randint(0, 9))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def average_matrix(matrix):
    counter = 0
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
            counter += 1
    avg = summ / counter
    return avg


def number_matrix(matrix, avg):
    counter = 0
    for row in matrix:
        for elem in row[::2]:
            if elem > avg:
                counter += 1
    return counter


def main():
    A = create_matrix(3, 3)
    print_matrix(A)
    avg = average_matrix(A)
    print(avg)
    number = number_matrix(A, avg)
    print(number)


if __name__ == '__main__':
    main()
