import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', get_lists_stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

def test_create_todo_creates_item(monkeypatch, client):
    created_item_name = None

    def post_create_stub_spy(url, params):
        nonlocal created_item_name
        created_item_name = params['name']
        return post_create_item_stub(url, params)

    monkeypatch.setattr(requests, 'post', post_create_stub_spy)
    monkeypatch.setattr(requests, 'get', get_lists_stub)
   
    form_data = {
        "todo": "Testcard"
    }

    response = client.post('/', data=form_data)
    assert response.status_code == 302
    assert created_item_name == "Testcard"

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_lists_stub(url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards':
        fake_response_data = [{
            'id': '12345',
            'name': 'Test card',
            'idList': '1'
        }]
        return StubResponse(fake_response_data)
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': '1',
            'name': 'To Do'
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def post_create_item_stub(url, params):
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }

    query_params = {
        "name": "Testcard",
        "idList": "1"
    }
    
    if url == 'https://api.trello.com/1/cards' and params==auth_params | query_params:
        fake_response_data = {
            "id": "54321",
            "name": "Testcard",
            "idList": "1"
        }
        return StubResponse(fake_response_data)

    raise Exception('Something went wrong')