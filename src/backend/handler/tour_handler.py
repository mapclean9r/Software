from flask import request
from backend.database.Tour import remove_bought_tour_sql, Tour_create, list_tours, \
    list_of_user_bought_tours, checkbox_outcomes, remove_favorite_tour_sql, remove_user_from_list


from backend.autentication.login import get_user_online
from backend.database.user import id_get
from backend.database.Tour import Tour_create, list_tours
from backend.database.favorites import remove_favorite_tour_sql
from backend.database.Tour_advanced import remove_bought_tour_sql, tours_that_i_have_created, \
    remove_tours_that_i_have_created, list_of_user_bought_tours, checkbox_outcomes, \
    list_tours_with_columns_title_and_number_of_people_attending



def get_remove_bought_tour(glob_id):
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_bought_tour')
        action = request.form.get('handle_action')
        return remove_bought_tour_sql(selected, action)


def get_remove_favorite_tour(id):
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_favorite_tour')
        action = request.form.get('handle_action')
        return remove_favorite_tour_sql(id, selected, action)


def get_who_bought(global_user_id):
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_who_bought')
        action = request.form.get('handle_action')
        return remove_tours_that_i_have_created(global_user_id, selected, action)


def get_checkbox_outcomes(global_id):
    selected = request.form.getlist('checkbox_row')
    action = request.form.get('handle_action')
    return checkbox_outcomes(global_id, selected, action)


def get_tour_create():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        country = request.form['Country']
        location = request.form['Location']
        date = request.form['Date']
        price = request.form['Price']
        created_by = id_get(get_user_online())
        print(created_by)
        return Tour_create(title, description, country, location, date, created_by,price)


def get_list_tours():
    return list_tours()


def get_remove_user():
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_userlist')
        action = request.form.get('handle_action')
        return remove_user_from_list(selected, action)


def get_Tour_who_bought(global_user_id):
    return tours_that_i_have_created(global_user_id)


def get_list_of_user_bought_tours(global_id):
    return list_of_user_bought_tours(global_id)


def get_list_tours_with_columns_title_and_number_of_people_attending():
    created_by = id_get(get_user_online())
    return list_tours_with_columns_title_and_number_of_people_attending(created_by)