"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания.
После колличество попыток. В случае правильного
ответа - выводить You are the winner. В случае неправильного
давать игроку подсказку(больше или меньше искомое число).
Если за указанное количество попыток число не угадано -
выводить: You are the loser и правильное число.
"""

from random import randint


def range_try(minn, maxx, try_numb):
    right_answer = randint(minn, maxx)
    for tries in range(1, try_numb+1):
        answer = int(input('Your answer: '))
        if answer == right_answer:
            print('You are the winner')
            break
        else:
            if tries < try_numb:
                if answer > right_answer:
                    print('Less')
                else:
                    print('More')
    else:
        print('You are the loser')
        print(f'Right answer: {right_answer}')


def main():
    range_try(1, 100, 3)


if __name__ == '__main__':
    main()
