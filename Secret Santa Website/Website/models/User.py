from datetime import datetime
import bcrypt

class User():
    data_created = datetime.utcnow

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validateEmail(self, email):
        pass
