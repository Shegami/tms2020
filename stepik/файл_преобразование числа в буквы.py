with open('dataset_3363_2.txt') as inf:
    str1 = inf.readline()
counter2 = 2
str2 = ''
for i in range(0, len(str1)):
    if 'a' <= str1[i] <= 'z' or 'A' <= str1[i] <= 'Z':
        counter = str(str1[i + 1])
        while '0' <= str1[i - len(str1) + counter2] <= '9':
            counter += str(str1[i + counter2])
            counter2 += 1
        str2 += str1[i] * int(counter)
        counter2 = 2
with open('1234.txt', 'w') as inf2:
    inf2.write(str2)