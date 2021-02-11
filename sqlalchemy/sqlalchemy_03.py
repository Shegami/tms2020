"""
Создать файл sqlalchemy_03.py.
Написать программу: пользователь вводит год.
Отобразить на экране те книги, год которых
меньше введенного пользователем года.
Если таких книг нет - вывести сообщение: Not found.
"""

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sa_test.db')

my_year = int(input('Input year: '))

result = engine.execute(f"""
    select * from Book
    where release_year < {my_year};
""")

books = list(result)

if books:
    for book in books:
        print(book)
else:
    print('Not found')


def main():
    pass


if __name__ == '__main__':
    main()
