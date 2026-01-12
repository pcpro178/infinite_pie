"""! Module for managing empire territory. """

################################################################################
# Imports
################################################################################

from enum import StrEnum
from typing import List

import logging

from ip_actionable import IActionable
from ip_system import System


################################################################################
# Constants & Globals
################################################################################

MENU_CHOICE_RETURN: str = "Return to Territory Menu"


################################################################################
# Class definitions
################################################################################

class MenuChoices(StrEnum):
    """! Enumeration for territory menu choices."""
    VIEW_DETAILS: str = 'View Details'


class Territory(IActionable):
    """! Class for managing empire territory. """

    def __init__(self):
        """! Initializes Territory object instance. """
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__} initializing . . .")

        super().__init__()

        self.menu.choices.extend([str(x) for x in MenuChoices])
        self.menu.title = "Territory Menu"

        self.__systems: List[System] = None

    @property
    def systems(self) -> List[System]:
        """! Getter for systems
        :return: List of systems
        """
        return self.__systems

    @systems.setter
    def systems(self, value: List[System]) -> None:
        """! Setter for systems
        :param value: List of systems
        """
        self.menu.choices.extend([str(system) for system in value])
        self.__systems = value

    def run(self) -> None:
        """! Display the territory menu selection."""
        if self.menu.response == str(MenuChoices.VIEW_DETAILS):
            print("Showing territory details...")
            for system in self.__systems:
                print(f"- {system}")
        elif self.menu.response in [str(system) for system in self.__systems]:
            print(f"Showing details for system: {self.menu.response}")
            selected_system: System = next((s for s in self.__systems if str(s) == self.menu.response), None)
            if selected_system:
                selected_system.show()
        else:
            print("Todo: Handle other territory menu choices.")
