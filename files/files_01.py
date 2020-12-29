"""
Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""


def main():
    # a
    print('# a')
    my_file = open('files_01.txt')
    print(my_file.readline(), end='')
    my_file.close()

    # b
    print('# b')
    my_file = open('files_01.txt')
    i = 1
    while True:
        line = my_file.readline()
        if i == 5:
            print(line, end='')
            break
        i += 1
    my_file.close()

    # c
    print('# c')
    my_file = open('files_01.txt')
    i = 1
    while i != 6:
        line = my_file.readline()
        print(line, end='')
        i += 1
    my_file.close()

    # d
    print('# d')
    my_file = open('files_01.txt')
    start = int(input('Choose line to start: '))
    stop = int(input('Choose line to stop: '))
    i = 1
    while True:
        line = my_file.readline()
        if start <= i <= stop:
            print(line, end='')
        i += 1
        if i > 19:
            break
    my_file.close()

    # e
    print('# e')
    my_file = open('files_01.txt')
    while line := my_file.readline():
        print(line, end='')
    my_file.close()


if __name__ == '__main__':
    main()
