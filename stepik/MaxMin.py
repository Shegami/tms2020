a, b, c = int(input()), int(input()), int(input())
y, x = (max(a, b, c)), (min(a, b, c))
print(y, x, sep='\n')
z = a + b + c
print(z - (y + x))