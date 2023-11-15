import pytest

from backend.database.Tour import Tour_create, Tour_delete_if_title_is_provided

def test_a_new_tour_is_not_none():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12", "krøsstvællæ")
    assert new_tour_id is not None
    Tour_delete_if_title_is_provided("skitur")


list_tours_illegal_input = [
    ("1", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("12", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("123", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("1234", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("Tittel er over 25 bokstaver eller mer", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("Denne er akkurat 25 lang 3", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("", "Empty title", "Norge", "Finmark", "2023-10-12", "krøsstvællæ"),
    ("", "", "", "", "", ""),
("A long title in a tour can not be made because we as developers has desided it", "description", "Country", "Location", "1999-12-22", "CreatedBy")
]
@pytest.mark.parametrize("Title_not_legal, Description_not_legal, Country_not_legal, Location_not_legal, Date_not_legal, created_by_not_legal",list_tours_illegal_input)
def test_not_possible_to_create_tour_with_title_under_5_or_over_24_characters(Title_not_legal, Description_not_legal, Country_not_legal, Location_not_legal, Date_not_legal, created_by_not_legal):
    new_tour_not_legal = Tour_create(Title_not_legal, Description_not_legal, Country_not_legal, Location_not_legal, Date_not_legal, created_by_not_legal)
    assert new_tour_not_legal == False
    Tour_delete_if_title_is_provided(Title_not_legal)


list_tours_legal_input = [
    ("12345", "description", "Country", "Location", "2023-10-12", "CreatedBy"),
    ("Denne er akkurat 24 lang!", "description", "Country", "Location", "1999-12-22", "CreatedBy")
]
@pytest.mark.parametrize("Title, Description, Country, Location, Date, created_by", list_tours_legal_input)
def test_possible_to_create_tour_with_title_between_5_and_24_characters(Title, Description, Country, Location, Date, created_by):
    new_tours_legal = Tour_create(Title, Description, Country, Location, Date, created_by)
    assert new_tours_legal == True
    Tour_delete_if_title_is_provided(Title)
