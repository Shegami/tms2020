"""
Описать модель Книга(Book) с помощью sqlalchemy
в файле models.py. Книга характеризуется названием,
количеством страниц и студентами у которых эта книга.
Создать файл sqlalchemy_13.py.
Создать 5 книг.
Получить всех студентов и добавить каждому студенту эти пять книг.
"""

from my_sqlalchemy.school.models import session,\
    Book, Student

students = session.query(Student).all()

book_1 = Book(name='War I', pages=100, students=students)
book_2 = Book(name='War II', pages=128, students=students)
book_3 = Book(name='War III', pages=119, students=students)
book_4 = Book(name='War IV', pages=194, students=students)
book_5 = Book(name='War V', pages=181, students=students)

session.add_all(
    [
        book_5,
        book_1,
        book_4,
        book_3,
        book_2
    ]
)

session.commit()
