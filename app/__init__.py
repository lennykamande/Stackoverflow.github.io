from flask import Flask
from flask_restful import Api
from app.resources.questions import Questionlist
from app.resources.questions import Question
from app.resources.answers import Answer


def create_app(env="dev"):

    # Initialize the application
    app = Flask(__name__)
    api = Api(app)

    # Load the resources 
    api.add_resource(Questionlist,'/api/v1/questions')

    return app








