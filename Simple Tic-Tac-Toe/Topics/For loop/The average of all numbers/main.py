# put your python code here
a = int(input())
b = int(input())
i = 0
sum_ = 0

for c in range(a, b + 1):
    if c % 3 == 0:
        i += 1
        sum_ += c

print(sum_ / i)
