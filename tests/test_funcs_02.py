"""
Написать программу для работы с матрицами:
1) Создание
2) Вывод
3) Сумма всех элементов
4) Нахождение максимального элемента
5) Нахождение минимального элемента.
"""

from funcs.funcs_02 import create_matrix, summ_matrix,\
                           max_elem_matrix, min_elem_matrix


def test_create_matrix():
    matrix = create_matrix(3, 3)
    assert type(matrix) == list
    assert len(matrix) == 3
    assert len(matrix[0]) == 3
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            assert type(matrix[i][j]) == int


matrix = [[6, 4, 3], [9, 4, 2], [1, 0, 7]]


def test_sum_matrix():
    result = summ_matrix(matrix)
    assert result == 36


def test_max_elem():
    result = max_elem_matrix(matrix)
    assert result == 9


def test_min_elem():
    result = min_elem_matrix(matrix)
    assert result == 0
