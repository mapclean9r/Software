from backend.autentication.register import validator_input_is_valid
from src.backend.autentication.login import *


def test_username_check_to_database_is_valid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Horse", False)
    assert UserLogin.username_check_to_database(name_password) is True


def test_username_check_to_database_is_invalid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Moose", "Horse", False)
    assert UserLogin.username_check_to_database(name_password) is False


def test_password_check_to_database_is_valid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Horse", False)
    assert UserLogin.password_check_to_database(name_password) is True


def test_password_check_to_database_is_invalid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Moose", False)
    assert UserLogin.password_check_to_database(name_password) is False


def test_admin_check_to_database_is_not_admin():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Horse", False)
    assert UserLogin.admin_check_to_database(name_password) is False


def test_admin_check_to_database_is_admin():
    create_user("ElgElg", "ElgElg", True)
    name_password = UserLogin("ElgElg", "ElgElg", True)
    assert UserLogin.admin_check_to_database(name_password) is True


# Register


def test_validator_input_is_true():
    username = "horse"
    password = "passw"
    assert validator_input_is_valid(username, password) is True


def test_register_validator_input_14_plus_letters():
    username = "horsefreuifjerufjerujf"
    password = "passwkjjjnnjnkjnkjnkjnkjnkjnkjn"
    assert validator_input_is_valid(username, password) is False


def test_register_validator_input_empty_field():
    username = ""
    password = "paweey"
    assert validator_input_is_valid(username, password) is False
