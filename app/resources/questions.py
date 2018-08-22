from flask_restful import Resource
from flask import request
from random import *

questionslist = list()		
class Questionlist(Resource):
   
    

    def __init__(self ):
        
        self.listsdict = {
        }

    def post(self):
        """ 
        a method to add a new question with the unique user
        
        """
        quiz_id = randint(1, 1000)
        self.listsdict = {'title' : request.json['title'],
                        'description' : request.json['description'],  
                        'user_id' : request.json['user_id'],
                        'quiz_id' : quiz_id}
        questionslist.append(dict(self.listsdict))
        return questionslist, 201

    def get(self):
        """ 
        a method to show the question list
        """
        
        return questionslist, 200

    

class Question(Resource):

    def get(self, quiz_id):
        """
        Method to get a specific question
        """
        pass

    def delete(self, quiz_id):
        """
        A method to delete a question from the list
        """
        pass

    def put(self, quiz_id):
        pass



