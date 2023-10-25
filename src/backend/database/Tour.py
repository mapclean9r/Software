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
        cur.execute("SELECT Title,Description,Country,Location,Date FROM Tour")
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
        cur.execute("INSERT INTO TourBooked (User_ID, Tour_ID) VALUES (?, ?)", (Bruker_id, Tur_id,))
        con.commit()
    except:
        print("FEIL I TOUR_BOUGHT")


def Tour_who_bought(user):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("SELECT Title, Description, Country, Location, Date FROM Tour INNER JOIN TourBooked ON Tour.ID = TourBooked.Tour_ID WHERE TourBooked.User_ID = ?", (user,))
        userr = cur.fetchall()
        con.commit()
        return userr
    except:
        print("FEIL I TOUR_WHO_BOUGHT")


def Tour_delete(id):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("DELETE FROM Tour WHERE ID = ?",(id,))
    con.commit()

def Tour_who_bought_delete(user,tur_id):
    #try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute("DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?",(user,tur_id,))
        userr = cur.fetchall()
        con.commit()
        return userr
    #except:
    #    print("FEIL I TOUR_WHO_BOUGHT")


def Tour_favoritt(user,tur_id):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute('INSERT INTO TourFavorites (User_ID, Tour_ID) VALUES (?, ?)', (user, tur_id))
        con.commit()
    except:
        print("FEIL I TOUR FAVORITT")
