import math

n = int(input())

for _ in range(1, n + 1):
    num = int(input())
    if num % 7 == 0:
        print(int(math.pow(num, 2)))
