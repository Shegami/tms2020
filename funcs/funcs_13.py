"""
Дан массив целых чисел A. Найти суммы положительных
и отрицательных элементов массива, используя
функцию определения суммы.
"""


def summa(A):
    positive_sum = 0
    negative_sum = 0
    for i in A:
        if i > 0:
            positive_sum += i
        else:
            negative_sum += i
    print(f'Сумма положительных: {positive_sum}'
          f'\nСумма отрицательных: {negative_sum}')


def main():
    summa(A=[1, 2, 4, -5, -10, -1])


if __name__ == '__main__':
    main()
