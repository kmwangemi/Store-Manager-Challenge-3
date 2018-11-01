from flask import request, jsonify, Blueprint
from app.api.V2.models.sale_model import Sale

sale2 = Sale()

sale = Blueprint('sale', __name__, url_prefix='/api/v2')

#sales routes

@sale.route('/sales', methods=['POST'])
def create_sale():
    """Creates a sale record"""
    response = sale2.create_sale()
    return response
   
@sale.route('/sales', methods=['GET'])
def get_all_sales():
    """Gets all sales"""
    response = sale2.get_all_sales()
    return jsonify({'Sales' : response}), 200

@sale.route('/sales/<saleId>', methods=['GET'])
def get_single_sale(saleId):
    """Gets a single sale"""
    response = sale2.get_single_sale(saleId)
    return jsonify({'Sale' : response}), 200



