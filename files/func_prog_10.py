"""
Создать lambda функцию, которая принимает на вход
неопределенное количество именных аргументов и
выводит словарь с ключами удвоенной длины.
{‘abc’: 5} -> {‘abcabc’: 5}
"""


def main():
    print((lambda **kwargs:
           {key*2: value for key, value in kwargs.items()})
          (a=2, b=3, c=4)
          )


if __name__ == '__main__':
    main()
