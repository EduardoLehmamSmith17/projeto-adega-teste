import unittest
from app import ProductManager

class TestProductManager(unittest.TestCase):
    def setUp(self):
        self.product_manager = ProductManager()

    def test_create_product(self):
        product = self.product_manager.create_product('Product 1', 'Category A', 10.99, 50)
        self.assertEqual(product.name, 'Product 1')

    def test_get_product(self):
        product = self.product_manager.create_product('Product 1', 'Category A', 10.99, 50)
        retrieved_product = self.product_manager.get_product(product.id)
        self.assertEqual(retrieved_product, product)

    def test_update_product(self):
        product = self.product_manager.create_product('Product 1', 'Category A', 10.99, 50)
        updated_product = self.product_manager.update_product(product.id, 'Updated Product', 'Category B', 15.99, 30)
        self.assertEqual(updated_product.name, 'Updated Product')

    def test_delete_product(self):
        product = self.product_manager.create_product('Product 1', 'Category A', 10.99, 50)
        deleted = self.product_manager.delete_product(product.id)
        self.assertTrue(deleted)
        deleted_product = self.product_manager.get_product(product.id)
        self.assertIsNone(deleted_product)

if __name__ == '__main__':
    unittest.main()
