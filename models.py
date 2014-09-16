from flask import Flask
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))    
    def __init__(self, username, password, name=None, email=None):
        self.username = username
        self.password = password
        if name is not None:
            self.name = name

        if email is not None:
            self.email = email

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username
