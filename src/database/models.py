import datetime
from src import db
from werkzeug.security import generate_password_hash



class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    completed = db.Column(db.Boolean, default = False, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    updated_at = db.Column(db.DateTime)  

    def __init__(self, title, completed = False, updated_at = datetime.datetime.now()):
        self.title = title
        self.completed = completed
        self.updated_at = updated_at


    def __repr__(self):
        return f'Todo({self.title},{self.completed}, timestamp = {self.updated_at})' 


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    remember_token = db.Column(db.Boolean, default = False, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'User: {self.name}, {self.email}'

