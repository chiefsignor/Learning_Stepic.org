x = input().split()
y = (int(i) for i in x)


def even(x):
    return x % 2 == 0

evens = filter(even, y)
for i in evens:
    print(i)

