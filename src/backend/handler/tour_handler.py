from backend.database.Tour import remove_bought_tour_sql, checkbox_function, Tour_create, list_tours, \
    list_of_user_bought_tours


def get_remove_bought_tour(id):
    return remove_bought_tour_sql(id)

def get_checkbox_to_lists(glob_id):
    return checkbox_function(glob_id)

def get_tour_create():
    return Tour_create()

def get_list_tours():
    return list_tours()

def get_list_of_user_bought_tours(global_id):
    return list_of_user_bought_tours(global_id)