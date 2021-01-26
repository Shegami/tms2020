"""
Создать родительский класс Pet, содержащий
все общие методы классов
og, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet.
Удалить в дочерних классах те методы, которые имеются у
родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""


class Pet:
    def __init__(self,
                 name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return 'Run, bitch!'

    def jump(self):
        return 'Jump, bitch!'

    def bithday(self):
        self.age += 1


class Dog(Pet):

    def bark(self):
        return 'Woof!'


class Cat(Pet):

    def meow(self):
        return 'Meow!'


class Parrot(Pet):

    def fly(self):
        return 'Fly!'


def main():
    dog = Dog('Sasha', 10, 'Alex')
    print(dog.bark())
    print(dog.jump())
    print(dog.run())
    dog.bithday()


if __name__ == '__main__':
    main()
