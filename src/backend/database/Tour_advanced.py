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


def remove_bought_tour_sql(selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for ID in selected:
            print(ID)
            cursor.execute('DELETE FROM TourBooked WHERE ID = ?', (ID,))
    database.commit()
    database.close()



def tours_that_i_have_created(user_ID):
    con = sqlite3.connect(pathing)
    cur = con.cursor()
    cur.execute("SELECT * FROM Tour WHERE CreatedBy = ?",(user_ID,))
    list_tours = cur.fetchall()
    print(list_tours)
    return list_tours


def remove_tours_that_i_have_created(global_user_id, selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for id in selected:
            #if global_user_id == cursor.execute("SELECT CreatedBy FROM Tour WHERE CreatedBy = ?",(global_user_id,)):
            cursor.execute("DELETE FROM Tour WHERE ID = ? AND CreatedBy = ?",(id, global_user_id))
    database.commit()
    database.close()


def list_of_user_bought_tours(global_id):
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute('''SELECT TourBooked.ID, Tour.Title, Tour.Description, Tour.Country, Tour.Location, Tour.Date, Tour.Price
        FROM Tour
        INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
        WHERE TourBooked.User_ID = ?
        ORDER BY Tour.Title''', (global_id,))
    list_of_bought_tours = cursor.fetchall()
    db.close()
    return list_of_bought_tours


def checkbox_outcomes(global_id, selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for ID in selected:
            #if Tour_get_all_columns(global_id)[6] == global_id:
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

def list_tours_with_columns_title_and_number_of_people_attending(created_by):
    db = sqlite3.connect(pathing)
    cursor = db.cursor()
    cursor.execute('''
            SELECT Tour.Title, COUNT(TourBooked.User_ID) AS Attending
            FROM Tour
            LEFT JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
            WHERE Tour.CreatedBy = ?
            GROUP BY Tour.Title
            ORDER BY Attending DESC
            ''', (created_by,))
    list_people_attending_tours = cursor.fetchall()
    db.close()
    return list_people_attending_tours