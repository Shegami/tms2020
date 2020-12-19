"""
Дан словарь:
{'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
"""


def key_len_for(dictt):
    for key in list(dictt.keys()):
        dictt[key + str(len(key))] = dictt.pop(key)
    print(dictt)


def key_len_while(dictt):
    keys = list(dictt.keys())
    index = 0
    while True:
        if index != len(keys):
            dictt[keys[index] + str(len(keys[index]))] = dictt.pop(keys[index])
            index += 1
        else:
            break
    print(dictt)


def main():
    dictt = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
    key_len_for(dictt)
#    key_len_while(dictt)


if __name__ == '__main__':
    main()
