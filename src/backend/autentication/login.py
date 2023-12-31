import json
from flask import Flask, render_template, url_for, redirect, request

from backend.database.user import *

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
        b = UserLogin.name_tuple_to_str(self)
        if self.name == b:
            return True
        else:
            return False

    def password_check_to_database(self):
        b = UserLogin.password_tuple_to_str(self)
        if self.password == b:
            return True
        else:
            return False

    def admin_check_to_database(self):
        b = UserLogin.admin_tuple_to_str(self)
        if b is True:
            return True
        else:
            return False

    # Saves the users username to a .json file & overwrites on reuse
    def save_user_online(self):
        pathing = os.path.dirname(__file__) + "/user_online.json"
        data = {'user_online': self.name}
        with open(pathing, 'w') as file:
            json.dump(data, file)

    def name_tuple_to_str(self):
        tuple = username_get(self.name)
        if tuple is not None:
            for x in tuple:
                return x

    def password_tuple_to_str(self):
        tuple = password_get(self.name)
        if tuple is not None:
            for x in tuple:
                return x

    def admin_tuple_to_str(self):
        tuple = admin_get(self.name)
        if isinstance(tuple, int):
            return bool(tuple)
        else:
            if tuple:
                if tuple is not None:
                    for x in tuple:
                        return bool(x)


# Gets the current username in the .json file
def get_user_online():
    pathing = os.path.dirname(__file__) + "/user_online.json"
    try:
        with open(pathing, 'r') as file:
            data = json.load(file)
            return data.get('user_online', '')
    except FileNotFoundError:
        return r'user_online.json File Not Found'


def login_proc_utils_db_list_of_bought_tours():
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()
    cursor.execute('''SELECT *
    FROM Tour
    INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
    WHERE TourBooked.User_ID = ?''', (global_user_id,))

    list_of_bought_tours = cursor.fetchall()
    db.close()
    return list_of_bought_tours


def login_proc_utils_db_list():
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()
    db.close()
    return list


def login_proc():
    global global_user_id

    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        list_of_bought_tours = login_proc_utils_db_list_of_bought_tours()
        list = login_proc_utils_db_list()

        t = UserLogin(username, password, False)
        UserLogin.save_user_online(t)

        userr = UserLogin.username_check_to_database(t)
        passw = UserLogin.password_check_to_database(t)
        is_admin = UserLogin.admin_check_to_database(t)
        if userr and passw:
            return render_template('/homepage.html', is_admin=is_admin, list_of_tours=list,
                                   list_of_bought_tours=list_of_bought_tours)
        else:
            return render_template('/index.html')
    return render_template('index.html')


def get_user_online_is_admin():
    admin_check = get_user_online()
    if admin_get(admin_check):
        return True
    else:
        return False

# Usage for json save_user_online & get_user_online
# login_cred1 = UserLogin("Horse", "pwHorse", True) // Parameters > String String Bool values
# UserLogin.save_user_online(login_cred1)

# print(get_user_online())
