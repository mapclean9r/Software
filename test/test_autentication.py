from src.backend.autentication.login import *


def test_username_check_to_database():
    create_user("Horse", "Horse", False)
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.username_check_to_database(name_password)


def test_password_check_to_database():
    create_user("Horse", "Horse", False)
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.password_check_to_database(name_password)


def test_admin_check_to_database():
    create_user("Horse", "Horse", False)
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.admin_check_to_database(name_password) == False

# Register

def test_