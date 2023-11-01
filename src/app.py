from flask import Flask, render_template, url_for, redirect

from backend.database.Tour import *

from backend.autentication.login import login_proc
from backend.handler.auth_handler import get_username_checker
from backend.handler.favorite_handler import get_favorite_tours_from_user
from backend.handler.tour_handler import *

application = Flask(__name__, template_folder='frontend/templates')

global_user_id = 0

@application.route('/', methods=['GET', 'POST'])
def index():
    return login_proc()

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
    if request.method == 'POST':
        global global_user_id
        get_remove_bought_tour(global_user_id)
    return redirect(url_for('homepage'))

@application.route('/favorites')
def favorites():
    global global_user_id
    list_of_favorited_tours = get_favorite_tours_from_user(global_user_id)
    return render_template('/favorites.html', list_of_favorited_tours=list_of_favorited_tours)


if __name__ == '__main__':
    application.run(debug=True)
