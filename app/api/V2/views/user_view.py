from flask import request, jsonify, Blueprint
from app.api.V2.models.user_model import User

user = Blueprint('user', __name__, url_prefix='/api/v2')
user_info = User('kelvin', 'mwangemi', 'kmwangemi', '12345', 'False')


#user routes

@user.route('/users', methods=['POST'])
def create_user():
    """Creates a new user"""
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please enter user'})
    new_user = user_info.add_users()
    return jsonify({'message' : 'User created', 'user' : new_user}), 201
   
@user.route('/users', methods=['GET'])
def get_all_users():
    """Gets all users"""
    response = user_info.get_all_users()
    return jsonify({'Users' : response}), 200

@user.route('/users/<userId>', methods=['GET'])
def get_one_user(userId):
    """Gets a single user"""
    response = user_info.get_one_user(userId)
    return jsonify({'User' : response}), 200
    





