from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.posts import Post
from flask_marshmallow import Marshmallow
import json

app = Flask(__name__)
ma = Marshmallow(app)

posts_routes = Blueprint('posts', __name__)

class PostsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "text", "username", "likes", "dislikes")
posts_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

@posts_routes.route('/posts', methods=["GET", "POST", "PATCH"])
def posts():
    if request.method == "POST":
        body = request.get_json()
        title = body["title"]
        text = body["text"]
        # date = body["date"]
        username = body["username"]

        post = Post(title=title, text=text, username=username, likes=0, dislikes=0)

        db.session.add(post)
        db.session.commit()
        return body
    elif request.method == "PATCH":
        body = request.get_json()
        id = body["id"]
        likes = body["likes"]
        dislikes = body["dislikes"]
        # Needs to be finished
    else:
        all_posts = Post.query.all()
        return(json.dumps(posts_schema.dump(all_posts)))
