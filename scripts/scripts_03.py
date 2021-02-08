"""
Создать скрипт, который принимает имя папки и создает ее рядом со скриптом
"""

import os
import sys


file_path = os.path.realpath(__file__)
print(file_path)
dir_name = os.path.dirname(file_path)
print(dir_name)
os.mkdir(f'{dir_name}/{sys.argv[1]}')


def main():
    pass


if __name__ == '__main__':
    main()
