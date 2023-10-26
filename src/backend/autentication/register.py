from src.backend.database.user import *
from flask import render_template
from src.backend.database import user


class UserRegister:
    def __init__(self, username, password, admin):
        self.name = username
        self.password = password
        self.admin = admin

    def register_user_in_database(self):
        create_user(self.name, self.password, self.admin)
        print(self.name, self.password, self.admin)


def username_checker(username, password, is_admin):
    if username == user.username_get:
        error_register = "Username exists."
        return render_template('/registrer.html', error_register=error_register)
    else:
        user.create_user(username, password, is_admin)
        return render_template('/registrer.html')
