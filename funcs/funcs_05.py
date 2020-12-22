"""
Создать функцию, принимающая на вход неопределенное
количество аргументом и возвращающая сумму args[i] * i
"""


def sum_args(*args):
    summ = 0
    for i, v in enumerate(args):
        summ += i * v
    return summ


def main():
    summa = sum_args(2, 3, 5, 8, 12, 26)
    print(summa)


if __name__ == '__main__':
    main()
