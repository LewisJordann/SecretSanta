from flask import Flask
from config import Config
import pyrebase
from key import db_key
# initalize firebase
firebase = pyrebase.initialize_app(db_key)
auth = firebase.auth()

def create_app(config_class=Config):
    # initalize Flask app
    app = Flask(__name__, template_folder="template", static_folder="static")
    app.config.from_object(config_class)

    from .main.views import views

    app.register_blueprint(views, url_prefix='/')

    return app