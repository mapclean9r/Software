import sqlite3

con =sqlite3.connect("src/backend/database/database.db")
cur = con.cursor()

def create_user(Username,Password):
    cur.execute("INSERT INTO User(Username, Password) VALUES(?,?)",(Username,Password,))
    con.commit()

def username_get(Username):
    cur.execute("SELECT Username FROM User WHERE Username = ?",(Username,))
    user = cur.fetchall()
    return user

def password_get(Username):
    cur.execute("SELECT Password FROM User WHERE Username = ?",(Username,))
    passs = cur.fetchone()
    return passs



create_user("TEST","TSET")
print(username_get("TEST"))
print(password_get("TEST"))

con.close()