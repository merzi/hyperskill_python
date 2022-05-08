import math
a = int(input())
b = int(input())
e = math.log(a, b) if b > 1 else math.log(a)
print(round(e, 2))
