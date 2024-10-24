from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
import requirements.txt
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Carregar arquivo JSON
with open('questions.json', 'r') as f:
    questions_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question/<int:id>')
def question(id):
    question = next((q for q in questions_data['questions'] if q['id'] == id), None)
    if 'result' in question:
        return render_template('result.html', result=question['result'])
    return render_template('question.html', question=question)

if __name__ == '__main__':
    app.run(debug=True)
