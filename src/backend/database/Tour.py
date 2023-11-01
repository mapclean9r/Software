import os
import sqlite3

from flask import request


pathing = os.path.dirname(__file__) + "/database.db"


def Tour_create():
    title = request.form['Title']
    description = request.form['Description']
    country = request.form['Country']
    location = request.form['Location']
    date = request.form['Date']

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

def get_booked_tour_from_current_user(global_key):
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_key,))

    list_of_bought_tours = cursor.fetchall()
    return list_of_bought_tours


def get_favorites_sql(id_user):
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()

    cursor.execute("SELECT * from Tour")

    cursor.execute('''SELECT *
            FROM Tour
            INNER JOIN TourFavorites on Tour.ID = TourFavorites.Tour_ID
            WHERE TourFavorites.User_ID = ?''', (id_user,))

    list_of_favorited_tours = cursor.fetchall()
    db.close()
    return list_of_favorited_tours


def remove_bought_tour_sql(user_id_global):
    selected = request.form.getlist('checkbox_bought_tour')
    action = request.form.get('handle_action')
    database = sqlite3.connect('backend/database/database.db')
    cursor = database.cursor()
    if action == 'delete':
        for id_user in selected:
            cursor.execute('DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?', (user_id_global, id_user,))
    database.commit()
    database.close()


def checkbox_function(glob_id):
    selected = request.form.getlist('checkbox_row')
    action = request.form.get('handle_action')
    database = sqlite3.connect('backend/database/database.db')
    cursor = database.cursor()

    if action == 'delete':
        for ID in selected:
            cursor.execute('DELETE FROM Tour WHERE ID = ?', (ID,))
    elif action == 'buy':
        for ID in selected:
            cursor.execute(
                'INSERT INTO TourBooked (User_ID, Tour_ID) VALUES (?, ?)', (glob_id, ID))
    elif action == 'favorite':
        for ID in selected:
            cursor.execute(
                'INSERT INTO TourFavorites (User_ID, Tour_ID) VALUES (?, ?)', (glob_id, ID))
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
