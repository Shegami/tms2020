"""
Дан список имен, отфильтровать все имена,
где есть буква o
"""


def main():
    names = [
        'Egor',
        'Alex',
        'Masha',
        'Olya'
    ]

    names_o = list(filter(lambda i: 'o' in i.lower(), names))
    print(names_o)


if __name__ == '__main__':
    main()
