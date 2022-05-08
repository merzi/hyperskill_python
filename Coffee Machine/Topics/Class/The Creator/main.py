# create an Elf here
class Elf:
    height: float = 1.8
    weapon: str = "longbow"
    emotional_maturity: int = 125

    def get_attributes(self):
        return self.height, self.weapon, self.emotional_maturity

