package store
import "testing"
func TestAddInventory(t *testing.T) {
	store := NewStore()
	store.AddProduct("p1", 100.0, 5)
	store.AddInventory("p1", 10)
	if store.Inventory["p1"].Stock != 15 { t.Errorf("Error en stock") }
}