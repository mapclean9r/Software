from backend.database.Tour import Tour_create, Tour_delete_if_title_is_provided


def test_a_new_tour_is_not_none():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id is not None
    Tour_delete_if_title_is_provided("skitur")

def test_create_a_tour_without_title():
    new_tour_id = Tour_create("", "Cool description", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id == False