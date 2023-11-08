from backend.database.favorites import get_favorites_sql


def get_favorite_tours_from_user(user_id):
    list_of_favorited_tours = get_favorites_sql(user_id)
    return list_of_favorited_tours