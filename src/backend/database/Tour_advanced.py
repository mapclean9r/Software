import sqlite3

from flask import redirect, url_for

from backend.autentication.login import get_user_online_is_admin
from backend.database.Tour import pathing, Tour_delete, Tour_bought


def get_booked_tour_from_current_user(global_key):
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_key,))

    list_of_bought_tours = cursor.fetchall()
    return list_of_bought_tours


def remove_bought_tour_sql(user_id_global, selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for id_user in selected:
            cursor.execute('DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?', (user_id_global, id_user,))
    database.commit()
    database.close()


def tours_that_i_have_created(user_name):
    con = sqlite3.connect(pathing)
    cur = con.cursor()

    cur.execute("SELECT * FROM Tour WHERE CreatedBy = ?",(user_name,))
    list_tours = cur.fetchall()
    return list_tours


def remove_tours_that_i_have_created(selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for id in selected:
            cursor.execute("DELETE FROM Tour WHERE ID = ?",(id,))
    database.commit()
    database.close()


def list_of_user_bought_tours(global_id):
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?''', (global_id,))
    list_of_bought_tours = cursor.fetchall()
    db.close()
    return list_of_bought_tours


def checkbox_outcomes(global_id, selected, action):
    database = sqlite3.connect(pathing)
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

def list_tours_with_columns_title_and_number_of_people_attending(user_id):
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute('''
            SELECT Tour.Title, COUNT(TourBooked.Tour_ID) AS Attending
            FROM Tour
            LEFT JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
            WHERE TourBooked.User_ID = ?
            GROUP BY Tour.Title
            ''', (user_id,))
    list_people_attending_tours = cursor.fetchall()
    db.close()
    return list_people_attending_tours