import math


class Sphere:
    PI = 3.1415
    # finish class Sphere here
    def __init__(self, radius):
        self.radius = radius
        self.volume = (4 / 3) * Sphere.PI * math.pow(self.radius, 3)
