frame = [[]]
n = int(input())
chisla = range(1, (n ** 2) + 1)
n1 = int((n * 2) / 2)
n2 = 0
x1 = 0
for i in range(n):
    for q in range(n):
        frame[i].append(0)
    frame.append([])
frame.remove([])
while True:
    for e in range(n + n - 1):
        if e != n + n - 2:
            if frame[n2][n1 - 1] == 0:
                for r in range(n2, n1):
                    frame[n2][r] = chisla[x1]
                    x1 += 1
            elif frame[n1 - 1][n1 - 1] == 0:
                for r in range(n2 + 1, n1):
                    frame[r][n1 - 1] = chisla[x1]
                    x1 += 1
            elif frame[n1 - 1][n2] == 0:
                for r in range(n2 + 2, n1 + 1):
                    frame[n1 - 1][-r] = chisla[x1]
                    x1 += 1
                n2 += 1
            elif frame[n2][n2 - 1] == 0:
                for r in range(n2 + 1, n1):
                    frame[-r][n2 - 1] = chisla[x1]
                    x1 += 1
                n1 -= 1
        else:
            frame[-n2 - 1][n2] = chisla[x1]
    break
for i in range(n):
    print(*frame[i])