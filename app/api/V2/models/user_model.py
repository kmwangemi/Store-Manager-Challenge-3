from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, make_response
import psycopg2
import datetime
import jwt
import os
import re
from psycopg2.extras import RealDictCursor
from db_con import db_url
conn = psycopg2.connect(db_url)
cur = conn.cursor(cursor_factory=RealDictCursor)

SECRET_KEY = os.getenv('SECRET_KEY')

'''Sale model'''

users = []

class User(object):
    """user model to store all users data"""

    def __init__(self, fname="str", lname="str", email="str", password="str", role="str"):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.role = role
        
    def get_all_users(self):
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        return rows

    def get_one_user(self, userId):
        query = "SELECT * FROM users WHERE id ='{0}'".format(userId)
        cur.execute(query)
        row = cur.fetchall()
        return row

    def login(self):
        """A user can login and get a token"""
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        if not data or not email or not password:
            return make_response(jsonify({"Message": "Please enter credentials"}))
     
        cur.execute("SELECT * FROM users WHERE email= '{}'".format(data["email"]))
        if cur.fetchone():
            cur.execute("SELECT password FROM users WHERE email= '{}'".format(data["email"]))
            for row in cur.fetchall():
                if check_password_hash(row["password"], data["password"]):
                    """generate token"""
                    cur.execute("SELECT role FROM users WHERE email= '{}'".format(data["email"]))
                    for row in cur.fetchall():
                        token = jwt.encode({"username": row["password"], 'exp': datetime.datetime.utcnow()
                                                                       + datetime.timedelta(minutes=100)},
                                           SECRET_KEY)
                        return make_response(jsonify({"Token": token.decode('UTF-8')}))
        return make_response(jsonify({"Message": "Invalid credentials"})) 

    def signup(self):
        data = request.get_json()
        if not data["fname"] or not data["password"] or not data["lname"] or not data["email"]:
            return make_response(jsonify({"message": "Enter missing credentials"}))

        if not re.match(r'\A[0-9a-zA-Z!@#$%&*]{6,20}\Z', data['password']):
            return make_response(jsonify({"Message": "Password must be 6-20 Characters"}), 406)

        password = generate_password_hash(data["password"], method="sha256")
    
        cur.execute("SELECT * FROM users WHERE email= '{}'".format(data["email"]))
        if cur.fetchone():
            return make_response(jsonify({"Message": "Email exists"}))

        query = """INSERT INTO users (fname, lname, email, password, role) VALUES
                        (%s,%s, %s,%s,%s)"""
        cur.execute(query, (data["fname"], data["lname"], data["email"], False, password))
        conn.commit()
        return make_response(jsonify({"Message": "User successfully added"}), 201)






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