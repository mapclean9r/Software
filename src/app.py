from flask import Flask, render_template, url_for, redirect, request
import sqlite3

from backend.database.Tour import *
from backend.autentication import *
from backend.database import user
from backend.autentication.login import UserLogin, get_user_online

# definerer hvor templates ligger
application = Flask(__name__, template_folder='frontend/templates')
application.secret_key = 'oursecretkey'

# våre paths:
global_user_id = 0


@application.route('/', methods=['GET', 'POST'])
def index():
    global global_user_id
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
        userlogin_is_valid = user.check_if_username_and_password_is_correct(
            username, password)
        print(f"Current user ID: {global_user_id}")

        list = Tour_get_all()
        list_of_bought_tours = Tour_who_bought(global_user_id)

        if userlogin_is_valid:
            print("You are logged in")
            return render_template('/homepage.html', list_of_tours=list, list_of_bought_tours=list_of_bought_tours)
        else:
            print("Something happend, you are not logged in")
            return render_template('/index.html')
    return render_template('/index.html')


@application.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        is_admin = request.form.get('admin_login', False)

        print(username, password, is_admin)

        if username == user.username_get:
            error_register = "Username exists."
            return render_template('/registrer.html', error_register=error_register)
        else:
            new_user = user.create_user(username, password, is_admin)
            return render_template('/registrer.html')
    return render_template('/registrer.html')


@application.route('/homepage')
def homepage():
    global global_user_id

    list = Tour_get_all()
    list_of_bought_tours = Tour_who_bought(global_user_id)



    return render_template('/homepage.html', list_of_tours=list, list_of_bought_tours=list_of_bought_tours)


@application.route('/create_a_tour', methods=['POST'])
def create_a_tour():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        country = request.form['Country']
        location = request.form['Location']
        date = request.form['Date']
        Tour_create(title, description, country, location, date)
    return redirect(url_for('homepage'))


@application.route('/checkbox_tour', methods=['POST'])
def checkbox_tour():
    if request.method == 'POST':
        global global_user_id
        selected = request.form.getlist('checkbox_row')
        action = request.form.get('handle_action')
        if action == 'delete':
            for ID in selected:
                print(global_user_id)
                print(ID)
                Tour_delete(ID)
        elif action == 'buy':
            for ID in selected:
                Tour_bought(ID,global_user_id)
        elif action == 'favorite':
            for ID in selected:
                Tour_favoritt(global_user_id,ID)
    return redirect(url_for('homepage'))

@application.route('/remove_bought_tour', methods=['POST'])
def remove_bought_tour():
    if request.method == 'POST':
        global global_user_id

        selected = request.form.getlist('checkbox_remove_bought_tour')
        action = request.form.get('handle_action')
        if action == 'delete':
            for ID in selected:
                print(global_user_id)
                print(ID)
                Tour_who_bought_delete(global_user_id,ID)
    return redirect(url_for('homepage'))


@application.route('/favorites')
def favorites():
    global global_user_id
    db = sqlite3.connect('src/backend/database/database.db')
    cursor = db.cursor()

    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()


    cursor.execute('''SELECT *
        FROM Tour
        INNER JOIN TourFavorites on Tour.ID = TourFavorites.Tour_ID
        WHERE TourFavorites.User_ID = ?''', (global_user_id,))


    list_of_favorited_tours = cursor.fetchall()

    return render_template('/favorites.html', list_of_tours=list, list_of_favorited_tours=list_of_favorited_tours)





if __name__ == '__main__':
    application.run(debug=True)
