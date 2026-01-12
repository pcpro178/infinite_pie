"""! Module for managing empires."""

################################################################################
# Imports
################################################################################

import logging
import os

from cmd import Cmd
from enum import StrEnum
from io import StringIO
from typing import List, Type

from ip_actionable import IActionable
from ip_name import Name
from ip_navy import Navy
from ip_ship import Ship
from ip_system import System
from ip_territory import Territory


################################################################################
# Constants & Globals
################################################################################

COL_PADDING: int = 2
MAX_AUTO_LIST: int = 5
MENU_CHOICE_RETURN: str = "Return to Empire Menu"


################################################################################
# Class definitions
################################################################################

class MenuChoices(StrEnum):
    """! Enumeration for empire menu choices."""
    VIEW_DETAILS: str = 'View Details'
    MANAGE_SYSTEMS: str = 'Manage Systems'
    MANAGE_SHIPS: str = 'Manage Ships'


class Empire(IActionable):
    """! Class for managing empires."""

    def __init__(self) -> None:
        """! Initializes Empire object instance."""
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__} initializing . . .")

        super().__init__()

        self.menu.choices.extend([str(x) for x in MenuChoices])
        self.menu.title = "Empire Menu"

        self.__name: Name = Name("Empire", f"Enter {self.__class__.__name__} name [or empty for random]: ")
        self.__name.assign(self)

        # Create initial systems
        self.__territory: Territory = Territory()
        self.__territory.systems = self.__init_systems()
        self.__territory.menu.choices.extend([MENU_CHOICE_RETURN])

        # Create initial ships
        self.__navy: Navy = Navy()
        self.__navy.ships = self.__init_ships()
        self.__navy.menu.choices.extend([MENU_CHOICE_RETURN])

        # Specify capital system
        self.__capital: System = self.__territory.systems[0]

    def __str__(self) -> str:
        """! Override function to generate object as human readable string
        :return: String representation of object
        """
        s: str = f"Empire: {self.__name}\r\n"
        s += self.__members_list_to_string(System, self.__territory.systems)
        s += self.__members_list_to_string(Ship, self.__navy.ships)
        return s

    def __init_systems(self) -> List[System]:
        """! Instaniates lists of object members
        :return: List of created systems
        """
        num_create_str: str = None
        system_lst: List[System] = []

        while num_create_str is None or num_create_str == 0 or not num_create_str.isdigit():
            num_create_str = input("Enter the starting number of systems: ")

        num_create_int: int = int(num_create_str)

        for i in range(num_create_int):
            system: System = System()
            system_lst.append(system)

        system_lst.sort()

        return system_lst

    def __init_ships(self) -> List[Ship]:
        """! Instaniates lists of object members
        :return: List of created ships
        """
        num_create_str: str = None
        ship_lst: List[Ship] = []

        while num_create_str is None or num_create_str == 0 or not num_create_str.isdigit():
            num_create_str = input("Enter the starting number of ships: ")

        num_create_int: int = int(num_create_str)

        for i in range(num_create_int):
            ship: Ship = Ship(self.__territory.systems[0].name)
            ship.coordinates = self.__territory.systems[0].coordinates
            ship_lst.append(ship)

        ship_lst.sort()

        return ship_lst

    def __members_list_to_string(self, typeof: Type, listof: list) -> str:
        """! Converts specified member list to string
        :param typeof: Member list type
        :param listof: Member list
        :return: String representation of member list
        """
        display_columns: int = os.get_terminal_size().columns
        type_name: str = typeof.__name__.lower()
        s: str = f"Number of {type_name[0].upper() + type_name[1:]}s: {len(listof)}\r\n"
        names_buffer: StringIO = StringIO()

        Cmd(stdout=names_buffer).columnize([str(x) for x in listof], displaywidth=display_columns)

        for line in names_buffer.getvalue().splitlines():
            s += "  " + line + "\r\n"

        return s

    @property
    def capital(self) -> System:
        """! Accessor property for capital attribute.
        :return: The capital attribute
        """
        return self.__capital

    @property
    def name(self) -> str:
        """! Accessor property for name attribute.
        :return: The name attribute
        """
        return self.__name.name

    def __manage_systems(self) -> None:
        """! Manage the empire's systems."""
        while self.__territory.menu.response != MENU_CHOICE_RETURN:
            self.__territory.run()
            self.__territory.show()

    def __manage_ships(self) -> None:
        """! Manage the empire's ships."""
        while self.__navy.menu.response != MENU_CHOICE_RETURN:
            self.__navy.run()
            self.__navy.show()

    def cycle(self) -> None:
        """! Complete a turn cycle for the object."""
        print(f"Function '{self.cycle.__name__}' not yet implemented.")

    def run(self) -> None:
        """! Run the empire menu selection."""
        if self.menu.response == MenuChoices.VIEW_DETAILS:
            print(str(self))
        elif self.menu.response == MenuChoices.MANAGE_SYSTEMS:
            self.__manage_systems()
        elif self.menu.response == MenuChoices.MANAGE_SHIPS:
            self.__manage_ships()
        else:
            raise ValueError(f"Invalid choice: {self.menu.response}")
