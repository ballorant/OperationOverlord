class Item:

    def __init__(self, name):
        self.identified = False
        self.requirements = Requirements()
        self.durability = 100
        self.rarity = "Unknown"
        self.name = name

    def use(self, lost):
        self.durability -= lost

        return self.durability > 0

    def pretty_string(self):
        return "{}\nRequirements: {}\nDurability: {}/100\nRarity: {}\n".format(
            self.name,
            self.requirements.string_pas_cher(),
            self.durability,
            self.rarity)


class Weapon(Item):

    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def pretty_string(self):
        return "{}Damage: {}".format(
            super().pretty_string(),
            self.damage
        )


class OneHandWeapon(Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)


class Sword(Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)


class OneHandSword(OneHandWeapon, Sword):

    def __init__(self, name, damage):
        super().__init__(name, damage)

    def print_item(self):
        return self.pretty_string()


class Requirements:

    def __init__(self, conditions=lambda x: True):
        self.conditions = conditions

    def is_valid(self, character):
        return self.conditions[0]
        # TODO

    def string_pas_cher(self):
        return "None"
        # TODO
