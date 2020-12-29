"""
Описать функцию fact2( n ), вычисляющую двойной
факториал :n!! = 1·3·5·...·n, если n — нечетное;
n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции
найти двойные факториалы пяти данных целых чисел
"""


def func2(n):
    for numb in n:
        factorial = 1
        if numb == 0 or numb == 1 or numb == 2:
            pass
        elif numb % 2 == 0:
            for i in range(2, numb+1, 2):
                factorial *= i
        else:
            for i in range(1, numb+1, 2):
                factorial *= i
        print(f'Факториал {numb} = {factorial}')


def main():
    n = [1, 6, 13, 24, 7]
    func2(n)


if __name__ == '__main__':
    main()
