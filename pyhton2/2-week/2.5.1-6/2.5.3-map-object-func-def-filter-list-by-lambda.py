x = input().split()
y = (int(i) for i in x)


#def even(x):
#    return x % 2 == 0

evens = list(filter(lambda x: x % 2 == 0, y))
print(evens)


#1 51 5 16 8 746 51 16 5  6 146