"""
Ввести предложение состоящее из двух слов.
Поменять местами слова, добавить восклицательный знак в начало и конец,
вывести итоговое предложение на экран.
"""

sentence = input().split(' ')
sentence = sentence[::-1]
print(f'! {sentence[0]} {sentence[1]}!')
