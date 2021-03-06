n = int(input())
frame = [[0] * n for i in range(n)]
q, w = 0, 0
for i in range(1, n * n + 1):
    frame[q][w] = i
    if i == n * n:
        break
    if q <= w + 1 and q + w < n - 1:
        w += 1
    elif q < w and q + w >= n - 1:
        q += 1
    elif q >= w and q + w > n - 1:
        w -= 1
    elif q > w + 1 and q + w <= n-1:
        q -= 1
for i in range(n):
    print(*frame[i])