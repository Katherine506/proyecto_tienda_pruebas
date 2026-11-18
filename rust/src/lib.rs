use std::collections::HashMap;
pub struct Product { pub price: f64, pub stock: u32 }
pub struct Store {
    pub inventory: HashMap<String, Product>,
    pub discounts: HashMap<String, f64>,
}
impl Store {
    pub fn new() -> Self { Store { inventory: HashMap::new(), discounts: HashMap::new() } }
    pub fn add_product(&mut self, id: String, price: f64, stock: u32) { self.inventory.insert(id, Product { price, stock }); }
    pub fn add_inventory(&mut self, id: &str, quantity: u32) { if let Some(product) = self.inventory.get_mut(id) { product.stock += quantity; } }
    pub fn add_discount(&mut self, code: String, percentage: f64) { self.discounts.insert(code, percentage); }
    pub fn checkout(&mut self, cart: &HashMap<String, u32>, discount_codes: &[String], tax_rate: f64) -> Result<f64, String> {
        if discount_codes.len() > 1 { return Err("Solo un código permitido".to_string()); }
        for (id, &qty) in cart {
            match self.inventory.get(id) {
                Some(product) if product.stock >= qty => continue,
                _ => return Err("Stock insuficiente".to_string()),
            }
        }
        let mut subtotal = 0.0;
        for (id, &qty) in cart {
            if let Some(product) = self.inventory.get_mut(id) {
                product.stock -= qty;
                subtotal += product.price * (qty as f64);
            }
        }
        if discount_codes.len() == 1 {
            if let Some(&discount) = self.discounts.get(&discount_codes[0]) { subtotal -= subtotal * discount; }
        }
        Ok(subtotal * (1.0 + tax_rate))
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_add_inventory() {
        let mut store = Store::new();
        store.add_product("p1".to_string(), 100.0, 5);
        store.add_inventory("p1", 10);
        assert_eq!(store.inventory.get("p1").unwrap().stock, 15);
    }
}