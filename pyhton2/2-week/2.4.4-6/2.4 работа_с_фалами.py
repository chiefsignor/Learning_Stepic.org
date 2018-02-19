f = open("text.txt")
x = f.read()
x = x.splitlines()
print(repr(x))


f.close()
