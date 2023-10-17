from flask import Flask, render_template, url_for, redirect, request
import sqlite3

from backend.database.Tour import Tour_create
from backend.autentication import *
from backend.database import user


# definerer hvor templates ligger
application = Flask(__name__, template_folder='frontend/templates')


# våre paths:
@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        # con = sqlite3.connect('backend/database/database.db')
        # cur = connection.cursor()

        print(username, password)
        userlogin_is_valid = user.check_if_username_and_password_is_correct(
            username, password)

        # login_info_send_to_sql = "SELECT Username, Password FROM User WHERE Username = ? AND Password = ?"
        # cursor.execute(login_info_send_to_sql, (username, password))

        # login_output = cursor.fetchall()

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
    db.close()

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


@application.route('/checkbox_tour_delete', methods=['POST'])
def checkbox_tour_delete():
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_row')

        database = sqlite3.connect('backend/database/database.db')
        cursor = database.cursor()

        for ID in selected:
            cursor.execute('DELETE FROM Tour WHERE ID = ?', (ID,))
        database.commit()
        database.close()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    application.run(debug=True)
