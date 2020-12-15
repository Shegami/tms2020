"""
Получить на ввод количество рублей и копеек
и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки.
"""

rubles = int(input())
cents = int(input())
# rubles
if rubles % 100 == 11 or rubles % 100 == 12\
        or rubles % 100 == 13 or rubles % 100 == 15:
    print(f'{rubles} рублей', end=' ')
elif rubles % 10 == 1 and rubles != 11\
        or rubles % 100 == 1 or rubles % 1000 == 1:
    print(f'{rubles} рубль', end=' ')
elif rubles % 10 == 2 and rubles != 12 or\
        rubles % 10 == 3 and rubles != 13 or\
        rubles % 10 == 4 and rubles != 14:
    print(f'{rubles} рубля', end=' ')
else:
    print(f'{rubles} рублей', end=' ')

# cents
if cents % 10 == 1 and cents != 11:
    print(f'{cents} копейка', end=' ')
elif cents % 10 == 2 or cents % 10 == 3 or cents % 10 == 4:
    print(f'{cents} копейки', end=' ')
else:
    print(f'{cents} копеек', end=' ')
