"""
Дан двумерный массив n × m элементов.
Определить, сколько раз встречается число 7
среди элементов массива.
"""

from random import randint

n = int(input())
m = int(input())
counter = 0
A = []

for i in range(n):
    row = []
    for q in range(m):
        row.append(randint(1, 9))
    A.append(row)

for row in A:
    for elem in row:
        if elem == 7:
            counter += 1

for listt in A:
    print(listt)
print(counter)
