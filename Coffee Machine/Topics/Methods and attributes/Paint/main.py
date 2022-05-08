class House:
    color: str

    def __init__(self, floors):
        self.floors = floors

    # create the method here
    def paint(self, color: str):
        self.color = color
