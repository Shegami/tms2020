"""
Просуммировать неопределенное количество чисел,
вводимых пользователем, суммировать до тех пор,
пока пользователь не введёт слово «стоп»
"""

string = input()
summ = 0

while True:
    if string == 'стоп':
        break
    else:
        summ += float(string)
        string = input()
print(summ)
