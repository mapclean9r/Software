import os
import sqlite3

pathing = os.path.dirname(__file__) + "/database.db"


def Tour_create(Title, Description, Country, Location, Date):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUES(?,?,?,?,?)",
                    (Title, Description, Country, Location, Date,))
        con.commit()
        print("Tur laget")
        return 1
    except:
        print("FEIL I CREATE TOUR ")
        return 0


def Tour_get_all():
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("SELECT * FROM Tour")
        tur = cur.fetchall()
        return tur
    except:
        print("FEIL I TOUR_GET_ALL")


def Tour_get(id):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute(
            "SELECT Title,Description,Country,Location,Date FROM Tour WHERE ID = ?", (id,))
        tour = cur.fetchall()
        return tour
    except:
        print("FEIL I TOUR_GET")


def Tour_find_title(Title):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute(
            "SELECT Title,Description,Country,Location,Date FROM Tour WHERE Title = ?", (Title,))
        title = cur.fetchall()
        return title
    except:
        print("FEIL I TOUR_FIND_TITLE")


def Tour_filter_by_country(Country):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute(
            "SELECT Title,Description,Country,Location,Date FROM Tour WHERE Country = ?", (Country,))
        land = cur.fetchall()
        return land
    except:
        print("FEIL I TOUR_FILTER_BY_COUNTRY")

def Tour_bought(Tur_id,Bruker_id):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO TourBooked (User_ID, Tour_ID) VALUES (?, ?)", (Bruker_id, Tur_id,))
        con.commit()
    except:
        print("FEIL I TOUR_BOUGHT")


def Tour_who_bought(user):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("SELECT Title, Description, Country, Location, Date FROM Tour INNER JOIN TourBooked ON Tour.ID = TourBooked.Tour_ID WHERE TourBooked.User_ID = ?", (user,))
        userr = cur.fetchall()
        return userr
    except:
        print("FEIL I TOUR_WHO_BOUGHT")


def Tour_delete(id):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("DELETE FROM Tour WHERE ID = ?",(id,))
    con.commit()

def Tour_remove(user,tur):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute('DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?', (user, tur,))
    con.commit()

def get_booked_tour_from_current_user(global_key):
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_key,))

    list_of_bought_tours = cursor.fetchall()
    return list_of_bought_tours

def Tour_edit(Title, Description, Country, Location, Date, ID):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        cur.execute("UPDATE Tour SET Title = ?, Description = ?, Country = ?, Location = ?, Date = ? WHERE ID = ?", (Title, Description, Country, Location, Date, ID,))
        con.commit()
        print("Tur endret")
    except:
        print("FEIL I EDIT TOUR ")
