"""
Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего)
"""

from random import randint


def numb_rise(listt):
    i = 1
    number = 0
    while i != len(listt) - 1:
        if listt[i - 1] < listt[i] > listt[i + 1]:
            i += 1
            number += 1
        else:
            i += 1
    if listt[-1] > listt[-2]:
        number += 1
    print(number)


def main():
    listt = []
    for i in range(10):
        listt.append(randint(0, 100))
    print(listt)
    numb_rise(listt)


if __name__ == '__main__':
    main()
