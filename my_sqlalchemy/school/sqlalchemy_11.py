from my_sqlalchemy.school import models

group_1 = models.Group(name='TMS-01')
group_2 = models.Group(name='TMS-02')

student_1 = models.Student(
    firstname='Kostia', lastname='Toukach', group_id=1)
student_2 = models.Student(
    firstname='Vlad', lastname='Petrov', group_id=1)
student_3 = models.Student(
    firstname='Igor', lastname='Ivanovich', group_id=1)

student_4 = models.Student(
    firstname='Janna', lastname='Derevyago', group_id=2)
student_5 = models.Student(
    firstname='Masha', lastname='Ebanko', group_id=2)
student_6 = models.Student(
    firstname='Anton', lastname='Klimenko', group_id=2)

models.session.add_all([
    group_1,
    group_2
])
models.session.add_all([
    student_1,
    student_2,
    student_3,
    student_4,
    student_5,
    student_6
])
models.session.commit()


def main():
    pass


if __name__ == '__main__':
    main()
