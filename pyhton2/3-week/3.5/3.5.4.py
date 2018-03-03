import json

input = input()
data = json.loads(input)
classs = dict()
offspr = dict()
check = dict()


def checking(name, elem):
    for x in classs[name]:
        if elem not in check[x]:
            check[x].append(elem)
            offspr[x] += 1
            checking(x, elem)

for y in data:
    classs[y['name']] = y['parents']
    offspr[y['name']] = 1
    check[y['name']] = [y['name']]

for name in classs:
    checking(name, name)

keys = []
for v in classs.keys():
    keys.append(v)

keys.sort()
for v in keys:
    print(str(v) + ' : ' + str(offspr[v]))