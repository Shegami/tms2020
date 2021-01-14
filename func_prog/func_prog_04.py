"""
Дан словарь, создать новый словарь,
поменяв местам ключ и значение
"""


def main():
    car = {'number': 1234,
           'year': 1999}
    car_new = {value: key for key, value in car.items()}
    print(car_new)


if __name__ == '__main__':
    main()
