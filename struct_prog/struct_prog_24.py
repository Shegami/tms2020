"""
Для каждого натурального числа в промежутке
от m до n вывести все делители, кроме единицы
и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105
"""


def divider(m, n):
    for number in range(m, n+1):
        dividers = []
        for divider in range(2, number):
            if number % divider == 0:
                dividers.append(divider)
        print(f'{number}: ', end='')
        for i in dividers:
            print(i, end=' ')
        print()


def main():
    divider(100, 105)


if __name__ == '__main__':
    main()
