"""
Описать модель школьного дневника(Diary)
с помощью sqlalchemy в файле models.py.
Дневник характеризуется Средним баллом
и студентом к которому он приурочен.
Создать файл sqlalchemy_12.py.
Получить всех студентов и создать для каждого дневник.
"""

from my_sqlalchemy.school.models import session, \
    Student, Diary

students = session.query(Student)
for student in students:
    print(student)
    diary = Diary(avg_mark=9, student=student)
    session.add(diary)
session.commit()
