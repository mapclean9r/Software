from ..database.user import *
from flask import render_template, request
from ..database import user


def user_create(username, password, is_admin):
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
