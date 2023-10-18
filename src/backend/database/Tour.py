import os
import sqlite3

pathing = os.path.dirname(__file__) + "/database.db"
con = sqlite3.connect(pathing)
cur = con.cursor()


def Tour_create(Title, Description, Country, Location, Date):
    try:
        cur.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUES(?,?,?,?,?)",(Title,Description,Country,Location,Date,))
        con.commit()
        print("Tur laget")
        return 1
    except:
        print("FEIL I CREATE TOUR ")
        return 0



def Tour_get_all():
    try:
        cur.execute("SELECT * FROM Tour")
        tur = cur.fetchall()
        return tur
    except:
        print("FEIL I TOUR_GET_ALL")

def Tour_get(id):
    try:
        cur.execute("SELECT Title,Description,Country,Location,Date FROM Tour WHERE ID = ?", (id,))
        tour = cur.fetchall()
        return tour
    except:
        print("FEIL I TOUR_GET")

def Tour_find_title(Title):
    try:
        cur.execute("SELECT Title,Description,Country,Location,Date FROM Tour WHERE Title = ?",(Title,))
        title = cur.fetchall()
        return title
    except:
        print("FEIL I TOUR_FIND_TITLE")

def Tour_filter_by_country(Country):
    try:
        cur.execute("SELECT Title,Description,Country,Location,Date FROM Tour WHERE Country = ?",(Country,))
        land = cur.fetchall()
        return land
    except:
        print("FEIL I TOUR_FILTER_BY_COUNTRY")

def Tour_bought(Tur_id,Bruker_id):
    #try:
        cur.execute("INSERT INTO TourBooked (User_ID, Tour_ID) VALUES (?, ?)",(Bruker_id,Tur_id,))
        con.commit()
    #except:
    #    print("IKKE FERDIG SÅ FEIL I TOUR_BOUGHT")

def Tour_who_bought(user):
    try:
        cur.execute("SELECT Title, Description, Country, Location, Date FROM Tour INNER JOIN TourBooked ON Tour.ID = TourBooked.Tour_ID WHERE TourBooked.User_ID = ?", (user,))
        userr = cur.fetchall()
        return userr
    except:
        print("FEIL I TOUR_WHO_BOUGHT")




