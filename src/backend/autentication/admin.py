from datetime import datetime

from login import get_user_online


def logging(action):
    timestamp = datetime.now()
    name = get_user_online()
    namestamp = f'{timestamp:Date: %d.%m.%y Time: %H:%M} User: {name} {action} '

    with open('userlogs.txt', 'a') as file:
        print(namestamp, file=file)


logging("Walked in the park")
