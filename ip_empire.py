"""! Module for managing empires."""

################################################################################
# Imports
################################################################################

import os

from cmd import Cmd
from enum import StrEnum
from io import StringIO
from typing import List, Type

from ip_actionable import Actionable
from ip_name import Name
from ip_ship import Ship
from ip_system import System


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


class Empire(Actionable):
    """! Class for managing empires."""

    def __init__(self, parent_choices: List[str] = None) -> None:
        """! Initializes Empire object instance.
        :param parent_choices: Optional menu choices from parent object
        """
        print("Setting up new Empire . . .")

        super().__init__([str(x) for x in MenuChoices] + (parent_choices or []), "Empire Menu")

        self.__name: Name = Name("Empire", f"Enter {self.__class__.__name__} name [or empty for random]: ")
        self.__name.assign(self)
        self.__ships: List[Ship] = []
        self.__systems: List[System] = []

        # Create initial systems
        self.__create_systems()

        # Create initial ships
        self.__create_ships()

        # Specify capital system
        self.__capital: System = self.__systems[0]

    def __str__(self) -> str:
        """! Override function to generate object as human readable string
        :return: String representation of object
        """
        s: str = f"Empire: {self.__name}\r\n"
        s += self.__members_list_to_string(System, self.__systems)
        s += self.__members_list_to_string(Ship, self.__ships)
        return s

    def __create_systems(self) -> None:
        """! Instaniates lists of object members"""
        num_create_str: str = None
        type_name: str = "system"

        while num_create_str is None or num_create_str == 0 or not num_create_str.isdigit():
            num_create_str = input(f"Enter the starting number of {type_name}s: ")

        num_create_int: int = int(num_create_str)

        print(f"{type_name[0].upper() + type_name[1:]}{'s' if 1 < num_create_int else ''} created:", end='')

        for i in range(num_create_int):
            system: System = System()
            self.__systems.append(system)
            print(f"{',' if 0 < i else ''} {system.name}", end='')

        self.__systems.sort()
        print()

    def __create_ships(self) -> None:
        """! Instaniates lists of object members"""
        num_create_str: str = None
        type_name: str = "ship"

        while num_create_str is None or num_create_str == 0 or not num_create_str.isdigit():
            num_create_str = input(f"Enter the starting number of {type_name}s: ")

        num_create_int: int = int(num_create_str)

        print(f"{type_name[0].upper() + type_name[1:]}{'s' if 1 < num_create_int else ''} created:", end='')

        for i in range(num_create_int):
            ship: Ship = Ship(self.__systems[0].name)
            self.__ships.append(ship)
            print(f"{',' if 0 < i else ''} {ship.name}", end='')

        self.__ships.sort()
        print()

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

    def cycle(self) -> None:
        """! Complete a turn cycle for the object."""
        print(f"Function '{self.cycle.__name__}' not yet implemented.")

    def run(self) -> None:
        """! Run the empire menu selection."""
        if self.menu.response == MenuChoices.VIEW_DETAILS:
            print(str(self))
        elif self.menu.response == MenuChoices.MANAGE_SYSTEMS:
            print(f"Menu option '{self.menu.response}' not yet implemented.")
        elif self.menu.response == MenuChoices.MANAGE_SHIPS:
            print(f"Menu option '{self.menu.response}' not yet implemented.")
        else:
            raise ValueError(f"Invalid choice: {self.menu.response}")

    def show(self) -> None:
        """! Show the empire menu to the user."""
        self.menu.show()
