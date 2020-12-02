infa, infa2 = [], []
with open('dataset_3380_5.txt', 'r') as inf:
    for j in inf:
        infa += [j.split()]
        infa2 += j.split()
klss = {}
for i in range(len(infa)):
    if int(infa[i][0]) not in klss:
        klss.setdefault(int(infa[i][0]), float(infa[i][2]))
    else:
        klss[int(infa[i][0])] = klss[int(infa[i][0])] + float(infa[i][2])
for i in klss:
    klss[i] = klss[i] / infa2.count(str(i))
with open('otvet.txt', 'w') as answer:
    for q in range(1, 12):
        answer.write(str(q) + ' ')
        answer.write(str(klss.setdefault(q, '-')) + '\n')