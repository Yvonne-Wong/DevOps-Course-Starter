import os;
import requests;
from todo_app.data.classes.item import Item
from todo_app.data.classes.list import List

base_url = 'https://api.trello.com/1'

def get_items():
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }
    trello_board_id = os.getenv('TRELLO_BOARD_ID')

    response = requests.get(f'{base_url}/boards/{trello_board_id}/cards', params=auth_params)
    response_data = response.json()
    items = list(map(Item.from_trello_card, response_data))
    return items

def get_item(id: str):
    items = get_items()
    return next((item for item in items if item.id == id), None)
    
def get_lists():
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }
    trello_board_id = os.getenv('TRELLO_BOARD_ID')

    response = requests.get(f'{base_url}/boards/{trello_board_id}/lists', params=auth_params)
    response_data = response.json()
    lists = list(map(List.from_trello_list, response_data))
    return lists

def get_list_by_name(list_name: str):
    lists = get_lists()
    return next((list for list in lists if list.name == list_name), None)

def add_todo(title: str):
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }

    list = get_list_by_name('To Do')
    query_params = {
        "name": title,
        "idList": list.id
    }

    response = requests.post(f'{base_url}/cards', params=auth_params | query_params)
    
def move_item(item_id: str, list_id: str):
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }

    query_params = {
        "idList": list_id
    }

    response = requests.put(f'{base_url}/cards/{item_id}', params=auth_params | query_params)
 
def start_item(item_id: str):
    list = get_list_by_name('Doing')
    return move_item(item_id, list.id)

def complete_item(item_id: str):
    list = get_list_by_name('Done')
    return move_item(item_id, list.id)

def undo_item(item_id: str):
    list = get_list_by_name('To Do')
    return move_item(item_id, list.id)
