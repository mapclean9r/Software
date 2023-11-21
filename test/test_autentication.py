from backend.autentication.admin import logging, get_logging
from backend.autentication.register import validator_input_is_valid
from backend.database.Tour import remove_user_from_list
from src.backend.autentication.login import *


# Login


def test_username_check_to_database_is_valid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Horse", False)
    assert UserLogin.username_check_to_database(name_password) is True

    # Tobias, når du ser disse tre linjene jeg har lagt til, så er den eneste funksjonaliteten til de tre linjene at
    # Brukeren du lager i testen blir sletta etter at testen er gjort. Slik slipper vi at testene våres lager mange
    # dummybrukere som vi ikke vil ha inni applikasjonen. Se for det at Sensor kjører alle testene våres før han kjører
    # applikasjonen. Da vil han se mange rare brukere som er registrert.
    user_id = id_if_provide_username("Horse")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_username_check_to_database_is_invalid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Moose", "Horse", False)
    assert UserLogin.username_check_to_database(name_password) is False

    user_id = id_if_provide_username("Horse")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_password_check_to_database_is_valid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Horse", False)
    assert UserLogin.password_check_to_database(name_password) is True

    user_id = id_if_provide_username("Horse")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_password_check_to_database_is_invalid():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Moose", False)
    assert UserLogin.password_check_to_database(name_password) is False

    user_id = id_if_provide_username("Horse")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_admin_check_to_database_is_not_admin():
    create_user("Horse", "Horse", False)
    name_password = UserLogin("Horse", "Horse", False)
    assert UserLogin.admin_check_to_database(name_password) is False

    user_id = id_if_provide_username("Horse")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_admin_check_to_database_is_admin():
    create_user("ElgElg", "ElgElg", True)
    name_password = UserLogin("ElgElg", "ElgElg", True)
    assert UserLogin.admin_check_to_database(name_password) is True

    user_id = id_if_provide_username("ElgElg")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_name_tuple_to_str():
    x = "ElgElg"
    create_user(x, "ElgElg", True)
    name_password = UserLogin(x, "ElgElg", True)
    assert UserLogin.name_tuple_to_str(name_password) == x

    user_id = id_if_provide_username("ElgElg")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_password_tuple_to_str():
    y = "ElgElg"
    create_user("ElgElg", y, True)
    name_password = UserLogin("ElgElg", y, True)
    assert UserLogin.password_tuple_to_str(name_password) == y

    user_id = id_if_provide_username("ElgElg")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_admin_tuple_to_str():
    z = True
    create_user("ElgElg", "ElgElg", z)
    name_password = UserLogin("ElgElg", "ElgElg", z)
    assert UserLogin.admin_tuple_to_str(name_password) is True

    user_id = id_if_provide_username("ElgElg")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_admin_tuple_to_str_where_tuple_is_int():
    w = 1
    create_user("ElgElg", "ElgElg", w)
    name_password = UserLogin("ElgElg", "ElgElg", w)
    assert UserLogin.admin_tuple_to_str(name_password) is True

    user_id = id_if_provide_username("ElgElg")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")


def test_save_user_online_to_json_and_returns_your_login_name():
    # Saves the current logged-in user to a json file and returns the name
    name = "ElgElg"
    login = UserLogin(name, "ElgElg", True)
    UserLogin.save_user_online(login)
    assert get_user_online() == name


def test_proc_utils_db_list_of_bought_tours():
    pass


def test_login_proc_utils_db_list():
    pass


def login_proc_credential_checks_renders_new_template_if_is_correct():
    pass


def login_proc_credential_checks_renders_the_same_template_if_is_incorrect():
    pass


# Register


def test_register_validator_input_is_valid():
    username = "horse"
    password = "passw"
    # True return if statement passes the test
    assert validator_input_is_valid(username, password) is True


def test_register_validator_both_input_has_14_plus_letters():
    username = "horsefreuifjerufjerujf"
    password = "passwkjjjnnjnkjnkjnkjnkjnkjnkjn"
    # False return if statement does not pass the test
    assert validator_input_is_valid(username, password) is False


def test_register_validator_username_input_has_14_plus_letters():
    username = "horsefreuifjerufjerujf"
    password = "passme"
    # False return if statement does not pass the test
    assert validator_input_is_valid(username, password) is False


def test_register_validator_password_input_has_14_plus_letters():
    username = "horser"
    password = "passwkjjjnnjnkjnkjnkjnkjnkjnkjn"
    # False return if statement does not pass the test
    assert validator_input_is_valid(username, password) is False


def test_register_validator_username_input_empty_field():
    username = ""
    password = "paweey"
    # False return if statement does not pass the test
    assert validator_input_is_valid(username, password) is False


def test_register_validator_password_input_empty_field():
    username = "ytgfhfgh"
    password = ""
    # False return if statement does not pass the test
    assert validator_input_is_valid(username, password) is False


def test_register_validator_both_input_empty_field():
    username = ""
    password = ""
    # False return if statement does not pass the test
    assert validator_input_is_valid(username, password) is False


# Admin

def test_save_log_and_get_log():
    create_user("ElgElg", "ElgElg", True)
    name = "ElgElg"
    login = UserLogin(name, "ElgElg", True)
    UserLogin.save_user_online(login)
    logging("Has tested the logging button")
    assert get_logging()[-1].__contains__("ElgElg Has tested")
