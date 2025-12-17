"""! Module for handling gameplay."""


from ip_empire import Empire

import ip_empire as empire


class Play:
    """! Class for handling gameplay."""

    __empire: Empire = None

    def __init__(self):
        """! Initialize a new Play object."""
        self.__empire = Empire()

    def cycle(self) -> bool:
        """! Complete a temporal cycle (i.e. a player turn, as it were).
        :return: Boolean indicating whether to continue playing
        """
        return True if self.__empire.menu() != empire.MENU_CHOICE_EXIT else False
