"""
Логика работы с БД.
"""

from library.classes import Book, session
from sqlalchemy import and_


#  add record to DB
def add_book(
        title,
        author,
        year,
        pages
):
    book = Book(
        title=title,
        author=author,
        year=year,
        pages=pages
    )
    session.add(book)
    session.commit()


#  get records from DB by title/author/title+author/all/ID
def get_book(title=None, author=None, book_id=None):
    #  title
    if all([title is not None, author is None, book_id is None]):
        books = session.query(Book).filter_by(
            title=title
        ).all()
        return books
    #  author
    elif all([title is None, author is not None, book_id is None]):
        books = session.query(Book).filter_by(
            author=author
        ).all()
        return books
    #  title + author
    elif all([title is not None, author is not None, book_id is None]):
        books = session.query(Book).filter(
            and_(
                Book.title == title,
                Book.author == author
            )
        ).all()
        return books
    #  all
    elif all([title is None, author is None, book_id is None]):
        books = session.query(Book).all()
        return books
    #  ID
    elif all(([title is None, author is None, book_id is not None])):
        book = session.query(Book).filter_by(
            id=book_id
        ).all()
        return book


#  update record in DB
def update_book(book_id, title, author, year, pages):
    book = session.query(Book).get(book_id)
    if book:
        book.title = title
        book.author = author
        book.year = year
        book.pages = pages
        session.commit()


#  delete record from DB
def delete_book(book_id):
    book = session.query(Book).get(book_id)
    session.delete(book)
    session.commit()
