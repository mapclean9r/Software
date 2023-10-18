import os
import sqlite3
pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def Tour_create(Title, Description, Country, Location, Date):
    con = sqlite3.connect(pathing)
    cur = con.cursor()

    con.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUES(?,?,?,?,?)",
                (Title, Description, Country, Location, Date))
    con.commit()
    con.close()


def Tour_get():
    con.execute("SELECT * FROM Tour")
