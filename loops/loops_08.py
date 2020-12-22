"""
Ввести два целых числа a и b ( a < b ).
Вывести в порядке возрастания все целые числа,
расположенные между a и b (включая сами числа a и b ),
а также количество n этих чисел.
"""


def ab_range(a, b):
    n = 0
    for i in range(a, b + 1):
        print(i, end=' ')
        n += 1
    print()
    print(n)


def main():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    if a < b:
        ab_range(a, b)
    else:
        print('Ошибка. a не может быть >= b')


if __name__ == '__main__':
    main()
