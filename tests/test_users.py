from flask import request, jsonify
import json
import unittest

from app import users, create_app


class test_question(unittest.TestCase):
    #This class represents the users test case

    def setUp(self):
        #Test cases
        # user setup
        self.test = True
        self.app = create_app()
        self.client = self.test_client()
        self.user = {
            'id': 1,
            'username': 'lennykamande',
            'email': 'lenny@andela.com',
            'password': '1234Ahuu!'
        }
        
    
    def test_get_all_users(self): ...

    def test_get_specific_user(self): ...
    def test_user_doesnot_exist(self): ...
    def test_user_can_register(self):
    
        #Test new user can be registered to the system.
        
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(self.user),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User successfully created", response_msg["Message"])