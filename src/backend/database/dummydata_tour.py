import sqlite3

conn = sqlite3.connect('src/backend/database/database.db')
cursor = conn.cursor()

tours = [
    ("Tur 1", "Beskrivelse 1", "Norge", "Oslo", "2023-10-15"),
    ("Tur 2", "Beskrivelse 2", "Sverige", "Stockholm", "2023-10-16"),
    ("Tur 3", "Beskrivelse 3", "Danmark", "København", "2023-10-17")
]

for tour in tours:
    cursor.execute(
        "INSERT INTO Tour (Title, Description, Country, Location, Date) VALUES (?, ?, ?, ?, ?)", tour)

conn.commit()
conn.close()
