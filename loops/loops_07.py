"""
Получить сумму кубов натуральных чисел
от n до m используя цикл for
"""

n = int(input())
m = int(input())
summ = 0

for i in range(n, m+1):
    summ += i ** 3
print(summ)
