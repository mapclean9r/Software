from src.backend.database.Tour import Tour_create, Tour_get_all, Tour_find_title, \
    Tour_delete_if_title_is_provided


def test_a_new_tour_is_not_none():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id is not None
    Tour_delete_if_title_is_provided("skitur")

def test_a_tours_id_is_of_int_datatype():
    new_tour_id = Tour_create("Fotball på løkka med guttæne", "rått", "gg", "Kautokeino", "2028-04-01", "GrusBane Hansen")
    assert isinstance(new_tour_id, int)
    Tour_delete_if_title_is_provided("Fotball på løkka med guttæne")

def test_can_find_tour_if_we_provide_the_correct_title_for_a_tour():
    new_tour_id = Tour_create("Safari i Skæven med gutta", "vil se en elg", "Norge", "Oslo", "2025-03-02","Kålrabi")
    assert Tour_find_title("Safari i Skæven med gutta")
    Tour_delete_if_title_is_provided("Safari i Skæven med gutta")

def test_we_can_return_all_tours():
    all_tours = Tour_get_all()
    assert all_tours is not None

def test_can_find_title_for_a_tour_when_we_provide_the_right_title():
    new_tour = Tour_create("burgerspisekonkuranse med dressing på salaten", "Nå er jeg mett", "Norge", "Oslo", "2023-09-02", "Rolf Maibrittson")
    assert len(Tour_find_title("burgerspisekonkuranse med dressing på salaten")) >= 1
    Tour_delete_if_title_is_provided("burgerspisekonkuranse med dressing på salaten")

def test_if_all_inputfields_in_a_created_tour_have_values():
    new_tour = Tour_create("tets1", "e", "Norge", "e", "2025-03-02","Kålrabi")
    for field in new_tour:
        str(field) 