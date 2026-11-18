class Store:
    def __init__(self):
        self.inventory = {}
        self.discounts = {}
    def add_product(self, prod_id, price, stock):
        self.inventory[prod_id] = {'price': price, 'stock': stock}
    def add_inventory(self, prod_id, quantity):
        if prod_id in self.inventory: self.inventory[prod_id]['stock'] += quantity
    def add_discount(self, code, percentage):
        self.discounts[code] = percentage
    def checkout(self, cart, discount_codes, tax_rate):
        if len(discount_codes) > 1: raise ValueError("Solo un código permitido.")
        for prod_id, qty in cart.items():
            if prod_id not in self.inventory or self.inventory[prod_id]['stock'] < qty:
                raise ValueError("Stock insuficiente.")
        subtotal = 0.0
        for prod_id, qty in cart.items():
            self.inventory[prod_id]['stock'] -= qty
            subtotal += self.inventory[prod_id]['price'] * qty
        if len(discount_codes) == 1 and discount_codes[0] in self.discounts:
            subtotal -= subtotal * self.discounts[discount_codes[0]]
        return subtotal * (1 + tax_rate)