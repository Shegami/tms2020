"""
Написать программу, в которой вводятся два операнда
Х и Y и знак операции sign (+, –, /, *).
Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак
операции, а также на ввод Y=0 при делении. Организовать
возможность многократных вычислений без перезагрузки программа
(т.е. построить бесконечный цикл). В качестве символа
прекращения вычислений принять ‘0’ (т.е. sign='0').
"""


def result_z(x, y, sign):
    while True:
        if sign == '0':
            break
        else:
            if sign != '/' and '+' and '*' and '-':
                print('Wrong sign')
            else:
                if sign == '+':
                    z = x + y
                elif sign == '-':
                    z = x - y
                elif sign == '/':
                    if y == 0:
                        print('Division by zero')
                        sign = input('sign: ')
                        x = int(input('x: '))
                        y = int(input('y: '))
                        continue
                    else:
                        z = x / y
                elif sign == '*':
                    z = x * y
                print(f'Answer: {z}')
        sign, x, y = input('sign: '), int(input('x: ')), int(input('y: '))


def main():
    result_z(input('sign: '), int(input('x: ')), int(input('y: ')))


if __name__ == '__main__':
    main()
