"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных
удалять все четные элементы из списка.
"""

from functools import wraps


def decorator(print_list):
    @wraps(print_list)
    def wrapper(some_list):
        new_list = list(filter(lambda x: x % 2 != 0, some_list))
        result = print_list(new_list)
        return result
    return wrapper


@decorator
def print_list(some_list):
    print(some_list)


def main():
    print_list([1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    main()
