"""
Написать функцию принимающая на вход неопределенным
количеством аргументов и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое
либо среднегеометрическое.
Написать программу в виде трех функций.
"""


def arithmetic_mean(args):
    summ = 0
    n = 0
    for elem in args:
        summ += elem
        n += 1
    return summ / n


def geometric_mean(args):
    mult = 1
    n = 0
    for elem in args:
        mult *= elem
        n += 1
    return mult ** (1 / n)


def choose_mean(*args, mean_type):
    if mean_type == 'arithmetic':
        avg = arithmetic_mean(args)
        return avg
    else:
        avg = geometric_mean(args)
        return avg


def main():
    avg = choose_mean(1, 2, 12, 32, 345, 21, 354, 92, 81,
                      mean_type='geometric')
    print(avg)


if __name__ == '__main__':
    main()
