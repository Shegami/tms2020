"""
Создать функцию, которая принимает на вход
неопределенное количество именованных аргументов
и выводит на экран те из них, длина ключа которых четна
"""


def len_even(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)


def main():
    len_even(a=23, bsnms=17, c=9, ddsa=20)


if __name__ == '__main__':
    main()
