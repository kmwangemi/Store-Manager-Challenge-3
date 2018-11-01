import unittest
import json
#from run import app
from app.api.V2.views.product_view import Product

class ProductstestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

        self.product = {
                        "product_name" : "product_name",
                        "category" : "category",
                        "quantity" : "quantity",
                        "price" : "price",
                        "description" : "description"
                        }

        self.empty_product = {
                                "product_name" : "",
                                "category" : "",
                                "quantity" : "",
                                "price" : "",
                                "description" : ""
                            }

    '''Tests for product creation'''
    def test_product_created_successfully(self):
        """Tests that a product is created successfully"""
        res = self.client().post('/api/v2/products', data=json.dumps(self.product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)
    
    def test_product_cannot_create_with_invalid_details(self):
        """Tests that a product cannot be created with empty fields"""
        res = self.client().post('/api/v2/products', data=json.dumps(self.empty_product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)

    '''Tests for getting successfully created products'''
    def test_gets_successfully_created_products(self):
        """Tests that api gets all created products"""
        res = self.client().get('/api/v2/products', data=json.dumps(self.product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)

    '''Tests for getting one product'''
    def test_gets_one_successfully_created_product(self):
        """Tests that api gets one successfully created product"""
        res = self.client().get('/api/v2/products/<productId>', data=json.dumps(self.product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)


   

    
  
    