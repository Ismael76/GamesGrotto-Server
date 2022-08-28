from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.users import User
from ..models.games import Game
import jwt
import os

games_routes = Blueprint('games', __name__)

@games_routes.route('/games', methods=["GET", "POST"])
def games():
    if request.method == "POST":
        body = request.get_json()
        type = body["type"]
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
    else:
        all_games = Game.query.all()
        return all_games


