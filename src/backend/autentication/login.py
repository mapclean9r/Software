import json
from flask import Flask, render_template, url_for, redirect, request

from ..database import user
from ..database.user import *


# Slik bruker du klassen
# x = "brukernavn" y = "passord" z = True eller False
# variabel_navn = UserLogin(x, y, z)
# UserLogin.username_check_to_database(variabel_navn)
global_user_id = 0


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
                return self.admin
            else:
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
        pathing = os.path.dirname(__file__) + "/user_online.json"
        data = {'user_online': self.name}
        with open(pathing, 'w') as file:
            json.dump(data, file)


# Gets the current username in the .json file
def get_user_online():
    try:
        with open('user_online.json', 'r') as file:
            data = json.load(file)
            return data.get('user_online', '')
    except FileNotFoundError:
        return r'user_online.json File Not Found'


def login_proc():
    global global_user_id

    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        db = sqlite3.connect('backend/database/database.db')
        cursor = db.cursor()
        cursor.execute("SELECT * from Tour")
        list = cursor.fetchall()
        cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_user_id,))

        list_of_bought_tours = cursor.fetchall()
        db.close()

        t = UserLogin(username, password, False)

        UserLogin.save_user_online(t)

        userr = UserLogin.username_check_to_database(t)
        passw = UserLogin.password_check_to_database(t)
        is_admin = True
        if userr is True and passw is True:
            return render_template('/homepage.html', is_admin=is_admin, list_of_tours=list,
                                   list_of_bought_tours=list_of_bought_tours)
        else:
            return render_template('/index.html')
    return render_template('index.html')


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
