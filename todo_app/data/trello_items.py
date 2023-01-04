import os;
import requests;
from todo_app.data.classes.item import Item
from todo_app.data.classes.list import List

key = os.getenv('API_KEY')
token = os.getenv('API_TOKEN')

auth_params = {
    "key": os.getenv('API_KEY'),
    "token": os.getenv('API_TOKEN')
}

base_url = 'https://api.trello.com/1'
board_id = os.getenv('TRELLO_BOARD_ID')

def get_items():
    response = requests.get(f'{base_url}/boards/{board_id}/cards', params=auth_params)
    response_data = response.json()
    items = list(map(Item.from_trello_card, response_data))
    return items

def get_item(id: str):
    items = get_items()
    return next((item for item in items if item.id == id), None)
    
def get_lists():
    response = requests.get(f'{base_url}/boards/{board_id}/lists', params=auth_params)
    response_data = response.json()
    lists = list(map(List.from_trello_list, response_data))
    return lists

def get_list_by_name(list_name: str):
    lists = get_lists()
    return next((list for list in lists if list.name == list_name), None)

def add_todo(title: str):
    list = get_list_by_name('To Do')
    query_params = {
        "name": title,
        "idList": list.id
    }

    response = requests.post(f'{base_url}/cards', params=auth_params | query_params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error from server: " + str(response.content))
    
def move_item(item_id: str, list_id: str):
    query_params = {
        "idList": list_id
    }

    response = requests.put(f'{base_url}/cards/{item_id}', params=auth_params | query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error from server: " + str(response.content))
    

def start_item(item_id: str):
    list = get_list_by_name('Doing')
    return move_item(item_id, list.id)

def complete_item(item_id: str):
    list = get_list_by_name('Done')
    return move_item(item_id, list.id)

def undo_item(item_id: str):
    list = get_list_by_name('To Do')
    return move_item(item_id, list.id)
