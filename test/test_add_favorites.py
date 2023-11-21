from backend.database.user import id_if_provide_username, create_user
from backend.handler.favorite_handler import get_favorite_tours_from_user
from backend.database.Tour import checkbox_outcomes, Tour_create, Tour_get_id_from_title, remove_user_from_list, \
    Tour_delete_if_title_is_provided, get_one_specified_favorite


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

    Tour_delete_if_title_is_provided("Find the onepiece")

    user_id = id_if_provide_username("Luffy D Monkey")[0]
    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")

def test_fav():
    create_user("Luffy D Monkey", "123", "True")
    user_id_int = id_if_provide_username("Luffy D Monkey")[0]

    Tour_create("SuperTour", "description1010", "country1010", "location1010", "23-08-1990", 230, user_id_int)
    id_from_tour1 = Tour_get_id_from_title("SuperTour")

    the_tour1 = get_one_specified_favorite(user_id_int, id_from_tour1[0])

    checkbox_outcomes(user_id_int, id_from_tour1, "favorite")

    the_tour2 = get_one_specified_favorite(user_id_int, id_from_tour1[0])
    assert the_tour1 != the_tour2
