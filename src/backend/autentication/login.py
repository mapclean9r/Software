from src.backend.database.user import *
import json
from flask import render_template

# from ..database.user import *


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
        tuple = username_get(self.name)
        if tuple is not None:
            for x in tuple:
                b = x
            if self.name == b:
                return True
            else:
                return False

    def password_check_to_database(self):
        tuple = password_get(self.name)
        if tuple is not None:
            for x in tuple:
                print(x)
                b = x
            if self.password == b:
                print(f"{self.name} True")
                return True
            else:
                return False

    def admin_check_to_database(self):
        tuple = admin_get(self.name)
        if tuple is not None:
            for x in tuple:
                print(x)
                b = x
            if admin_get(b):
                print(f"{admin_get(self.name)} trueee")
                print(self.admin)
                return self.admin
            else:
                print(f"{admin_get(self.name)} falseee" )
                return False


    def login_process(self):
        self.save_user_online()
        user = self.username_check_to_database()
        passw = self.password_check_to_database()
        if user is True and passw is True:
            return render_template('/homepage.html')
        else:
            return render_template('/index.html')

    # Saves the users username to a .json file & overwrites on reuse
    def save_user_online(self):
        data = {'user_online': self.name}
        with open('backend/autentication/user_online.json', 'w') as file:
            json.dump(data, file)


# Gets the current username in the .json file
def get_user_online():
    try:
        with open('user_online.json', 'r') as file:
            data = json.load(file)
            return data.get('user_online', '')
    except FileNotFoundError:
        return r'user_online.json File Not Found'


def login_checker(username_input, password_input, user_check_function, globalkey):
    userlogin_is_valid = user_check_function(
        username_input, password_input)

    print(f"Current user ID: {globalkey}")
    if userlogin_is_valid:
        print("You are logged in")
        return render_template('/homepage.html')
    else:
        print("Something happend, you are not logged in")
        return render_template('/index.html')


def get_user_online_is_admin():
    admin_check = get_user_online()
    if admin_get(admin_check) is True:
        return True
    else:
        return False

# Usage for json save_user_online & get_user_online
# login_cred1 = UserLogin("Horse", "pwHorse", True) // Parameters > String String Bool values
# UserLogin.save_user_online(login_cred1)

# print(get_user_online())


