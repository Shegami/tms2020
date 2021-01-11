"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""


def plus_3_lines(file):
    with open(file, 'a') as my_file:
        my_file.write('\n')
        for line in range(3):
            my_file.writelines([input('Введите строку: '), '\n'])


def main():
    file = 'files_03.txt'
    plus_3_lines(file)


if __name__ == '__main__':
    main()
