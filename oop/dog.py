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
                 weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    # oop_05
    def change_name(self, name):
        self.name = name


def main():
    dog = Dog(1.5, 13, 'Stefan', 7)
    print(dog.name)
    dog.change_name('Mustang')
    print(dog.name)


if __name__ == '__main__':
    main()
