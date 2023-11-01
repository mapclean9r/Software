from flask import Flask, render_template, url_for, redirect

from backend.database.Tour import *
from backend.database import user
from backend.autentication.login import UserLogin
from backend.autentication.register import username_checker
from backend.handler.favorite_handler import get_favorite_tours_from_user
from backend.handler.tour_handler import get_remove_bought_tour, get_checkbox_to_lists

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
    t = UserLogin(username, password, False)
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        # Jeg gjør om fra tupple til int:
        global_user_id_in_tuple = user.get_id_if_provide_username(username)
        if global_user_id_in_tuple:
            global_user_id_int = int(global_user_id_in_tuple[0])
            global_user_id = global_user_id_int
        # Den er gjort om til int:

        t = UserLogin(username, password, False)

    return UserLogin.login_process(t)


@application.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    username_checker()
    return render_template('/registrer.html')

@application.route('/homepage')
def homepage():
    global global_user_id
    list_tours = get_list_tours()
    list_of_bought_tours = get_list_of_user_bought_tours(global_user_id)
    return render_template('/homepage.html', list_of_tours=list_tours, list_of_bought_tours=list_of_bought_tours)

@application.route('/create_a_tour', methods=['POST'])
def create_a_tour():
    if request.method == 'POST':
        Tour_create()
    return redirect(url_for('homepage'))

@application.route('/checkbox_tour', methods=['POST'])
def checkbox_tour():
    if request.method == 'POST':
        global global_user_id
        get_checkbox_to_lists(global_user_id)
    return redirect(url_for('homepage'))

@application.route('/remove_bought_tour', methods=['POST'])
def remove_bought_tour():
    if request.method == 'POST':
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

if __name__ == '__main__':
    application.run(debug=True)
