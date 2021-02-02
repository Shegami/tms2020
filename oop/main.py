from oop.matrix import Matrix,\
                       max_elem, min_elem, sum_elem


def main():
    matrix = Matrix(3, 3, 1, 9)
    print(matrix)
    print(max_elem(matrix))
    print(min_elem(matrix))
    print(sum_elem(matrix))


if __name__ == '__main__':
    main()
