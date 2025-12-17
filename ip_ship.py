"""! Module for base ship type."""

from __future__ import annotations

import ip_name


class Ship:
    """!Class for base ship type."""

    __name: ip_name.Name = None

    def __init__(self):
        """! Initialize a new Ship."""
        self.__name = ip_name.Name(self.__class__.__name__)

    def __eq__(self, obj: Ship) -> bool:
        """! Override equality comparison (==) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name() == obj.__name.name()

    def __gt__(self, obj: Ship) -> bool:
        """! Override greater-than (>) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name() > obj.__name.name()

    def __lt__(self, obj: Ship) -> bool:
        """! Override less-than (\<) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name() < obj.__name.name()

    def __str__(self) -> str:
        """! String representation of the Ship."""
        return f"Ship: {self.__name}"

    def name(self, name: str = None) -> str:
        """! Accessor function for name attribute.
        :param name: Name of interest
        :return: The name attribute
        """
        if name is not None:
            self.__name.name(name)
        return self.__name.name()
