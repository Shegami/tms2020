s = input()
x = 0
c = 1
b = ''
n = len(s) - 1
for v in s[0:]:
    if x < n:
        while (x < n) and (s[x] == s[x + 1]):
            x += 1
            c += 1
        b = b + s.replace(s, s[x] + str(c))
        x += 1
        c = 1
    elif x == n:
        b = b + s.replace(s, s[x] + str(c))
        x += 1
        print(b)
    else:
        print(b)
        break