from flask import Flask, render_template, url_for, redirect

from backend.handler.auth_handler import get_username_checker, get_start_login_process
from backend.handler.favorite_handler import get_favorite_tours_from_user
from backend.handler.tour_handler import *

application = Flask(__name__, template_folder='frontend/templates')

global_user_id = 0

@application.route('/', methods=['GET', 'POST'])
def index():
    return get_start_login_process()

@application.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    get_username_checker()
    return render_template('/registrer.html')

@application.route('/homepage')
def homepage():
    global global_user_id
    list_tours = get_list_tours()
    list_of_bought_tours = get_list_of_user_bought_tours(global_user_id)
    return render_template('/homepage.html', list_of_tours=list_tours, list_of_bought_tours=list_of_bought_tours)

@application.route('/create_a_tour', methods=['POST'])
def create_a_tour():
    get_tour_create()
    return redirect(url_for('homepage'))

@application.route('/checkbox_tour', methods=['POST'])
def checkbox_tour():
    global global_user_id
    get_checkbox_to_lists(global_user_id)
    get_checkbox_outcomes(global_user_id)
    return redirect(url_for('homepage'))

@application.route('/remove_bought_tour', methods=['POST'])
def remove_bought_tour():
    global global_user_id
    get_remove_bought_tour(global_user_id)
    return redirect(url_for('homepage'))

@application.route('/favorites')
def favorites():
    global global_user_id
    list_of_favorited_tours = get_favorite_tours_from_user(global_user_id)
    return render_template('/favorites.html', list_of_favorited_tours=list_of_favorited_tours)

@application.route('/who_bought')
def who_bought():
    return render_template('/who_bought.html')

@application.route('/remove_favorite_tour', methods=['POST'])
def remove_favorite_tour():
    if request.method == 'POST':
        global global_user_id

        selected = request.form.getlist('checkbox_favorite_tour')
        action = request.form.get('handle_action')
        database = sqlite3.connect('backend/database/database.db')
        cursor = database.cursor()


        if action == 'delete':
                    for id in selected:
                        cursor.execute('DELETE FROM TourFavorites WHERE User_ID = ? AND Tour_ID = ?', (global_user_id,id,))

        database.commit()
        database.close()
    return redirect(url_for('favorites'))


def get_user_list():
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute("SELECT Username FROM User")
    users = cursor.fetchall()
    db.close()

    return [user[0] for user in users]


@application.route('/adminpage')
def adminpage():
    global global_user_id
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()

    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()

    # list_of_bought_tours = Tour_who_bought(global_user_id)

    cursor.execute('''SELECT *
    FROM Tour
    INNER JOIN TourBooked on Tour.ID = TourBooked.Tour_ID
    WHERE TourBooked.User_ID = ?''', (global_user_id,))

    list_of_bought_tours = cursor.fetchall()
    list_of_users = get_user_list()

    db.close()


    return render_template('/adminpage.html', list_of_tours=list, list_of_bought_tours=list_of_bought_tours, users=list_of_users)


@application.route('/users')
def users():
    list_of_users = get_user_list()

    return render_template('/users.html', users=list_of_users)



if __name__ == '__main__':
    application.run(debug=True)
