"""
Имеется текстовый файл. Переписать в другой файл все его строки
с заменой в них символа 0 на символ 1 и наоборот.
"""


def zero_to_one(file, new_file):
    with open(file) as my_file:
        file_lines = my_file.readlines()
    with open(new_file, 'w') as my_new_file:
        for i in range(len(file_lines)):
            if '0' or '1' in file_lines[i]:
                line_to_list = list(file_lines[i])
                for elem in range(len(line_to_list)):
                    if line_to_list[elem] == '0':
                        line_to_list[elem] = '1'
                    elif line_to_list[elem] == '1':
                        line_to_list[elem] = '0'
                file_lines[i] = ''.join(line_to_list)
        my_new_file.writelines(file_lines)


def main():
    file = 'files_04.txt'
    new_file = 'files_04_new.txt'
    zero_to_one(file, new_file)


if __name__ == '__main__':
    main()
