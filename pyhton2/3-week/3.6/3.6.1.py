import requests
with open("dataset_24476_3.txt") as f:
    for numeric in f:
        res = requests.get("http://numbersapi.com/"+numeric.strip()+"/math?json=true")
        if res.json()["found"]:
            print("Interesting")
        else:
            print("Boring")