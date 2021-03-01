"""
Логика работы с Пользователем.
"""

from cars.business_logic import add_brand, add_car, get_brand,\
    get_car, update_brand, update_car, delete_brand, \
    delete_car


#  UI print records by query
def print_rec(records):
    for rec in records:
        print(rec)


def ui_add_brand():
    name = input('Name: ')
    commit = input(f'\nNew record will be added: '
                   f'{name}\n (yes/no): ')
    if commit == 'yes' or commit == 'y':
        add_brand(name=name)


def ui_add_car():
    try:
        name = input('Brand: ')
        model = input('Model: ')
        year = int(input('Year: '))
    except ValueError:
        print('Wrong input. Try again')
    else:
        commit = input(f'\nNew record will be added: '
                       f'{name} - {model} - {year}\n (yes/no): ')
        if commit == 'yes' or commit == 'y':
            brand = get_brand(name=name)
            add_car(
                model=model,
                release_year=year,
                brand=brand
            )


def ui_get_brand():
    brands = get_brand()
    if brands:
        print()
        print_rec(brands)
    else:
        print('No brands yet')


def ui_get_car():
    cars = get_car()
    if cars:
        print()
        print_rec(cars)
    else:
        print('No cars yet')


def ui_update_brand():
    try:
        brand_id = int(input('\nEntry the ID: '))
    except ValueError:
        print('Wrong input. Try again')

    else:
        brand = get_brand(brand_id=brand_id)
        if brand:
            print(brand)
            name = input('New name: ')
            commit = input('The record will be changed to: '
                           f'{name}. (yes/no): ')
            if commit == 'yes' or commit == 'y':
                update_brand(brand_id=brand_id, name=name)
        else:
            print('The brand with the specified ID was not found\n')


def ui_update_car():
    try:
        car_id = int(input('\nEntry the ID: '))
    except ValueError:
        print('Wrong input. Try again')

    else:
        car = get_car(car_id=car_id)
        if car:
            print(car)
            name = input('New brand: ')
            model = input('New model: ')
            year = int(input('New year: '))
            commit = input('The record will be changed to: '
                           f'{name} - {model} - {year}. (yes/no): ')
            if commit == 'yes' or commit == 'y':
                brand = get_brand(name=name)
                if brand:
                    update_car(
                            car_id=car_id,
                            model=model,
                            release_year=year,
                            brand=brand
                        )
                else:
                    print('Wrong input. Try again')
        else:
            print('The car with the specified ID was not found\n')


def ui_delete_brand():
    brand_id = int(input('Entry the brand ID: '))
    brand = get_brand(brand_id=brand_id)
    if brand:
        print(brand)
        commit = input('The record will be deleted (yes/no): ')
        if commit == 'yes' or commit == 'y':
            delete_brand(brand_id=brand_id)
    else:
        print('The brand with the specified ID was not found\n')


def ui_delete_car():
    car_id = int(input('Entry the car ID: '))
    car = get_car(car_id=car_id)
    if car:
        print(car)
        commit = input('The record will be deleted (yes/no): ')
        if commit == 'yes' or commit == 'y':
            delete_car(car_id=car_id)
    else:
        print('The car with the specified ID was not found\n')


#  UI
def start_session():
    while True:
        #  check choice == int
        try:
            choice = int(input(
                '1. Brands\n'
                '2. Cars\n'
                '3. Exit\n'
                '\nPlease choose a table: '
            ))
        except ValueError:
            print('Wrong input. Try again')
        else:
            #  brand
            if choice == 1:
                action = input(
                    '\n1. Add brand\n'
                    '2. Get brand\n'
                    '3. Update brand\n'
                    '4. Delete brand\n'
                    '5. Exit\n'
                    '\nPlease choose an action: '
                )
                if action == '1':
                    ui_add_brand()
                elif action == '2':
                    ui_get_brand()
                elif action == '3':
                    ui_update_brand()
                elif action == '4':
                    ui_delete_brand()
                elif action == '5':
                    continue
                else:
                    print('Wrong input. Try again')

            #  car
            if choice == 2:
                action = input(
                    '\n1. Add car\n'
                    '2. Get car\n'
                    '3. Update car\n'
                    '4. Delete car\n'
                    '5. Exit\n'
                    '\nPlease choose an action: '
                )
                if action == '1':
                    ui_add_car()
                elif action == '2':
                    ui_get_car()
                elif action == '3':
                    ui_update_car()
                elif action == '4':
                    ui_delete_car()
                elif action == '5':
                    continue
                else:
                    print('Wrong input. Try again')

            #  exit from app
            elif choice == 3:
                exit()

            #  one more time
            loop = input('\nDo you want to continue? (yes/no): ')
            if loop == 'yes' or loop == 'y':
                continue
            else:
                break
