
"""Pruebas unitarias del motor de tienda; cada caso usa un Store nuevo."""
import unittest
from store import Store


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.store.add_product('p1', 100.0, 5)

    # Grupo 1: gestión de inventario
    def test_registrar_producto_con_stock_inicial(self):
        self.store.add_product('p2', 25.0, 8)
        self.assertEqual(self.store.inventory['p2'], {'price': 25.0, 'stock': 8})

    def test_incrementar_inventario_existente(self):
        self.store.add_inventory('p1', 10)
        self.assertEqual(self.store.inventory['p1']['stock'], 15)

    # Grupo 2: validaciones y atomicidad de la venta
    def test_stock_insuficiente_lanza_excepcion_y_no_descuenta(self):
        with self.assertRaisesRegex(ValueError, 'Stock insuficiente'):
            self.store.checkout({'p1': 6}, [], 0.13)
        self.assertEqual(self.store.inventory['p1']['stock'], 5)

    def test_dos_codigos_lanzan_excepcion_y_no_descuentan_stock(self):
        self.store.add_discount('DIEZ', 0.10)
        self.store.add_discount('CINCO', 0.05)
        with self.assertRaisesRegex(ValueError, 'Solo un código permitido'):
            self.store.checkout({'p1': 1}, ['DIEZ', 'CINCO'], 0.13)
        self.assertEqual(self.store.inventory['p1']['stock'], 5)

    # Grupo 3: cálculos financieros y actualización del inventario
    def test_venta_sin_descuento_calcula_subtotal_impuesto_y_stock(self):
        total = self.store.checkout({'p1': 2}, [], 0.13)
        self.assertAlmostEqual(total, 226.0, places=7)
        self.assertEqual(self.store.inventory['p1']['stock'], 3)

    def test_venta_con_descuento_aplica_primero_descuento_luego_impuesto(self):
        self.store.add_discount('DIEZ', 0.10)
        total = self.store.checkout({'p1': 2}, ['DIEZ'], 0.13)
        self.assertAlmostEqual(total, 203.4, places=7)
        self.assertEqual(self.store.inventory['p1']['stock'], 3)

    # Casos adicionales
    def test_stock_igual_a_cantidad_permite_venta(self):
        total = self.store.checkout({'p1': 5}, [], 0.0)
        self.assertAlmostEqual(total, 500.0)
        self.assertEqual(self.store.inventory['p1']['stock'], 0)

    def test_tres_codigos_lanzan_excepcion_y_conservan_stock(self):
        for code in ('A', 'B', 'C'):
            self.store.add_discount(code, 0.05)
        with self.assertRaisesRegex(ValueError, 'Solo un código permitido'):
            self.store.checkout({'p1': 1}, ['A', 'B', 'C'], 0.13)
        self.assertEqual(self.store.inventory['p1']['stock'], 5)

    def test_carrito_multiproducto_fallido_no_modifica_ningun_stock(self):
        self.store.add_product('p2', 50.0, 1)
        with self.assertRaisesRegex(ValueError, 'Stock insuficiente'):
            self.store.checkout({'p1': 2, 'p2': 2}, [], 0.13)
        self.assertEqual(self.store.inventory['p1']['stock'], 5)
        self.assertEqual(self.store.inventory['p2']['stock'], 1)

    def test_producto_inexistente_lanza_excepcion_sin_descontar(self):
        with self.assertRaisesRegex(ValueError, 'Stock insuficiente'):
            self.store.checkout({'p1': 1, 'desconocido': 1}, [], 0.13)
        self.assertEqual(self.store.inventory['p1']['stock'], 5)

    def test_carrito_con_dos_productos_calcula_total_y_ambos_stocks(self):
        self.store.add_product('p2', 50.0, 3)
        total = self.store.checkout({'p1': 2, 'p2': 1}, [], 0.10)
        self.assertAlmostEqual(total, 275.0)
        self.assertEqual(self.store.inventory['p1']['stock'], 3)
        self.assertEqual(self.store.inventory['p2']['stock'], 2)

    def test_impuesto_cero_no_modifica_subtotal(self):
        total = self.store.checkout({'p1': 1}, [], 0.0)
        self.assertAlmostEqual(total, 100.0)
        self.assertEqual(self.store.inventory['p1']['stock'], 4)


if __name__ == '__main__':
    unittest.main()
