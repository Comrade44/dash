from flask import Flask, render_template, request
from dummy_data import dummy_data

flask_app = Flask(__name__)

# @flask_app.route('/')
# def index():
#     return render_template('index.html')

@flask_app.route('/')
def notes():
    return render_template('notes.html', notes=dummy_data)

@flask_app.route('/update_notes', methods=["POST"])
def update_notes():
    print(request.form)
    return render_template('update_notes.html')

print(dummy_data)