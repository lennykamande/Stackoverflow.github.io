from random import *
from flask_restful import Resource, Api
from flask import request

"""
This module handles users, questions and answers. 
Implementation of multilevel inheritance as taught in OOP
"""

class App:
    users = {}

    def register_user(self, user):
        """
        This methods checks whether a user already exists, if not
        the user is added registered by adding them to the dictionary otherwise
        """
        if user.username in self.users.keys():
            return False
        else:
            self.users[user.username] = user
        return True

    def login_user(self, username, password):
        """
        This method logins in a user by first checking whether their passwords match. 
        Otherwise False is returned. 
        """
        if self.users[username].password == password:
            return True
        return False

    def does_user_exist(self, username):
        """
        This method check whether the user already exists within the
        user dictionary. 
        """
        if username in self.users.keys():
            return True
        return False

    def get_user(self, username):
        """
        Get an instance of the User from the user dictionary using the
        username
        """
        if username in self.users.keys():
            return self.users[username]
        return None

    def generate_random_key(self):
        """
        Generate a random id to act as an Id when asking a question
        """
        return randint(1, 10000)


class User:
    """
    User model class 
    """

    def __init__(self, username, password, name=None):
        self.username = username
        self.name = name
        self.password = password
        self.questions = {}

    def ask_question(self, questions):
        """
        Ask a questionS
        """
        if questions.id in self.questions.keys():
            return {'message': 'No user found'}, 400
        else:
            self.questions[questions.id] = questions
            return {"status": "success", "data": questions}, 200

    def get_questions(self):
        """
        get all questions
        """
        return {'status': 'success', 'data': self.questions}, 200

    def get_specific_question(self, questions_id):
        """
        Get a user's question by Id 
        """
        if questions_id in self.questions.keys():
            return {'status': 'success', 'data': self.questions[questions_id]}, 200
        return {'status': 'error', 'message': 'Question Id not found'}, 400


class Questions:
    """
    Questions class
    """

    def __init__(self, questions_id, title, description):
        self.id = questions_id
        self.title = title
        self.description = description
        self.answers = {}

    def write_answer(self, answer):
        """
        Write an answer to a question
        """
        if answer.id in self.answers.keys():
            return False
        else:
            self.answers[answer.id] = answer
            return True

    def get_all_answers(self, answer_id):
        if answer_id in self.answers.keys():
            return {"status": "success", "data": self.answers[answer_id]}, 200    
        return None


class Answers:
    """
    Answer class
    That contains an answer or answers to the questions
    """

    def __init__(self, answer_id, answer):
        self.id = answer_id
        self.answer = answer