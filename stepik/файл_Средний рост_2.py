d = {str(i):[0]*2 for i in range(1,12)}
with open('dataset_3380_5.txt') as f:
    for key, n in [l.split()[::2] for l in f]:
        d[key] = [d[key][0] + int(n), d[key][1] + 1]
[print(key + ' ', n[0] / n[1] if n[0] else '-') for key, n in d.items()]