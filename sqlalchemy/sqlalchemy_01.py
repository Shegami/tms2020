"""
Все операции выполнять с помощью sqlalchemy.
Создать файл sqlalchemy_01.py. Создать базу sa_test.db.
Создать таблицу Book с помощью sqlalchemy.
Атрибуты: id(integer primary key),
title(varchar), pages(int), author(varchar),
price(float), release_year(int)
"""


from sqlalchemy import create_engine

engine = create_engine('sqlite:///sa_test.db')
engine.execute("""
    create table Book (
    id integer primary key autoincrement,
    title varchar,
    pages int,
    author varchar,
    price float,
    release_year int);
""")


def main():
    pass


if __name__ == '__main__':
    main()
