from datetime import datetime
from ..autentication.login import get_user_online


def logging(action):
    timestamp = datetime.now()
    name = get_user_online()
    namestamp = f'{timestamp:Date: %d.%m.%y Time: %H:%M} User: {name} {action} '

    with open('userlogs.txt', 'a') as file:
        print(namestamp, file=file)


def get_logging():
    log = []
    with open("userlogs.txt", 'r') as file:
        for i in file:
            log.append(i)
    return log


print(get_logging())
get_logging()

