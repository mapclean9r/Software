from backend.database.Tour import remove_bought_tour_sql, checkbox_function


def get_remove_bought_tour(id):
    return remove_bought_tour_sql(id)

def get_checkbox_to_lists(glob_id):
    return checkbox_function(glob_id)