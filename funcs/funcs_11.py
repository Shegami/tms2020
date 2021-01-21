"""
Написать функцию по решению квадратных уравнений.
"""


def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 'Корней нет'
    elif D == 0:
        return (-b + D ** 0.5) / (2 * a)
    else:
        root = (-b + D ** 0.5) / (2 * a)
        root_2 = (-b - D ** 0.5) / (2 * a)
        return root, root_2


def main():
    print(discriminant(1, 12, 36))


if __name__ == '__main__':
    main()
