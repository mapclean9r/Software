from backend.database.Tour import remove_bought_tour_sql


def get_remove_bought_tour(id):
    return remove_bought_tour_sql(id)