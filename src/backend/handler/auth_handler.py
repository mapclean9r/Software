from flask import request
from backend.autentication.login import login_proc, get_user_online
from backend.autentication.register import username_create
from backend.database.user import username_get, id_get, id_if_provide_username


def get_username():
    return username_get(get_user_online())

def get_id_from_username():
    return id_get(get_username())
def get_username_checker():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        is_admin = request.form.get('admin_login', False)
        return username_create(username, password, is_admin)

def get_start_login_process():
    return login_proc()

def get_id_if_provide_username():
    return id_if_provide_username(get_user_online())[0]