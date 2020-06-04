from flask import Flask
import threading, webbrowser

from web_app.routes.home_routes import home_routes
from web_app.Twitter import db, migrate

# DATABASE_URI = "sqlite:///C:\Users\Joe.Maulin\Desktop\DS-Unit-3-Sprint-3-Productization-and-Cloud\module1-web-application-development-with-flask\web_app\twitter.db"
DATABASE_URI = "sqlite:///web_app_twitter.db"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()

    port = 5003
    host = "127.0.0.1"
    url = f"http://127.0.0.1:{port}"

    threading.Timer(0.5, lambda: webbrowser.open(url) ).start()
    print("Starting Flask_API")

    my_app.run(host=host, port=port, debug=False)
