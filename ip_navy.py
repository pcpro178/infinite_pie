"""! Module for managing empire navy. """

################################################################################
# Imports
################################################################################

from enum import StrEnum
from typing import List

import logging

from ip_actionable import IActionable
from ip_ship import Ship


################################################################################
# Constants & Globals
################################################################################

MENU_CHOICE_RETURN: str = "Return to Navy Menu"


################################################################################
# Class definitions
################################################################################

class MenuChoices(StrEnum):
    """! Enumeration for territory menu choices."""
    VIEW_DETAILS: str = 'View Details'


class Navy(IActionable):
    """! Class for managing empire navy. """

    def __init__(self):
        """! Initializes Navy object instance. """
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__} initializing . . .")

        super().__init__()

        self.menu.choices.extend([str(x) for x in MenuChoices])
        self.menu.title = "Navy Menu"

        self.__ships: List[Ship] = None

    @property
    def ships(self) -> List[Ship]:
        """! Getter for ships
        :return: List of ships
        """
        return self.__ships

    @ships.setter
    def ships(self, ships: List[Ship]) -> None:
        """! Setter for ships
        :param ships: List of ships to set
        """
        self.__ships = ships

    def run(self) -> None:
        """! Display the navy menu selection."""
        print("Todo: Handle navy menu choices.")
