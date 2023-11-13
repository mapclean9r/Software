import os
import sqlite3


pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def create_user(Username, Password, Admin):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        cur.execute("SELECT Username FROM User")
        user = cur.fetchall()
        cur.execute("SELECT Username FROM User WHERE Username = ?", (Username,))
        user2 = cur.fetchone()
        cur.execute("INSERT INTO User(Username, Password,Admin) VALUES(?,?,?)",
                    (Username, Password, Admin))
        for i in user:
            if i == user2:
                print("Brukernavn allerede i bruk")
        con.commit()
        return print("Bruker opprettet")
    except:
        return print("FEIL I CREATE_USER")


def username_get(Username):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("SELECT Username FROM User WHERE Username = ?", (Username,))
    Username = cur.fetchone()
    return Username


def id_if_provide_username(Username):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("SELECT ID FROM User WHERE Username = ?", (Username,))
    id = cur.fetchone()
    return id


def check_if_username_and_password_is_correct(username, password):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM User WHERE Username = ? AND Password = ?", (username, password))
    result_sql = cur.fetchall()
    con.close()
    return result_sql


def password_get(Username):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("SELECT Password FROM User WHERE Username = ?", (Username,))
        passs = cur.fetchone()
        return passs
    except:
        print("FEIL I PASSWORD_GET")


def admin_get(Username):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("SELECT Admin FROM User WHERE Username = ?", (Username,))
        admin = cur.fetchone()
        return admin[0]
    except:
        print("FEIL I ADMIN_GET")


def id_get(Username):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("SELECT ID FROM User WHERE Username = ?", (Username,))
        user = cur.fetchone()
        return sum(user)
    except:
        print("FEIL I ID_GET")
