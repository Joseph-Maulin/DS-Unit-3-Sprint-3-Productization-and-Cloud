
from flask import Flask
import threading, webbrowser

from web_app.routes.home_routes import home_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)

    return app


my_app = create_app()

port = 5003
host = "127.0.0.1"
url = f"http://127.0.0.1:{port}"

threading.Timer(0.5, lambda: webbrowser.open(url) ).start()
print("Starting Flask_API")

my_app.run(host=host, port=port, debug=False)
