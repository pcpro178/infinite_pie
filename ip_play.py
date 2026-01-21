"""! Module for handling gameplay."""

################################################################################
# Imports
################################################################################

from enum import StrEnum

import logging

from ip_actionable import IActionable
from ip_empire import Empire


################################################################################
# Constants & Globals
################################################################################

MENU_CHOICE_RETURN: str = "Return to Main Menu"


################################################################################
# Class definitions
################################################################################

class MenuChoices(StrEnum):
    """! Enumeration for main menu choices."""
    NEW_EMPIRE: str = 'New Empire'
    MANAGE_EMPIRE: str = 'Manage Empire'
    END_TURN: str = 'End Turn'


class Play(IActionable):
    """! Class for handling gameplay."""

    def __init__(self):
        """! Initialize a new Play object."""
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__} initializing . . .")

        super().__init__()

        self.menu.choices.extend([str(x) for x in MenuChoices])
        self.menu.title = "Infinite PIE Menu"

        self.__empire: Empire = None

    def __selection_new_empire(self) -> None:
        """! Handle new empire selection."""
        do_create: bool = True

        if self.__empire is not None:
            choice: str = input("An empire already exists. Creating a new empire will overwrite the existing one. "
                                "Continue? (y/n): ")
            do_create = choice == '' or choice[0].lower() == 'y'

        if do_create:
            self.__empire = Empire()
            self.__empire.menu.choices.extend([MENU_CHOICE_RETURN])

        print()
        print(f"Empire {self.__empire.name} created. Capital system: {self.__empire.capital}")
        print()

    def __selection_manage_empire(self) -> None:
        """! Handle manage empire selection."""
        if self.__empire is None:
            print("No empire created. Create a new empire to begin.")
        else:
            self.__empire.show()

            while self.__empire.menu.response != MENU_CHOICE_RETURN:
                self.__empire.run()
                self.__empire.show()

    def __selection_end_turn(self) -> None:
        """! Handle end turn selection."""
        if self.__empire is None:
            print("No empire created. Create a new empire to begin.")
        else:
            self.__empire.cycle()

    def run(self) -> None:
        """! Run the main gameplay loop."""
        if self.menu.response == MenuChoices.NEW_EMPIRE:
            self.__selection_new_empire()
        elif self.menu.response == MenuChoices.MANAGE_EMPIRE:
            self.__selection_manage_empire()
        elif self.menu.response == MenuChoices.END_TURN:
            self.__selection_end_turn()
        else:
            raise ValueError(f"Invalid choice: {self.menu.response}")
