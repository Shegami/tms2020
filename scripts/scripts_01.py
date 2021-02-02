"""
Создать скрипт, который при запуске принимает
неопределенное количество аргументов и считает
сумму тех из них, что являются цифрами.
Пример:
python test.py 1 2 3 4 a b 5 6 -->  21
"""

import sys


def summ(args):
    summa = 0
    for i in args[1:]:
        if i.isdigit():
            summa += int(i)
    return summa


print(summ(sys.argv))


def main():
    pass


if __name__ == '__main__':
    main()
