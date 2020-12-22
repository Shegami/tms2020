"""
Дана целочисленная квадратная матрица.
Найти в каждой строке наибольший элемент
и поменять его местами с элементом главной диагонали.
"""

from random import randint


def create_matrix(a):
    matrix = []
    for row in range(a):
        row = []
        for elem in range(a):
            row.append(randint(0, 9))
        matrix.append(row)
        print(row)
    return matrix


def max_elem(matrix):
    index = 0
    for row in range(len(matrix)):
        max_elem = matrix[row][0]
        for elem in matrix[row]:
            if elem > max_elem:
                max_elem = elem
        matrix[row][index] = max_elem
        index += 1
    return matrix


def main():
    A = create_matrix(5)
    print()
    for row in max_elem(A):
        print(row)


if __name__ == '__main__':
    main()
