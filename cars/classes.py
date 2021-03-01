"""
Создать ветку cars от master.
Создать пакет cars.
Создать таблицы Brand(name), Car(model, release_year,
brand(foreing key на таблицу Brand)).
Реализовать CRUD(создание, чтение, обновление по id, удаление по id)
для бренда и машины.
Создать пользовательский интерфейс.
"""

from sqlalchemy import Column, Integer, String, \
    create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker, relationship

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'cars'
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}'
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return f'{self.name}'


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    brand_id = Column(
        Integer,
        ForeignKey('brand.id'),
        nullable=False
    )
    brand = relationship(
        'Brand',
        foreign_keys='Car.brand_id',
        backref='cars'
    )

    def __str__(self):
        return f'{self.brand} - {self.model} - {self.release_year}'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
