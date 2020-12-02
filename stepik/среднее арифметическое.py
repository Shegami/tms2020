a, b = int(input()), int(input())
w = 0
f = 0
for q in range(a, b):
    if q % 3 == 0:
        w += q
        f += 1
print(w / f)