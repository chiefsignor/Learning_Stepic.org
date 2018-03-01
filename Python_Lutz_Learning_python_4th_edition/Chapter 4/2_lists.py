>>> S = 'A\0B\0C'
>>> len(S)
5
>>> msg = """ aaaaaaaaaaaaaaa
... bbb'''bbbbbbbbbbbbbbbbbb""bbbbbbbbbbb'bbbbbb
... cccccccccccccccccccccc"""
>>> msg
' aaaaaaaaaaaaaaa\nbbb\'\'\'bbbbbbbbbbbbbbbbbb""bbbbbbbbbbb\'bbbbbb\ncccccccccccccccccccccc'
>>> msg = """ aaaaaaaaaaaaaaa
... """
>>> msg
' aaaaaaaaaaaaaaa\n'
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello    Python world')
>>> match.group(1)
'Python '
>>> match.group(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
>>> match.group(0)
'Hello    Python world'
>>> match.group(len(1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> match.group(len())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: len() takes exactly one argument (0 given)
>>> match = re.match('/(.*)/(.*)/(.*)', '/home/sanzh/py_lutz')
>>> match.groups()
('home', 'sanzh', 'py_lutz')
>>> 
[7]+  Stopped                 python3
sanzh@sanzh-desktop ~ $ clear

sanzh@sanzh-desktop ~ $ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> l = [123, 'spam', 1.23]
>>> len(l)
3
>>> l[0]
123
>>> l[:-1]
[123, 'spam']
>>> l + [4, 5, 6]
[123, 'spam', 1.23, 4, 5, 6]
>>> l
[123, 'spam', 1.23]
>>> l.append('NI')
>>> l
[123, 'spam', 1.23, 'NI']
>>> l.pop(2)
1.23
>>> l
[123, 'spam', 'NI']
>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']
>>> M.reverse()
>>> M
['cc', 'bb', 'aa']
>>> L
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'L' is not defined
>>> l
[123, 'spam', 'NI']
>>> l[2]
'NI'
>>> l[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> m = [[1, 2, 3]
...      [4, 5, 6]
...      [7, 8, 9]]
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> m = [[1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9]]
>>> m
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> m[1]
[4, 5, 6]
>>> m[2]
[7, 8, 9]
>>> m[1][2]
6
>>> m[2][1]
8
>>> m[2][0]
7
>>> col2 = [row[1] for row in m]
>>> col2
[2, 5, 8]
>>> stolbec2 = [row[1] for row in m]
>>> stolbec2
[2, 5, 8]
>>> stolbec3 = [row[2] for row in m]
>>> stolbec2
[2, 5, 8]
>>> stolbec3
[3, 6, 9]
>>> m
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> [row[0] + 1 for row in m]
[2, 5, 8]
>>> [row[0] for row in m row[0] % 2 == 0]
  File "<stdin>", line 1
    [row[0] for row in m row[0] % 2 == 0]
                           ^
SyntaxError: invalid syntax
>>> [row[0] for row in m if row[0] % 2 == 0]
[4]
>>> [row[1] for row in m if row[1] % 2 == 0]
[2, 8]
>>> diag = [m[i][i] for i in [0, 1, 2]]
>>> diag
[1, 5, 9]
>>> doubles = [c * 2 for c in 'spam']
>>> doubles
['ss', 'pp', 'aa', 'mm']
>>> g = (sum(row) for row in m)
>>> next(g)
6
>>> next(g)
15
>>> next(g)
24
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> m
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> list(map(sum, m))
[6, 15, 24]
>>> {sum(row) for row in m}
{24, 6, 15}
>>> {i : sum(m[i]) for i in range(3)}
{0: 6, 1: 15, 2: 24}
>>> [ord(x) for x in 'spaam']
[115, 112, 97, 97, 109]
>>> {ord(x) for x in 'spaam'}
{112, 97, 115, 109}
>>> {x: ord(x) for x in 'spaam'}
{'m': 109, 's': 115, 'a': 97, 'p': 112}
>>> 

