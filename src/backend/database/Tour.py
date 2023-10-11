import sqlite3

con =sqlite3.connect("src/backend/database/database.db")
cur = con.cursor()

def Tour_create(Title,Description,Country,Location,Date):
    con.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUE(?,?,?,?,?)",(Title,Description,Country,Location,Date))
    con.commit()

def Tour_get():
    con.execute("SELECT * FROM Tour")


con.close()