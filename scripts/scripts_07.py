"""
Написать скрипт - таймер.
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время
для фокусировки(по-умолчанию 25 минут),
длину перерыва(по-умолчанию 5 минут), количество
циклов(по-умолчанию 4) и название задачи.
Программа указывает оставшееся время фокусировки,
после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки.
Программа должна вести файл лога о всех запусках.
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
    '-ft',
    '--focus_time',
    default=datetime.timedelta(minutes=25)
)
parser.add_argument(
    '-bt',
    '--break_time',
    default=datetime.timedelta(minutes=5)
)
parser.add_argument(
    '-сs',
    '--cycles',
    type=int,
    default=4
)
parser.add_argument(
    '-tn',
    '--task_name',
    required=True
)

args = parser.parse_args()

for n in range(int(args.cycles)):
    print(f'Time to focus is {args.focus_time} min')
    time.sleep(int(args.focus_time) * 60)
    print(f'Time to break for {args.break_time} min')
    time.sleep(int(args.break_time) * 60)

with open(os.path.join(
        dir_path,
        'scripts_07_log.txt'
        ), 'w') as my_file:
    my_file.writelines('\n'.join([
        f'User name: {args.first_name}',
        f'User last name: {args.last_name}',
        f'Time to focus: {args.focus_time} min',
        f'Time to break: {args.break_time} min',
        f'Cycles: {args.cycles}'
    ]))


def main():
    pass


if __name__ == '__main__':
    main()
