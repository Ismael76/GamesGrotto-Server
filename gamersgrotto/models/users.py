from ..database.db import db

# create db model for user auth

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    # full_name = db.Column(db.String(100), nullable=True)
