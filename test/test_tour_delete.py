from backend.database.Tour import Tour_create, Tour_get_id_from_title, remove_user_from_list
from backend.database.Tour_advanced import remove_tours_that_i_have_created, tours_that_i_have_created
from backend.database.user import id_if_provide_username, create_user

def test_a_user_can_delete_a_tour_that_he_has_created():

    create_user("testbruker40457", "123", "True")
    user_id = id_if_provide_username("testbruker40457")[0]

    Tour_create("title1010", "description1010", "country1010", "location1010", "23-08-1990", user_id, 200)
    n_of_created_tours = len(tours_that_i_have_created(user_id))

    id_from_tour = Tour_get_id_from_title("title1010")

    remove_tours_that_i_have_created(user_id, id_from_tour, 'delete')
    n_of_created_tours2 = len(tours_that_i_have_created(user_id))

    assert n_of_created_tours != n_of_created_tours2
    assert n_of_created_tours2 + 1 == n_of_created_tours
    assert n_of_created_tours - 2 != n_of_created_tours2
    assert n_of_created_tours + 5 != n_of_created_tours2

    assert Tour_get_id_from_title("title1010") != True

    user_to_remove = (user_id,)
    remove_user_from_list(user_to_remove, "delete")

def test_can_not_find_title_of_a_deleted_tour():

    create_user("GregerHansenOlav", "123", "True")
    user_id_int = id_if_provide_username("GregerHansenOlav")[0]

    Tour_create("test_title very cool", "description", "Country", "Location", "2020-01-01", user_id_int, 100)
    id_from_tour = Tour_get_id_from_title("test_title very cool")

    remove_tours_that_i_have_created(user_id_int, id_from_tour, 'delete')
    id_from_tour2 = Tour_get_id_from_title("test_title very cool")

    assert id_from_tour2 == None
    user_to_remove = (user_id_int,)
    remove_user_from_list(user_to_remove, "delete")
