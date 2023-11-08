from src.backend.database.Tour import Tour_create, Tour_get_all, Tour_get, Tour_find_title, \
    Tour_delete_if_title_is_provided


def test_new_tour_is_created():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id is not None
    Tour_delete_if_title_is_provided("skitur")

def test_a_tours_id_is_int_datatype():
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

def test_we_can_not_find_title_for_a_tour_if_we_provide_wrong_title():
    new_tour = Tour_create("spydkasting i akebakken i brattbakken", "kul tur", "Norge", "Finmark", "2023-10-12", "Sambafotball mannen")
    assert len(Tour_find_title("triksekonkuransen i ballbingen")) == 0
    Tour_delete_if_title_is_provided("spydkasting i akebakken i brattbakken")

def test_can_find_title_for_a_tour_when_we_provide_the_right_title():
    new_tour = Tour_create("burgerspisekonkuranse med dressing på salaten", "Nå er jeg mett", "Norge", "Oslo", "2023-09-02", "Rolf Maibrittson")
    assert len(Tour_find_title("burgerspisekonkuranse med dressing på salaten")) >= 1
    Tour_delete_if_title_is_provided("burgerspisekonkuranse med dressing på salaten")
