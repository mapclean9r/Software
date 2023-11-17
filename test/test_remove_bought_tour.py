from backend.database.Tour import tour_create_manual, Tour_bought, list_of_user_bought_tours
from backend.database.Tour_advanced import remove_tours_that_i_have_created
from backend.database.user import id_if_provide_username, create_user
from backend.database.Tour import checkbox_outcomes, remove_bought_tour_sql


def test_number_of_bought_tours_is_updated_when_removing_a_bought_tour():
    create_user('testUser', '123', 'True')
    user_id = id_if_provide_username("testUser")[0]

    tour_create_manual(800, "my title test1", "description1010", "country1010", "location1010", "23-08-1990", user_id)
    checkbox_outcomes(user_id, (800,), "buy")

    number_of_tours_before_buying_tours = len(list_of_user_bought_tours(user_id))

    remove_bought_tour_sql(user_id,(800,), "delete")
    number_of_tours_after_buying = len(list_of_user_bought_tours(user_id))

    remove_tours_that_i_have_created(user_id, (800,), 'delete')

    assert number_of_tours_before_buying_tours - 1 == number_of_tours_after_buying
