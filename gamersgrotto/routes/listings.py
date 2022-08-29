from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.users import User
from ..models.listings import Listing
from flask_marshmallow import Marshmallow
import json
import datetime

app = Flask(__name__)
ma = Marshmallow(app)

listings_routes = Blueprint('listings', __name__)

class GamesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("type", "price", "title", "description", "image", "username", "location", "marketstatus", "date")
games_schema = GamesSchema()
games_schema = GamesSchema(many=True)

@listings_routes.route('/', methods=["GET", "POST"])
def listings():
    if request.method == "POST":
        body = request.get_json()
        type = body["type"]
        price = body["price"]
        title = body["title"]
        description = body["description"]
        image = body["image"]
        username = body["username"]
        location = body["location"]
        marketstatus = body["marketstatus"]
        date = datetime.datetime.now()

        game = Listing(type=type, price=price, title=title, description=description, image=image, username=username, location=location, marketstatus=marketstatus, date=date)

        db.session.add(game)
        db.session.commit()
        return body
    else:
        all_games = Listing.query.all()
        return(json.dumps(games_schema.dump(all_games)))
