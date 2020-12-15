"""
ВВести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1
до n (включая n) используя цикл while.
"""

n = abs(int(input()))
summ = 0

while True:
    summ += n ** 3
    n -= 1
    if n == 0:
        break
print(summ)
