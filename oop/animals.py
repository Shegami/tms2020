"""
Добавить в класс Parrot  новый атрибут - species
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

    def jump(self, meters):
        print(f'Jump, {meters} meters bitch!')

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

    def jump(self, meters):
        if meters > 0.5:
            print('Dogs cannot jump so high, retard')
        else:
            super().jump(meters)


class Cat(Pet):
    def meow(self):
        return 'Meow!'

    def jump(self, meters):
        if meters > 2:
            print('Cats cannot jump so high, retard')
        else:
            super().jump(meters)


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

    def jump(self, meters):
        if meters > 0.05:
            print('Parrots cannot jump so high, retard')
        else:
            super().jump(meters)

    def __init__(self,
                 name, age,
                 master, weight,
                 height, species):
        super().__init__(name, age,
                         master, weight,
                         height)
        self.species = species


def main():
    parrot = Parrot('Kyky', 1, 'Pirat', 1, 0.7, 'karlik')
    parrot.jump(0.03)
    parrot.jump(1)


if __name__ == '__main__':
    main()
