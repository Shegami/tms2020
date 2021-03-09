s = input()
s_new = ''
counter = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1
    else:
        s_new += s[i] + str(counter)
        i += 1
        counter = 1
print(s_new + s[i] + str(counter))