from ..database.db import db

# create db model for comments

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400), nullable=False)
    # date = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=True)
    dislikes = db.Column(db.Integer, nullable=True)


