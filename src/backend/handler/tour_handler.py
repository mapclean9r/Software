from flask import request

from backend.autentication.login import get_user_online
from backend.database.Tour import Tour_create, list_tours
from backend.database.favorites import remove_favorite_tour_sql
from backend.database.Tour_advanced import remove_bought_tour_sql, tours_that_i_have_created, \
    remove_tours_that_i_have_created, list_of_user_bought_tours, checkbox_outcomes, \
    list_tours_with_columns_title_and_number_of_people_attending
from backend.handler.auth_handler import get_id_from_username


def get_remove_bought_tour(id):
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_bought_tour')
        action = request.form.get('handle_action')
        return remove_bought_tour_sql(id, selected, action)


def get_remove_favorite_tour(id):
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_favorite_tour')
        action = request.form.get('handle_action')
        return remove_favorite_tour_sql(id, selected, action)

def get_who_bought():
    if request.method == 'POST':
        selected = request.form.getlist('checkbox_who_bought')
        action = request.form.get('handle_action')
        return remove_tours_that_i_have_created(selected, action)

def get_checkbox_outcomes(gloal_id):
    selected = request.form.getlist('checkbox_row')
    action = request.form.get('handle_action')
    return checkbox_outcomes(gloal_id, selected, action)

def get_tour_create():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        country = request.form['Country']
        location = request.form['Location']
        date = request.form['Date']
        created_by = get_user_online()
        print(created_by)
        return Tour_create(title, description, country, location, date, created_by)

def get_list_tours():
    return list_tours()

def get_Tour_who_bought():
    created_by = get_user_online()
    return tours_that_i_have_created(created_by)

def get_list_of_user_bought_tours(global_id):
    return list_of_user_bought_tours(global_id)

def get_list_tours_with_columns_title_and_number_of_people_attending(my_id):
    return list_tours_with_columns_title_and_number_of_people_attending(my_id)