"""! Module for handling stellar systems."""

################################################################################
# Imports
################################################################################

from __future__ import annotations
from random import randrange
from typing import Tuple

from ip_name import Name


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
