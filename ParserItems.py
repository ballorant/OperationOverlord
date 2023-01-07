import Item


class Pool:
    """
    Class has only one attribute so far, pool, containing a list of instances of items. It provides creation and search
    methods on the pool.
    """
    @staticmethod
    def parse(directory):
        out = []
        f = open(directory, "r")
        for line in f:
            parsed_line = eval(line)
            req_fun = Item.Requirements(parsed_line[2])
            new_item = Item.Weapon(parsed_line[0], parsed_line[1], req_fun)
            out.append(new_item)
        return out

    def __init__(self, directory):
        self.pool = self.parse(directory)

    def __str__(self):
        out = "List of all the elements of this item pool:\n"
        for item in self.pool:
            out += item.pretty_string()
            out += "\n"
        return out

    def search_item(self, name):
        return [item for item in self.pool if name in item.name]
