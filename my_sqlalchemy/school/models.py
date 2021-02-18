"""
Создать таблицу Студент(Student) с помощью
sqlalchemy в файле models.py.
Студент характеризуется именем(firstname)
и фамилией(lastname) и группой к которой он приурочен.
Создать файл sqlalchemy_11.py.
Создать две группы.
Добавить в каждую по три студента.
"""
from sqlalchemy import create_engine,\
    Column, String, Integer, ForeignKey, Float
from sqlalchemy_utils import create_database, \
    database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,\
    sessionmaker, backref

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'school'

engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}',
    echo=True,
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(
        Integer,
        ForeignKey('group.id'),
        nullable=False,
    )

    group = relationship(
        'Group',
        foreign_keys='Student.group_id',
        backref='students',
    )


class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    avg_mark = Column(Float)
    student_id = Column(
        Integer,
        ForeignKey('student.id'),
        nullable=False,
    )
    student = relationship(
        'Student',
        foreign_keys='Diary.student_id',
        backref=backref('diary', uselist=False)
    )


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
