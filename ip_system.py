"""! Module for handling stellar systems."""

from __future__ import annotations

import ip_name


class System:
    """!Class for handling stellar systems."""

    __name: ip_name.Name = None

    def __init__(self):
        """! Initialize a new System."""
        self.__name = ip_name.Name(self.__class__.__name__)

    def __eq__(self, obj: System) -> bool:
        """! Override equality comparison (==) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not System:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name() == obj.__name.name()

    def __gt__(self, obj: System) -> bool:
        """! Override greater-than (>) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not System:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name() > obj.__name.name()

    def __lt__(self, obj: System) -> bool:
        """! Override less-than (\<) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not System:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name() < obj.__name.name()

    def __str__(self) -> str:
        """! String representation of the System."""
        return f"System: {self.__name}"

    def name(self, name: str = None) -> str:
        """! Accessor function for name attribute.
        :param name: Name of interest
        :return: The name attribute
        """
        if name is not None:
            self.__name.name(name)
        return self.__name.name()
