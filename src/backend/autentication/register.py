

from ..database.user import *
from flask import render_template,request
from ..database import user



class UserRegister:
    def __init__(self, username, password, admin):
        self.name = username
        self.password = password
        self.admin = admin

    def register_user_in_database(self):
        create_user(self.name, self.password, self.admin)
        print(self.name, self.password, self.admin)


def username_checker():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        is_admin = request.form.get('admin_login', False)
        if username == user.username_get(username):
            error_register = "Username exists."
            return render_template('/registrer.html', error_register=error_register)
        elif username != user.username_get(username):
            if validator_input_is_valid(username, password) is True:
                user.create_user(username, password, is_admin)
                return render_template('/registrer.html')
            else:
                return render_template('/registrer.html')


def validator_input_is_valid(username, password):
    if username == "" or password == "":
        return False
    if len(username) >= 14 or len(password) >= 14:
        return False
    else:
        return True
