import psycopg2
from psycopg2.extras import RealDictCursor
from db_con import db_url

'''Product model'''
products = []

class Product(object):
    """product model to store all products data"""

    def __init__(self, product_name="maize", category="cereals", quantity=0, price=0, description="small"):
        self.product_name = product_name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.description = description

    def add_products(self):
        '''add products into database'''
        query = """
                INSERT INTO products(product_name, category, quantity, price, description)
                VALUES(%s, %s, %s, %s, %s) 
                """
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query,(
            self.product_name,
            self.category,
            self.quantity,
            self.price,
            self.description
        ))
        conn.commit()

    def get_all_products(self):
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        return rows

    def get_one_product(self, product_id):
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM products WHERE id ='{0}'".format(product_id)
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