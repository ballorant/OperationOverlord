class Item:

    def __init__(self):
        self.identified = False
        self.requirements = Requirements()


class Weapon(Item):

    def __init__(self, damage):
        super().__init__()
        self.damage = damage


class OneHandWeapon(Weapon):

    def __init__(self, damage):
        super().__init__(damage)


class Sword(Weapon):

    def __init__(self, damage):
        super().__init__(damage)


class OneHandSword(OneHandWeapon, Sword):

    def __init__(self, damage):
        super().__init__(damage)


class Requirements:

    def __init__(self):
        self.conditions = [True]

    def is_valid(self, character):
        return self.conditions[0]
        #TODO

