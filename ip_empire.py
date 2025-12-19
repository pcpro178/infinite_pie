"""! Module for managing empires."""

################################################################################
# Imports
################################################################################

import os

from cmd import Cmd
from enum import StrEnum
from io import StringIO
from typing import List, Type, TypeVar

import inquirer

from ip_actionable import Actionable
from ip_menu import Menu
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

    __choices: List[str] = [str(x) for x in MenuChoices]
    __name: Name = None
    __ships: List[Ship] = []
    __systems: List[System] = []

    def __init__(self, parent_choices: List[str] = None) -> None:
        """! Initializes Empire object instance.
        :param parent_choices: Optional menu choices from parent object
        """
        print("Setting up new Empire . . .")

        self.__choices.extend(parent_choices or [])

        super().__init__(self.__choices, "Empire Menu")

        self.__name = Name("Empire", f"Enter {self.__class__.__name__} name [or empty for random]: ")
        self.__name.assign(self)

        # Create initial systems
        self.__create_members(System, self.__systems)

        # Create initial ships
        self.__create_members(Ship, self.__ships)

        print(f"Empire {self.__name} created.")

    def __str__(self) -> str:
        """! Override function to generate object as human readable string
        :return: String representation of object
        """
        s: str = f"Empire: {self.__name}\r\n"
        s += self.__members_list_to_string(System, self.__systems)
        s += self.__members_list_to_string(Ship, self.__ships)
        return s

    def __create_members(self, typeof: Type, listof: list) -> None:
        """! Instaniates lists of object members
        :param typeof: Member list type
        :param listof: Member list
        """
        num_create_str: str = None
        type_name: str = typeof.__name__.lower()
        while num_create_str is None or num_create_str == 0 or not num_create_str.isdigit():
            num_create_str = input(f"Enter the starting number of {type_name}s: ")
        num_create_int: int = int(num_create_str)
        print(f"{type_name[0].upper() + type_name[1:]}{'s' if 1 < num_create_int else ''} created:", end='')
        for i in range(num_create_int):
            obj: object = typeof()
            listof.append(obj)
            print(f"{',' if 0 < i else ''} {obj.name}", end='')
        listof.sort()
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
        Cmd(stdout=names_buffer).columnize([x.name for x in listof], displaywidth=display_columns)
        for line in names_buffer.getvalue().splitlines():
            s += "  " + line + "\r\n"
        return s

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
