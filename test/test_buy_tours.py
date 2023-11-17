from backend.database.Tour import tour_create_manual, Tour_bought, list_of_user_bought_tours, Tour_get_id_from_title, \
    Tour_create
from backend.database.Tour_advanced import remove_tours_that_i_have_created
from backend.database.user import id_if_provide_username, create_user
from backend.database.Tour import checkbox_outcomes, remove_bought_tour_sql



def test_number_of_bought_tours_is_updated_when_buying_a_tour():
    create_user('testUser', '123', 'True')
    user_id = id_if_provide_username("testUser")

    number_of_tours_before_buying_tours = len(list_of_user_bought_tours(user_id))

    Tour_create("my title test1", "description1010", "country1010", "location1010", "23-08-1990", 233, user_id)
    id_from_tour = Tour_get_id_from_title("my title test1")
    checkbox_outcomes(user_id, id_from_tour, "buy")


    number_of_tours_after_buying = len(list_of_user_bought_tours(user_id))
    remove_bought_tour_sql(user_id, id_from_tour, "delete")


    remove_tours_that_i_have_created(user_id, id_from_tour, 'delete')

    assert number_of_tours_after_buying != number_of_tours_before_buying_tours
    assert number_of_tours_after_buying == number_of_tours_before_buying_tours +1
    assert number_of_tours_after_buying != number_of_tours_before_buying_tours + 2


