"""
Использовать результаты files_08.
Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в files_09.py.

1) Создать функцию подсчета полной суммы всех товаров.
2) Создать функцию поиска самого дорогого товара.
3) Создать функцию самого дешевого товара.
4) Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""

from files.csv_utils import csv_goods_sum,\
                            csv_goods_expensive,\
                            csv_goods_cheapest,\
                            csv_goods_reduce


def main():
    goods_sum = csv_goods_sum('files_08_goods.csv')
    print(goods_sum)
    most_expensive = csv_goods_expensive('files_08_goods.csv')
    print(most_expensive)
    cheapest = csv_goods_cheapest('files_08_goods.csv')
    print(cheapest)
    csv_goods_reduce('files_08_goods.csv')


if __name__ == '__main__':
    main()
