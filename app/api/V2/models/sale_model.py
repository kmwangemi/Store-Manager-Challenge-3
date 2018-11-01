import psycopg2
from flask import request, make_response, jsonify
from psycopg2.extras import RealDictCursor
from db_con import db_url

conn = psycopg2.connect(db_url)
cur = conn.cursor(cursor_factory=RealDictCursor)

'''Sale model'''

sales = []

class Sale(object):
    """sale model to store all sales data"""

    def __init__(self, product_name="beans", quantity=2, price=150, total=300):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.total = total
        
    def create_sale(self):
        """Adds a new sale to the sales list"""
        data = request.get_json()
        query1 = "SELECT * FROM products WHERE product_name = '{}'".format(data["product_name"])
        cur.execute(query1)
        rows = cur.fetchone()
        if not rows:
            return jsonify({'message' : 'Sorry product unavailable'})
       
        productId = rows['id']
        product_name = rows['product_name']
        quantity = rows["quantity"]
        category = rows["category"]
        price = rows["price"]
        description = rows["description"]

        if int(data["quantity"]) > int(quantity):
            return jsonify({'message' : 'Less product available'})

        new_quantity = int(quantity) - int(data["quantity"])
        query2 = """ UPDATE products SET quantity = %s WHERE id = %s"""
        cur.execute(query2, (new_quantity, productId))
        conn.commit()
    
        total = price * int(data["quantity"])
        query3 = """INSERT INTO sales (product_name, quantity, price, total) VALUES (
                %s,%s,%s,%s)"""
        cur.execute(query3, (product_name, quantity, price, total))
        conn.commit()
        return jsonify({'message' : 'Sale created successfully'}), 201
          
    def get_all_sales(self):
        cur.execute("SELECT * FROM sales")
        rows = cur.fetchall()
        return rows

    def get_single_sale(self, saleId):
        query = "SELECT * FROM sales WHERE id ='{}'".format(saleId)
        cur.execute(query)
        row = cur.fetchall()
        return row
