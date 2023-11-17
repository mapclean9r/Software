from backend.database.Tour import tour_create_manual, Tour_bought, list_of_user_bought_tours, Tour_get_id_from_title, \
    Tour_create
from backend.database.Tour_advanced import remove_tours_that_i_have_created
from backend.database.user import id_if_provide_username, create_user
from backend.database.Tour import checkbox_outcomes, remove_bought_tour_sql


def test_number_of_bought_tours_is_updated_when_removing_a_bought_tour():
    create_user('testUsererer', '123', 'True')
    user_id = id_if_provide_username("testUsererer")

    Tour_create("my title test1rrrrr", "description1010", "country1010", "location1010", "23-08-1990", 230, user_id)
    id_from_tour1 = Tour_get_id_from_title("my title test1rrrrr")

    Tour_create("myee333 title test1", "description1010", "country1010", "location10103", "23-08-1991", 232, user_id)
    id_from_tour2 = Tour_get_id_from_title("myee333 title test1")

    checkbox_outcomes(user_id, id_from_tour1, "buy")
    checkbox_outcomes(user_id, id_from_tour2, "buy")

    first_list = len(list_of_user_bought_tours(user_id))

    checkbox_outcomes(user_id, id_from_tour1, "delete")

    number_of_tours_after_buying = len(list_of_user_bought_tours(user_id))

    checkbox_outcomes(user_id, id_from_tour2, 'delete')

    assert first_list != number_of_tours_after_buying
    assert first_list - 1 == number_of_tours_after_buying
    assert first_list - 2 != number_of_tours_after_buying
    assert first_list + 1 != number_of_tours_after_buying
