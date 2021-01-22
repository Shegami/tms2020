"""
Создать функцию, которая принимает на вход неопределенное
количество аргументов и возвращает их сумму и максимальное из них.
"""


def sum_max_args(*args):
    summ = 0
    maxx = args[0]
    for elem in args:
        summ += elem
        if elem > maxx:
            maxx = elem
    return summ, maxx


def main():
    summ, maxx = sum_max_args(234, 4, 3, 6, 5, 12, 28)
    print(summ, maxx)


if __name__ == '__main__':
    main()
