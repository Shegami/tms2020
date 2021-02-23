"""
Логика работы с Пользователем.
"""

from library.business_logic import add_book, \
    get_book, update_book, delete_book


#  UI print records by query
def print_books(books):
    for book in books:
        print(book)


def ui_add_book():
    try:
        title = input('\nTitle: ')
        author = input('Author: ')
        year = int(input('Year: '))
        pages = int(input('Number of pages: '))
    except ValueError:
        print('Wrong input. Try again')
    else:
        commit = input(f'\nNew record will be added: {title} - {author} - '
                       f'{year} - {pages}\n (yes/no): ')
        if commit == 'yes' or commit == 'y':
            add_book(title, author, year, pages)


def ui_get_book():
    while True:
        #  check input == int
        try:
            search_type = int(input(
                '\n1. Search by title\n'
                '2. Search by author\n'
                '3. Search by title and author\n'
                '4. Get all books\n'
                '5. Back to menu'
                '\nPlease make a choice: '
            ))
        except ValueError:
            print('Wrong input. Try again')

        else:
            #  by title
            if search_type == 1:
                title = input('Entry the title: ')
                books = get_book(title=title)
                if books:
                    print_books(books)
                    break
                else:
                    print('No matches found')
                    continue

            #  by author
            elif search_type == 2:
                author = input('Entry the author: ')
                books = get_book(author=author)
                if books:
                    print_books(books)
                    break
                else:
                    print('No matches found')
                    continue

            #  by title + author
            elif search_type == 3:
                title = input('Entry the title: '),
                author = input('Entry the author: ')
                books = get_book(title=title, author=author)
                if books:
                    print_books(books)
                    break
                else:
                    print('No matches found')
                    continue

            #  get all
            elif search_type == 4:
                books = get_book()
                if books:
                    print_books(books)
                    break

            #  back to menu
            elif search_type == 5:
                break

            else:
                print('Wrong input')
                continue


def ui_update_book():
    while True:
        is_id = input('To change a record you need a book ID.\n'
                      'Do you have a book ID? (yes/no): ')
        if is_id == 'yes' or is_id == 'y':
            pass
        elif is_id == 'no' or is_id == 'n':
            print('\nUse search to get a book ID.')
            ui_get_book()
            break
        #  try again
        else:
            print('Wrong input')
            continue

        try:
            book_id = int(input('\nEntry the book ID: '))
        except ValueError:
            print('Wrong input. Try again')
            break
        else:
            book = get_book(book_id=book_id)
            print_books(book)
            if book:
                try:
                    title = input('New title: ')
                    author = input('New author: ')
                    year = int(input('New year: '))
                    pages = int(input('New number of pages: '))
                except ValueError:
                    print('Wrong input. Try again')
                else:
                    commit = input('The record will be changed to: '
                                   f'{title} - {author} - '
                                   f'{year} - {pages} (yes/no): ')
                    if commit == 'yes' or commit == 'y':
                        update_book(book_id, title, author, year, pages)
                break
            else:
                print('The book with the specified ID was not found\n')
                break


def ui_delete_book():
    while True:
        is_id = input('To delete a record you need a book ID.\n'
                      'Do you have a book ID? (yes/no): ')
        if is_id == 'yes' or is_id == 'y':
            pass
        elif is_id == 'no' or is_id == 'n':
            print('Use search to get a book ID.')
            ui_get_book()
            break
        else:
            print('Wrong input')
            continue
        book_id = int(input('Entry the book ID: '))
        book = get_book(book_id=book_id)
        if book:
            print_books(book)
            commit = input('The record will be deleted (yes/no): ')
            if commit == 'yes' or commit == 'y':
                delete_book(book_id)
        else:
            print('The book with the specified ID was not found\n')
            break
        break


#  UI
def start_session():
    while True:
        #  check choice == int
        try:
            choice = int(input(
                '1. Add book\n'
                '2. Find book\n'
                '3. Update record\n'
                '4. Delete record\n'
                '5. Exit'
                '\nPlease make a choice: '
            ))
        except ValueError:
            print('Wrong input. Try again')
        else:
            #  add record
            if choice == 1:
                ui_add_book()

            #  get record
            elif choice == 2:
                ui_get_book()

            #  update record
            elif choice == 3:
                ui_update_book()

            #  delete record
            elif choice == 4:
                ui_delete_book()

            #  exit from app
            elif choice == 5:
                exit()

            #  one more time
            loop = input('\nDo you want to continue? (yes/no): ')
            if loop == 'yes' or loop == 'y':
                continue
            else:
                break
