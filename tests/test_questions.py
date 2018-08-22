from unittest import TestCase
from app import create_app
import os
import json

class BaseTestCase(TestCase):

    def setUp(self):
        """Configure test enviroment."""
        os.environ['APP_SETTINGS'] = 'Testing'
        self.app = create_app("Testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()
        self.data = [{'title' : 'Flask question',
                        'description' : 'How can one deploy a flask app to heroku',
                        'quiz_id' : '1',
                        'user_id' : '22'},

                        {'title' : 'Heroku question',
                        'description' : 'How can one see end points on heroku',
                        'quiz_id' : '3',
                        'user_id' : '2'} ]

    def tearDown(self):
        self.app_context.pop()

class QuestionsTestCase(BaseTestCase):
    def test_get_all_questions(self):
        results = self.test_client.get('/api/v1/questions')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 200)
        self.assertEqual(results_payload['message'], 'Succesfully retrieved')

        
    def test_get_all_questions_from_specific_user(self):
        results = self.test_client.get('/api/v1/users/22')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 200)
        self.assertEqual(results_payload['message'], 'Succesfully retrieved')
    def test_get_one_question(self):
        results = self.test_client.get('/api/v1/questions/22')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 200)
        self.assertEqual(results_payload['message'], 'Succesfully retrieved')

    def test_question_doesnot_exist(self):
        results = self.test_client.get('/api/v1/questions/40')
        results_payload = json.loads(results.data)
        self.assertEqual(results.status_code, 200)
        self.assertEqual(results_payload['message'], 'Succesfully retrieved')
    def test_post_question(self): ...
    def test_update_question(self): ...
    def test_update_error_question(self): ...
    def test_delete_question(self): ...



