class Angel:
    color: str = "white"
    feature = "wings"
    home = "Heaven"

    def get_information(self):
        return self.color, self.feature, self.home


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"

    def get_information(self):
        return self.color, self.feature, self.home


angel = Angel()
demon = Demon()
print(angel.color)
print(angel.feature)
print(angel.home)
print(demon.color)
print(demon.feature)
print(demon.home)
