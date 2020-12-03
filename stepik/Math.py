name = input()
if name == 'прямоугольник':
    S = float(input()) * float(input())
elif name == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif name == 'круг':
    P = 3.14
    S = P * (float(input()) ** 2)
print(S)