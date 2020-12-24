"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им
все четные по значению элементы.
"""

from random import randint


def max_number(listt):
    maxx = listt[0]
    for number in listt:
        if number > maxx:
            maxx = number
    for i in range(len(listt)):
        if listt[i] % 2 == 0:
            listt[i] = maxx
    return listt


def main():
    listt = []
    for i in range(19):
        listt.append(randint(0, 101))
    numbers = max_number(listt)
    print(numbers)


if __name__ == '__main__':
    main()
