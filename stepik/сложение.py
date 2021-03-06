list = [int(i) for i in input().split()]
len = len(list) - 1
if len > 0:
    for q in range(int(len)):
        print(list[q + 1] + list[q - 1], end=' ')
    print(list[-2] + list[0])
else:
    print(list[0])