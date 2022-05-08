import math


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist(self, other_point):
        a = math.pow(self.x - other_point.x, 2)
        b = math.pow(self.y - other_point.y, 2)
        return math.sqrt(a + b)
