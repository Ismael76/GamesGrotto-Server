from flask import Blueprint, request, jsonify, Flask, make_response, render_template
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.users import User
from ..models.listings import Listing
from flask_marshmallow import Marshmallow
import json
from flask_cors import CORS
import datetime
from ..mailers import mail_config
from flask_mail import Mail, Message


app = Flask(__name__)
ma = Marshmallow(app)


CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

mail = mail_config(app)

listings_routes = Blueprint('listings', __name__)


class GamesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "type", "price", "title", "description",
                  "image", "username", "location", "marketstatus", "date")


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

        game = Listing(type=type, price=price, title=title, description=description, image=image,
                       username=username, location=location, marketstatus=marketstatus, date=date)

        db.session.add(game)
        db.session.commit()
        return body
    else:
        all_games = Listing.query.all()
        return (json.dumps(games_schema.dump(all_games)))


@listings_routes.route('/<string:username>', methods=["POST", "GET"])
def getUserListings(username):
    if request.method == "POST":
        usersListing = Listing.query.filter_by(username=username).all()
        return (json.dumps(games_schema.dump(usersListing)))


@listings_routes.route('/<int:post_id>', methods=["DELETE"])
def deleteUserListing(post_id):
    if request.method == "DELETE":
        body = request.get_json()
        username = body["username"]
        deletedListing = Listing.query.filter_by(id=post_id).delete()
        updatedUserListings = Listing.query.filter_by(username=username).all()
        db.session.commit()
        return (json.dumps(games_schema.dump(updatedUserListings)))


@listings_routes.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        body = request.get_json()
        seller_username = body["seller_username"]
        listing_title = body["listing_title"]
        name = body["name"]
        mobile_number = body["mobile_number"]
        message = body["message"]
        sender_username = body["sender_username"]

        seller_user = User.query.filter_by(username=seller_username).first()
        seller_email = seller_user.email

        sender_user = User.query.filter_by(username=sender_username).first()
        sender_email = sender_user.email

        print(message)
        print(seller_email)
        msg = Message("NEW MESSAGE! @ GamesGrotto",
                      sender="games.grotto.uk@gmail.com", recipients=[seller_email])
        print(msg)
        u'\u2013'.encode('utf-8')
        msg.html = render_template(
            'mail.html', username=seller_username, listing_title=listing_title, name=name, mobile_number=mobile_number, message=message, sender_email=sender_email)
        mail.send(msg)
        return {"sent": True}
