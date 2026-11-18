const test = require('node:test');
const assert = require('node:assert');
const Store = require('./store');

test('Store - Ingreso de unidades a inventario', () => {
  const store = new Store();
  store.addProduct('p1', 100, 5);
  store.addInventory('p1', 10);
  assert.strictEqual(store.inventory.get('p1').stock, 15, 'El stock debería ser 15');
});