from flask import Blueprint, request, jsonify, Flask, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.users import User
import jwt
import os


auth_routes = Blueprint('auth', __name__)
app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# generates token for user so they can access restricted routes. TODO: Will also need similar system in main.py

def token_required(func):
    """
    Decorator for verifying access token.
    """

    @wraps(func)
    def decorated():
        token = None

        if "Authorization" in request.headers:
            auth = request.headers["Authorization"]
            token = str.replace(str(auth), "Bearer ", "") # remove 'Bearer' in token

        if not token:
            return jsonify({"message": "Token is missing."}), 401 # unauthorized

        try:
            user_data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"]) # get decoded user data
            current_user = User.query.filter_by(username=user_data["username"]).first()
        except:
            return jsonify({"message": "Invalid token."}), 401 # unauthorized

        return func(current_user)

    return decorated



@auth_routes.route('/login', methods=["POST"])
def login():
    """
    Receives a username and password in the request body and generates a token
    that can be used to verify a user"s identity.
    """

    body = request.get_json()
    username = body["username"]
    password = body["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        return make_response("No such user.", 401) # unauthorized

    if check_password_hash(user.password, password):

        # generate token with encoded user data

        token = jwt.encode({
            "username": user.username,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }, app.config["SECRET_KEY"], algorithm="HS256")

        return make_response(jsonify({"token": token}), 201) # resource created

    return make_response("Incorrect password.", 403) # forbidden

@auth_routes.route("/register", methods=["POST"])
def register():

    # Should receive a username and password in the request body and generate a token that can be used to verify a user's identity.


    body = request.get_json()
    username = body["username"]
    password = body["password"]

    # checks for existing user with the same username
    user = User.query.filter_by(username=username).first()

    # stores user securely in the database
    if not user:
        password = generate_password_hash(password)
        user = User(username = username, password=password)

        db.session.add(user)
        db.session.commit()

        return make_response("Successfully registered.", 201) # resource created
    else:
        return make_response("User already exists.", 409) # conflict


@auth_routes.route("/user", methods=["GET", "PATCH"])
@token_required
def update_and_get_user(current_user):
    user = User.query.filter_by(username=current_user.username).first()

    # Used to edit a users security info
    if not user:
        return make_response("User not found.", 202) # accepted

    if request.method == "PATCH":
        body = request.get_json()
        for key, value in body.items():
            if key != "username" and key != "password":
                setattr(user, key, value)

        db.session.commit()

    return make_response(jsonify({
        "username": user.username,
        "full_name": user.full_name,
        "email": user.email
    }), 200)

if __name__ == "__main__":
    app.run(debug = True)
