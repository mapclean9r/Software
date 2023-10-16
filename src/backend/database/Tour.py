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
    

def Tour_get_all():
    try:
        con.execute("SELECT * FROM Tour")
    except:
        print("FEIL I TOUR_GET_ALL")

def Tour_get(id):
    try:
        con.execute("SELECT Title,Description,Country,Location,Date FROM Tour WHERE ID = ?",(id,))
    except:
        print("FEIL I TOUR_GET")

def Tour_find_title(Title):
    try:
        con.execute("SELECT Title,Description,Country,Location,Date FROM Tour WHERE Title = ?",(Title,))
    except:
        print("FEIL I TOUR_FIND_TITLE")

def Tour_filter_by_country(Country):
    try:
        con.execute("SELECT Title,Description,Country,Location,Date FROM Tour WHERE Country = ?",(Country,))
    except:
        print("FEIL I TOUR_FILTER_BY_COUNTRY")

def Tour_bought(Tur_id,Bruker_id):
    try:
        con.execute("INSERT INTO TourBooked(User_ID,Tour_ID VALUES(?,?))",(Tur_id,Bruker_id))
    except:
        print("IKKE FERDIG SÅ FEIL I TOUR_BOUGHT")
    


