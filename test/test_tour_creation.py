import pytest

from backend.database.Tour import Tour_create, Tour_delete_if_title_is_provided


def test_a_new_tour_is_not_none():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id is not None
    Tour_delete_if_title_is_provided("skitur")

def test_create_a_tour_without_title():
    new_tour_id = Tour_create("", "Cool description", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id == False

list_tours_illegal_input = [
    ("1", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("12", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("123", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("1234", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("Tittel er over 25 bokstaver eller mer", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("Denne er akkurat 25 lang 3", "description", "Country", "Location", "2023-10-12", "CreatedBy")
]
@pytest.mark.parametrize("ID, Title, Description, Country, Location, Date", list_tours_illegal_input)
def test_not_possible_to_create_tour_with_title_under_5_or_over_24_characters(ID, Title, Description, Country, Location, Date):
    new_tour_id = Tour_create(ID, Title, Description, Country, Location, Date)
    assert new_tour_id == False

list_tours_legal_input = [
    ("12345", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("Denne er akkurat 24 lang!", "description", "Country", "Location", "2023-10-12", "CreatedBy")
]
@pytest.mark.parametrize("ID, Title, Description, Country, Location, Date", list_tours_legal_input)
def test_possible_to_create_tour_with_title_between_5_and_24_characters(ID, Title, Description, Country, Location, Date):
    new_tour_id = Tour_create(ID, Title, Description, Country, Location, Date)
    assert new_tour_id == True