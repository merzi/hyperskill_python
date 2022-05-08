import math


class Hexagon:
    side_length: float

    def __init__(self, side_length: float):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        length_square = self.side_length ** 2
        x = (length_square * 3) / 2
        return round(x * math.sqrt(3), 3)
