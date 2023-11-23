from src.backend.database.user import *


def test_create_user_name_is_in_db():
    create_user("Swain", "Swain", 1)
    username = username_get("Swain")
    assert username[0] == "Swain"
    user_delete("Swain")


def test_create_user_name_is_not_in_db():
    create_user("Swain", "Swain", 1)
    username = username_get("Swain")
    assert username[0] != "Darius"
    user_delete("Swain")


def test_create_user_password_is_in_db():
    create_user("Swain", "Swain", 1)
    password = password_get("Swain")
    assert password[0] == "Swain"
    user_delete("Swain")


def test_create_user_password_not_in_db():
    create_user("Swain", "Swain", 1)
    password = password_get("Swain")
    assert password[0] != "Demacia"
    user_delete("Swain")


def test_create_user_is_admin():
    create_user("Swain", "Swain", 1)
    admin = admin_get("Swain")
    assert admin == 1
    user_delete("Swain")


def test_create_user_is_not_admin():
    create_user("Jericho", "Jericho", 0)
    admin = admin_get("Jericho")
    assert admin == 0
    user_delete("Jericho")


def test_username_get_valid_name_from_db():
    create_user("Jericho", "Jericho", 0)
    l = username_get("Jericho")
    assert l[0] == "Jericho"
    user_delete("Jericho")


def test_username_get_name_that_does_not_exist_from_db():
    create_user("Jericho", "Jericho", 0)
    username = username_get("Jericho")
    assert username[0] != "Not_Jericho"
    user_delete("Jericho")


def test_id_if_provide_username_get_id_from_name():
    # A duplicate func exists in the code // only 1 was written
    create_user("Jericho", "Jericho", 0)
    id = id_if_provide_username("Jericho")
    # Checking if the id is an int (gets added as an int) since it auto-increments in sql.
    assert isinstance(id[0], int) is True
    user_delete("Jericho")


def test_check_if_username_and_password_is_correct():
    create_user("Jericho", "Biggus", 0)
    check = check_if_username_and_password_is_correct("Jericho", "Biggus")
    assert check[0][1] == "Jericho"
    assert check[0][2] == "Biggus"
    user_delete("Jericho")


def test_check_if_username_and_password_is_incorrect():
    create_user("Swain", "Swain", 0)
    check = check_if_username_and_password_is_correct("Swain", "Swain")
    assert check[0][1] != "Jericho"
    assert check[0][2] != "Jericho"
    user_delete("Jericho")


def test_password_get_provided_username():
    create_user("Singed", "Swain", False)
    passs = password_get("Singed")
    assert passs[0] == "Swain"
    user_delete("Singed")


def test_password_get_provided_username_is_invalid():
    create_user("Singed", "Draven", 0)
    passs = password_get("Singed")
    assert passs[0] != "Swain"
    user_delete("Singed")


def test_admin_get_user_is_admin():
    create_user("Swain", "lain", False)
    admin = admin_get("Swain")
    assert admin == 0
    user_delete("Swain")


def test_admin_get_user_is_not_admin():
    create_user("Swain", "lain", False)
    admin = admin_get("Swain")
    assert admin != 1
    user_delete("Swain")


def test_user_delete_checks_if_user_is_detected_in_db_after_deletion():
    create_user("Swain", "Swain", 0)
    before = username_get("Swain")
    assert before[0] == "Swain"
    user_delete("Swain")
    after = username_get("Swain")
    assert after != before
