"""
Дано число. Найти сумму и произведение его цифр.
"""


def sum_mult(number):
    summ = mult = int(number[0])
    for i in number[1::]:
        summ += int(i)
        mult *= int(i)
    print(f'Sum: {summ}, Multiple: {mult}')


def main():
    number = input('Your number: ')
    sum_mult(number)


if __name__ == '__main__':
    main()
