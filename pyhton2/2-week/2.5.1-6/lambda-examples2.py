def addition(x):
    return lambda y: x + y
add_to_ten = addition(10)
print(add_to_ten(8))
print(add_to_ten(6))