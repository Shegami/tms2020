"""
Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”
Примечание: после ввода переменных преобразовать переменные к типу int
 >> first_number = int(first_number)
"""

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(f'{x} плюс {y} равно {x + y}')
