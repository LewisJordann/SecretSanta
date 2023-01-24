from flask import Flask
from Website.extensions import db
from config import Config

def create_app(config_class=Config):
    # initalize Flask app
    app = Flask(__name__, template_folder="template", static_folder="static")
    app.config.from_object(config_class)

    from .main.views import views
    from .main.auth import auth

    # init extension here
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app