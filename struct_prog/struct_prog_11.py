"""
Дан список целых чисел.
Создать новый список, каждый элемент которого
равен исходному элементу умноженному на -2
"""

listt = [1, 2, 5, 12, 213, 712]
i = 0
listt_new = []

while True:
    if i == len(listt):
        break
    else:
        listt_new.append(listt[i] * -2)
        i += 1
print(listt_new)
