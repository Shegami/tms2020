"""
Дан список целых чисел.
Подсчитать сколько четных чисел в списке.
"""

listt = [1, 2, 5, 12, 213, 712]
i = 0
counter = 0

while i != len(listt):
    if listt[i] % 2 == 0:
        counter += 1
    i += 1

print(counter)
