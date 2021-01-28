"""
Добавить в класс Pet пустой метод voice.
Заменить имена методов bark, meow на voice.
Добавить voice для класса Parrot.
Создать функцию, принимающая список животных
и вызывающая у каждого животного метод voice.
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

    def voice(self):
        pass


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
    mule = Mule('Oleg', 3, 'Vasya', 12, 1.5)
    mule.voice()


if __name__ == '__main__':
    main()
