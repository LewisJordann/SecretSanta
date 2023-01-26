from extensions import db
from sqlalchemy import Text
from datetime import datetime
import bcrypt

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validateEmail(self, email):
        pass

