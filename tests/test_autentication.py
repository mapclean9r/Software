from src.backend.autentication.login import *


def test_username_check_to_database():
    create_user("Horse", "Horse")
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.username_check_to_database(name_password)


def test_password_check_to_database():
    create_user("Horse", "Horse")
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.password_check_to_database(name_password)
