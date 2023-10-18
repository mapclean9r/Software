import json

from src.backend.autentication.login import UserLogin, get_user_online
from src.backend.database.Tour import Tour_get


class Favorite:
    def __init__(self, json_file_name):
        self.json_file_name = json_file_name
        self.json_data = {}
        self.load_json()

    def load_json(self):
        try:
            with open(self.json_file_name, "r") as file:
                self.json_data = json.load(file)
        except FileNotFoundError:
            self.json_data = {}

    def save_json(self):
        with open(self.json_file_name, 'w') as file:
            json.dump(self.json_data, file, indent=4)

    def add_item_to_json(self, username, item):
        if username in self.json_data:
            self.json_data[username].append(item)
            print("W")
        else:
            self.json_data[username] = [item]
            print("L")
        self.save_json()


#Tour = "BBIIIGIGIG"
#tur_data = {"Tour": Tour}
#test = Favorite("ufavorite.json")
#Favorite.add_item_to_json(test, "bigboyuser", tur_data)
#Tour_get()
