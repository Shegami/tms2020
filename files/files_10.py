"""
Создать csv файл с данными следующей структуры:
Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу.
Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+
"""

from files.csv_utils import csv_write


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
    fields_sorted = {
        '1-12': 0,
        '13-18': 0,
        '19-25': 0,
        '26-40': 0,
        '40+': 0
    }

    for i in range(len(data_input)):
        if data_input[i][2] < 13:
            fields_sorted['1-12'] += 1
        elif 12 < data_input[i][2] < 19:
            fields_sorted['13-18'] += 1
        elif 18 < data_input[i][2] < 26:
            fields_sorted['19-25'] += 1
        elif 25 < data_input[i][2] < 41:
            fields_sorted['26-40'] += 1
        else:
            fields_sorted['40+'] += 1

    csv_write('files_10_people_sort.csv', fields_sorted.keys(), [fields_sorted.values()])


if __name__ == '__main__':
    main()
    
