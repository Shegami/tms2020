"""
Создать скрипт. Программа принимает имя папки и имя файла.
Создает папку и создает в ней файл.
"""

import sys
import os

file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
os.mkdir(os.path.join(dir_path, sys.argv[1]))


with open(os.path.join(
        dir_path,
        sys.argv[1],
        sys.argv[2]),
        'w') as file:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
