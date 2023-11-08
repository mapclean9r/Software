import sqlite3

from backend.database.Tour import pathing


def remove_favorite_tour_sql(user_id_global, selected, action):
    database = sqlite3.connect(pathing)
    cursor = database.cursor()
    if action == 'delete':
        for id in selected:
            cursor.execute('DELETE FROM TourFavorites WHERE User_ID = ? AND Tour_ID = ?', (user_id_global, id,))
    database.commit()
    database.close()


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
