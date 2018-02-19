x = [
    ("Guido", "van", "Rossum"),
    ("Haskel", "Curry"),
    ("John", "Backus")
]

def lenght(name):
    return len(" ".join(name))

name_lenghts = [lenght(asd) for asd in x]
print(name_lenghts)

x.sort(key=lenght)
print(x)
