"""
В файле files_08 импортировать функции.
С помощью функций создать файл с информацией
о товарах(Имя товара, цена, количество, комментарий).
Прочесть файл, Добавить новую позицию в конец.
Удалить третью строку.
"""

from files.csv_utils import csv_read, csv_write, csv_add_row, csv_pop_row


def main():
    fields = [
        'product',
        'price',
        'quantity',
        'comment'
    ]
    data = [
        [
            'Iphone 12 PRO',
            3090,
            15,
            'discount 15 %'
        ],
        [
            'Huawei P20 Lite',
            1000,
            38,
            'black colour'
        ],
        [
            'Xiaomi Redmi Note 9',
            1810,
            51,
            'no charger'
        ]
    ]

    csv_write('files_08_goods.csv', fields, data)
    new_row = [
        'Samsung LX',
        1750,
        17,
        'sales start: 12.03.2021'
    ]
    csv_read('files_08_goods.csv')
    csv_add_row('files_08_goods.csv', new_row)
    csv_pop_row('files_08_goods.csv', 3)


if __name__ == '__main__':
    main()
