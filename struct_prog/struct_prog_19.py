"""
Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
"""


def summ_n(n):
    s = 1
    for i in range(2, n+1):
        s += 1 / i
    print(s)


def main():
    summ_n(int(input('Your number: ')))


if __name__ == '__main__':
    main()
