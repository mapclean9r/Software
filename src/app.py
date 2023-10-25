from flask import Flask, render_template, url_for, redirect, request

from backend.database.Tour import *
from backend.database import user
from backend.autentication.login import get_user_online, UserLogin
from backend.autentication.login import login_checker
from backend.autentication.register import UserRegister

# definerer hvor templates ligger
application = Flask(__name__, template_folder='frontend/templates')
application.secret_key = 'oursecretkey'

# våre paths:
global_user_id = 0


@application.route('/', methods=['GET', 'POST'])
def index():
    global global_user_id
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        # Jeg gjør om fra tupple til int:
        global_user_id_in_tuple = user.get_id_if_provide_username(username)
        if global_user_id_in_tuple:
            global_user_id_int = int(global_user_id_in_tuple[0])
            global_user_id = global_user_id_int
            print(f"Current user ID: {global_user_id_int}")
        # Den er gjort om til int:

        t = UserLogin(username, password, False)
        UserLogin.username_check_to_database(t)
        UserLogin.password_check_to_database(t)
        UserLogin.admin_check_to_database(t)
        UserLogin.save_user_online(t)
        print(get_user_online(), "get_user_online")

        print(UserLogin.username_check_to_database(t))
        print(UserLogin.password_check_to_database(t))
        print(UserLogin.admin_check_to_database(t))


        print(username, password)


    return login_checker(username, password,
                         user.check_if_username_and_password_is_correct,
                         global_user_id)


@application.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        is_admin = request.form.get('admin_login', False)

        print(username, password, is_admin)

        UserRegister.username_checker(username, password, is_admin)

    return render_template('/registrer.html')



@application.route('/homepage')
def homepage():
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
    db.close()

    return render_template('/homepage.html', list_of_tours=list, list_of_bought_tours=list_of_bought_tours)


@application.route('/create_a_tour', methods=['POST'])
def create_a_tour():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        country = request.form['Country']
        location = request.form['Location']
        date = request.form['Date']

        # Jeg bruker "Tour_create-funksonen" som ligger i backend/database/tour.py
        Tour_create(title, description, country, location, date)

    return redirect(url_for('homepage'))


@application.route('/checkbox_tour', methods=['POST'])
def checkbox_tour():
    if request.method == 'POST':
        global global_user_id

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
                    'INSERT INTO TourBooked (User_ID, Tour_ID) VALUES (?, ?)', (global_user_id, ID))
        elif action == 'favorite':
            for ID in selected:
                cursor.execute(
                    'INSERT INTO TourFavorites (User_ID, Tour_ID) VALUES (?, ?)', (global_user_id, ID))
        database.commit()
        database.close()
    return redirect(url_for('homepage'))

@application.route('/remove_bought_tour', methods=['POST'])
def remove_bought_tour():
    if request.method == 'POST':
        global global_user_id

        selected = request.form.getlist('checkbox_bought_tour')
        action = request.form.get('handle_action')
        database = sqlite3.connect('backend/database/database.db')
        cursor = database.cursor()

        i = 0
        if action == 'delete':
                    for id in selected:
                        cursor.execute('DELETE FROM TourBooked WHERE User_ID = ? AND Tour_ID = ?', (global_user_id,id,))
                    i += 1
        database.commit()
        database.close()
    return redirect(url_for('homepage'))


@application.route('/favorites')
def favorites():
    global global_user_id
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()

    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()


    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourFavorites on Tour.ID = TourFavorites.Tour_ID
        WHERE TourFavorites.User_ID = ?''', (global_user_id,))


    list_of_favorited_tours = cursor.fetchall()
    db.close()

    return render_template('/favorites.html', list_of_tours=list, list_of_favorited_tours=list_of_favorited_tours)





if __name__ == '__main__':
    application.run(debug=True)
