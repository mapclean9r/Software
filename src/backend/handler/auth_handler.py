from backend.autentication.login import login_proc
from backend.autentication.register import username_checker


def get_username_checker():
    return username_checker()

def get_start_login_process():
    return login_proc()