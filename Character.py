
class Char_stats:
    def __init__(self, name):
        self.name = name
        self.value = {}
        self.add_mod = {}
        self.mul_mod = {}

    def new_stat(self, stat_name, def_add = 0, def_mul = 1):
        if stat_name in self.value.keys():
            raise ValueError
        else :
            self.value[stat_name] = def_add*def_mul
            self.add_mod[stat_name] = def_add
            self.mul_mod[stat_name] = def_mul

    def init_char_stat(self):
        if self.value.keys():
            raise ValueError
        else :
            self.new_stat("strength", 2)
            self.new_stat("intel", 2)
            self.new_stat("dext", 2)
    def update(self, target_stat):
        if stat not in self.value.keys():
            raise ValueError
        else :
            self.value[target_stat] = self.add_mod[target_stat]*self.mul_mod[target_stat]


class Character:

    def __init__(self, name):
        char_stats = Char_stats(name)

        self.name = None
    def __str__(self):
        return str(self.name)
