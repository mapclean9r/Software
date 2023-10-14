from flask import Flask, render_template, url_for, redirect, request
import sqlite3

# definerer hvor templates ligger
application = Flask(__name__, template_folder='frontend/templates')


# våre paths:


@application.route('/')
def index():

    return render_template('/index.html')


@application.route('/registrer')
def registrer_page():

    return render_template('/registrer.html')


@application.route('/homepage')
def homepage():
    db = sqlite3.connect('backend/database/database.db')
    cursor = db.cursor()
    cursor.execute("SELECT * from Tour")
    list_med_turer = cursor.fetchall()
    db.close()

    return render_template('/homepage.html', turer=list_med_turer)


@application.route('/create_a_tour', methods=['POST'])
def create_a_tour():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        country = request.form['Country']
        location = request.form['Location']
        date = request.form['Date']

        database = sqlite3.connect('backend/database/database.db')
        cursor = database.cursor()

        cursor.execute('INSERT INTO Tour (Title, Description, Country, Location, Date) VALUES (?, ?, ?, ?, ?)', (
            title, description, country, location, date))
        database.commit()
        database.close()
    return redirect(url_for('homepage'))


@application.route('/delete_a_tour', methods=['POST'])
def delete_a_tour():
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    application.run(debug=True)
