import unittest
import requests

class TestProductAPI(unittest.TestCase):

    def test_insert_product_valid(self):
        # Testa a inserção de um produto válido
        data = {
            "name": "Produto de Teste",
            "description": "Descrição do Produto de Teste",
            "value": 10.99,
            "quantity": 100,
            "category": "Teste"
        }
        response = requests.post('http://localhost:5000/api/insert/products', json=data)
        self.assertEqual(response.status_code, 200)
        product = response.json()
        self.assertIsInstance(product, dict)
        self.assertIn("name", product)
        self.assertIn("description", product)
        self.assertIn("value", product)
        self.assertIn("quantity", product)
        self.assertIn("category", product)

    def test_insert_product_invalid_name(self):
        # Testa a inserção de um produto com nome inválido
        data = {
            "name": "12345",  # Nome inválido, contém números
            "description": "Descrição do Produto de Teste",
            "value": 10.99,
            "quantity": 100,
            "category": "Teste"
        }
        response = requests.post('http://localhost:5000/api/insert/products', json=data)
        self.assertEqual(response.status_code, 400)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn("error", error)

    def test_insert_product_invalid_category(self):
        # Testa a inserção de um produto com categoria inválida
        data = {
            "name": "Produto de Teste",
            "description": "Descrição do Produto de Teste",
            "value": 10.99,
            "quantity": 100,
            "category": "Categoria#Teste"  # Categoria inválida, contém caracteres especiais
        }
        response = requests.post('http://localhost:5000/api/insert/products', json=data)
        self.assertEqual(response.status_code, 400)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn("error", error)

    def test_insert_product_invalid_description(self):
        # Testa a inserção de um produto com descrição inválida
        data = {
            "name": "Produto de Teste",
            "description": "",  # Descrição vazia, inválida
            "value": 10.99,
            "quantity": 100,
            "category": "Teste"
        }
        response = requests.post('http://localhost:5000/api/insert/products', json=data)
        self.assertEqual(response.status_code, 400)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn("error", error)

    def test_insert_product_invalid_value(self):
        # Testa a inserção de um produto com valor inválido
        data = {
            "name": "Produto de Teste",
            "description": "Descrição do Produto de Teste",
            "value": "ValorInválido",  # Valor inválido, não é um float
            "quantity": 100,
            "category": "Teste"
        }
        response = requests.post('http://localhost:5000/api/insert/products', json=data)
        self.assertEqual(response.status_code, 400)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn("error", error)

    def test_insert_product_invalid_quantity(self):
        # Testa a inserção de um produto com quantidade inválida
        data = {
            "name": "Produto de Teste",
            "description": "Descrição do Produto de Teste",
            "value": 10.99,
            "quantity": "QuantidadeInválida",  # Quantidade inválida, não é um inteiro
            "category": "Teste"
        }
        response = requests.post('http://localhost:5000/api/insert/products', json=data)
        self.assertEqual(response.status_code, 400)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn("error", error)

if __name__ == '__main__':
    unittest.main()
