lst, x = [int(i) for i in input().split()], int(input())
if x not in lst:
    print('Отсутствует')
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')