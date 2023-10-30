from flask import Flask, render_template, url_for
# Denne filen er ikke i bruk per dags dato. pather er definert direkte i app.py

our_views = Blueprint('views', __name__)


@our_views.route('/', methods=['GET', 'POST'])
def display_index():

    return render_template('frontend/routes/index.html')


@application.route('/homepage', methods=['GET', 'POST'])
def display_homepage():

    return render_template('frontend/routes/homepage.html')


@application.route('/registrer')
def display_registrer_page():

    return render_template('frontend/routes/registrer.html')
