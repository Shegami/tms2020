slvr, slvr2 = {}, {}
def shifr(x, y):
    for i in range(len(x)):
        slvr.setdefault(x[i], y[i])
        slvr2.setdefault(y[i], x[i])
shifr(input(), input())
[print(slvr.get(i), end='') for i in input()]
print()
[print(slvr2.get(i), end='') for i in input()]