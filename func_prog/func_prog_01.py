"""
Создать lambda функцию, которая принимает
на вход имя и выводит его в формате “Hello, {name}”
"""


def main():
    print((lambda name: f'Hello, {name}')(input('Name: ')))


if __name__ == '__main__':
    main()
