"""
Написать функцию, которая получает на вход имя
и выводит строку вида: “Hello, {name}”.
Создать список из 5 имен. Вызвать функцию
для каждого элемента списка в цикле.
"""


def hello_name(name_var):
    return f'Hello, {name_var}'


def main():
    names = ['Kostia', 'Igor', 'Zhenya', 'Katya', 'Elena']
    for name in names:
        print(hello_name(name))


if __name__ == '__main__':
    main()
