slovar = {}
with open('dataset_3363_3.txt', 'r') as inf:
    stroka = inf.read().lower().split()
for i in stroka:
    slovar.setdefault(i, stroka.count(i))
value = 0
for q in slovar:
    if slovar.get(q) > value:
        key = q
        value = slovar.get(q)
    elif slovar.get(q) == value:
        key1 = q
        value1 = slovar.get(q)
if value > value1:
    print(key, value, sep=' ')
elif value == value1:
    if key[0] < key1[0]:
        print(key, value, sep=' ')
    else:
        print(key1, value1, sep=' ')
else:
    print(key1, value1, sep=' ')