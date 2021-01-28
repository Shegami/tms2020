"""
Создать метод класса get_counter.
Создать три объекта класса. Вызвать через класс метод get_counter.
"""


class Pet:
    __counter = 0

    def __init__(self,
                 name, age, master,
                 weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

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

    def voice(self):
        pass

    def __eq__(self, other):
        return all([
            self.weight == other.weight,
            self.height == other.height,
            self.age == other.age
        ])

    def __ne__(self, other):
        return not self == other


class Dog(Pet):
    def voice(self):
        print('Woof!')

    def jump(self, meters):
        if meters > 0.5:
            print('Dogs cannot jump so high, retard')
        else:
            super().jump(meters)


class Cat(Pet):
    def voice(self):
        print('Meow!')

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

    def voice(self):
        print('AAAAAAAAAAAA!')


class Horse(Pet):
    def voice(self):
        print('Igo-go!')


class Donkey(Pet):
    def voice(self):
        print('IIIIIAAAAAAAAA!!!!!!!!!!')


class Mule(Donkey, Horse):
    def voice(self):
        super(Mule, self).voice()


def print_voice(listt):
    for animal in listt:
        animal.voice()


def main():
    Mule('Oleg', 3, 'Vasya', 12, 1.5)
    Mule('Dima', 3, 'Olega', 12, 1.3)
    print(Pet.get_counter())


if __name__ == '__main__':
    main()
