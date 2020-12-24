"""
Дан список чисел.
Посчитать сколько раз встречается каждое число.
Использовать функцию.

Подсказка: для хранения данных использовать словарь.
Для проверки нахождения элемента в словаре
использовать метод get(), либо оператор in
"""


def numb_count(listt):
    dictt = {}
    for elem in listt:
        if elem not in dictt.keys():
            dictt[elem] = 1
        else:
            dictt[elem] += + 1
    return dictt


def main():
    listt = [1, 2, 1, 2, 3, 4, 5, 2, 3, 4]
    dictt = numb_count(listt)
    print(dictt)


if __name__ == '__main__':
    main()
