a, b = int(input()), int(input())
n = 0
if n == 0:
    n += 1
while n % b != 0 or n % a != 0:
    n += 1
print(n)