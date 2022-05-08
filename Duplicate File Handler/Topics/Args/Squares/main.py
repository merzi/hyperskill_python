import math


def sq_sum(*numbers):
    sum_value = 0
    for num in numbers:
        sum_value += math.pow(num, 2)
    return sum_value
