import pytest

from backend.database.Tour import Tour_create, Tour_delete_if_title_is_provided, Tour_get_id_from_title
from backend.database.Tour_advanced import tours_that_i_have_created, remove_tours_that_i_have_created
from backend.database.user import id_if_provide_username, create_user


def test_a_new_tour_is_not_of_none_value():
    new_tour_id = Tour_create("skitur", "kul tur", "Norge", "Finmark", "2023-10-12", "krøsstvællæ", 23)
    assert new_tour_id is not None
    Tour_delete_if_title_is_provided("skitur")


list_tours_illegal_input = [
    ("1", "description", "Country", "Location", "2023-10-12", "CreatedBy", 22),
    ("12", "description", "Country", "Location", "2023-1-1",  "CreatedBy", 159),
    ("123", "description", "Country", "Location", "2023-12",  "CreatedBy", 159),
    ("1234", "description", "Country", "Location", "2023-10-12", "CreatedBy", 225),
    ("Tittel er over 25 bokstaver eller mer", "description", "Country", "Location", "2023-10-12", "CreatedBy", 222),
    ("Denne er akkurat 25 lang 3", "description", "Country", "Location", "2023-10-12", 300,  "CreatedBy"),
    ("", "Empty title", "Norge", "Finmark", "2023-10-12",  "krøsstvællæ", 10000),
    ("", "", "", "", "", "", 0),
    ("A long title in a tour can not be made because we as developers has desided it", "description", "Country", "Location", "1999-12-22", "CreatedBy", 100)
]
@pytest.mark.parametrize("Title_not_legal, Description_not_legal, Country_not_legal, Location_not_legal, Date_not_legal, created_by_not_legal, price_not_legal",list_tours_illegal_input)
def test_not_possible_to_create_tour_with_illegal_input(Title_not_legal, Description_not_legal, Country_not_legal, Location_not_legal, Date_not_legal, created_by_not_legal, price_not_legal):
    new_tour_not_legal = Tour_create(Title_not_legal, Description_not_legal, Country_not_legal, Location_not_legal, Date_not_legal, created_by_not_legal, price_not_legal)
    assert new_tour_not_legal == False
    Tour_delete_if_title_is_provided(Title_not_legal)


list_tours_legal_input = [
    ("12345", "description", "Country", "Location", "2023-10-12", "CreatedBy", 300),
    ("Denne er akkurat 24 lang!", "description", "Country", "Location", "1999-12-22", "CreatedBy", 334)
]
@pytest.mark.parametrize("Title, Description, Country, Location, Date, created_by, Price", list_tours_legal_input)
def test_not_possible_to_create_tour_with_legal_input(Title, Description, Country, Location, Date, created_by, Price):
    new_tours_legal = Tour_create(Title, Description, Country, Location, Date, created_by, Price)
    assert new_tours_legal == True
    Tour_delete_if_title_is_provided(Title)


def test_number_of_my_created_tours_is_increased_when_creating_a_new_tour():

    create_user("wassup12", "123", "True")
    user_id_int = id_if_provide_username("wassup12")[0]

    len_list = len(tours_that_i_have_created(user_id_int))

    Tour_create("test_title very fun", "description", "Country", "Location", "2020-01-01", user_id_int, 100)
    id_from_tour = Tour_get_id_from_title("test_title very fun")

    len_list_with_new_tour = len(tours_that_i_have_created(user_id_int))

    assert len_list + 1 == len_list_with_new_tour
    assert len_list + 2 != len_list_with_new_tour
    assert len_list + 0 != len_list_with_new_tour
    assert len_list + 45 != len_list_with_new_tour
    remove_tours_that_i_have_created(user_id_int, id_from_tour, 'delete')
