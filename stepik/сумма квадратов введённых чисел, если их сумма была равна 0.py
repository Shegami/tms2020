chisla = [int(input())]
while sum(chisla) != 0:
    chisla.append(int(input()))
print(sum(i ** 2 for i in chisla))