import os
import sqlite3
pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()

def databasecreation():
    cur.execute('''CREATE TABLE IF NOT EXISTS User (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username CHAR(45),
            Password TEXT,
            Admin BOOLEAN
    );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Tour(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Description TEXT,
                Country TEXT,
                Location TEXT,
                Date DATETIME,
                Price DECIMAL(10, 2),
                CreatedBy 
    );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS TourBooked(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                User_ID INTEGER,
                Tour_ID INTEGER
    );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS TourFavorites(
                User_ID INTEGER,
                Tour_ID INTEGER
    );''')


databasecreation()
#cur.execute("ALTER TABLE TourBooked DROP COLUMN ID")
#cur.execute("ALTER TABLE TourBooked ADD ID INTEGER AUTOINCREMENT")
#cur.execute("ALTER TABLE TourBooked ADD COLUMN ID INTEGER PRIMARY KEY AUTOINCREMENT")


