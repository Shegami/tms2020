"""
Дан список чисел.
Вернуть список, где каждый число переведено в строку
"""


def main():
    numb_str = list(map(str, [1, 2, 3, 4, 5, 6]))
    print(numb_str)


if __name__ == '__main__':
    main()
