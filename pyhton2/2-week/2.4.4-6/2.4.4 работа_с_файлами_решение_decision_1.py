with open("dataset_24465_4.txt") as f, open("dataset_24465_4_copy.txt", "w") as f2:
  for line in reversed(list(f)):
    f2.write(line)