import Item


class Pool:
    def __init__(self, directory):
        self.pool = self.parse(directory)

    def search_item(self, name):
        return [item for item in self.pool if name in item.name]

    def __str__(self):
        out = "List of all the elements of this item pool:\n"
        for item in self.pool:
            out += item.pretty_string()
            out += "\n"
        return out

    """
    Next functions are design to handle the content of the pool, merging two item pool, adding and removing items
    on a one to one basis.
    """
    def merge(self, other_pool):
        """
        Creation and gestion of mixed type item pools is handled by merging datasets.
        """
        merged_pool = Pool(self.pool + other_pool.pool)
        return merged_pool

    def add(self, item):
        self.pool.append(item)

    def remove(self, item_to_rem, purge=0):
        if purge:
            self.pool = [item for item in self.pool if item_to_rem.name == item.name]
        else:
            self.pool.remove(item_to_rem)


    @staticmethod
    def parse(directory):
        out = []
        f = open(directory, "r")
        for line in f:
            parsed_line = eval(line)
            req_fun = Item.Requirements(parsed_line[1])
            new_item = Item.Item(parsed_line[0], req_fun)
            out.append(new_item)
        return out


class WeaponPool(Pool):
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

    def __str__(self):
        out = "List of all the elements of this item pool:\n"
        for item in self.pool:
            out += item.pretty_string()
            out += "\n"
        return out
