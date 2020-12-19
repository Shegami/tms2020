"""
Дано число. Найти сумму и произведение его цифр.
"""


def sum_mult(number):
    summ = mult = number[0]
    for i in number[1::]:
        summ += i
        mult *= i
    print(summ, mult)


def main():
    number = int(input('Your number: '))
    sum_mult(number)


if __name__ == '__main__':
    main()
