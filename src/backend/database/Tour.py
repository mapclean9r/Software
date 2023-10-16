import os
import sqlite3
pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()

def Tour_create(Title, Description, Country, Location, Date):
    

    con.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUES(?,?,?,?,?)",
                (Title, Description, Country, Location, Date))
    con.commit()
    con.close()




def Tour_create_values_into_table(Title,Description,Country,Location,Date):
    con.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUES('Tour','Nice tour','Tourland','Tour Ave','2023-01-01')",
                (Title, Description, Country, Location, Date))
    con.commit()
    con.close()


def Tour_get():
    con.execute("SELECT * FROM Tour")
