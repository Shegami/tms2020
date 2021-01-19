"""
Написать декоратор, который будет выводить время выполнения функции
"""

from functools import wraps
from datetime import datetime


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.now()
        result = func(*args, **kwargs)
        time_end = datetime.now() - time
        print(time_end)
        return result
    return wrapper


@my_decorator
def my_func(x, y, z):
    return x * y * z


def main():
    my_func(3823847, 3475987, 45678987654456)


if __name__ == '__main__':
    main()
