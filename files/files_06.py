"""
Имеются два текстовых файла с одинаковым числом строк.
Выяснить, совпадают ли их строки.
Если нет, то получить номер первой строки,
в которой эти файлы отличаются друг от друга.
"""


def numb_of_different_line(file_1, file_2):
    with open(file_1, 'r') as first_file:
        lines_fst_file = first_file.readlines()
    with open(file_2, 'r') as second_file:
        lines_sec_file = second_file.readlines()
    for i in range(len(lines_fst_file)):
        if lines_fst_file[i] != lines_sec_file[i]:
            different_line = i+1
            return different_line
    return 'Строки совпадают'


def main():
    file_1 = 'files_06_1.txt'
    file_2 = 'files_06_2.txt'
    value = numb_of_different_line(file_1, file_2)
    print(f'№ первой отличной строки - {value}')


if __name__ == '__main__':
    main()
