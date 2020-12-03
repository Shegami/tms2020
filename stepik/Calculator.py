# Калькулятор не дэбильный

a, b = float(input()), float(input())
what = input()

if what == '+':
    с = a + b
    print(str(с))
elif what == '-':
    с = a - b
    print(str(с))
elif what == '*':
    с = a * b
    print(str(с))
elif what == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        с = a / b
        print(str(с))
elif what == '**' or what == 'pow':
    с = a ** b
    print(str(с))
elif what == '%' or what == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        с = a % b
        print(str(с))
elif what == '//' or what == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        с = a // b
        print(str(с))