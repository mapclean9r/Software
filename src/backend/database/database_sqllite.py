import sqlite3
con = sqlite3.connect("src/backend/database/database.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Bruker (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username CHAR(45),
            Password TEXT   
);''')