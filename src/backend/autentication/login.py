from src.backend.database.user import *
import json

from src.backend.database.user import username_get


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
        if username_get(self.name):
            print("username WWWW")
            return self.name
        else:
            print("mini LL")
            return False

    def password_check_to_database(self):
        if password_get(self.name):
            print("pw dub")
            return self.password
        else:
            return False

    def admin_check_to_database(self):
        if admin_get(self.name):
            print("admin dub")
            return self.admin
        else:
            return False

    # Saves the users username to a .json file & overwrites on reuse
    def save_user_online(self):
        data = {'user_online': self.name}
        with open('backend/autentication/user_online.json', 'w') as file:
            json.dump(data, file)

    # Gets the current username in the .json file


def get_user_online():
    try:
        with open('backend/autentication/user_online.json', 'r') as file:
            data = json.load(file)
            return data.get('user_online', '')
    except FileNotFoundError:
        return r'user_online.json File Not Found'


# Usage for json save_user_online & get_user_online
# login_cred1 = UserLogin("Horse", "pwHorse", True) // Parameters > String String Bool values
# UserLogin.save_user_online(login_cred1)

# print(get_user_online())
