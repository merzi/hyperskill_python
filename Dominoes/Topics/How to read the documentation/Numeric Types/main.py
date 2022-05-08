from math import pow


def some_calculate(a, b):
    print(int(abs((a % b) - pow(b, a))))

