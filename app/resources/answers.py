from flask_restful import Resource
from flask import request
from random import *
from app.resources import questions


answers = []
class Answer(Resource):
   
    

    def __init__(self ):
        
        self.itemsdict = {}
    """ 
    a method to add items belonging to a specific question
    """
    def get(self):
        pass

    """ 
    a method to show items belonging to a specific question
    """
    def delete(self):
        pass
       

    """ 
    a method to delete a particular question
    """
    def post(self):
        pass
        