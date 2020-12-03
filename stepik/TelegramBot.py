HRec = int(input()) # 8
HMax = int(input()) # 10
HAnya = int(input()) # 9

if HRec > HAnya:
    print('Недосып')
elif HRec <= HAnya <= HMax:
    print('Здоровье')
else:
    print('Пересып')
