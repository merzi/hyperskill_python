# the list "walks" is already defined
# your code here
sum_ = 0
for entry in walks:
    sum_ += entry.get("distance")

print(round(sum_ / len(walks)))
