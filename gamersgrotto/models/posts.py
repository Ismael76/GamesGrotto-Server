
from ..database.db import db

# create db model for posts

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(400), nullable=False)
    # date = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.JSON, nullable=True)
    dislikes = db.Column(db.JSON, nullable=True)
    
    def __init__(self, title, text, username, likes, dislikes):
        self.title = title
        self.text = text
        self.username = username
        self.likes = likes
        self.dislikes = dislikes


