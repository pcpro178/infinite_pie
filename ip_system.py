"""! Module for handling stellar systems."""

################################################################################
# Imports
################################################################################

from __future__ import annotations
from random import randrange
from typing import List, Tuple

from ip_name import Name
from ip_ship import Ship


################################################################################
# Class definitions
################################################################################

class System:
    """! Class for handling stellar systems."""

    def __init__(self):
        """! Initialize a new System."""
        self.__coordinates: Tuple[int, int, int] = (
            randrange(-1000, 1000), randrange(-1000, 1000), randrange(-1000, 1000))
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

    def __str__(self) -> str:
        """! String representation of the System."""
        return f"{self.__name} {self.__coordinates}"

    @property
    def coordinates(self) -> Tuple[int, int, int]:
        """! Accessor property for coordinates attribute.
        :return: The coordinates attribute
        """
        return self.__coordinates

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
