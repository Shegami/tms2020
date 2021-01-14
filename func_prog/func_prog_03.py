"""
Дан список словарей.
Каждый словарь описывает машину(серийный номер и год выпуска).
Создать новый список со всеми машинами,
год выпуска которых больше n
"""


def main():
    cars = [
        {
            'number': 1234,
            'year': 1999
        },
        {
            'number': 4875,
            'year': 1978
        },
        {
            'number': 7843,
            'year': 2001
        }
    ]

    n = 1995
    cars_sorted = [car for car in cars if car['year'] > n]
    print(cars_sorted)


if __name__ == '__main__':
    main()
