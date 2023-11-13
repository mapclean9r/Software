from backend.autentication.register import username_create
from backend.database.Tour_advanced import remove_tours_that_i_have_created
from backend.database.user import id_if_provide_username


def test_a_user_can_delete_a_tour_that_he_has_created():
    username_create("testbruker400", "123", True)
    user_id = id_if_provide_username("testbruker400")

    action = "delete"
    selected = [(500, "title", "description", "country", "location", "23-08-1990", user_id),
                (501, "title1", "description1", "country1", "location1", "23-08-1990", user_id)]

    remove_tours_that_i_have_created(selected, action)