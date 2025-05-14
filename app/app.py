from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

db = SQLAlchemy(flask_app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    complete = db.Column(db.Boolean)

with flask_app.app_context():
    db.create_all()
    new_todo1 = Todo(content="Todo item 1", complete=False)
    new_todo2 = Todo(content="Todo item 2", complete=True)
    new_todo3 = Todo(content="Todo item 3", complete=True)
    new_todo4 = Todo(content="Todo item 4", complete=False)
    db.session.add(new_todo1)
    db.session.add(new_todo2)
    db.session.add(new_todo3)
    db.session.add(new_todo4)
    db.session.commit()

@flask_app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('index.html', todo_list=todo_list)

@flask_app.route('/add', methods=["POST"])
def add():
    content = request.form.get("content")
    new_todo = Todo(content=content, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@flask_app.route("/update", methods=["POST"])
def update():
    todo = Todo.query.filter_by(id=request.form.get("update")).first()
    todo.content  = request.form.get("content")
    if request.form.get("complete") == "on":
        todo.complete = True
    else:
        todo.complete = False
    db.session.commit()
    return redirect(url_for("index"))

@flask_app.route("/delete", methods=["POST"])
def delete():
    todo = (Todo.query.filter_by(id=request.form.get("delete")).first())
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
