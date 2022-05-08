class Mountain:
    name: str
    height: float

    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    # create convert_height here
    def convert_height(self):
        foot_conversion_number = 0.3048
        return self.height / foot_conversion_number
