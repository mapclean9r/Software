import os
import sqlite3

pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()
'''
con = sqlite3.connect("src/backend/database/database.db")
cur = con.cursor()
'''

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
                Date DATETIME
    );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS TourBooked(
                User_ID INTEGER,
                Tour_ID INTEGER
    );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS TourFavorites(
                User_ID INTEGER,
                Tour_ID INTEGER
    );''')


databasecreation()