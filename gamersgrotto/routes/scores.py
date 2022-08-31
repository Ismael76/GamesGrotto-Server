from flask import Blueprint, request, jsonify, Flask, make_response
from datetime import datetime, timedelta
from functools import wraps
from ..database.db import db
from ..models.scores import Score
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json

app = Flask(__name__)
ma = Marshmallow(app)

CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

scores_routes = Blueprint('scores', __name__)


class ScoresSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "score")


scores_schema = ScoresSchema()
scores_schema = ScoresSchema(many=True)


@scores_routes.route('/', methods=["GET", "PATCH", "POST"])
def scores():
    if request.method == "PATCH":
        body = request.get_json()
        username = body["username"]
        score = body["score"]
        score_to_patch = Score.query.order_by(Score.score).first()
        result = 0
        if score >= score_to_patch.score:
            score_to_patch.username = username
            score_to_patch.score = score
            result = 1
        db.session.commit()
        return str(result)
    elif request.method == "POST":
        body = request.get_json()
        username = body["username"]
        score = body["score"]
        highscore = Score(username=username, score=score)
        db.session.add(highscore)
        db.session.commit()
        return body
    else:
        all_scores = Score.query.all()
        return (json.dumps(scores_schema.dump(all_scores)))
