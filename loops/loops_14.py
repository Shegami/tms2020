"""
Создать список учеников подобной структуры.
Определить средний балл оценок по всем предметам,
и вывести сведения о студентах,
средний балл которых больше 4.
"""


def avg_mark(listt):
    for row in listt:
        summ = row['math'] + row['economics'] + row['physics']
        if (summ / 3) > 4:
            print(
                f'Фамилия: {row["firstname"]}',
                f'Группа: {row["group"]}',
                f'Математика: {row["math"]}',
                f'Экономика: {row["economics"]}',
                f'Физика: {row["physics"]}',
                sep='\n'
            )
            print()


def main():
    pupils = [
        {
            'firstname': 'Petrov',
            'group': 1,
            'math': 5,
            'economics': 7,
            'physics': 6
        },
        {
            'firstname': 'Sidorov',
            'group': 1,
            'math': 4,
            'economics': 3,
            'physics': 2
        },
        {
            'firstname': 'Popov',
            'group': 1,
            'math': 8,
            'economics': 10,
            'physics': 7
        }
    ]
    avg_mark(pupils)


if __name__ == '__main__':
    main()
