str, stl, bomb = (int(i) for i in input().split(' '))                     # высота, ширина кол-во бомб
frame = [[0 for i in range(stl)] for q in range(str)]                     # создание поля
bombs = [[int(i) - 1 for i in input().split()] for q in range(bomb)]      # координаты бомб
for q in range(bomb):
    frame[bombs[q][0]][bombs[q][1]] = -1
for i in range(str):
    for j in range(stl):
        if frame[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < str and 0 <= aj < stl and frame[ai][aj] == -1:
                        frame[i][j] += 1
for i in range(str):
    for j in range(stl):
        if frame[i][j] == 0:
            frame[i][j] = '.'
        elif frame[i][j] == -1:
            frame[i][j] = '*'
for q in range(len(frame)):
    print(frame[q])