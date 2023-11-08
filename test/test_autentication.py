from backend.autentication.register import validator_input_is_valid
from src.backend.autentication.login import *


def test_username_check_to_database():
    create_user("Horse", "Horse", False)
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.username_check_to_database(name_password) is True


def test_password_check_to_database():
    create_user("Horse", "Horse", False)
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.password_check_to_database(name_password) is True


def test_admin_check_to_database():
    create_user("Horse", "Horse", False)
    x = "Horse"
    y = "Horse"
    z = False
    name_password = UserLogin(x, y, z)
    assert UserLogin.admin_check_to_database(name_password) is False


# Register


def test_validator_input_is_true():
    username = "horse"
    password = "passw"
    assert validator_input_is_valid(username,password) is True


def test_validator_input_is_false():
    username = "horsefreuifjerufjerujf"
    password = "passwkjjjnnjnkjnkjnkjnkjnkjnkjn"
    assert validator_input_is_valid(username,password) is False
    