import os
import sqlite3
pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def Tour_create(Title,Description,Country,Location,Date):
    try:
        con.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUE(?,?,?,?,?)",(Title,Description,Country,Location,Date))
        con.commit()
    except:
        print("FEIL I TOUR_CREATE")
    

def Tour_get():
    try:
        con.execute("SELECT * FROM Tour")
    except:
        print("FEIL I TOUR_GET")

