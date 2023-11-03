from src.backend.database.Tour import Tour_create, Tour_get_all, Tour_get
import pytest


def test_new_tour_is_created():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12")

    assert new_tour_id is not None

def test_a_tours_id_is_int_datatype():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12")
    assert isinstance(new_tour_id, int)

def test_we_can_get_id_from_a_tour_if_we_provide_the_correct_id_for_a_tour():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12")
    assert Tour_get(175)
def test_we_can_return_all_tours():
    all_tours = Tour_get_all()
    assert all_tours is not None

'''
def test_we_can_get_a_tour_when_providing_a_tourID():
    assert None
'''
