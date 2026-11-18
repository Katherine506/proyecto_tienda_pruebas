import unittest
from store import Store

class TestStore(unittest.TestCase):
    def test_add_inventory(self):
        store = Store()
        store.add_product('p1', 100.0, 5)
        store.add_inventory('p1', 10)
        self.assertEqual(store.inventory['p1']['stock'], 15)

if __name__ == '__main__':
    unittest.main()