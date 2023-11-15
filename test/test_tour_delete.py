from backend.database.Tour import Tour_create
from backend.database.Tour_advanced import remove_tours_that_i_have_created
from backend.database.user import id_if_provide_username, create_user


def test_a_user_can_delete_a_tour_that_he_has_created():
    create_user("testbruker400", "123", True)
    user_id = id_if_provide_username("testbruker400")

    #TODO denne testen må ventes med til Vetle har fiksa funksjon for å slette en bruker.
    action = "delete"
    selected = [(500, "title", "description", "country", "location", "23-08-1990", user_id),
                (501, "title1", "description1", "country1", "location1", "12-03-1991", user_id)]
    tour1 = Tour_create(500, "title", "description", "country", "location", "23-08-1990")
    tour2 = Tour_create(501, "title1", "description1", "country1", "location1", "12-03-1991")
    remove_tours_that_i_have_created(selected, action)