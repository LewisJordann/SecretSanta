from flask import Flask, url_for

def create_app():
    # initalize Flask
    app = Flask(__name__, template_folder="template", static_folder="static")

    # remove secret key before pushing
    app.config['SECRET_KEY'] = ''

    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app