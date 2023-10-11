from flask import Flask, render_template, request, Blueprint

our_views = Blueprint('views', __name__)


@our_views.route('/', methods=['GET', 'POST'])
def display_index():
    data = request.form
    print(data)
    # if request.method == 'GET':

    # connection = sqlite3.connect('..backend/database/database.db')
    # cursor = connection.cursor()

    return render_template('index.html')


@application.route('/homepage', methods=['GET', 'POST'])
def display_homepage():
    # if request.method == 'GET':

    # connection = sqlite3.connect('..backend/database/database.db')
    # cursor = connection.cursor()

    return render_template('homepage.html')
