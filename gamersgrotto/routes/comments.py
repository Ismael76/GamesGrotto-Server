from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.comments import Comment
from flask_marshmallow import Marshmallow
import json
from flask_cors import CORS

app = Flask(__name__)
ma = Marshmallow(app)

CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

comments_routes = Blueprint('comments', __name__)


class CommentsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        #
        fields = ("id", "text", "username", "post_id", "likes", "dislikes")


comments_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)


@comments_routes.route('/', methods=["GET", "POST", "PATCH"])
def comments():
    if request.method == "POST":
        body = request.get_json()
        text = body["text"]
        # date = body["date"]
        username = body["username"]
        post_id = body["post_id"]

        comment = Comment(text=text, username=username,
                          post_id=post_id, likes=[], dislikes=[])

        db.session.add(comment)
        db.session.commit()
        return body
    elif request.method == "PATCH":
        body = request.get_json()
        username = body["username"]
        option = body["option"]
        id = body["id"]
        likes = body["likes"]
        dislikes = body["dislikes"]
        post_to_patch = Comment.query.filter_by(id=id).first()
        if option == "likes":
            if username in likes:
                likes.remove(username)
                number = -1
            else:
                likes.append(username)
                number = 1
        else:
            if username in dislikes:
                dislikes.remove(username)
                number = -1
            else:
                dislikes.append(username)
                number = 1
        post_to_patch.likes = likes
        post_to_patch.dislikes = dislikes
        db.session.commit()
        return str(number)
    else:
        all_comments = Comment.query.all()
        return (json.dumps(comments_schema.dump(all_comments)))


@comments_routes.route('/<int:post_id>', methods=["GET"])
def comments_post(post_id):
    all_comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.id.desc()).all()
    return (json.dumps(comments_schema.dump(all_comments)))
