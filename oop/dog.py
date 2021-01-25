class Dog:
    # oop_2
    def bark(self):
        print('Woof Woof!')

    def look_at_moon(self):
        for i in range(3):
            self.bark()

    # oop_03
    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    # oop_04
    def __init__(self, height,
                 weight, name,
                 age, master):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__address = 'Minsk'

    # oop_08
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


def main():
    dog = Dog(1.5, 13, 'Stefan', 7, 'KOSTIA')
    dog.name = 'Izmail'
    print(dog.name)
    dog.weight = 1
    print(dog.weight)
    dog.height = 12
    print(dog.height)
    dog.age = 76
    print(dog.age)
    dog.master = 'ALESA'
    print(dog.master)
    dog.address = 'Mahachkala'
    print(dog.address)


if __name__ == '__main__':
    main()
