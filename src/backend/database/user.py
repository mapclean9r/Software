import sqlite3

con =sqlite3.connect("src/backend/database/database.db")
cur = con.cursor()

def create_user(Username,Password):
    cur.execute("INSERT INTO User(Username, Password) VALUE(?,?)",(Username,Password))
    con.commit()

def username_get(Username):
    cur.execute("SELECT Username FROM User WHERE Username = ?",(Username,))

def password_get(Username):
    cur.execute("SELECT Password FROM User WHERE Username = ?",(Username,))





con.close()