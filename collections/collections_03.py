"""
Создать список произвольного содержания. После каждой операции выводить список на экран.

1) Создать еще один список произвольного содержания.
2) Расширить первый список вторым.
3) Вставить 123 пятым элементом.
4) Вывести на экран длину итогового списка.
"""

spisok1 = ['1', '2', '3']
spisok2 = [1, 23, 123, 'kpss', 2131, 1, 2]
#  2
spisok1.extend(spisok2)
print(spisok1)
#  3, 4
spisok1.insert(4, 123)
print(spisok1)
print(len(spisok1))
