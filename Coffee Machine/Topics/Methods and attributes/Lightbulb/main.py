class Lightbulb:
    def __init__(self):
        self.state = "off"

    # create method change_state here
    def change_state(self):
        if self.state == "on":
            self.state = "off"
        else:
            self.state = "on"

        print("Turning the light", self.state)
