s = input()
a = s[0]
counter = 0
for i in s[0:]:
    if i == a:
        counter += 1
    else:
        print(a + str(counter), sep='', end='')
        counter = 1
        a = i
else:
    print(a + str(counter), sep='', end='') 