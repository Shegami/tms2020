"""
Создать csv файл с данными о ежедневной погоде.
Структура: Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду(скорость ветра и градусы)
для Минск за последние 7 дней.
"""

from files.csv_utils import csv_write,\
                            csv_read,\
                            csv_degree_avg,\
                            csv_wind_spd

from datetime import date


def main():
    fields = [
        'Date',
        'Place',
        'Degree',
        'Wind speed'
    ]
    data = [
        [
            date(2020, 1, 15),
            'Minsk',
            -19,
            13
        ],
        [
            date(2020, 1, 16),
            'Minsk',
            -16,
            7
        ],
        [
            date(2020, 1, 17),
            'Minsk',
            -17,
            10
        ],
        [
            date(2020, 1, 18),
            'Minsk',
            -14,
            5
        ],
        [
            date(2020, 1, 19),
            'Minsk',
            -21,
            9
        ],
        [
            date(2020, 1, 20),
            'Minsk',
            -16,
            8.5
        ],
    ]
    csv_write('files_11_weather.csv', fields, data)
    _, data = csv_read('files_11_weather.csv')
    degree_avg = csv_degree_avg(data) / len(data)
    print(degree_avg)
    wind_spd_avg = csv_wind_spd(data) / len(data)
    print(wind_spd_avg)


if __name__ == '__main__':
    main()
