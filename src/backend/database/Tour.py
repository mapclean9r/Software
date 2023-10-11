import os
import sqlite3
pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def Tour_create(Title,Description,Country,Location,Date):
    con.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUE(?,?,?,?,?)",(Title,Description,Country,Location,Date))
    con.commit()

def Tour_get():
    con.execute("SELECT * FROM Tour")
