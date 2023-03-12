import re
class User():
    def __init__(self, email, password, confirmPassword):
        self.email = email
        self.password = password
        self.confirmPassword = confirmPassword

    def validateEmailSyntax(self):
        emailFormat = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        if re.search(emailFormat, self.email):
            return True
        return False

    def validatePasswordSyntax(self):
        passwordFormat = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
        if re.search(passwordFormat, self.password):
            return True
        return False
    
    def comparePasswords(self):
        if self.password != self.confirmPassword:
            return False
        return True
