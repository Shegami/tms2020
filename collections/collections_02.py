"""
Создать список произвольного содержания. После каждой операции выводить список на экран.

1) Добавить к нему строку “Hello”.
2) Удалить первый элемент.
3) Поменять второй элемент на строку “World”.
4) Удалить элемент “World”
5) Вывести на экран перевернутый список
"""

spisok = [1, 23, 'qwe', 'spisok1', 999]

#  1
spisok.append('Hello')
print(spisok)
#  2
spisok.pop(0)
print(spisok)
#  3
spisok[1] = 'World'
print(spisok)
#  4
spisok.remove('World')
print(spisok)
#  5
print(spisok[::-1])
