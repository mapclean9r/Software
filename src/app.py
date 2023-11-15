#from backend.autentication.admin import get_logging
from backend.database.Tour import get_user_list
from backend.handler.auth_handler import get_id_if_provide_username
from backend.handler.auth_handler import get_username_checker, get_start_login_process
from backend.handler.favorite_handler import get_favorite_tours_from_user
from backend.handler.tour_handler import *
from backend.autentication.login import *

application = Flask(__name__, template_folder='frontend/templates')

global_user_id = 0


@application.route('/', methods=['GET', 'POST'])
def index():
    return get_start_login_process()


@application.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    global global_user_id
    get_username_checker()
    global_user_id = get_id_if_provide_username()
    return render_template('/registrer.html')


@application.route('/homepage')
def homepage():
    global global_user_id

    list_tours = get_list_tours()
    list_of_bought_tours = get_list_of_user_bought_tours(global_user_id)
    is_admin = get_user_online_is_admin

    return render_template('/homepage.html', is_admin=is_admin,  list_of_tours=list_tours,
                           list_of_bought_tours=list_of_bought_tours)


@application.route('/create_a_tour', methods=['POST'])
def create_a_tour():
    get_tour_create()
    return redirect(url_for('homepage'))


@application.route('/checkbox_tour', methods=['POST'])
def checkbox_tour():
    global global_user_id
    get_checkbox_outcomes(global_user_id)
    return redirect(url_for('homepage'))


@application.route('/remove_bought_tour', methods=['POST'])
def remove_bought_tour():
    get_remove_bought_tour()
    return redirect(url_for('homepage'))


@application.route('/favorites')
def favorites():
    global global_user_id
    list_of_favorited_tours = get_favorite_tours_from_user(global_user_id)
    is_admin = get_user_online_is_admin

    return render_template('/favorites.html', list_of_favorited_tours=list_of_favorited_tours, is_admin=is_admin)


@application.route('/my_created_tours')
def my_created_tours():
    global global_user_id

    global_user_id = get_id_if_provide_username()
    list_who_bought_my_tours = get_Tour_who_bought()
    print(list_who_bought_my_tours)
    list_people_attending = get_list_tours_with_columns_title_and_number_of_people_attending()
    is_admin = get_user_online_is_admin

    return render_template('/my_created_tours.html',
                           list_my_bought_tours=list_who_bought_my_tours,
                           list_people_attending_my_tours=list_people_attending, is_admin=is_admin)


@application.route('/remove_my_created_tours', methods=['POST'])
def remove_who_bought():
    global global_user_id
    get_who_bought()
    return redirect(url_for('my_created_tours'))


@application.route('/remove_favorite_tour', methods=['POST'])
def remove_favorite_tour():
    global global_user_id
    get_remove_favorite_tour(global_user_id)
    return redirect(url_for('favorites'))


@application.route('/adminpage')
def adminpage():
    global global_user_id
    list_tours = get_list_tours()
    list_of_bought_tours = get_list_of_user_bought_tours(global_user_id)
    list_of_users = get_user_list()
    is_admin = get_user_online_is_admin

    return render_template('/adminpage.html', is_admin=is_admin, list_of_tours=list_tours, list_of_bought_tours=list_of_bought_tours, users=list_of_users)


@application.route('/admin_checkbox_tour', methods=['POST'])
def admin_checkbox_tour():
    get_checkbox_outcomes(global_user_id)
    return redirect(url_for('adminpage'))


@application.route('/admin_remove_bought_tour', methods=['POST'])
def admin_remove_bought_tour():
    get_remove_bought_tour()
    return redirect(url_for('adminpage'))


@application.route('/admin_create_a_tour', methods=['POST'])
def admin_create_a_tour():
    get_tour_create()
    return redirect(url_for('adminpage'))


@application.route('/users')
def users():
    list_of_users = get_user_list()
    is_admin = get_user_online_is_admin
    #log_of_users = get_logging()

    return render_template('/users.html', users=list_of_users, is_admin=is_admin)


@application.route('/remove_user', methods=['POST'])
def remove_user():
    global global_user_id
    get_remove_user()
    return redirect(url_for('users', user_id=global_user_id))


@application.route('/support_senter')
def support_senter():
    is_admin = get_user_online_is_admin
    return render_template('/support_senter.html', is_admin=is_admin)


if __name__ == '__main__':
    application.run(debug=True)
