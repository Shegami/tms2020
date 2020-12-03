frame = []
a = [i for i in input().split()]
while a[0] != 'end':                          # end останавливает матрицу
    frame.append(a)
    a = [i for i in input().split()]          # в матрицу попадают строки
for i in range(len(frame)):
    for q in range(len(frame[i])):
        frame[i][q] = int(frame[i][q])        # преобразуем строки в int
frame2 = [[]]
str = len(frame)                              # кол-во строк
for q in range(str):
    stl = len(frame[q])                       # кол-во столбцов
    for w in range(stl):
        a = frame[q - 1][w] +\
            frame[q - str + 1][w] +\
            frame[q][w - 1] +\
            frame[q][w - stl + 1]             # вычисляем сумму крайних значений
        frame2[q].insert(w, a)                # чтобы матрица была разбита на 3 отдельных списка
    frame2.append([])                         # вставляем пустой список, куда кладём новые значения
frame2.remove([])                             # после последнего значения убираем пустой список, т.к. лишний
for m in range(len(frame2)):
    print(*frame2[m])