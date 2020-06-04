
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))

    def __repr__(self):
        return f"<User {self.id} {self.user_name}>"

class Tweet(db.Model):

    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    tweet = db.Column(db.String(1000))

    def __repr__(self):
        return f"<Tweet {self.id} {self.user_id} {self.tweet}>"
