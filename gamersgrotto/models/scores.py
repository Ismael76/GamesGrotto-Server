from ..database.db import db
# create db model for posts
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    # date = db.Column(db.String(100), nullable=False)
