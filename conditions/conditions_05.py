"""
Ввести число, проверить на то, что было введено именно число.
Возвести его в куб.
"""

string = input()

if string.isdigit():
    print(float(string) ** 3)
else:
    print('Not digit')
