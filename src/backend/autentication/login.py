from src.backend.database.user import *

class UserLogin:
    def __init__(self, username, password):
        self.name = username
        self.password = password

    def username_check_to_database(self):
        if self.name in username_get(self.name):
            return self.name
        else:
            return False

    def password_check_to_database(self):
        if self.password in password_get(self.password):
            return self.name
        else:
            return False

