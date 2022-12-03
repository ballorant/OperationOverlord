import Item


class ItemPool:
    def __init__(self):
        self.itempool = []

    def searchitem(self, name):
        return [item for item in self.itempool if name in item.name]
