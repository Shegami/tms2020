list = [int(i) for i in input().split()]
q = len(list)
list.sort()
for w in range(q):
    if q > 1:
        if w + 1 != q:
            if list[w - 1] == list[w] != list[w + 1]:
                print(list[w], end=' ')
        else:
            if list[w] == list[w - 1]:
                print(list[w])