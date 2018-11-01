from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
import datetime
import jwt
import re

from app.api.V2.models.user_model import User
SECRET_KEY = os.getenv('SECRET_KEY')

user2 = User()

user = Blueprint('user', __name__, url_prefix='/api/v2')

#user routes
'''
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing, login to get token'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY)
            current_user = user2.get_one_user[email]
            if not current_user:
                return jsonify({"message": "You are not logged in"}), 401   
        except:
            return jsonify({'message': 'Token is invalid or Expired!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated
'''

@user.route('/register', methods=['POST'])
def create_user():
    """Creates a new user"""
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    if not data:
        return jsonify({'message' : 'Please insert data'})
    if not data or not data['fname'] or not data['lname'] or not data['email'] or not hashed_password:
        return jsonify({'message': "email or password missing"}), 400

    if not re.match(r'\A[0-9a-zA-Z!@#$%&*]{6,20}\Z', data['password']):
        return jsonify({"Message": "Password must be 6-20 Characters"}), 406    
    user_info = User(data['fname'], data['lname'], data['email'], hashed_password, data['role'])
    user_info.add_users()
    return jsonify({'message' : 'User created'}), 201
   
@user.route('/users', methods=['GET'])
def get_all_users():
    """Gets all users"""
    response = user2.get_all_users()
    return jsonify({'Users' : response}), 200

@user.route('/users/<userId>', methods=['GET'])
def get_one_user(userId):
    """Gets a single user"""
    response = user2.get_one_user(userId)
    return jsonify({'User' : response}), 200



@user.route('/login', methods=['POST'])
def login():
    """users will login to the app via this route"""
    auth = request.authorization
    if not auth or not auth['email'] or not auth['password']:
        return jsonify({'message' : 'Could not verify'}), 401 

    user = get_one_user(auth['email'])
    if not user:
        return jsonify({'message' : 'Could not verify'}), 401
    
    if check_password_hash(user['password'], auth['password']):
        token = jwt.encode({'id' : user[id], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=240)}, SECRET_KEY)
            
        return jsonify({"token": token.decode('UTF-8')})

    return jsonify({'message' : 'Could not verify'}), 401

