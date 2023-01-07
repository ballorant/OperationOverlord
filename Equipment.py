class Equipment:
    """
    Class to represent the equipment of character.
    """

    def __init__(self, character):
        self.character = character


class ItemSlot:
    """
    Class to represent an item slot of the equipment of a character.
    """

    def __init__(self, name="Slot"):
        self._currentItem = None
        self.itemPresent = False
        self.name = name

    def is_free(self):
        return not self.itemPresent

    def get_item(self):
        """
        Method to get the current item in the slot.
        :return: the item in the slot.
        """
        if self.is_free():
            return None
        else:
            return self._currentItem

    def set_item(self, item):
        """
        Set item to be the item in the slot if the slot is free.
        :param item: the item to be equipped in the slot.
        :return: success value of item equipment .
        """
        if self.itemPresent:
            return False

        self._currentItem = item
        self.itemPresent = True

        return True

    def remove_item(self):
        """
        Method to remove the item present in the item slot.
        :return: the item that has been removed.
        """
        previous_item = self._currentItem
        self._currentItem = None
        self.itemPresent = False
        return self._currentItem


class Boots(ItemSlot):

    def __init__(self):
        super().__init__("BootsSlot")


class RightHand(ItemSlot):

    def __init__(self):
        super().__init__("RightHandSlot")
