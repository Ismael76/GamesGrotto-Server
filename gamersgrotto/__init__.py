from dotenv import load_dotenv
from os import environ
from flask import Flask
from flask_cors import CORS

from .database.db import db
from .routes.main import main_routes
# route for auth
from .routes.auth import auth_routes
# route for listings
from .routes.listings import listings_routes
# routes for forum posts and comments
from .routes.posts import posts_routes
from .routes.comments import comments_routes
from .routes.scores import scores_routes
# Load environment variables

load_dotenv()

database_uri = environ.get('DATABASE_URL')

if 'postgres:' in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")

# Set up the app

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})


db.app = app
db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes, url_prefix="/auth")
app.register_blueprint(listings_routes, url_prefix="/listings")
app.register_blueprint(posts_routes)
app.register_blueprint(comments_routes, url_prefix="/comments")
app.register_blueprint(scores_routes, url_prefix="/scores")
# add another route for auth

# Main

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
