import math


class RightTriangle:
    a: int
    b: int
    c: int
    area: float

    def __init__(self, hyp: int, leg_1: int, leg_2: int):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.calculate_area()

    def calculate_area(self):
        self.area = (1 / 2) * self.a * self.b

    def is_right_triangle(self):
        return math.pow(self.c, 2) == math.pow(self.a, 2) + math.pow(self.b, 2)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)

if triangle.is_right_triangle():
    print(triangle.area)
else:
    print("Not right")
