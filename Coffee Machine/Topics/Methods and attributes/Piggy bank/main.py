class PiggyBank:
    dollars: int = 0
    cents: int = 0

    # create __init__ and add_money methods
    def __init__(self, deposit_dollars: int = 0, deposit_cents: int = 0):
        self.add_money(deposit_dollars, deposit_cents)

    def add_money(self, deposit_dollars: int, deposit_cents: int) -> None:
        self.cents += deposit_cents
        self.dollars += deposit_dollars + self.cents // 100
        self.cents = self.cents % 100



