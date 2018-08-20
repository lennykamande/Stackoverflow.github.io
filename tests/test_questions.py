import unittest
import os
import json
from app import questions, create_app


class test_question(unittest.TestCase):
    #This class represents the questions test case

    def setup(self):
        self.app = create_app()
        self.question = [
        
        {'user_id': 1,
        'topic': 'how to create a flask-api app', 
        'description':'I am having a problem creating a flask api app please help'
        },

        {'user_id': 2,
        'topic': 'testing a flask app', 
        'description':'Should i use pytest or just unittest for python?'
        }
        ]
    
    def test_get_all_questions(self):
          res = self.client.post('/bucketlists/',
                               data=json.dumps(self.bucketlist),
                               content_type='application/json',
                               headers={
                                   "Authorization": token['access_token']})
        self.assertEqual(res.status_code, 201)

        
    def test_get_all_questions_from_specific_user(self): ...
    def test_get_one_question(self): ...
    def test_question_doesnot_exist(self): ...
    def test_post_question(self): ...
    def test_update_question(self): ...
    def test_update_error_question(self): ...
    def test_delete_question(self): ...