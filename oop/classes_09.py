"""
Создать файл classes09.py.
Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных
атрибута, конструктор, геттеры и
сеттеры для каждого атрибута, два метода.
"""


class Phone:
    def __init__(self, brand,
                 model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def play_music(self):
        return 'Dzin-Don, Dzin-Don!'

    def alarm(self):
        return 'Wake up, piece of lazy shit'

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
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


def main():
    phone_1 = Phone('Apple', 'Iphone XR', 1700)
    print(phone_1.model)
    print(phone_1.brand)
    print(phone_1.price)
    phone_1.model = 'P20 Lite'
    print(phone_1.model)
    phone_1.brand = 'Huawei'
    print(phone_1.brand)
    phone_1.price = 750
    print(phone_1.price)


if __name__ == '__main__':
    main()
