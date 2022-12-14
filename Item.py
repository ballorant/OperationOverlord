class Item:
    """
    Class that cover the generic type of all items in the game:

    - Whether its identified or not: bool
    - Requirements : Requirements as a boolean function.
    - Durability : between 0 and 100
    - Rarity
    - Name
    """

    def __init__(self, name, requirements=lambda x: True):
        self.identified = False
        self.requirements = Requirements(requirements)
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
    """
    Class covering the weapon. Inherits from Item with an extra attribute for damage.
    """

    def __init__(self, name, damage=lambda x: 1, requirements=lambda x: True):
        super().__init__(name, requirements)
        self.damage = damage

    def pretty_string(self):
        return "{}Damage: {}".format(
            super().pretty_string(),
            self.damage
        )


class OneHandWeapon(Weapon):

    def __init__(self, name, damage=lambda x: 1, requirements=lambda x: True):
        super().__init__(name, damage, requirements)


class Sword(Weapon):

    def __init__(self, name, damage=lambda x: 1, requirements=lambda x: True):
        super().__init__(name, damage, requirements)


class OneHandSword(OneHandWeapon, Sword):

    def __init__(self, name, damage=lambda x: 1, requirements=lambda x: True):
        super().__init__(name, damage, requirements)

    def print_item(self):
        return self.pretty_string()


class Requirements:

    def __init__(self, conditions=lambda x: True):
        self.conditions = conditions

    def is_valid(self, character):
        return self.conditions(character)
        # TODO

    def string_pas_cher(self):
        return "None"
        # TODO
