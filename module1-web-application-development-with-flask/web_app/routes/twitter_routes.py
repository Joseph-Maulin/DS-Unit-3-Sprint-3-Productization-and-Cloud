


from flask import Blueprint, render_template, request, jsonify
from web_app.Twitter import User, Tweet, db


twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/tweet")
def tweet():
    return render_template("tweet.html")

@twitter_routes.route("/tweet/create", methods=["POST"])
def add_tweet():

    error = None

    try:
        user = db.session.query(User).filter(User.user_name == request.form['user']).all()
        if user:
            user_tweet = Tweet(user_id=int(user[0].id), tweet=request.form['tweet'])
        else:
            user = User(user_name=request.form['user'])
            db.session.add(user)
            user = db.session.query(User).filter(User.user_name == request.form['user']).all()
            user_tweet = Tweet(user_id=int(user[0].id), tweet=request.form['tweet'])
            print(user_tweet.user_id, user_tweet.tweet)

        db.session.add(user_tweet)

    except Exception as e:
        error = e

    if not error:
        db.session.commit()
        return jsonify({
            "message": "TWEET ADDED OK",
            "tweet" : dict(request.form)
        })

    else:
        db.session.rollback()
        return jsonify({
            "message": "TWEET FAILED",
            "tweet" : str(error)
        })
