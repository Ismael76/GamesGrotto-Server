from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.listings import Listing

main_routes = Blueprint("main", __name__)


@main_routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "Games Grotto API"
