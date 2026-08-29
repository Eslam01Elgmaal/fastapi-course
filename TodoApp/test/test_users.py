from http.client import responses

from .utils import *
from ..models import Users
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users")
    # print(response.json())
    assert response.status_code == status.HTTP_200_OK
    # print(response.json())

def test_my_information(test_user):
    response = client.get("/users/me")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['email'] == "eslam.ibrahim@yahoo.com"
    assert response.json()['username'] == 'Eslam'
    assert response.json()['first_name'] == 'eslam'
    assert response.json()['last_name'] == 'ibrahim'
    assert bcrypt_context.verify("12345", response.json()["hashed_password"])# very importint
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '+201065869833'

def test_change_password_success(test_user):
    request_data = {
        'password': '12345',
        'new_password': '123456'
    }

    response = client.put("/users/password", json= request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    request_data = {
        'password': 'wrong password',
        'new_password': '123456'
    }

    response = client.put("/users/password", json=request_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail" : "Error on change password"}


