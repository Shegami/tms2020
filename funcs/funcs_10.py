"""
Рассчитать значение х определив
и использовав необходимую функции.
"""


def divide(x):
    return (x ** (1 / 2) + x) / 2


def main():
    result_1 = divide(5)
    result_2 = divide(12)
    result_3 = divide(19)
    print(result_1 + result_2 + result_3)


if __name__ == '__main__':
    main()
