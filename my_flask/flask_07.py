"""
Создать ветку flask_school от мастера.
Описать модель группы(id, fullname).
Создать сайт. Создать напрямую в базе 3 группы.
Описать шаблон и вью для получения и отображения списка всех групп.
Создать шаблон и вью для создания группы.
Добавить ссылку для перехода на создание группы
на страницу отображения всех групп.
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groups.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column(
         db.Integer,
         primary_key=True
    )
    name = db.Column(
        'name',
        db.String(100)
    )


db.init_app(app)
db.create_all()


@app.route('/get_group')
def get_groups():
    groups = Group.query.all()
    return render_template('get_group.html', groups=groups)


@app.route('/create_group', methods=['POST', 'GET'])
def create_group():
    if request.method == 'GET':
        return render_template('create_group.html')
    else:
        new_group = Group(name=request.form['group_name'])
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('get_groups'))


if __name__ == '__main__':
    app.run()
