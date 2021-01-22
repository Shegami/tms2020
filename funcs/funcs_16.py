"""
Даны три слова. Выяснить, является ли хоть одно
из них палиндромом ("перевертышем"), т. е. таким,
которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую
распознавать слова палиндромы.)
"""


def palindrom(listt):
    result = {}
    for i in range(len(listt)):
        if listt[i].lower() == listt[i].lower()[::-1]:
            result.setdefault(listt[i], "палиндром")
    return result


def main():
    words = ['Лиса', 'Шалаш', 'Дом']
    print(palindrom(words))


if __name__ == '__main__':
    main()
