"""
Создать шаблон с формой Имя, фамилия, возраст.
Передать данные на вью дописать эти данные в файл
"""

from flask import Flask, url_for, redirect, request

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        return redirect(url_for(
            'success',
            first_name=first_name,
            last_name=last_name,
            age=age
        ))
    else:
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        age = request.args.get('age')
        return redirect(url_for(
            'success',
            first_name=first_name,
            last_name=last_name,
            age=age
        ))


@app.route('/success/<first_name>-<last_name>-<age>')
def success(first_name, last_name, age):
    with open('log_04.txt', 'a') as my_file:
        my_file.writelines([
            f'First name: {first_name}\n',
            f'Last name: {last_name}\n',
            f'Age: {age}\n',
            '\n'
            ])
    return f'welcome {first_name} {last_name}, ' \
           f'your age is {age}'


if __name__ == '__main__':
    app.run()
