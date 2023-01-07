class CharStats:
    """
    Class with all the stats of a character.
     It currently has 4 attributes:
    - name : a string with the name.
    - value : a dictionary with stat_names as keys and current values as values.
    - add_mod : a dictionary with stat_names as keys and total values of additive modifiers as values.
    - mul_mod : a dictionary with stat_names as keys and total values of multiplicative modifiers as values.
    """

    def __init__(self, name):
        self.name = name
        self.value = {}
        self.add_mod = {}
        self.mul_mod = {}
        self.init_char_stat()

    def new_stat(self, stat_name, def_add=0, def_mul=1):
        """
        :param stat_name: name of stat
        :param def_add: starting value of additive modifier, by default = 0
        :param def_mul: starting value of multiplicative modifier, by default = 1
        """
        if stat_name in self.value.keys():
            raise ValueError
        else:
            self.value[stat_name] = def_add * def_mul
            self.add_mod[stat_name] = def_add
            self.mul_mod[stat_name] = def_mul

    def init_char_stat(self):
        """
        Initialize a character with it Strength, Intelligence, Dexterity, HP and Mana.
        """
        if self.value.keys():
            raise ValueError
        else:
            self.new_stat("Strength", 2)
            self.new_stat("Intel", 2)
            self.new_stat("Dext", 2)
            self.new_stat("HP", 10)
            self.new_stat("Mana", 10)

    def incr_hp_from_str(self):
        """
        Compute the HP modifier from Strength stat.
        """
        if "Strength" not in self.value.keys():
            raise ValueError
        else:
            return 1 + 0.1 * self.value["Strength"]

    def incr_strength(self, value):
        """
        Raise strength and updates life accordingly.
        :param value: value of the strength raise.
        """
        curr_incr = self.incr_hp_from_str()
        self.add_mod["Strength"] += value
        self.update("Strength")
        self.add_mul_mod("HP", (self.incr_hp_from_str() / curr_incr))
        self.update("HP")

    def incr_mana_from_intel(self):
        """
        Compute the Mana modifier from Intelligence stat.
        """
        if "Intel" not in self.value.keys():
            raise ValueError
        else:
            return 1 + 0.1 * self.value["Intel"]

    def incr_intel(self, value):
        """
        Raise intelligence and updates mana accordingly.
        :param value: value of intelligence raise.
        """
        curr_incr = self.incr_mana_from_intel()
        self.add_mod["Intel"] += value
        self.update("Intel")
        self.add_mul_mod("Mana", (self.incr_hp_from_str() / curr_incr))
        self.update("Mana")

    def update(self, target_stat):
        """
        Update the real value of a stat according to its current modifiers.
        :param target_stat: name of stat to update.
        """
        if target_stat not in self.value.keys():
            raise ValueError
        else:
            self.value[target_stat] = int(round(self.add_mod[target_stat] * self.mul_mod[target_stat]))

    def add_add_mod(self, target_stat, mod):
        """
        Add an additive modifier to a stat.
        :param target_stat: name of the stat to be modified.
        :param mod: value of the modifier to be added.
        """
        if target_stat not in self.value.keys():
            raise ValueError
        if target_stat == "Strength":
            self.incr_strength(mod)
        else:
            self.add_mod[target_stat] += mod
            self.update(target_stat)

    def add_mul_mod(self, target_stat, mod):
        """
        Add a multiplicative modifier to a stat.
        :param target_stat: name of the stat to be modified.
        :param mod: value of the modifier to be added.
        """
        if target_stat not in self.value.keys():
            raise ValueError
        else:
            self.mul_mod[target_stat] = self.mul_mod[target_stat] * mod
            self.update(target_stat)


class Character:
    """
    Class with the information related to a character.
    -   name : character's name.
    -   chat_stats : character's stats.
    """

    def __init__(self, name):
        self.name = name
        self.char_stats = CharStats(name)
        self.position = (0, 0)
        self.equipment = Equipment(self)

    def __str__(self):
        """
        String of character for debug purpose.
        :return: A string
        """
        out = "Character {} :\n".format(self.name)
        for stat in self.char_stats.value.keys():
            out += "{} : {}\n".format(stat, self.char_stats.value[stat])
        return out




class CharacterInstance:
    def __init__(self):
        self.position = (0, 0)
        pass  # TODO

    def x_pos(self):
        return self.position[0]

    def y_pos(self):
        return self.position[1]
