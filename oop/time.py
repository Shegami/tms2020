"""
Создать файл time.py. Создать класс MyTime.
Атрибуты: hours, minutes, seconds.
Переопределить магические методы сравнения(равно, не равно),
сложения, вычитания, вывод на экран.
Перегрузить конструктор на обработку входных параметров вида:
одна строка, три числа, другой объект класса MyTime.
В остальных случаях создавать объект по-умолчанию(0-0-0)
"""


class MyTime:
    def __init__(self, *args):
        if args != () and type(args[0]) == int and len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif args != () and type(args[0]) == str:
            time = args[0].split('-')
            self.hours = int(time[0])
            self.minutes = int(time[1])
            self.seconds = int(time[2])
        elif args != () and type(args[0]) == MyTime:
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def __eq__(self, other):
        return all([
            self.hours == other.hours,
            self.minutes == other.minutes,
            self.seconds == other.seconds
        ])

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        sec = self.seconds + other.seconds
        mints = self.minutes + other.minutes
        hours = self.hours + other.hours
        return MyTime(hours, mints, sec)

    def __sub__(self, other):
        sec = self.seconds - other.seconds
        mints = self.minutes - other.minutes
        hours = self.hours - other.hours
        if sec < 0 or mints < 0 or hours < 0:
            return MyTime(0, 0, 0)
        else:
            return MyTime(hours, mints, sec)

    def __str__(self):
        return f'{self.hours + self.minutes // 60}-'\
               f'{(self.minutes % 60) +(self.seconds // 60)}-'\
               f'{self.seconds % 60}'


def main():
    time = MyTime(1, 13, 64)
    time_2 = MyTime('1-12-64')
    time_3 = MyTime(time)
    time_4 = MyTime()
    print(time)
    print(time_2)
    print(time_3)
    print(time_4)
    print(time_2 - time)
    print(time - time_2)


if __name__ == '__main__':
    main()
