class Item:
    """
    Classe qui regroupe l'ensemble des items du jeu, les attributs d'un item sont:

    - Son état d'identification: bool
    - Ses requirements : Requirements issues d'une fonction booléenne
    - Sa durabilité : entre 0 et 100
    - Sa rareté
    - Son nom
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
    Classe qui représente l'ensemble des armes, elle a en attibut une fonction de dégat en plus.
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
