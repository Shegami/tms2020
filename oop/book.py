"""
Создать файл book.py.
Создать класс Book.
Атрибуты: количество страниц, год издания, автор, цена.
Добавить валидацию в конструкторе на ввод корректных данных.
Создать иерархию ошибок.
Ошибки вызываются при попытке создания не правильного объекта.
"""


class CheckDataInt(Exception):
    def __init__(self, message='Type of Data must be int'):
        super().__init__(message)


class CheckDataFloatInt(Exception):
    def __init__(self, message='Type of Data must be int or float'):
        super().__init__(message)


class CheckDataStr(Exception):
    def __init__(self, message='Type of Data must be str'):
        super().__init__(message)


class CheckNumbPages(Exception):
    def __init__(self, message='Pages must be > 0'):
        super().__init__(message)


class CheckPrice(Exception):
    def __init__(self, message='Price must be >= 0'):
        super().__init__(message)


class CheckYear(Exception):
    def __init__(self, message='No books were written that time'):
        super().__init__(message)


class Book:
    def __init__(self,
                 pages, year, author, price):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price
        if type(self.pages) != int or type(self.year) != int:
            raise CheckDataInt
        elif self.pages <= 0:
            raise CheckNumbPages
        elif self.year < 868:
            raise CheckYear
        elif type(self.price) != int and type(self.price) != float:
            raise CheckDataFloatInt
        elif self.price < 0:
            raise CheckPrice
        elif type(self.author) != str:
            raise CheckDataStr

    def __str__(self):
        return f'Author: {self.author}, '\
               f'Pages: {self.pages}, year: {self.year}, '\
               f'Price: {self.price}'


def main():
    harrypotter = Book('dfd', 1000, 'Andrew', 0)
    print(harrypotter)


if __name__ == '__main__':
    main()
