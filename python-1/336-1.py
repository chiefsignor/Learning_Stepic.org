import requests
with open('dataset_3378_3.txt') as txt:
    a = txt.readline().strip()
print(a)
a = str(requests.get(a).text)
b = 'https://stepic.org/media/attachments/course67/3.6.3/'
while 'we' not in a:
    print(a)
    a = requests.get(b + a).text
print(a)
