class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        new_item = {"name": name, "price": price}
        self.items.append(new_item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item['price']
        return total


sklepJanusza = Store("JanuszSklep")
sklepJanusza.add_item("wódka", 10)
sklepJanusza.add_item("kiełbasa", 15)
sklepJanusza.add_item("ogórki", 15)

print(sklepJanusza.stock_price())
