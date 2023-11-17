from src.backend.database.Tour import Tour_create, Tour_get_all, Tour_find_title, \
    Tour_delete_if_title_is_provided


def test_a_tours_id_is_of_int_datatype():
    new_tour_id = Tour_create("Fotball på løkka med guttæne", "rått", "gg", "Kautokeino", "2028-04-01", 29.58, "GrusBane Hansen")
    assert isinstance(new_tour_id, int)
    Tour_delete_if_title_is_provided("Fotball på løkka med guttæne")

def test_can_find_tour_if_we_provide_the_correct_title_for_a_tour():
    Tour_create("Safari i Skæven med gutta", "vil se en elg", "Norge", "Oslo", "2025-03-02",34.29, "Kålrabi")
    assert Tour_find_title("Safari i Skæven med gutta")
    Tour_delete_if_title_is_provided("Safari i Skæven med gutta")

def test_we_can_return_all_tours():
    all_tours = Tour_get_all()
    assert all_tours is not None

def test_can_find_title_for_a_tour_when_we_provide_the_right_title():
    Tour_create("spisekonkuranse", "Nå er jeg mett", "Norge", "Oslo", "2023-09-02",34.29, "Rolf Maibrittson")
    length_of_title = len(Tour_find_title("spisekonkuranse"))
    if (length_of_title >= 1):
        assert True
    Tour_delete_if_title_is_provided("spisekonkuranse")
