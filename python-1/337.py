classes = {c:[] for c in range(1,12)}
with open('dataset_3380_5.txt') as inf:
    [classes[int(line.strip().split()[0])].append(int(line.strip().split()[2])) for line in inf.readlines()]
[print(i, ' ', '-' if classes[i]==[] else sum(classes[i])/len(classes[i])) for i in range(1,12)]
