"""
Создать файл animals.py. Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы:
run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly.
Cat - meow, Dog - bark.
"""


class Dog:
    def __init__(self,
                 name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return 'Run, dog!'

    def jump(self):
        return 'Jump, dog!'

    def bithday(self):
        self.age += 1

    def bark(self):
        return 'Woof!'


class Cat:
    def __init__(self,
                 name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return 'Run, cat!'

    def jump(self):
        return 'Jump, cat!'

    def birthday(self):
        self.age += 1

    def meow(self):
        return 'Meow!'


class Parrot:
    def __init__(self,
                 name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return 'Run, parrot!'

    def jump(self):
        return 'Jump, parrot!'

    def birthday(self):
        self.age += 1

    def fly(self):
        return 'Fly!'


def main():
    pass


if __name__ == '__main__':
    main()
