"""
Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все
четные элементы и сохранить в другой файл
"""

from random import randint
import json


def create_matrix(x):
    matrix = []
    for row in range(x):
        row = []
        for elem in range(x):
            row.append(randint(0, 9))
        matrix.append(row)
    return matrix


def matrix_to_json(matrix):
    with open('files_07.json', 'w') as my_file:
        dict_matrix = {'matrix': matrix}
        data = json.dumps(dict_matrix)
        my_file.write(data)


def json_even_to_0():
    with open('files_07.json') as json_file:
        data = json.loads(json_file.read())
    print(data)
    matrix = data['matrix']
    print(matrix)
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem % 2 == 0:
                matrix[i][j] = 0
    with open('files_07_0.json', 'w') as my_file:
        dict_matrix = {'matrix': matrix}
        data = json.dumps(dict_matrix)
        my_file.write(data)


def main():
    matrix = create_matrix(3)
    matrix_to_json(matrix)
    json_even_to_0()


if __name__ == '__main__':
    main()
