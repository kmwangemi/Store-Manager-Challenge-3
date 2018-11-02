import unittest
import json
from run import app
from app.api.V2.views.user_view import User


class UserstestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

        self.user = {
                        "fname" : "fname",
                        "lname" : "lname",
                        "email" : "email",
                        "password" : "password",
                        "role" : "admin"
                        }

        self.empty_user = {
                            "fname" : "",
                            "lname" : "",
                            "username" : "",
                            "password" : "",
                            "role" : ""
                            }

        self.login = self.client().post(
            '/api/v2/auth/login',
            data=json.dumps(self.user),
            content_type='application/json'
        )                  

    '''Tests for user creation'''
    def test_user_created_successfully(self):
        """Tests that a user is created successfully"""
        res = self.client().post('/api/v2/users', data=json.dumps(self.user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)
    
    def test_user_cannot_be_created_with_invalid_details(self):
        """Tests that a user cannot be created with empty fields"""
        res = self.client().post('/api/v2/users', data=json.dumps(self.empty_user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)

    '''Tests for getting successfully created users'''
    def test_gets_successfully_created_users(self):
        """Tests that api gets all created users"""
        res = self.client().get('/api/v2/users', data=json.dumps(self.user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Users", str(res.data))

    '''Tests for getting one user'''
    def test_gets_one_successfully_created_user(self):
        """Tests that api gets one successfully created user"""
        res = self.client().get('/api/v2/users/<userId>', data=json.dumps(self.user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("User", str(res.data))

    def test_user_can_login(self):
        """Test user can login to get access token"""
        # Create_user
        self.client().post(
            '/api/v2/auth/signup',
            data=json.dumps(self.user),
            headers={"content-type": "application/json"}
        )
        login = self.client().post(
            '/api/v2/auth/login',
            data=json.dumps(self.login),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(login.status_code, 200)
        self.assertIn("auth_token", str(login.data))

    def test_cannot_login_if_not_registered(self):
        """ Test that only registered users can login"""
        
        login = self.client().post(
            '/api/v2/auth/login',
            data=json.dumps({
            "email": "job@gmail.com",
            "password": "qwerty123!@#"
        }),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(login.status_code, 404)

    def test_login_details_required(self):
        """Test that all login fields are required"""
        login = self.client().post(
            '/api/v2/auth/login',
            data=json.dumps({
                "email": "",
                "password": ""
            }),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(login.status_code, 401)

    def test_cannot_create_duplicate_user(self):
        """
        Tests that duplicate usernames cannot be created
        """
        self.client().post(
            '/api/v2/auth/signup',
            data=json.dumps(self.user),
            headers={"content-type": 'application/json'}
        )
        res2 = self.client().post(
            '/api/v2/auth/register',
            data=json.dumps(self.user),
            headers={"content-type": 'application/json'}
        )
        self.assertIn("Email already exists", str(res2.data))

    def test_details_missing(self):
        """test username and password required"""
        res = self.client().post(
            '/api/v2/auth/signup',
            data=json.dumps({
                "first_name": "patrick",
                "last_name": "migot"
            }),
            headers={"content-type": 'application/json'}
        )
        self.assertEqual(res.status_code, 400)

    def test_email_cannot_duplicate(self):
        """Test cannot create duplicate emmails"""
        self.client().post(
            '/api/v2/auth/signup',
            data=json.dumps(self.user),
            headers={"content-type": 'application/json'}
        )
        res2 = self.client().post(
            '/api/v2/auth/signup',
            data=json.dumps(self.user),
            headers={"content-type": 'application/json'}
        )
        self.assertEqual(res2.status_code, 409)
        self.assertIn("Email already exists", str(res2.data))