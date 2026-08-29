from http.client import responses

from .utils import *
from ..routers.admin import get_db,get_current_user
from fastapi import status
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_admin_read_all_authenticated(test_todo):
    response = client.get('/admin/todo')
    assert response.status_code == status.HTTP_200_OK
    # print(response.json())
    assert response.json() == [{"title": "Eslam Coding now!",
                                "priority": 4,
                                "complete": False,
                                "description": "we are test The todo Function now and i'm looking to working well!",
                                "id": 1, "owner_id": 1}]

def test_admin_delete_todo(test_todo):
    response = client.delete('/admin/todo/1')
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None


def test_admin_delete_todo_not_found(test_todo):
    response = client.delete('admin/todo/909')
    assert response.status_code == 404
    assert response.json() == {'detail': 'todo not found'}