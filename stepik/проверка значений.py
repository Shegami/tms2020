s = input()
i = 0
b = len(s) - 1
palindrom = False
while b > i:
    if s[i] != s[b]:
        print('NOOO!')
        break
    else:
        while b > i:
            b -= 1
            i += 1
    print('YEEES!')