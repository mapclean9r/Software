import pytest
from src.backend.autentication.login import *

def test_username_check_to_database():
    x = "Horse"
    y = "Horse"
    name_password = UserLogin(x, y)
    assert UserLogin.username_check_to_database(name_password)
    