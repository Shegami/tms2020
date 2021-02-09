"""
Написать скрипт - таймер.
Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
После программа начинает обратный отсчет выводя оставшееся время.
Программа должна хранить файл логирования с информацией
о том кто запускал программу и когда.
"""

import argparse
import os
import time
import datetime

file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)

parser = argparse.ArgumentParser()
parser.add_argument(
    '-fn',
    '--first_name',
    required=True
)
parser.add_argument(
    '-ln',
    '--last_name',
    required=True
)
parser.add_argument(
    '-hr',
    '--hour'
)
parser.add_argument(
    '-mn',
    '--minutes'
)
parser.add_argument(
    '-sc',
    '--seconds'
)

n = 3
for i in range(n):
    print(datetime.timedelta(seconds=n))
    n -= 1
    time.sleep(1)
print('Allahu Acbar!')

args = parser.parse_args()

with open(os.path.join(
        dir_path,
        'log.txt'
        ), 'w') as my_file:
    my_file.writelines('\n'.join([
        f'User name: {args.first_name}',
        f'User last name: {args.last_name}',
        f'Time access: {args.hour}.{args.minutes}.{args.seconds}'
    ]))


def main():
    pass


if __name__ == '__main__':
    main()
