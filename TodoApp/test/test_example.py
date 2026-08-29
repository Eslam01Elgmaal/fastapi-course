import pytest


def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 4

def test_is_instance():
    assert isinstance("this is Eslam Ibrahim", str)
    assert not isinstance("344", int)

def test_boolean():
    validated = True
    assert validated is True
    assert ("Eslam" == "Ibrahim") is False

def test_type():
    assert type("hello" is str)
    assert type('england' is not int)

def test_greater_and_less_than():
    assert 7 < 9
    assert 700 > 699

def test_list():
    num_list = [1,2,3,4,5,6]
    any_list = [True, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert any(any_list)

class Student():
    def __init__(self, first_name: str , last_name: str , major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture()
def default_employee():
    return Student('Eslam', "Ibrahim", "Computer since", 19)


def test_person_initialization(default_employee):
    assert default_employee.first_name == "Eslam", "first name should be Eslam"
    assert default_employee.last_name == "Ibrahim", "last name should be Ibrahim"
    assert default_employee.major == "Computer since", ' Major should be Computer Since'
    assert default_employee.years == 19 , 'The Years should be 19 years'