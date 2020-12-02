matches = int(input())
games = [input().split(';') for i in range(matches)] # создаём список, где каждая игра - это одтельный список
s = ''
lst = {}
w, l = '', ''
spisok = []
sp2 = set()
teams = []
for i in range(matches):
    for q in range(0, 4, 2):
        sp2.add(games[i][q])       # используем множества, чтобы затем преобразовать в список с командами-участниками
        spisok += [games[i][q]]    # создаём список с названиями команд (будем использовать для подсчёта игр)
for i in sp2:
    teams += [i]                   # преобразуем множества в список с командами-участниками
for a, b, c, d in games:
    if int(b) > int(d):            # делаем строки, где находятся только победители
        w += a
        l += c
    elif int(b) < int(d):          # и проигравшие
        w += c
        l += a
for i in range(len(teams)):        # для вывода результата считаем, сколько раз команда была в строке побед/поражений
    lst.setdefault(teams[i], (spisok.count(teams[i]), w.count(teams[i]), spisok.count(teams[i]) - w.count(teams[i]) - l.count(teams[i]), l.count(teams[i]), w.count(teams[i]) * 3 + (spisok.count(teams[i]) - w.count(teams[i]) - l.count(teams[i])) * 1))
for key, value in lst.items():
    print (key,end=':')
    print (*value)