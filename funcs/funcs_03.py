"""
Написать программу для нахождения факториала.
Факториал натурального числа n определяется,
как произведение всех натуральных чисел
от 1 до n включительно
"""


def fact(n):
    if n == 0:
        return 1
    else:
        numb = 1
        for i in range(1, n+1):
            numb *= i
        return numb


def main():
    result = fact(4)
    print(result)


if __name__ == '__main__':
    main()
