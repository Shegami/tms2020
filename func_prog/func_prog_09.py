"""
Дан список строк.
Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке.
Использовать генератор списков.
"""


def main():
    strings = ['Marry', 'Christmas', 'happy', 'New', 'Year']
    strings_i = [f'{i} - {string}' for i, string in enumerate(strings, 1)]
    print(strings_i)


if __name__ == '__main__':
    main()
