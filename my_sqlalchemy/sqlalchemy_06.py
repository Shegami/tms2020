from my_sqlalchemy.book import Book, session

book_1 = Book('War I', 100, 'Tolstoi', 75, 1996)
book_2 = Book('War II', 122, 'Tolstoi', 162, 1999)
book_3 = Book('War III', 156, 'Tolstoi', 181, 2006)

session.add_all([book_1, book_2, book_3])
session.commit()
