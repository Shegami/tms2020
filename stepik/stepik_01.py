parents = {}
namespaces = {}


def create(namespace, parent):
    if parent in parents:
        parents[parent].append(namespaces[namespace])
    else:
        if namespace in namespaces:
            parents[parent] = namespaces[namespace]
        else:
            if parent in namespaces:
                namespaces[parent].append(namespace)
                parents[parent] = namespaces[parent]
            else:
                parents[parent] = [namespace]


def add(namespace, var):
    if namespace in namespaces:
        namespaces[namespace].append(var)
    else:
        namespaces[namespace] = [var]


def get(namespace, var):
    if namespace in namespaces and var in namespace:
        for key, value in parents.items():
            if namespace in value:
                print(key)
    elif namespace in namespaces and var not in namespace:
        for key, value in parents.items():
            if namespace in value:
                if var in value:
                    print(key)
                    break
                else:
                    print(None)
    elif namespace in namespaces and var in namespace:
        print(namespace)
    else:
        print(None)


n = int(input())
data = []

for i in range(n):
    cmd, namesp, arg = input().split()
    data.append(cmd)
    data.append(namesp)
    data.append(arg)

print(data)

counter = 0

for i in range(n):
    if data[counter] == 'create':
        create(data[counter + 1], data[counter + 2])
        counter += 3
    elif data[counter] == 'add':
        add(data[counter + 1], data[counter + 2])
        counter += 3
    else:
        get(data[counter + 1], data[counter + 2])
        counter += 3

print(parents)
print(namespaces)


def main():
    pass


if __name__ == '__main__':
    main()
