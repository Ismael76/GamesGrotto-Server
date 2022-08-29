from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.users import User
from ..models.games import Game
from flask_marshmallow import Marshmallow
import json

app = Flask(__name__)
ma = Marshmallow(app)

games_routes = Blueprint('games', __name__)

class GamesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "type", "title", "description", "username", "location")
games_schema = GamesSchema()
games_schema = GamesSchema(many=True)

@games_routes.route('/games', methods=["GET", "POST"])
def games():
    if request.method == "POST":
        body = request.get_json()
        type = body["type"]
        # price = body["price"]
        title = body["title"]
        description = body["description"]
        # image = body["image"]
        username = body["username"]
        location = body["location"]
        # marketstatus = body["marketstatus"]
        # tradestatus = body["tradestatus"]
        # date = body["date"]

        game = Game(type=type, title=title, description=description, username=username, location=location)

        db.session.add(game)
        db.session.commit()
        return body
    else:
        all_games = Game.query.all()
        return(json.dumps(games_schema.dump(all_games)))


