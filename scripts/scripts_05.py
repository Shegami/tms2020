"""
Создать скрипт.
Программа принимает имя папки и имя файла с расширением.
Создает папку и создает в ней файл.
Если расширение файла py - записывает в файл следующее:
"""

import os
import sys


file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
os.mkdir(os.path.join(
    dir_path,
    sys.argv[1]
))

if sys.argv[2][-1:-3:-1] == 'yp':
    with open(os.path.join(
            dir_path,
            sys.argv[1],
            sys.argv[2],
            ), 'w') as my_file:
        my_file.writelines('\n'.join([
            'def main():',
            '    pass',
            '',
            '',
            "if __name__ == '__main__':",
            '    main()'
            ]))
else:
    with open(os.path.join(
            dir_path,
            sys.argv[1],
            sys.argv[2],
            ), 'w') as my_file:
        pass


def main():
    pass


if __name__ == '__main__':
    main()
