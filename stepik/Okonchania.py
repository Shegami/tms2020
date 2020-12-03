a = int(input())
if 10 < a % 100 < 15:
    print(str(a) + ' программистов')
elif a % 10 == 1:
    print(str(a) + ' программист')
elif 1 < a % 10 < 5:
    print(str(a) + ' программиста')
else:
    print(str(a) + ' программистов')