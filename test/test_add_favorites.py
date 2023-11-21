from backend.database.user import id_if_provide_username, create_user
from backend.handler.favorite_handler import get_favorite_tours_from_user
from backend.database.Tour import checkbox_outcomes, Tour_create, Tour_get_id_from_title


def test_when_a_tour_is_favorited_then_number_of_favorites_for_the_user_is_increased():
    create_user("Luffy D Monkey", "123", "True")
    user_id_int = id_if_provide_username("Luffy D Monkey")[0]

    Tour_create("Find the onepiece", "description1010", "country1010", "location1010", "23-08-1990", 230, user_id_int)
    id_from_tour1 = Tour_get_id_from_title("Find the onepiece")

    fav_list1 = len(get_favorite_tours_from_user(user_id_int))
    checkbox_outcomes(user_id_int, id_from_tour1, "favorite")

    fav_list2 = len(get_favorite_tours_from_user(user_id_int))

    assert fav_list2 -1 == fav_list1
    assert fav_list2 - 2 != fav_list1
    assert fav_list2 + 1 != fav_list1
    assert fav_list2 + 2 != fav_list1
