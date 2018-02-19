f = open("text.txt")
x = f.readline().rstrip()
print(repr(x))
x = f.readline()
print(repr(x))



f.close()