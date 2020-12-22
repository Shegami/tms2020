"""
Дан список. Создать новый список,
сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1
"""


def num_plus_for(listt):
    index = 0
    for i in list(listt):
        listt[index - 1] = i
        index += 1
    print(listt)


def num_plus_while(listt):
    index = 0
    copy_list = list(listt)
    while True:
        if index != len(listt):
            listt[index - 1] = copy_list[index]
            index += 1
        else:
            print(listt)
            break


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    num_plus_for(numbers)
    # num_plus_while(numbers)


if __name__ == '__main__':
    main()
