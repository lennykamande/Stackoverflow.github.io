from flask import jsonify, request, redirect
from app import app
from app.models import User
from app.models import Questions
from app.models import Answers



@app.route("/api/v1/login", methods=['GET', 'POST'])
def get_question():
    """
    This will show all questions a user has asked

    """
    data = User.get_questions()
    response = app.response_class(
        response=jsonify.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response



@app.route("/api/v1/question", methods=["GET"])
def get_question():
    """
    This will show all questions a user has asked

    """
    data = User.get_questions()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

