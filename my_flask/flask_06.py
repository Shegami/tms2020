"""
Создать шаблон flask_06_form.html с формой Имя, фамилия, возраст.
Создать вью /form: при GET запросе отображать форму,
при POST запросе Выводить данные пользователю с
помощью шаблона flask_06_display.html
"""

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        return render_template(
            'flask_06_display.html',
            last_name=last_name,
            first_name=first_name,
            age=age
        )
    else:
        return render_template('flask_06_form.html',)


if __name__ == '__main__':
    app.run()
