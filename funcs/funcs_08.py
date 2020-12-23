"""
Написать функцию принимающая на вход неопределенным
количеством аргументов и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое
либо среднегеометрическое.
Написать программу в виде трех функций.
"""


def arithmetic_mean(args):
    summ = 0
    for elem in args:
        summ += elem
    return summ / len(args)


def geometric_mean(args):
    mult = 1
    for elem in args:
        mult *= elem
    return mult ** (1 / len(args))


def choose_mean(*args, mean_type):
    if mean_type == 'arithmetic':
        avg = arithmetic_mean(args)
    else:
        avg = geometric_mean(args)
    return avg


def main():
    avg = choose_mean(2, 4, 6, 9, 10, 11, 7, 12,
                      mean_type='arithmetic', )
    print(avg)


if __name__ == '__main__':
    main()
