import os
from datetime import datetime
from ..autentication.login import get_user_online
path = os.path.dirname(__file__) + "/userlogs.txt"

def logging(action):
    timestamp = datetime.now()
    name = get_user_online()
    namestamp = f'{timestamp:Date: %d.%m.%y Time: %H:%M} User: {name} {action} '

    with open(path, 'a') as file:
        print(namestamp, file=file)


def get_logging():
    log = []
    with open(path, 'r') as file:
        for i in file:
            log.append(i)
    return log
