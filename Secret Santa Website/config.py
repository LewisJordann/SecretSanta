import os

# basedir - os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False