"""
Создать ветку flask_school от мастера.
Описать модель группы(id, fullname).
Создать сайт. Создать напрямую в базе 3 группы.
Описать шаблон и вью для получения и отображения списка всех групп.
Создать шаблон и вью для создания группы.
Добавить ссылку для перехода на создание группы
на страницу отображения всех групп.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///groups.db'
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


@app.route('/groups', methods=['GET'])
def groups():
    groupss = Group.query.all()
    return render_template('groups.html', groups=groupss)


if __name__ == '__main__':
    app.run()
