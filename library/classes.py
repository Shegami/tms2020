"""
Создать ветку library от master.
Создать ветку library_solution от ветки library.
Создать пакет library.
Написать программу с пользовательским интерфейсом.
Программа реализует CRUD для работы с книгами.
Также программа позволяет фильтровать книги по автору.
Реализовать программу в виде раздельных
модулей(classes.py, buisness_logic.py, ui.py, main.py).
Сделать пул реквест из ветки library_solution в library
"""

from sqlalchemy import Column, Integer, String, \
    create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'library'
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}',
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String)
    year = Column(String)
    pages = Column(Integer, nullable=False)

    def __str__(self):
        return f'ID: {self.id} - {self.title} - ' \
               f'{self.author} - {self.pages} - {self.year}'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
