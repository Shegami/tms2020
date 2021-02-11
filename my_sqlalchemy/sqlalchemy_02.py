"""
Создать файл sqlalchemy_02.py.
Создать соединение к базе sa_test.db.
Создать 5 книг с помощью my_sqlalchemy.
"""


from sqlalchemy import create_engine

engine = create_engine('sqlite:///sa_test.db')
engine.execute("""
    insert into book (
    title,
    pages,
    author,
    price,
    release_year)
    
    values
    ('Matrix', 102, 'Garry', 777, 2001),
    ('Matrix Revolution', 137, 'Garry', 832, 2001),
    ('Matrix Reload', 181, 'Garry', 894, 2005),
    ('Matrix Comeback', 201, 'Garry', 975, 2007),
    ('Matrix Final', 264, 'Garry', 1034, 2012);
""")


def main():
    pass


if __name__ == '__main__':
    main()
