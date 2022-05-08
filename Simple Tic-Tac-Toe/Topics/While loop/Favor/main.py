k = int(input())
counter = 1
storage = []

while counter <= k:
    storage.append(counter)
    counter += 1

print(sum(storage))
