"""
Ввести почтовый адрес. Проверить доменной имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика.
Иначе вывести надпись 'DOMAIN NAME is not supported’
"""

e_mail = input()

if e_mail.split('@')[1] == 'gmail.com':
    print(e_mail)
else:
    print('DOMAIN NAME is not supported')
