"""
Описать функцию is_power_n( k , n ) логического типа,
возвращающую True, если целый параметр k (> 0)
является степенью числа n (> 1), и False
в противном случае.
Дано число n (> 1) и набор из 10 целых положительных чисел.
С помощью функции is_power_n найти количество
степеней числа n в данном наборе.
"""


def is_power_n(k, n):
    counter = 0
    for i in range(len(k)):
        while True:
            if k[i] == 0 or k[i] == 1:
                counter += 1
                break
            n = n / k[i]
            if n > 1:
                continue
            elif n == 1:
                counter += 1
                break
            else:
                break
    print(counter)


def main():
    numbers = [0, 1, 2, 3]
    is_power_n(numbers, 4)


if __name__ == '__main__':
    main()
