"""
Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность,
в которой первые два числа равны либо 1 и 1, либо 0 и 1,
а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
"""


def fib_15_for(listt):
    for i in range(13):
        listt.append(listt[i] + listt[i + 1])
    print(listt)


def fib_15_while(listt):
    i = 0
    while True:
        if len(listt) != 15:
            listt.append(listt[i] + listt[i + 1])
            i += 1
        else:
            print(listt)
            break


def main():
    numbers = [int(input('Insert 0 or 1: ')), 1]
    fib_15_for(numbers)
    #fib_15_while(numbers)


if __name__ == '__main__':
    main()
