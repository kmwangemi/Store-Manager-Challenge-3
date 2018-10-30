from flask import request, jsonify, Blueprint
from app.api.V2.models.product_model import Product

product = Blueprint('product', __name__, url_prefix='/api/v2')

#products routes
@product.route('/products',methods=['POST'])
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please insert data'})
    product_info = Product(data['product_name'], data['category'], data['quantity'], data['price'], data['description'])
    product_info.add_products()
    return jsonify({'message' : 'Product created'}), 201
  
@product.route('/products',methods=['GET'])
def get_all_products():
    """Gets all products"""
    product = Product()
    response = product.get_all_products()
    return jsonify({'Products' : response}), 200

@product.route('/products/<product_id>', methods=['GET']) 
def get_one_product(product_id):
    """Gets one product"""
    product = Product()
    response = product.get_one_product(product_id)
    return jsonify({'Product' : response}), 200