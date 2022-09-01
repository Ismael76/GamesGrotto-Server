from ..database.db import db

# create db model for comments

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400), nullable=False)
    # date = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.JSON, nullable=True)
    dislikes = db.Column(db.JSON, nullable=True)

    def __init__(self, text, username, post_id, likes, dislikes):
        self.text = text
        self.username = username
        self.post_id = post_id
        self.likes = likes
        self.dislikes = dislikes

