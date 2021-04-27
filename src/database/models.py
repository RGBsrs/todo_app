import datetime
import uuid
from src import db



class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key = True)
    uuid = db.Column(db.String(36), unique = True)
    title = db.Column(db.String(120), nullable = False)
    completed = db.Column(db.Boolean, default = False, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    updated_at = db.Column(db.DateTime)  

    def __init__(self, title, completed = False, updated_at = datetime.datetime.now()):
        self.title = title
        self.completed = completed
        self.updated_at = updated_at
        self.uuid = str(uuid.uuid4())


    def __repr__(self):
        return f'Todo({self.title},{self.completed}, timestamp = {self.updated_at})' 

