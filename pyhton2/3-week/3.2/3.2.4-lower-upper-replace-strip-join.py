#s = "The man in black fled across the desert, and the gunslinger follwed"
#print(s.lower())
#print(s.upper())
#print(s.count("the"))
#print(s.lower().count("the"))

#s = "1,2,3,4"
#print(s)
#print(s.replace(",", ", ", 2))
#print(s.replace.__doc__)

#s = "1 2 3 4"
#print(s.split(" ", 2))
#print(s.split.__doc__)

#s = "1\t\t 2  3           4          "
#print(s.split())
#print(s.split.__doc__)

#s = "      1, 2, 3, 4        "
#print(repr(s.rstrip()))
#print(repr(s.lstrip()))
#print(repr(s.strip()))

#s = "_*__1, 2, 3, 4__*_"
#print(repr(s.rstrip("*_")))
#print(repr(s.lstrip("*_")))
#print(repr(s.strip("*_")))

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" ".join(numbers)))



