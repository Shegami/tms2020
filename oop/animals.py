"""
Добавить два новых атрибута в родительский класс:
weight и height.
Добавить методы change_weight, change_height
принимающий один параметр и прибавляющий его к
соответствующему аргументу.
В случае если параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot.
Если вес больше 0.1 выводить сообщение This parrot cannot fly.
"""


class Pet:
    def __init__(self,
                 name, age, master,
                 weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        return 'Run, bitch!'

    def jump(self):
        return 'Jump, bitch!'

    def bithday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height += height
        else:
            self.height += 0.2


class Dog(Pet):

    def bark(self):
        return 'Woof!'


class Cat(Pet):

    def meow(self):
        return 'Meow!'


class Parrot(Pet):

    def fly(self):
        if self.weight > 0.1:
            print("Too fat, cant fly")
        else:
            print('fly, bitch!')


def main():
    dog = Dog('Sasha', 10, 'Alex', 1.5, 0.7)
    print(dog.weight)
    print(dog.height)
    dog.change_height(7)
    dog.change_weight(1)
    print(dog.weight)
    print(dog.height)


if __name__ == '__main__':
    main()
