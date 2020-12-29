"""
Реализовать функцию возвращающую матрицу.
На вход принимает n - размерность матрицы,
random_from(по-умолчанию 1), random_to(по-умолчанию(9))
"""

from random import randint


def create_matrix(n, random_from=1, random_to=9):
    M = []
    for row in range(n):
        row = []
        for elem in range(n):
            row.append(randint(random_from, random_to))
        M.append(row)
    return M


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    matrix = create_matrix(3, 5, 27)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
