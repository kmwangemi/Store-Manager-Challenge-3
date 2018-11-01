import psycopg2
from flask import request, make_response, jsonify
from psycopg2.extras import RealDictCursor
from db_con import db_url

conn = psycopg2.connect(db_url)
cur = conn.cursor(cursor_factory=RealDictCursor)

'''Product model'''
products = []

class Product(object):
    """product model to store all products data"""

    def __init__(self, product_name='maize', category='cereal', quantity=10, price='110', description='large'):
        self.product_name = product_name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.description = description

    def add_products(self):
        '''add products into database'''
        data = request.get_json()
        query1 = "SELECT * FROM products WHERE product_name = '{}'".format(data["product_name"])
        cur.execute(query1)
        rows = cur.fetchall()
        if len(rows) != 0:
            return jsonify({'message' : 'Product already exists'})                                                                                                                                                                                  
        else:   
        
            query = """
                    INSERT INTO products(product_name, category, quantity, price, description)
                    VALUES(%s, %s, %s, %s, %s) 
                    """
            cur.execute(query,(
                self.product_name,
                self.category,
                self.quantity,
                self.price,
                self.description
            ))
            conn.commit()

            
    def get_all_products(self):
        """Gets a sale record"""
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        return rows

    def get_one_product(self, productId):
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM products WHERE id ='{}'".format(productId)
        cur.execute(query)
        row = cur.fetchall()
        return row

    def update_product(self, productId):
        conn = psycopg2.connect(self)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("UPDATE products SET product_name=%s, category=%s, quantity=%s, price=%s, description=%s WHERE productId = %s",
        (
            self.product_name,
            self.category,
            self.quantity,
            self.price,
            self.description
            ))
        conn.commit()

    def delete_product(self, productId):
        conn = psycopg2.connect(self)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("DELETE FROM products WHERE productId=%s",(
                productId
            ))
        conn.commit()