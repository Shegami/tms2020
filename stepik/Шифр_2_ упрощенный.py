s1, s2, s3, s4 = (input() for i in range(4))
print(*[s2[s1.find(i)] for i in s3], sep='')
print(*[s1[s2.find(i)] for i in s4], sep='')