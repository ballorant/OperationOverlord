
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
            self.new_stat("Strength", 2)
            self.new_stat("Intel", 2)
            self.new_stat("Dext", 2)
    def update(self, target_stat):
        if target_stat not in self.value.keys():
            raise ValueError
        else :
            self.value[target_stat] = self.add_mod[target_stat]*self.mul_mod[target_stat]

    def add_add_mod(self, target_stat, mod):
        if target_stat not in self.value.keys():
            raise ValueError
        else :
            self.add_mod[target_stat] += mod
    def add_mul_mod(self, target_stat, mod):
        if target_stat not in self.value.keys():
            raise ValueError
        else :
            self.add_mod[target_stat]  = self.add_mod[target_stat]*mod
class Character:

    def __init__(self, name):
        char_stats = Char_stats(name)
        char_stats.init_char_stat()
        self.name = name
        self.char_stats = char_stats
        self.position = (0, 0)

    def __str__(self):
        out = "Character {} :\n".format(self.name)
        for stat in self.char_stats.value.keys():
            out += "{} : {}\n".format(stat, self.char_stats.value[stat])
        return out




class Character_instance:
    def __init__(self):
        self.position = (0, 0)
        pass ## TODO
    def x_pos(self):
        return self.position[0]
    def y_pos(self):
        return  self.position[1]

