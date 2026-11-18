/** Pruebas independientes: cada test construye su propia tienda. */
const test = require("node:test");
const assert = require("node:assert/strict");
const Store = require("./store");

function newStore() {
  const store = new Store();
  store.addProduct("p1", 100, 5);
  return store;
}

function assertAmount(actual, expected) {
  assert.ok(
    Math.abs(actual - expected) < 1e-8,
    `Total esperado ${expected}, total recibido ${actual}`,
  );
}

// Grupo 1: gestión de inventario
test("registrar producto nuevo conserva precio y stock inicial", () => {
  const store = newStore();
  store.addProduct("p2", 25, 8);
  assert.deepStrictEqual(store.inventory.get("p2"), { price: 25, stock: 8 });
});

test("incrementar inventario existente suma las unidades", () => {
  const store = newStore();
  store.addInventory("p1", 10);
  assert.equal(store.inventory.get("p1").stock, 15);
});

// Grupo 2: validaciones y atomicidad de la venta
test("stock insuficiente lanza error y no descuenta inventario", () => {
  const store = newStore();
  assert.throws(
    () => store.checkout({ p1: 6 }, [], 0.13),
    /Stock insuficiente/,
  );
  assert.equal(store.inventory.get("p1").stock, 5);
});

test("dos descuentos lanzan error y no descuentan inventario", () => {
  const store = newStore();
  store.addDiscount("DIEZ", 0.1);
  store.addDiscount("CINCO", 0.05);
  assert.throws(
    () => store.checkout({ p1: 1 }, ["DIEZ", "CINCO"], 0.13),
    /Solo se permite un código/,
  );
  assert.equal(store.inventory.get("p1").stock, 5);
});

// Grupo 3: cálculos financieros y actualización de inventario
test("venta sin descuento calcula subtotal impuesto y stock", () => {
  const store = newStore();
  const total = store.checkout({ p1: 2 }, [], 0.13);
  assertAmount(total, 226);
  assert.equal(store.inventory.get("p1").stock, 3);
});

test("venta con un descuento aplica descuento antes de impuesto", () => {
  const store = newStore();
  store.addDiscount("DIEZ", 0.1);
  const total = store.checkout({ p1: 2 }, ["DIEZ"], 0.13);
  assertAmount(total, 203.4);
  assert.equal(store.inventory.get("p1").stock, 3);
});

// Casos adicionales
test("compra exacta del stock disponible es válida", () => {
  const store = newStore();
  assertAmount(store.checkout({ p1: 5 }, [], 0), 500);
  assert.equal(store.inventory.get("p1").stock, 0);
});

test("tres descuentos lanzan error y conservan stock", () => {
  const store = newStore();
  for (const code of ["A", "B", "C"]) {
    store.addDiscount(code, 0.05);
  }
  assert.throws(
    () => store.checkout({ p1: 1 }, ["A", "B", "C"], 0.13),
    /Solo se permite un código/,
  );
  assert.equal(store.inventory.get("p1").stock, 5);
});

test("carrito multiproducto fallido conserva el stock completo", () => {
  const store = newStore();
  store.addProduct("p2", 50, 1);
  assert.throws(
    () => store.checkout({ p1: 2, p2: 2 }, [], 0.13),
    /Stock insuficiente/,
  );
  assert.equal(store.inventory.get("p1").stock, 5);
  assert.equal(store.inventory.get("p2").stock, 1);
});

test("producto inexistente produce error y conserva el otro stock", () => {
  const store = newStore();
  assert.throws(
    () => store.checkout({ p1: 1, desconocido: 1 }, [], 0.13),
    /Stock insuficiente/,
  );
  assert.equal(store.inventory.get("p1").stock, 5);
});

test("venta multiproducto suma subtotales y reduce ambos stocks", () => {
  const store = newStore();
  store.addProduct("p2", 50, 3);
  assertAmount(store.checkout({ p1: 2, p2: 1 }, [], 0.1), 275);
  assert.equal(store.inventory.get("p1").stock, 3);
  assert.equal(store.inventory.get("p2").stock, 2);
});

test("impuesto cero conserva el subtotal", () => {
  const store = newStore();
  assertAmount(store.checkout({ p1: 1 }, [], 0), 100);
  assert.equal(store.inventory.get("p1").stock, 4);
});
