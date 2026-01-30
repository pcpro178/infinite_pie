"""! Module for handling stellar systems."""

################################################################################
# Imports
################################################################################

from __future__ import annotations
from enum import StrEnum
from random import randrange
from typing import List

import logging

from ip_actionable import IActionable
from ip_locatable import ILocatable
from ip_name import Name
from ip_ship import Ship


################################################################################
# Constants & Globals
################################################################################

DEFAULT_XCOORD_MIN: int = -1000
DEFAULT_XCOORD_MAX: int = 1000
DEFAULT_YCOORD_MIN: int = -1000
DEFAULT_YCOORD_MAX: int = 1000
DEFAULT_ZCOORD_MIN: int = -1000
DEFAULT_ZCOORD_MAX: int = 1000


################################################################################
# Class definitions
################################################################################

class MenuChoices(StrEnum):
    """! Enumeration for system menu choices."""
    VIEW_DETAILS: str = 'View Details'
    BUILD_SHIP: str = 'Build Ship'


class System(IActionable, ILocatable):
    """! Class for handling stellar systems."""

    def __init__(self):
        """! Initialize a new System."""
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__} initializing . . .")

        super().__init__(x=randrange(DEFAULT_XCOORD_MIN, DEFAULT_XCOORD_MAX),
                         y=randrange(DEFAULT_YCOORD_MIN, DEFAULT_YCOORD_MAX),
                         z=randrange(DEFAULT_ZCOORD_MIN, DEFAULT_ZCOORD_MAX))

        self.menu.choices.extend([str(x) for x in MenuChoices])
        self.menu.title = "System Menu"

        self.__name: Name = Name("System")
        self.__ships: List[Ship] = []

    def __eq__(self, obj: System) -> bool:
        """! Override equality comparison (==) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not System:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name == obj.__name.name

    def __gt__(self, obj: System) -> bool:
        """! Override greater-than (>) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not System:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name > obj.__name.name

    def __lt__(self, obj: System) -> bool:
        """! Override less-than (\<) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not System:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name < obj.__name.name

    def __repr__(self) -> str:
        """! String representation of the System object for program usage
        :return: String representation of the System object
        """
        return f"{self.__name} {self.coordinates}"

    def __str__(self) -> str:
        """! String representation of the System object for user display
        :return: String representation of the System
        """
        return f"{self.__name}"

    @property
    def name(self) -> str:
        """! Accessor property for name attribute.
        :return: The name attribute
        """
        return self.__name.name

    @property
    def ships(self) -> List[Ship]:
        """! Accessor property for ships attribute.
        :return: The ships attribute
        """
        return self.__ships

    def add_ship(self, ship: Ship) -> None:
        """! Add a ship to the system.
        :param ship: The ship to add
        """
        self.__ships.append(ship)

    def remove_ship(self, ship: Ship) -> None:
        """! Remove a ship from the system.
        :param ship: The ship to remove
        """
        self.__ships.remove(ship)

    def run(self) -> None:
        """! Display the system menu selection."""
        print(f"System: {self.__name}")
        print(f"Coordinates: {self.coordinates}")
        print(f"Number of ships: {len(self.__ships)}")
        # todo jfell implement system menu
