frame = []
while True:                          # end - последняя строка
    a = input().split()
    if a ==['end']:
        break
    frame.append(a)                  # в матрицу попадают строки
a, b = len(frame), len(frame[0])
for q in range(a):
    for w in range(b):
        x = int(frame[q][w-1]) + int(frame[q][w+1-b]) + int(frame[q-1][w]) + int(frame[q+1-b][w])
        print(x, end=' ')
    print()