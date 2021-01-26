"""
Создать файл car10.py.
Создать класс Car.
Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5),
уменьшение скорости(скорость  - 5),
стоп(сброс скорости на 0),
отображение скорости,
разворот(изменение знака скорости).
Все атрибуты приватные.
"""


class Car:
    def __init__(self,
                 brand, model,
                 year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop_speed(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def reverse_speed(self, speed):
        self.__speed = -speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed


def main():
    car_1 = Car('volvo', 'S90', 1997)
    print(car_1.brand)
    print(car_1.model)
    print(car_1.year)

    print(car_1.speed)
    car_1.speed = 17
    print(car_1.speed)

    car_1.increase_speed()
    print(car_1.speed)


if __name__ == '__main__':
    main()
