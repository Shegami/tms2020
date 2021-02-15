"""
Создать класс Book и сессию в файле book.py.
Создать файл sqlalchemy_06.
Импортировать Book и сессию из модуля book.
Создать 3 книги с помощью сессии.
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, \
    Column, Integer, String, Float

from sqlalchemy.orm import mapper, sessionmaker
engine = create_engine('sqlite:///book.db', echo=True)
metadata = MetaData()

book_table = Table(
    'book', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('pages', Integer),
    Column('author', String),
    Column('price', Float),
    Column('release_year', Integer),
)

metadata.create_all(engine)


class Book:
    def __init__(self,
                 title, pages,
                 author, price,
                 release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


mapper(Book, book_table)

Session = sessionmaker(bind=engine)
session = Session()
