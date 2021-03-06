spisok = {}
for i in range(int(input())):
    y = int(input())
    if y not in spisok:
        spisok.setdefault(y, f(y))
        print(spisok.get(y))
    else:
        print(spisok.get(y))