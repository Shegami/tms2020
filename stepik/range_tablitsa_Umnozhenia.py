a, b, c, d = input().split(',')
a, b, c, d = int(a), int(b), int(c), int(d),
for e in range(c, d + 1):
    print(' ', e, sep='\t', end='')
print()
for q in range(a, b + 1):
    print(q, end='\t')
    for w in range(c, d + 1):
        print(q * w, end='\t')
    print()