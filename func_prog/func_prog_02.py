"""
Дан список слов.
Сгенерировать новый список с перевернутыми словами.
"""


def main():
    names = ['Kolya', 'Igor', 'Pasha']

    names_rev = [name[::-1] for name in names]
    print(names_rev)


if __name__ == '__main__':
    main()
