import Item

class WeaponPool:
    @staticmethod
    def parse(directory):
        out = []
        f = open(directory, "r")
        for line in f:
            parsed_line = eval(line)
            req_fun = Item.Requirements(parsed_line[2])
            newitem = Item.Weapon(parsed_line[0], parsed_line[1], req_fun)
            out.append(newitem)
        return out

    def __init__(self, directory):
        self.pool = self.parse(directory)

    def searchitem(self, name):
        return [item for item in self.pool if name in item.name]
