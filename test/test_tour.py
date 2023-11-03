from backend.database.Tour import Tour_create, Tour_get_all, Tour_get
import pytest

def test_new_tour_is_created():
    new_tour = Tour_create("skitur", "kul tur", "Norge", "Finmark","2023-10-12")
    assert new_tour is not None

def test_we_can_get_all_tours_in_return_from_this_function():
    all_tours = Tour_get_all()
    assert all_tours is not None

def test_we_can_get_a_tour_when_providing_a_tourID():
    assert None