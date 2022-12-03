class CharStats:
    """
    Classe qui contient toutes les stats d'un perso, hors situation.
    elle possede 4 attributs :
    - name : un string avec le nom
    - value : un dictionnaire avec comme clés les noms des stats, et en valeur leur valeur actuelle en mémoire.
    - add_mod : un dictionnaire avec comme clés les noms des stats, et en valeur le
    resultat des modificateurs additifs.
    - mul_mod : un dictionnaire avec comme clés les noms des stats, et en valeur le
    resultat des modificateurs multiplicatifs.
    """

    def __init__(self, name):
        self.name = name
        self.value = {}
        self.add_mod = {}
        self.mul_mod = {}

    def new_stat(self, stat_name, def_add=0, def_mul=1):
        """
        :param stat_name: Nom de la stat crée
        :param def_add: Valeur de départ du modificateur additif, default = 0
        :param def_mul: Valeur de départ du modificateur multiplicatif, default = 1
        """
        if stat_name in self.value.keys():
            raise ValueError
        else:
            self.value[stat_name] = def_add * def_mul
            self.add_mod[stat_name] = def_add
            self.mul_mod[stat_name] = def_mul

    def init_char_stat(self):
        if self.value.keys():
            raise ValueError
        else:
            self.new_stat("Strength", 2)
            self.new_stat("Intel", 2)
            self.new_stat("Dext", 2)
            self.new_stat("HP", 10)
            self.new_stat("Mana", 10)

    def incr_hp_from_str(self):
        if "Strength" not in self.value.keys():
            raise ValueError
        else:
            return 1 + 0.1 * self.value["Strength"]

    def incr_strength(self, value):
        curr_incr = self.incr_hp_from_str()
        self.add_mod["Strength"] += value
        self.update("Strength")
        self.add_mul_mod("HP", (self.incr_hp_from_str() / curr_incr))
        self.update("HP")

    def incr_mana_from_intel(self):
        if "Intel" not in self.value.keys():
            raise ValueError
        else:
            return 1 + 0.1*self.value["Intel"]

    def incr_intel(self, value):
        curr_incr = self.incr_mana_from_intel()
        self.add_mod["Intel"] += value
        self.update("Intel")
        self.add_mul_mod("Mana", (self.incr_hp_from_str() / curr_incr))
        self.update("Mana")

    def update(self, target_stat):
        if target_stat not in self.value.keys():
            raise ValueError
        else:
            self.value[target_stat] = int(round(self.add_mod[target_stat] * self.mul_mod[target_stat]))

    def add_add_mod(self, target_stat, mod):
        if target_stat not in self.value.keys():
            raise ValueError
        if target_stat == "Strength":
            self.incr_strength(mod)
        else:
            self.add_mod[target_stat] += mod
            self.update(target_stat)

    def add_mul_mod(self, target_stat, mod):
        if target_stat not in self.value.keys():
            raise ValueError
        else:
            self.mul_mod[target_stat] = self.mul_mod[target_stat] * mod
            self.update(target_stat)


class Character:

    def __init__(self, name):
        char_stats = CharStats(name)
        char_stats.init_char_stat()
        self.name = name
        self.char_stats = char_stats
        self.position = (0, 0)

    def __str__(self):
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
