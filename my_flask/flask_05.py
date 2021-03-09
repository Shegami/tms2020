"""
Создать папку templates в корне проекта.
Создать шаблон flask_05.html с формой Имя, фамилия, возраст.
Создать вью /form: при GET запросе отображать форму,
при POST запросе дописывать переданные данные в файл.
"""

from flask import Flask, request, url_for,\
    redirect, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def main():
    return render_template('flask_05.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        return redirect(
            url_for(
                'success',
                last_name=last_name,
                first_name=first_name,
                age=age,
            ))


@app.route('/success/<last_name>-<first_name>-<age>')
def success(last_name, first_name, age):
    with open('flask_05.txt', 'a') as my_file:
        my_file.writelines([
            f'First name: {first_name}\n',
            f'Last name: {last_name}\n',
            f'Age: {age}\n',
            '\n'
            ])
    return redirect(url_for(
        'main'
    ))


if __name__ == '__main__':
    app.run()
