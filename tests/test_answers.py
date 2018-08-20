import unittest
import os
import json
from app import answers


class test_question(unittest.TestCase):
    #This class represents the answers test case

    def setup(self):
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
    
    def test_get_all_questions_answers(self): ...
    def test_question_answer_doesnt_exsist(self): ...
    def test_post_question_answer(self): ...
    def test_update_question_answer(self): ...
    def test_update_error_question_answer(self): ...
    def test_delete_question_answer(self): ...
    def test_get_all_answers_from_user(self): ...