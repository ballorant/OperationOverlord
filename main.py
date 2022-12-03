# This is a sample Python script.
from Character import Character
from Item import OneHandSword


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test_chara(name):
    """ Ceci est un test de doc:

    Vous voyez ca marche bien.

    Cette fonction prend en paramètre: name un string

    et fait des choses inutiles.
    """
    moi = Character(name)

    print(moi)

    excalibur = OneHandSword("Excalibourré", 10)

    print(excalibur.pretty_string())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_chara("Roosevelt")
# Nyaa
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
