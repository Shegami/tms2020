"""
Получить все группы, где есть студенты с именем Anton.
"""

from my_sqlalchemy.school.models import session,\
    Group, Student

students = session.query(
    Group, Student).join(
    Student, Group.id == Student.group_id).filter(
    Student.firstname == 'Anton').all()
for gr, std in students:
    print(f'Group: {gr.id}')
