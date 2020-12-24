"""
Описать функцию is_power_n( k , n ) логического типа,
возвращающую True, если целый параметр k (> 0)
является степенью числа n (> 1), и False
в противном случае.
Дано число n (> 1) и набор из 10 целых положительных чисел.
С помощью функции is_power_n найти количество
степеней числа N в данном наборе.
"""


def is_power_n(k, n):
    counter = 0
    while True:
        k = k / n
        if k > 1:
            counter += 1
            continue
        elif k == 1:
            return True, counter
        else:
            break


def main():
    result = is_power_n(16, 2)
    print(result)


if __name__ == '__main__':
    main()
