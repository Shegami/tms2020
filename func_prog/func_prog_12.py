"""
Создать универсальный декоратор, который
меняет порядок аргументов в функции на противоположный.
"""

from functools import wraps


def decorator(print_list):
    @wraps(print_list)
    def wrapper(*args, **kwargs):
        new_kwargs = {}
        for key in reversed(kwargs.keys()):
            new_kwargs.setdefault(key, kwargs[key])
        result = print_list(*args[::-1], **new_kwargs)
        return result
    return wrapper


@decorator
def print_list(*args, **kwargs):
    print(args)
    print(kwargs)


def main():
    print_list(1, 2, 3, 4, 5, a=5, b=4, c=2871)


if __name__ == '__main__':
    main()
