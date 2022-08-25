from ..database.db import db

# create db model for a game template

class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    # additional tags for type of game and whether it is for sale or trade etc.
    # tag = db.Column(db.String(100), nullable=True)
