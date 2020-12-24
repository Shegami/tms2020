"""
Создать список с фамилиями.
Вывести все фамилии, которые
начинаются на П и заканчиваются на а
"""


def name(listt):
    for elem in listt:
        if elem[0] == 'П' and elem[-1] == 'а':
            print(elem)


def main():
    surnames = ['Петров', 'Сидоров', 'Павлова']
    name(surnames)


if __name__ == '__main__':
    main()
