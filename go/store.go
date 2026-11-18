package store
import ( "errors"; "fmt" )
type Product struct { Price float64; Stock int }
type Store struct {
	Inventory map[string]*Product
	Discounts map[string]float64
}
func NewStore() *Store {
	return &Store{ Inventory: make(map[string]*Product), Discounts: make(map[string]float64) }
}
func (s *Store) AddProduct(id string, price float64, stock int) { s.Inventory[id] = &Product{Price: price, Stock: stock} }
func (s *Store) AddInventory(id string, quantity int) { if prod, exists := s.Inventory[id]; exists { prod.Stock += quantity } }
func (s *Store) AddDiscount(code string, percentage float64) { s.Discounts[code] = percentage }
func (s *Store) Checkout(cart map[string]int, discountCodes []string, taxRate float64) (float64, error) {
	if len(discountCodes) > 1 { return 0, errors.New("solo un código permitido") }
	for id, qty := range cart {
		if prod, exists := s.Inventory[id]; !exists || prod.Stock < qty { return 0, fmt.Errorf("stock insuficiente") }
	}
	subtotal := 0.0
	for id, qty := range cart {
		prod := s.Inventory[id]
		prod.Stock -= qty
		subtotal += prod.Price * float64(qty)
	}
	if len(discountCodes) == 1 {
		if discount, exists := s.Discounts[discountCodes[0]]; exists { subtotal -= subtotal * discount }
	}
	return subtotal * (1 + taxRate), nil
}