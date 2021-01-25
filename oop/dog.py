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


def main():
    dog = Dog(1.5, 13, 'Stefan', 7)
    dog.jump()
    dog.run()
    dog.bark()
    print(dog.height)
    print(dog.weight)
    print(dog.name)
    print(dog.age)


if __name__ == '__main__':
    main()
