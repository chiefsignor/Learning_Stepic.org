x = input().split()
y = (int(i) for i in x)


def even(x):
    return x % 2 == 0

evens = list(filter(even, y))
print(evens)



