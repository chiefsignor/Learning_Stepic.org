import re

# . ^ $ * + ? { } [ ] \ | ( ) --- метасимволы
# [] - можно указать множество подходящих символов
# \d - [0-9] -- цифры
# \D - [^0-9] -- не цифры
# \s - [ \t\n\r\f\v] -- переносы строк, пробел, таб и т.д.
# \S - [^ \t\n\r\f\v] -- все кроме: переносы строк, пробел, таб и т.д.
# \w - [a-zA-Z0-9] -- буквы + цифры + _
# \W - [a-zA-Z0-9] -- кроме: буквы + цифры + _

#pattern = r"a[^a-zA-Z]c"
#pattern = r"a\wc"
#pattern = r"a[\w.]c"
pattern = r"a.c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, a.c, aac, a-c, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)