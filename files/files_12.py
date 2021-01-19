"""
Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год.
Найти самую раннюю дату.
"""

from files.csv_utils import csv_write, \
                            csv_read
from datetime import date


def main():
    fields = [
        'Date'
    ]

    data = [
        [
            date(2021, 1, 16)
        ],
        [
            date(2021, 3, 23)
        ],
        [
            date(2021, 1, 17)
        ],
        [
            date(2021, 1, 29)
        ],
        [
            date(2021, 2, 15)
        ],
        [
            date(2021, 1, 7)
        ],
        [
            date(2021, 4, 3)
        ],
        [
            date(2021, 1, 30)
        ],
        [
            date(2020, 1, 30)
        ],

    ]

    csv_write('files_12_dates.csv', fields, data)
    _, data = csv_read('files_12_dates.csv')
    min_date = data[0][0]
    for i in range(1, len(data)):
        if data[i][0] < min_date:
            min_date = data[i][0]
    print(min_date)


if __name__ == '__main__':
    main()
