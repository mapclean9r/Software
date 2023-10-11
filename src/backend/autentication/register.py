from src.backend.database.user import *


class UserRegister:
    def __init__(self, username, password, admin):
        self.name = username
        self.password = password
        self.admin = admin

    def register_user_in_database(self):
        create_user(self.name, self.password, self.admin)
