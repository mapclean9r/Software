from flask import Flask, render_template, url_for, redirect, request
import sqlite3
from backend.database import Tour

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

        database = sqlite3.connect('backend/database/database.db')
        cursor = database.cursor()

        # TODO funksjonen som er kommentert ut under burde heller brukes, da får vi separert ut funksjonalitet i flere filer.
        # Tour.Tour_create(title, description, country, location, date)
        cursor.execute('INSERT INTO Tour (Title, Description, Country, Location, Date) VALUES (?, ?, ?, ?, ?)', (
            title, description, country, location, date))
        database.commit()
        database.close()
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
