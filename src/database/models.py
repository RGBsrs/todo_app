import datetime
from src import db



class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    timestamp = db.Column(db.Date, default = datetime.datetime.now())  

    def __repr__(self):
        return f'Todo({self.title},{self.completed}, timestamp = {self.timestamp})' 

