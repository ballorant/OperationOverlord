# This is a sample Python script.
from Character import Character


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
    moi.char_stats.new_stat("Charme", 10, 0)
    moi.char_stats.add_add_mod("Charme", -5)
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    print(moi.char_stats.mul_mod["HP"])
    moi.char_stats.add_add_mod("Strength", 10)
    moi.char_stats.update("Charme")
    moi.char_stats.update("Strength")
    print(moi.char_stats.mul_mod["HP"])
    print(moi)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_chara("Roosevelt")
# Nyaa
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
