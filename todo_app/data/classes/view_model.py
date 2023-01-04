class ViewModel:
    def __init__(self, items, lists):
        self._items = items
        self._lists = lists

    @property
    def items(self):
        return self._items

    @property
    def lists(self):
        return self._lists

    @property
    def to_do_items(self):
        list_id = next((list.id for list in self._lists if list.name == 'To Do'), None)
        return [item for item in self._items if item.list_id == list_id]

    @property
    def doing_items(self):
        list_id = next((list.id for list in self._lists if list.name == 'Doing'), None)
        return [item for item in self._items if item.list_id == list_id]

    @property
    def done_items(self):
        list_id = next((list.id for list in self._lists if list.name == 'Done'), None)
        return [item for item in self._items if item.list_id == list_id]