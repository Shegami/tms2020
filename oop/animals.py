"""
Переопределить методы change_weight, change_height в классе Parrot.
В случае не передачи параметра - вес изменяется на 0.05
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
    def change_weight(self, weight=0.05):
        self.weight += weight

    def change_height(self, height=0.05):
        self.height += height

    def fly(self):
        if self.weight > 0.1:
            print("Too fat, cant fly")
        else:
            print('fly, bitch!')


def main():
    parrot = Parrot('Kyky', 1, 'Pirat', 1, 0.7)
    print(parrot.weight)
    parrot.change_weight()
    print(parrot.weight)


if __name__ == '__main__':
    main()
