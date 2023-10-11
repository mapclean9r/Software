import os
import sqlite3

pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def create_user(Username, Password, Admin):
    try:
        cur.execute("SELECT Username FROM User")
        user = cur.fetchall()
        cur.execute("SELECT Username FROM User WHERE Username = ?", (Username,))
        user2 = cur.fetchone()
        cur.execute("INSERT INTO User(Username, Password,Admin) VALUES(?,?,?)", (Username, Password, Admin))
        for i in user:
            if i == user2:
                return print("Brukernavn allerede i bruk")
        con.commit()
        return print("Bruker opprettet")
    except:
        print("FEIL I CREATE_USER")


def username_get(Username):
    cur.execute("SELECT Username FROM User WHERE Username = ?", (Username,))
    user = cur.fetchone()
    return user


def password_get(Username):
    cur.execute("SELECT Password FROM User WHERE Username = ?", (Username,))
    passs = cur.fetchone()
    return passs


def admin_get(Username):
    cur.execute("SELECT Admin FROM User WHERE Username = ?", (Username,))
    admin = cur.fetchone()
    return admin


