# our class Ship
class Ship:
    name: str
    capacity: int
    cargo: int

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination: str):
        return "The {} has sailed for {}!".format(self.name, destination)


black_pearl_capacity = 800
black_pearl = Ship("Black Pearl", black_pearl_capacity)
print(black_pearl.sail(input()))
