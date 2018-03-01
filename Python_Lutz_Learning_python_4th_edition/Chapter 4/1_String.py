sanzh@sanzh-desktop ~ $ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> len(str(2 ** 1000000))
^[[F301030
>>> len(str(2 ** 1000000))
301030
>>> 3.1415 * 2
6.283
>>> print (3.1415 * 2)
6.283
>>> math.pi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> import math
>>> math.pi
3.141592653589793
>>> math sqrt(49)
  File "<stdin>", line 1
    math sqrt(49)
            ^
SyntaxError: invalid syntax
>>> import math
>>> math sqrt(49)
  File "<stdin>", line 1
    math sqrt(49)
            ^
SyntaxError: invalid syntax
>>> math.sqrt(49)
7.0
>>> import random
>>> random.random
<built-in method random of Random object at 0x190ff08>
>>> random.random()
0.9411023837980821
>>> random.random(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: random() takes no arguments (1 given)
>>> random.choice([1,2,3,4])
1
>>> random.choice([1,2,3,4])
2
>>> random.choice([1,2,3,4])
3
>>> random.choice([1,2,3,4])
1
>>> random.choice([1,2,3,4])
1
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
1
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
2
>>> random.choice([1,2,3,4])
3
>>> random.choice([1,2,3,4])
3
>>> random.choice([1,2,3,4])
3
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
2
>>> random.choice([1,2,3,4])
4
>>> S = 'Spam'
>>> lan(S)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lan' is not defined
>>> len(S)
4
>>> S[0]
'S'
>>> S[1]
'p'
>>> ~
  File "<stdin>", line 1
    ~
    ^
SyntaxError: invalid syntax
>>> 
[1]+  Stopped                 python3
sanzh@sanzh-desktop ~ $ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
[2]+  Stopped                 python3
sanzh@sanzh-desktop ~ $ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> S
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'S' is not defined
>>> S = 'Spam'
>>> S
'Spam'
>>> S[1:3]
'pa'
>>> S[0:2]
'Sp'
>>> S
'Spam'
>>> S + 'xyz'
'Spamxyz'
>>> S
'Spam'
>>> S * 9
'SpamSpamSpamSpamSpamSpamSpamSpamSpam'
>>> S[0] = 'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> S = 'z' + S[1:]
>>> S
'zpam'
>>> s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> S.find('pa')
1
>>> S
'zpam'
>>> S = 'S' + S[1:]
>>> S
'Spam'
>>> S.replace('pa', 'XYZ')
'SXYZm'
>>> S
'Spam'
>>> S
'Spam'
>>> line = 'aaa,bbb,ccccc,dd\n'
>>> дшту
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'дшту' is not defined
>>> line
'aaa,bbb,ccccc,dd\n'
>>> line = line.rstrip()
>>> line
'aaa,bbb,ccccc,dd'


>>> '%s, eggs, and %s' % ('spam', 'SPAM!')
'spam, eggs, and SPAM!'
>>> '{0}, eggs, and {1}
  File "<stdin>", line 1
    '{0}, eggs, and {1}
                      ^
SyntaxError: EOL while scanning string literal
>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!')
'spam, eggs, and SPAM!'
>>> '{0}, eggs, and {2}'.format('spam', 'S', 'onetwothree')
'spam, eggs, and onetwothree'
>>> 

>>> S = 'A\nB\tC'
>>> S
'A\nB\tC'
>>> len(S)
5
>>> ord('\n')
10
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

# Далее Списки







