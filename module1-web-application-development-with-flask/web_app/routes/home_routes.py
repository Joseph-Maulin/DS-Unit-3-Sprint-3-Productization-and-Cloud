

from flask import Blueprint


home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def home():
    return "home"

@home_routes.route("/about")
def about():
    return "simple flask app"
