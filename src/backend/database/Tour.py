import os
import sqlite3

pathing = os.path.dirname(__file__) + "/database.db"

def Tour_create(title, description, country, location, date, created_by):
    if len(title) <5 or len(title) >25:
        print("title needs to be between 5 and 25 characters")
        return 0
    elif len(description) <5 or len(description) > 200:
        print("description needs to be between 5 and 45 characters")
        return 0
    elif len(country) <1:
        print("You have not entered a Country in the tour")
        return 0
    elif len(location) <1:
        print("You have not entered a location in the tour")
        return 0
    elif len(date) <8:
        print("You have not entered a date in the tour")
        return 0
    else:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO Tour(Title,Description,Country,Location,Date,CreatedBy) VALUES(?,?,?,?,?,?)",
                        (title, description, country, location, date, created_by))
            con.commit()
            print("Tur laget")
            return 1
        except:
            print("FEIL I CREATE TOUR ")
            return 0


def tour_create_manual(ID, title, description, country, location, date, created_by):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Tour(Title,Description,Country,Location,Date,CreatedBy) VALUES(?,?,?,?,?,?)",
                    (ID, title, description, country, location, date, created_by))
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


def Tour_get_all_columns(id):
    try:
        con = sqlite3.connect(pathing)
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM Tour WHERE ID = ?", (id,))
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


def Tour_delete(id):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("DELETE FROM Tour WHERE ID = ?",(id,))
    con.commit()


def Tour_delete_if_title_is_provided(title):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("DELETE FROM Tour WHERE Title = ?",(title,))
    con.commit()


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


def Tour_bought(Tur_id, Bruker_id):
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

def Tour_remove(user,tur):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute('DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?', (user, tur,))
    con.commit()


def list_tours():
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()
    return list


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


def get_user_list():
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute("SELECT ID, Username FROM User")
    users = cursor.fetchall()

    return users


def remove_user_from_list(selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete' and selected:
        for id_selected in selected:
            cursor.execute("DELETE FROM User WHERE ID = ?", (id_selected,))
    database.commit()
    database.close()


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
    database.commit()
    database.close()
