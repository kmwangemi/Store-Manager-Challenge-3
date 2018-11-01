import psycopg2
from psycopg2.extras import RealDictCursor
from db_con import db_url

'''Sale model'''

users = []

class User(object):
    """user model to store all users data"""

    def __init__(self, fname="kelvin", lname="mwangemi", email="mwangemik@gmail.com", password="123", role="admin"):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.role = role
        
    def add_users(self):
        """Adds a new user to the users database"""
        query = """
                INSERT INTO users(fname, lname, email, password, role)
                VALUES(%s, %s, %s, %s, %s) 
                """
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query,(
            self.fname,
            self.lname,
            self.email,
            self.password,
            self.role
        ))
        conn.commit()
        
    def get_all_users(self):
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        return rows

    def get_one_user(self, userId):
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM users WHERE id ='{0}'".format(userId)
        cur.execute(query)
        row = cur.fetchall()
        return row