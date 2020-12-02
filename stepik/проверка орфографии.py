slvr, slvr2, output = [], [], set()
[slvr.append(str(input()).lower()) for i in range(int(input()))]
[[(output.add(i)) for i in input().lower().split() if i not in slvr] for q in range(int(input()))]
[print(i) for i in output]