# Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def list_items(self):
        if not self.items:
            print("Cart is empty.")
            return
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['name']} - Rp{item['price']}")

    def show_items(self):
        print("Item List:")
        self.list_items()

    def total_price(self):
        return sum(item["price"] for item in self.items)

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"{name} has been removed.")
                return
        print(f"{name} not found in the cart.")

# --- Testing ---
cart = ShoppingCart()
cart.add_item("Book", 50000)
cart.add_item("Pen", 10000)
cart.add_item("Pencil", 5000)

cart.remove_item("Pen")
cart.show_items()
print("Total purchase:", cart.total_price())