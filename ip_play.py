"""! Module for handling gameplay."""

################################################################################
# Imports
################################################################################

from enum import StrEnum
from typing import List

from ip_actionable import Actionable
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


class Play(Actionable):
    """! Class for handling gameplay."""

    def __init__(self, parent_choices: List[str] = None):
        """! Initialize a new Play object.
        :param parent_choices: Parent menu choices
        """
        super().__init__([str(x) for x in MenuChoices] + (parent_choices or []), "Infinite PIE Menu")
        self.__empire: Empire = None

    def __selection_new_empire(self) -> None:
        """! Handle new empire selection."""
        if self.__empire is not None:
            choice: str = input("An empire already exists. Creating a new empire will overwrite the existing one. "
                                "Continue? (y/n): ")
            self.__empire = Empire([MENU_CHOICE_RETURN]) if choice == '' or choice[0].lower() == 'y' else None
        else:
            self.__empire = Empire([MENU_CHOICE_RETURN])

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

    def show(self) -> None:
        """! Show the main menu to the user."""
        self.menu.show()
