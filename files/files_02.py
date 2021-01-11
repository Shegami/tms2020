"""
Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры.
"""


def create_file(file):
    with open(file, 'w') as my_file:
        for line in range(6):
            my_file.writelines([input('Введите текст строки: '), '\n'])


def main():
    file = 'files_02.txt'
    create_file(file)


if __name__ == '__main__':
    main()
