from backend.autentication.register import validator_input_is_valid
from src.backend.autentication.login import *


# Login


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


def test_name_tuple_to_str():
    x = "ElgElg"
    create_user(x, "ElgElg", True)
    name_password = UserLogin(x, "ElgElg", True)
    assert UserLogin.name_tuple_to_str(name_password) == x


def test_password_tuple_to_str():
    y = "ElgElg"
    create_user("ElgElg", y, True)
    name_password = UserLogin("ElgElg", y, True)
    assert UserLogin.password_tuple_to_str(name_password) == y


def test_admin_tuple_to_str():
    z = True
    create_user("ElgElg", "ElgElg", z)
    name_password = UserLogin("ElgElg", "ElgElg", z)
    assert UserLogin.admin_tuple_to_str(name_password) is True


def test_admin_tuple_to_str_where_tuple_is_int():
    w = 1
    create_user("ElgElg", "ElgElg", w)
    name_password = UserLogin("ElgElg", "ElgElg", w)
    assert UserLogin.admin_tuple_to_str(name_password) is True


# Register


def test_register_validator_input_is_valid():
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
