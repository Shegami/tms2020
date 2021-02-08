"""
Создать скрипт, который принимает имя, фамилию и возраст
и дописывает их в файл
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-fn',
    '--first-name',
    required=True
)
parser.add_argument(
    '-ln',
    '--last-name',
    required=True
)
parser.add_argument(
    '-ag',
    '--age',
    required=True
)

args = parser.parse_args()
print('First name:', args.first_name)
print('Last name:', args.last_name)
print('Age:', args.age)

with open("scripts_02.txt", 'a') as my_file:
    my_file.write(f"First name: {args.first_name}\n"
                  f"Last name: {args.last_name}\n"
                  f"Age: {args.age}\n")


def main():
    pass


if __name__ == '__main__':
    main()
