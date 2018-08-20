from flask import jsonify, request, redirect
from app import app
from app.models import User
from app.models import Questions
from app.models import Answers



@app.route("/api/v1/question", methods=["GET"])
def get_question():
    """
    This will show all questions a user has asked

    """
    data = User.get_questions()
    return jsonify({'data' : data})
