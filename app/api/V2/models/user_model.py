'''Sale model'''

users = []

class User(object):
    """user model to store all users data"""

    def __init__(self, fname, lname, username, password, role):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.role = role
        
    def add_users(self):
        """Adds a new user to the users list"""
        new_user = {}
        new_user['userId'] = str(len(users)+1)
        new_user['fname'] = self.fname
        new_user['lname'] = self.lname
        new_user['username'] = self.username
        new_user['password'] = self.password
        new_user['role'] = self.role
        users.append(new_user)
        return new_user
        
    def get_all_users(self):
        return users

    def get_one_user(self, userId):
        one_user = [one_user for one_user in users if one_user['userId'] == userId] #list comprehension
        if len(one_user) == 0:
            return {"message": "User not found"}
        return one_user[0]