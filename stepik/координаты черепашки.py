coord = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
for i in range(int(input())):
    stroka = input().split()
    coord[stroka[0]] += int(stroka[1])
print(coord['восток'] - coord['запад'], coord['север'] - coord['юг'])