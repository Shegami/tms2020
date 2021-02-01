"""
Создать файл animals_hierarchy.py.
Реализовать интерфейсы: Feline(), Canine().
Все кошачьи должны уметь царапаться.
Все собачьи должны уметь выть на луну.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    pass


class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass


class Feline(Animal):
    @abstractmethod
    def scratch(self):
        raise NotImplementedError


class Canine(Animal):
    @abstractmethod
    def howl(self):
        raise NotImplementedError


class Cat(Feline, Pet):
    def scratch(self):
        print("I'm gonna scratch you!")


class Dog(Canine, Pet):
    def howl(self):
        print("AuuuuuF!")


class Lion(Feline, WildAnimal):
    def scratch(self):
        print("I'm gonna scratch you!")


class Wolf(Canine, WildAnimal):
    def howl(self):
        print("AuuuuuF!")


def main():
    wolf = Wolf()
    wolf.howl()
    cat = Cat()
    cat.scratch()


if __name__ == '__main__':
    main()
