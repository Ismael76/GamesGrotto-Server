from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.listings import Listing

main_routes = Blueprint("main", __name__)

# these will be the main app routes for game database CRUD.

@main_routes.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":

        pass

    else:

        pass
