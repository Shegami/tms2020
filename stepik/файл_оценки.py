lst = []
sr1, sr2, sr3 = (0 for i in range(3))
with open('dataset_3363_4.txt', 'r') as inf:
    for j in inf:
        lst += [j.strip().split(';')]
if [''] in lst:
    lst.remove([''])
x = len(lst)
with open('Marks.txt', 'w') as mar:
    for i in range(x):
        lst0 = (int(lst[i][1]) + int(lst[i][2]) + int(lst[i][3]))/3
        mar.write(str(round(lst0, 12)))
        mar.write('\n')
        sr1 += int(lst[i][1])
        sr2 += int(lst[i][2])
        sr3 += int(lst[i][3])
    mar.write(str(round(sr1/x, 12)))
    mar.write(' ')
    mar.write(str(round(sr2/x, 12)))
    mar.write(' ')
    mar.write(str(round(sr3/x, 12)))