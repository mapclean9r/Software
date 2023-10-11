from src.backend.database.user import *


# Slik bruker du klassen
# x = "brukernavn" y = "passord" z = True eller False
# variabel_navn = UserLogin(x, y, z)
# UserLogin.username_check_to_database(variabel_navn)

class UserLogin:
    def __init__(self, username, password, admin):
        self.name = username
        self.password = password
        self.admin = admin

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

    def admin_check_to_database(self):
        if self.admin == admin_get(self.admin):
            return self.admin
        else:
            return False
