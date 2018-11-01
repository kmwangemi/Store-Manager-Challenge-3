from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, Blueprint, make_response
import re
from psycopg2.extras import RealDictCursor
from db_con import db_url
import psycopg2
conn = psycopg2.connect(db_url)
cur = conn.cursor(cursor_factory=RealDictCursor)
from app.api.V2.models.user_model import User

user2 = User()

user = Blueprint('user', __name__, url_prefix='/api/v2')
auth = Blueprint('auth', __name__, url_prefix='/api/v2/auth')

#user routes

@auth.route('/signup', methods=['POST'])
def signup():
    response = user2.signup()
    return response
        
@auth.route('/login', methods=['POST'])
def login():
    """users will login to the app via this route"""
    response = user2.login()
    return response    
   
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

