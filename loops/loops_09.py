"""
Создать квадратную матрицу разменостью n
и заполнить ее случайными значениями от 1 до 9
"""
from random import randint

n = int(input())
m = int(input())
A = []

for i in range(n):
    row = []
    for q in range(m):
        row.append(randint(1, 9))
    print(row)
    A.append(row)
