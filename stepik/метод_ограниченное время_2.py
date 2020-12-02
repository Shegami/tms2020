str = input().split()
spisok = {}
for i in range(len(str)):
    str[i] = str[i].lower()
    spisok.update({str[i]: str.count(str[i])})
for i in spisok:
    print(i, spisok[i], sep=' ')