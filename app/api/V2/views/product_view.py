from flask import request, jsonify, Blueprint
from app.api.V2.models.product_model import Product

product2 = Product()

product = Blueprint('product', __name__, url_prefix='/api/v2')


#products routes
@product.route('/products', methods=['POST'])
def create_product():
    """Creates a product record"""
    data = request.get_json()
    product2 = Product(data['product_name'], data['category'], data['quantity'], data['price'], data['description'])
    response = product2.add_products()
    if response:
        return jsonify({'message' : 'Product already exists'}), 201
    else:
            return jsonify({'message' : 'Product created successfully'})


@product.route('/products',methods=['GET'])
def get_all_products():
    """Gets all products"""
    response = product2.get_all_products()
    return jsonify({'Products' : response}), 200

@product.route('/products/<productId>', methods=['GET']) 
def get_one_product(productId):
    """Gets one product"""
    response = product2.get_one_product(productId)
    return jsonify({'Product' : response}), 200

@product.route('/products/<productId>', methods=['PUT']) 
def update_product(productId):
    """Updates product"""
    response = product2.update_product(productId)
    return response

@product.route('/products/<productId>', methods=['DELETE']) 
def delete_product(productId):
    """Deletes product"""
    response = product2.delete_product(productId)
    return response    