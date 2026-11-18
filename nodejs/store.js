class Store {
  constructor() {
    this.inventory = new Map();
    this.discounts = new Map();
  }
  addProduct(id, price, stock) { this.inventory.set(id, { price, stock }); }
  addInventory(id, quantity) { if (this.inventory.has(id)) { this.inventory.get(id).stock += quantity; } }
  addDiscount(code, percentage) { this.discounts.set(code, percentage); }
  checkout(cart, discountCodes, taxRate) {
    if (discountCodes.length > 1) throw new Error("Solo se permite un código de descuento por compra.");
    for (const [id, qty] of Object.entries(cart)) {
      const item = this.inventory.get(id);
      if (!item || item.stock < qty) throw new Error(`Stock insuficiente para el producto ${id}.`);
    }
    let subtotal = 0;
    for (const [id, qty] of Object.entries(cart)) {
      const item = this.inventory.get(id);
      item.stock -= qty;
      subtotal += item.price * qty;
    }
    if (discountCodes.length === 1 && this.discounts.has(discountCodes[0])) {
      subtotal -= subtotal * this.discounts.get(discountCodes[0]);
    }
    return subtotal * (1 + taxRate);
  }
}
module.exports = Store;