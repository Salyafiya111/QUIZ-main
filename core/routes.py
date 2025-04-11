from flask import flask 
from . import create_app

app = flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz/<int:quiz_id>')
def quiz(quiz_id):
    return render_template('quiz.html', quiz_id=quiz_id) 