"""
Создать сайт.
При запросе по урлу /my_word/[word],
в случае если длина слова четна - выводит строку содержащую
все нечетные элементы строки(abcde -> ace).
В ином случае перенаправлять на домашнюю сранинцу.
"""

from flask import Flask, url_for, redirect
from datetime import date

app = Flask(__name__)


@app.route('/')
def current_date():
    return f'{date.today()}'


@app.route('/my_word/<string:word>')
def my_word(word):
    assert isinstance(word, str)
    if len(word) % 2 == 0:
        return f'{word[::2]}'
    else:
        return redirect(url_for('current_date'))


if __name__ == '__main__':
    app.run()
