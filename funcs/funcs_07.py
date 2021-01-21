"""
Создать функцию, которая принимает на вход
неопределенное количество именованных аргументов
и выводит на экран те из них, длина ключа которых четна
"""


def len_even(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            result.setdefault(key, value)
    return result


def main():
    result = len_even(a=23, bsms=17, c=9, ddsa=20)
    print(result)


if __name__ == '__main__':
    main()
