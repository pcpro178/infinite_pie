"""! Module for base ship type."""

################################################################################
# Imports
################################################################################

from __future__ import annotations

from ip_name import Name


################################################################################
# Class definitions
################################################################################

class Ship:
    """!Class for base ship type."""

    def __init__(self):
        """! Initialize a new Ship."""
        self.__name: Name = Name("Ship")

    def __eq__(self, obj: Ship) -> bool:
        """! Override equality comparison (==) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name == obj.__name.name

    def __gt__(self, obj: Ship) -> bool:
        """! Override greater-than (>) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name > obj.__name.name

    def __lt__(self, obj: Ship) -> bool:
        """! Override less-than (<) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name < obj.__name.name

    def __str__(self) -> str:
        """! String representation of the Ship."""
        return f"{self.__name}"

    @property
    def name(self) -> str:
        """! Accessor function for name attribute.
        :return: The name attribute
        """
        return self.__name.name
