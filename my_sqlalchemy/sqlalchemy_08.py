"""
Создать файл sqlalchemy_08.py.
Написать программу: пользователь вводит границы фильтрации по году.
Отобразить на экране те книги, год которых находиться в
заданных границах.
Если таких книг нет - вывести сообщение: Not found.
"""

from my_sqlalchemy.book import session, Book
from sqlalchemy import and_

year_from = int(input('Year from: '))
year_to = int(input('Year to: '))

books = list(session.query(Book).filter(
    and_(
        Book.release_year >= year_from,
        Book.release_year <= year_to
    )
))

if len(books) > 0:
    for book in books:
        print(f'- {book.title}')
else:
    print('Not found')
