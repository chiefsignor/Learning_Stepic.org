def func(x):
    func = lambda x: x + 1
    return 100

import dis
print(dis.dis(func))