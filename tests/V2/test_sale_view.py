import unittest
import json
from run import app
from app.api.V2.views.sale_view import Sale

class SalestestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

        self.sale = {
                        "product" : "product",
                        "description" : "description",
                        "quantity" : "quantity",
                        "price" : "price",
                        "total" : "total"
                    }

        self.empty_sale = {
                            "product" : "",
                            "description" : "",
                            "quantity" : "",
                            "price" : "",
                            "total" : ""
                            }


    '''Tests for sale creation'''
    def test_sale_created_successfully(self):
        """Tests that a sale is created successfully"""
        res = self.client().post('/api/v2/sales', data=json.dumps(self.sale), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)
    
    def test_sale_cannot_create_with_no_details(self):
        """Tests that a sale cannot be created with no details"""
        res = self.client().post('/api/v2/sales', data=json.dumps(self.empty_sale), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)

    '''Tests for getting successfully created sales'''
    def test_gets_successfully_created_sales(self):
        """Tests that api gets all created sales"""
        res = self.client().get('/api/v2/sales', data=json.dumps(self.sale), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)    
    
    '''Tests for getting single sale'''
    def test_gets_single_successfully_created_sale(self):
        """Tests that api gets single successfully created sale"""
        res = self.client().get('/api/v2/sales/<saleId>', data=json.dumps(self.sale), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)

   
   
