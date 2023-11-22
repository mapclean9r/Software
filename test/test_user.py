from src.backend.database.user import *


def test_create_user_name():
    create_user("Swain", "Swain", 1)
    username = username_get("Swain")
    assert username[0] == "Swain"
    user_delete("Swain")

def test_create_user_not_name():
    create_user("Swain", "Swain", 1)
    username = username_get("Swain")
    assert username[0] != "Darius"
    user_delete("Swain")

def test_create_user_password():
    create_user("Swain", "Swain", 1)
    password = password_get("Swain")
    assert password[0] == "Swain"
    user_delete("Swain")

def test_create_user_not_password():
    create_user("Swain", "Swain", 1)
    password = password_get("Swain")
    assert password[0] != "Demacia"
    user_delete("Swain")

def test_create_user_admin():
    create_user("Swain", "Swain", 1)
    admin = admin_get("Swain")
    assert admin == 1
    user_delete("Swain")

def test_create_user_admin():
    create_user("Jericho", "Jericho", 0)
    admin = admin_get("Jericho")
    assert admin == 0
    user_delete("Jericho")

def test_username_get():
    create_user("Jericho", "Jericho", 0)
    l = username_get("Jericho")
    assert l[0] == "Jericho"
    user_delete("Jericho")

def test_username_get_fail():
    create_user("Jericho", "Jericho", 0)
    username = username_get("Jericho")
    assert username[0] != "Not_Jericho"
    user_delete("Jericho")

def test_id_if_provide_username():
    create_user("Jericho", "Jericho", 0)
    id = id_if_provide_username("Jericho")
    assert isinstance(id[0], int) is True
    user_delete("Jericho")

#Hvordan bevise at det ikke er en int???


def test_check_if_username_and_password_is_correct():
    create_user("Jericho", "Jericho", 0)
    check = check_if_username_and_password_is_correct("Jericho","Jericho")
    assert check[0][1] == "Jericho"
    assert check[0][2] == "Jericho"
    user_delete("Jericho")

def test_check_if_username_and_password_is_not_correct():
    create_user("Swain", "Swain", 0)
    check = check_if_username_and_password_is_correct("Swain","Swain")
    assert check[0][1] != "Jericho"
    assert check[0][2] != "Jericho"
    user_delete("Jericho")

def test_password_get():
    create_user("Swain", "Swain", 0)
    passs = password_get("Swain")
    assert passs[0] == "Swain"
    user_delete("Swain")

def test_password_get_fail():
    create_user("Swain", "Swain", 0)
    passs = password_get("Swain")
    assert passs[0] != "Swainn"
    user_delete("Swain")

def test_admin_get():
    create_user("Swain", "Swain", 0)
    admin = admin_get("Swain")
    assert admin == 0
    user_delete("Swain")

def test_admin_get_fail():
    create_user("Swain", "Swain", 0)
    admin = admin_get("Swain")
    assert admin != 1
    user_delete("Swain")

def test_user_delete():
    create_user("Swain", "Swain", 0)
    before = username_get("Swain")
    assert before[0] == "Swain"
    user_delete("Swain")
    after = username_get("Swain")
    assert after != before

