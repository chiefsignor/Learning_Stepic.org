import re

#pattern = r"ab*a"
#pattern = r"ab+a"
#pattern = r"ab?a"
#pattern = r"ab{3}a"
#pattern = r"ab{2,5}a"
#string = "aa, aba, abba"
#string = "aa, aba, abba, abbba, abbbba, abbbbba"
#all_incusions = re.findall(pattern, string)
#print(all_incusions)

#pattern = r"a[ab]+a"
pattern = r"a[ab]+?a"
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))