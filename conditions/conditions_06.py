"""
Вычислить квадратное уравнение ax ** 2 + bx + c = 0 (*)
D = b ** 2 – 4ac;
x1,2 = (-b +/- sqrt (D)) / 2a
Предусмотреть 3 варианта:
1) Два действительных корня
2) Один действительный корень
3) Нет действительных корней
"""

a, b, c, = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c

if d > 0:
    print(f'Первый корень = {-b - d ** 0.5 / 2 * a}')
    print(f'Второй корень = {-b + d ** 0.5 / 2 * a}')
elif d == 0:
    print(f'Корень = {- b / 2 * a}')
else:
    print('Нет корней')
