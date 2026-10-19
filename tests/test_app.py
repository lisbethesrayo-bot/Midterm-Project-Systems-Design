import tempfile
import unittest
from pathlib import Path
from app import create_app

class CoffeeShopTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        db_path = str(Path(self.tmp.name) / "test.sqlite")
        self.app = create_app({"TESTING": True, "DATABASE": db_path, "SECRET_KEY": "test"})
        self.client = self.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def test_dashboard_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Good service starts here", response.data)

    def test_product_page_loads(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Americano", response.data)

    def test_create_walkin_order(self):
        response = self.client.post("/orders", data={
            "customer_id": "",
            "product_id": ["1", "2"],
            "quantity": ["2", "1"],
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Order #", response.data)
        self.assertIn(b"8.50", response.data)

    def test_empty_order_rejected(self):
        response = self.client.post("/orders", data={
            "customer_id": "", "product_id": [""], "quantity": ["1"]
        }, follow_redirects=True)
        self.assertIn(b"Select at least one product", response.data)

if __name__ == "__main__":
    unittest.main()
