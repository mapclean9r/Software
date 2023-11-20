from backend.database.Tour import tour_create_manual, Tour_create, Tour_get_id_from_title
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
    print(n_of_created_tours)
    print(n_of_created_tours2)

    assert n_of_created_tours != n_of_created_tours2
    assert n_of_created_tours2 + 1 == n_of_created_tours
    assert n_of_created_tours - 2 != n_of_created_tours2
    assert n_of_created_tours + 5 != n_of_created_tours2

    assert Tour_get_id_from_title("title1010") != True

    #remove_user_from_list(user_id, "delete")