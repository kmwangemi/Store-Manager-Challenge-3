from flask import request, jsonify, Blueprint
from app.api.V2.models.sale_model import Sale

sale = Blueprint('sale', __name__, url_prefix='/api/v2')
sale_info = Sale('product_name', 'description', 'quantity', 'stock_quantity', 'price', 'total')


#sales routes

@sale.route('/sales', methods=['POST'])
def create_sale():
    """Creates a sale record"""
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please enter sale'})
    new_sale = sale_info.add_sales()
    return jsonify({'message' : 'Sale created', 'sale' : new_sale}), 201
   
@sale.route('/sales', methods=['GET'])
def get_all_sales():
    """Gets all sales"""
    response = sale_info.get_all_sales()
    return jsonify({'Sales' : response}), 200

@sale.route('/sales/<saleId>', methods=['GET'])
def get_single_sale(saleId):
    """Gets a single sale"""
    response = sale_info.get_single_sale(saleId)
    return jsonify({'Sale' : response}), 200



