import re

#print(re.match)
#print(re.search)
#print(re.findall)
#print(re.sub)

# [] - можно указать множество подходящих символов

#pattern = r"abc"
pattern = r"a[abc]c"
#string = "abcd"
#string = "accd"
#string = "babc"
string = "acc"
#match_object = re.search(pattern, string)
match_object = re.match(pattern, string)
print(match_object)
