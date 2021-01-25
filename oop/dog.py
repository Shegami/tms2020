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
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__address = 'Minsk'

    # oop_05
    def change_name(self, name):
        self.name = name

    # oop_06
    def get_master(self):
        return self.__master

    # oop_07
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


def main():
    dog = Dog(1.5, 13, 'Stefan', 7, 'KOSTIA')
    print(dog.name)
    dog.change_name('Mustang')
    print(dog.name)
    print(dog.get_master())
    print(dog.get_address())
    dog.set_address('Piter')
    print(dog.get_address())


if __name__ == '__main__':
    main()