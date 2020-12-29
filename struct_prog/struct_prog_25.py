"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания
в пути которых превышает 7 часов 20 минут.
"""

from datetime import datetime, timedelta


def travel_time_more_7h_20m(listt):
    for i in range(len(listt)):
        date_time_departure = datetime(listt[i]['departure'][1],
                                       listt[i]['departure'][2],
                                       listt[i]['departure'][3],
                                       listt[i]['departure'][4],
                                       listt[i]['departure'][5])
        date_time_arrival = datetime(listt[i]['arrival'][1],
                                     listt[i]['arrival'][2],
                                     listt[i]['arrival'][3],
                                     listt[i]['arrival'][4],
                                     listt[i]['arrival'][5])
        common_time_travel = date_time_arrival - date_time_departure
        if common_time_travel > timedelta(minutes=20, hours=7):
            print(f'train #{listt[i]["number"]}\n'
                  f'departure: {date_time_departure}\n'
                  f'arrival: {date_time_arrival}\n'
                  f'common time in travel: {common_time_travel}\n')
            print()


def main():
    schedule = [
        {
            'number': 124_01,
            'arrival': ['Moscow', 2020, 12, 5, 19, 27],
            'departure': ['Minsk', 2020, 12, 5, 10, 35]
        },
        {
            'number': 137_29,
            'arrival': ['Paris', 2020, 12, 7, 5, 57],
            'departure': ['Limoges', 2020, 12, 7, 00, 11]
        },
        {
            'number': 101_17,
            'arrival': ['Vladivostok', 2020, 12, 10, 19, 27],
            'departure': ['Saint Petersburg', 2020, 12, 5, 7, 54]
        }]
    travel_time_more_7h_20m(schedule)


if __name__ == '__main__':
    main()
