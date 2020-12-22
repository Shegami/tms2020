"""
Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300.
"""


def num_friends(a, b):
    summ_1 = 0
    summ_2 = 0
    numbers = set()
    for i in range(a, b+1):
        for q in range(1, i):
            if i % q == 0:
                summ_1 += q
        for w in range(1, summ_1):
            if summ_1 % w == 0:
                summ_2 += w
        if summ_2 == i and summ_1 in range(a, b+1):
            numbers.add(i)
            numbers.add(summ_1)
        summ_1 = 0
        summ_2 = 0

    print(numbers)


def main():
    num_friends(200, 300)


if __name__ == '__main__':
    main()
