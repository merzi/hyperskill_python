class Store:
    name: str
    category: str

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category


shop = Store("GAP", "clothes")
print(shop.name, shop.category)
