from flask import Flask, render_template, url_for, redirect, request
import sqlite3

from backend.database.Tour import Tour_create
from backend.autentication import *
from backend.database import user


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

        # global_user_id = 0

        # Jeg gjør om fra tupple til int:
        global_user_id_in_tuple = user.get_id_if_provide_username(username)
        if global_user_id_in_tuple:
            global_user_id_int = int(global_user_id_in_tuple[0])
            global_user_id = global_user_id_int
            print(f"Current user ID: {global_user_id_int}")
        # Den er gjort om til int:

        print(username, password)
        userlogin_is_valid = user.check_if_username_and_password_is_correct(
            username, password)
        print(f"Current user ID: {global_user_id}")

        if userlogin_is_valid:
            print("You are logged in")
            return render_template('/homepage.html')
        else:
            print("Something happend, you are not logged in")
            return render_template('/index.html')
    return render_template('/index.html')


@application.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    if request.method == 'POST':
        connection = sqlite3.connect('backend/database/database.db')
        cursor = connection.cursor()
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
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()

    cursor.execute("SELECT * from Tour")
    list = cursor.fetchall()

    # cur.execute("SELECT ID FROM User WHERE Username = ?", (Username,))
    # list_of_bought_tours = cursor.fetchall()
    # db.close()

    return render_template('/homepage.html', list_of_tours=list)


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
        database.commit()
        database.close()
    return redirect(url_for('homepage'))


@application.route('/favorites')
def favorites():

    return render_template('/favorites.html')


if __name__ == '__main__':
    application.run(debug=True)
