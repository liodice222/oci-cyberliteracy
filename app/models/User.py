from flask_login import UserMixin
from app.db import db

#set up user model to be stored in user database  
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)


