


from flask import Blueprint, render_template


twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/tweet")
def tweet():
    return render_template("tweet.html")

@twitter_routes.route("/tweet/create", methods=["POST"])
def add_tweet():
    return "create tweet"
