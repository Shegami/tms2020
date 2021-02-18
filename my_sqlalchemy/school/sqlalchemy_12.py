"""
Описать модель школьного дневника(Diary)
с помощью sqlalchemy в файле models.py.
Дневник характеризуется Средним баллом
и студентом к которому он приурочен.
Создать файл sqlalchemy_12.py.
Получить всех студентов и создать для каждого дневник.
"""

from my_sqlalchemy.school.models import session,\
    Student, Diary

students = session.query(Student.lastname)
for student in students:
    print(student)

diary_1 = Diary(avg_mark=9, student_id=1)
diary_2 = Diary(avg_mark=4, student_id=2)
diary_3 = Diary(avg_mark=3, student_id=3)
diary_4 = Diary(avg_mark=6, student_id=4)
diary_5 = Diary(avg_mark=8, student_id=5)
diary_6 = Diary(avg_mark=10, student_id=6)

session.add_all(
    [
        diary_6,
        diary_5,
        diary_4,
        diary_3,
        diary_2,
        diary_1
    ]
)
session.commit()
