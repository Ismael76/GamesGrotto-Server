from ..database.db import db

# create db model for a game template

class Listing(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=True)
    username = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    marketstatus = db.Column(db.String(100), nullable=True)
    # tradestatus = db.Column(db.String(100), nullable=True)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, title, description, image, username, marketstatus, date):
        self.title = title
        self.description = description
        self.image = image
        self.username = username
        self.marketstatus = marketstatus
        self.date = date



    # additional tags for type of game and whether it is for sale or trade etc.
    # tag = db.Column(db.String(100), nullable=True)
