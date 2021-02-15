from sqlalchemy import create_engine

engine = create_engine('sqlite:///sa_test.db')

title = input('Название: ')
pages = int(input('Кол-во страниц: '))
author = input('Автор: ')
price = float(input('Цена: '))
release_year = int(input('Год выпуска: '))

conn = engine.connect()
trans = conn.begin()

conn.execute(f"""
    insert into Book
    (title, pages, author, price, release_year)
    values
    ('{title}', {pages}, '{author}', {price}, {release_year});
""")

print(title, pages, author, price, release_year)
print()

if input('Хотите сохранить эту книгу? ') == 'Да':
    trans.commit()
else:
    trans.rollback()
conn.close()
