"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
"""


def str_to_list(string):
    string = ' '.join(string.split()[::-1])
    print(string)


def main():
    string = input('Your text: ')
    str_to_list(string)


if __name__ == '__main__':
    main()
