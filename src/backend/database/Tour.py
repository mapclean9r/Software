import os
import sqlite3

from flask import redirect, url_for
from backend.autentication.login import get_user_online_is_admin

pathing = os.path.dirname(__file__) + "/database.db"


def Tour_create(title, description, country, location, date):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Tour(Title,Description,Country,Location,Date) VALUES(?,?,?,?,?)",
                    (title, description, country, location, date,))
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
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_key,))

    list_of_bought_tours = cursor.fetchall()
    return list_of_bought_tours


def get_favorites_sql(id_user):
    db = sqlite3.connect(pathing)
    cursor = db.cursor()

    cursor.execute("SELECT * from Tour")

    cursor.execute('''SELECT *
            FROM Tour
            INNER JOIN TourFavorites on Tour.ID = TourFavorites.Tour_ID
            WHERE TourFavorites.User_ID = ?''', (id_user,))

    list_of_favorited_tours = cursor.fetchall()
    db.close()
    return list_of_favorited_tours


def remove_bought_tour_sql(user_id_global, selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for id_user in selected:
            cursor.execute('DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?', (user_id_global, id_user,))
    database.commit()
    database.close()


def remove_favorite_tour_sql(user_id_global, selected, action):
    database = sqlite3.connect('backend/database/database.db')
    cursor = database.cursor()
    if action == 'delete':
        for id in selected:
            cursor.execute('DELETE FROM TourFavorites WHERE User_ID = ? AND Tour_ID = ?', (user_id_global, id,))
    database.commit()
    database.close()


def list_of_user_bought_tours(global_id):
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_id,))
    list_of_bought_tours = cursor.fetchall()
    db.close()
    return list_of_bought_tours


def list_tours():
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()
    return list

def get_user_list():
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute("SELECT Username FROM User")
    users = cursor.fetchall()

    #db.close()
    #return [user[0] for user in users]
    return users

def Tour_edit(Title, Description, Country, Location, Date, ID):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        cur.execute("UPDATE Tour SET Title = ?, Description = ?, Country = ?, Location = ?, Date = ? WHERE ID = ?", (Title, Description, Country, Location, Date, ID,))
        con.commit()
        print("Tur endret")
    except:
        print("FEIL I EDIT TOUR ")

def checkbox_outcomes(global_id, selected, action):
    database = sqlite3.connect('backend/database/database.db')
    cursor = database.cursor()
    if action == 'delete':
        for ID in selected:
            Tour_delete(ID)
    elif action == 'buy':
        for ID in selected:
            Tour_bought(ID, global_id)
    elif action == 'favorite':
        for ID in selected:
            cursor.execute(
                'INSERT INTO TourFavorites (User_ID, Tour_ID) VALUES (?, ?)', (global_id, ID))
    elif action == 'admin':
        if get_user_online_is_admin():
            return redirect(url_for('adminpage'))
    elif action == 'users':
        return redirect(url_for('users'))
    database.commit()
    database.close()
