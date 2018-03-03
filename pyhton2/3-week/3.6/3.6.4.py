es = []
with open('dataset_24476_4.txt', 'r') as f, open('result.txt', 'w', encoding='utf-8') as w:
    for i in f:
        req_str = 'https://api.artsy.net/api/artists/' + i.rstrip()
        j = requests.get(req_str, headers=headers).json()
        res.append(j['birthday']+j['sortable_name'])
    for i in sorted(res):
        w.write(i[4:]+'\n')