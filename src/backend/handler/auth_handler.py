from backend.autentication.login import login_proc, get_user_online
from backend.autentication.register import username_checker
from backend.database.user import username_get, id_get, id_if_provide_username


def get_username():
    return username_get(get_user_online())

def get_id_from_username():
    return id_get(get_username())
def get_username_checker():
    return username_checker()

def get_start_login_process():
    return login_proc()

def get_id_if_provide_username():
    return id_if_provide_username(get_user_online())[0]