"""
Создать csv файл с данными следующей структуры:
Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу.
Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+
"""

from files.csv_utils import csv_write, csv_age_sort


def main():
    fields = [
        'Name',
        'Firstname',
        'Age'
    ]

    data_input = [
        [
            'Igor',
            'Petrovich',
            41
        ],
        [
            'Maria',
            'Pavlova',
            24
        ],
        [
            'Egor',
            'Mahov',
            9
        ],
        [
            'Andrei',
            'Balahov',
            32
        ],
        [
            'Nastya',
            'Lyashko',
            16
        ],
    ]
    csv_write('files_10_people.csv', fields, data_input)
    fields_sorted = [
        '1-12',
        '13-18',
        '19-25',
        '26-40',
        '40+'
    ]

    data_output = csv_age_sort(data_input, [[0, 0, 0, 0, 0]])
    csv_write('files_10_people_sort.csv', fields_sorted, data_output)


if __name__ == '__main__':
    main()
