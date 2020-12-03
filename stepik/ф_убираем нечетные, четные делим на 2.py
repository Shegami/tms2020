lst = [1, 2, 3, 4, 5, 6]


def modify_list(l):
    for q in range(len(l)):
        if l[q] % 2 != 0:
            l[q] = 'x'
    for i in range(l.count('x')):
        l.remove('x')
    for i in range(len(l)):
        l[i] = l[i] // 2


modify_list(lst)
print(lst)
modify_list(lst)
print(lst)