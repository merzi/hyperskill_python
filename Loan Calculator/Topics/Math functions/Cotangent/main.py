import math

angle = int(input())

res = 1 / math.tan(math.radians(angle))

print(round(res, 10))
