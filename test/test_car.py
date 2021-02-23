import unittest
from oop.car_10 import Car


class CarTestCase(unittest.TestCase):
    def test_unit_speed_up(self):
        car = Car('Toyota', 'Camry 3.5', 2020)
        car.increase_speed()
        self.assertEqual(car.speed, 5)

    def test_unit_decrease_speed(self):
        car = Car('Toyota', 'Camry 3.5', 2020)
        car.decrease_speed()
        self.assertEqual(car.speed, -5)

    def test_unit_stop(self):
        car = Car('Toyota', 'Camry 3.5', 2020)
        car.increase_speed()
        car.stop_speed()
        self.assertEqual(car.speed, 0)

    def test_unit_reverse(self):
        car = Car('Toyota', 'Camry 3.5', 2020)
        car.reverse_speed(10)
        self.assertEqual(car.speed, -10)
