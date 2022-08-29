from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.comments import Comment
from flask_marshmallow import Marshmallow
import json

app = Flask(__name__)
ma = Marshmallow(app)

comments_routes = Blueprint('comments', __name__)

class CommentsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "text", "username", "post_id", "likes", "dislikes")
comments_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

@comments_routes.route('/comments', methods=["GET", "POST", "PATCH"])
def comments():
    if request.method == "POST":
        body = request.get_json()
        text = body["text"]
        # date = body["date"]
        username = body["username"]
        post_id = body["post_id"]

        comment = Comment(text=text, username=username, post_id=post_id, likes=0, dislikes=0)

        db.session.add(comment)
        db.session.commit()
        return body
    elif request.method == "PATCH":
        body = request.get_json()
        id = body["id"]
        likes = body["likes"]
        dislikes = body["dislikes"]
        # Needs to be finished
    else:
        all_comments = Comment.query.all()
        return(json.dumps(comments_schema.dump(all_comments)))

