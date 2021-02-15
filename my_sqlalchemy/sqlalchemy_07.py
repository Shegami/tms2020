"""
Создать файл sqlalchemy_07.py.
Получить все книги и вывести их на экран в формате
год - название - автор
"""

from my_sqlalchemy.book import session, Book

books = session.query(Book)

for book in books:
    print(f'{book.release_year} - {book.title} - {book.author}')
