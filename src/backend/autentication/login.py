from src.backend.database.user import *
import json


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

    # Saves the users username to a .json file & overwrites on reuse
    def save_user_online(self):
        data = {'user_online': self.name}
        with open('user_online.json', 'w') as file:
            json.dump(data, file)

    # Gets the current username in the .json file


def get_user_online():
    try:
        with open('user_online.json', 'r') as file:
            data = json.load(file)
            return data.get('user_online', '')
    except FileNotFoundError:
        return r'user_online.json File Not Found'


# Usage for json save_user_online & get_user_online
# login_cred1 = UserLogin("Horse", "pwHorse", True) // Parameters > String String Bool values
# UserLogin.save_user_online(login_cred1)

# print(get_user_online())
