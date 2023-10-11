import os
import sqlite3
pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def create_user(Username,Password):
        try:
            cur.execute("SELECT Username FROM Uer")
            user = cur.fetchall()
            cur.execute("SELECT Username FROM User WHERE Username = ?",(Username,))
            user2 = cur.fetchone()
            cur.execute("INSERT INTO User(Username, Password) VALUES(?,?)",(Username,Password,))
            for i in user:
                if i == user2:
                    return print("Brukernavn allerede i bruk")
                else:
                    con.commit()
        except:
             print("FEIL I CREATE_USER")



    

def username_get(Username):
    cur.execute("SELECT Username FROM User WHERE Username = ?",(Username,))
    user = cur.fetchone()
    return user

def password_get(Username):
    cur.execute("SELECT Password FROM User WHERE Username = ?",(Username,))
    passs = cur.fetchone()
    return passs



create_user("LAST","TSET")
print(username_get("TEST"))
print(password_get("TEST"))

