x = input().split()
print(x)
map_obj = map(int, x) # f [a, b, c, ...] -> f(a), f(b), F(c), ...
print(map_obj)
n = next(map_obj)
k = next(map_obj)
print(n + k)
