"""
Имеется текстовый файл.
Все четные строки этого файла записать во второй файл,
а нечетные — в третий файл. Порядок следования строк сохраняется.
"""


def odd_even_files(file, file_odd, file_even):
    with open(file, 'r') as main_file:
        file_lines = main_file.readlines()
    with open(file_odd, 'w') as odd_file:
        for i in file_lines[::2]:
            odd_file.write(i)
    with open(file_even, 'w') as even_file:
        for i in file_lines[1::2]:
            even_file.write(i)


def main():
    file = 'files_05.txt'
    file_odd = 'files_05_odd.txt'
    file_even = 'files_05_even.txt'
    odd_even_files(file, file_odd, file_even)


if __name__ == '__main__':
    main()
